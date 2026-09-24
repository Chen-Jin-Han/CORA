import copy
import torch
from torch import nn
import torch.nn.functional as F

import networks
import tools

to_np = lambda x: x.detach().float().cpu().numpy()


def _parse_csv(value):
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [str(x).strip() for x in value if str(x).strip()]
    return [x.strip() for x in str(value).split(",") if x.strip()]


def _infer_num_task_heads(state: dict) -> int:
    ids = set()
    for k in state.keys():
        if not k.startswith("task_mask_heads."):
            continue
        parts = k.split(".")
        if len(parts) < 3:
            continue
        try:
            ids.add(int(parts[1]))
        except Exception:
            continue
    return (max(ids) + 1) if ids else 0


def _normalize_task_key(task: str) -> str:
    if not isinstance(task, str):
        return str(task)
    if "_" not in task:
        return task
    prefix, rest = task.split("_", 1)
    if prefix in ("dmc", "dmcgb"):
        return rest
    return task


class RewardEMA:
    """running mean and std"""

    def __init__(self, device, alpha=1e-2):
        self.device = device
        self.alpha = alpha
        self.range = torch.tensor([0.05, 0.95], device=device)

    def __call__(self, x, ema_vals):
        flat_x = torch.flatten(x.detach())
        x_quantile = torch.quantile(input=flat_x, q=self.range)
        # this should be in-place operation
        ema_vals[:] = self.alpha * x_quantile + (1 - self.alpha) * ema_vals
        scale = torch.clip(ema_vals[1] - ema_vals[0], min=1.0)
        offset = ema_vals[0]
        return offset.detach(), scale.detach()


class WorldModel(nn.Module):
    def __init__(self, obs_space, act_space, step, config):
        super(WorldModel, self).__init__()
        self._step = step
        self._use_amp = True if config.precision == 16 else False
        self._amp_dtype = torch.bfloat16 if self._use_amp else None
        self._config = config
        shapes = {k: tuple(v.shape) for k, v in obs_space.spaces.items()}
        self._expected_image_shape = shapes.get("image", None)
        self.encoder = networks.MultiEncoder(shapes, **config.encoder)
        self.embed_size = self.encoder.outdim
        self._use_moe_restore = bool(getattr(config, "use_moe_restore", False))
        self._use_single_unet_restore = bool(
            getattr(config, "use_single_unet_restore", False)
        )
        self._use_dual_stream_unet_restore = bool(
            getattr(config, "use_dual_stream_unet_restore", False)
        )
        self._dual_stream_unet = None
        self._dual_stream_unet_ref = None
        self._dual_stream_unet_task_conditioned = False
        self._dual_stream_unet_task_id = None
        self._dual_stream_unet_on_cpu = bool(
            getattr(config, "dual_stream_unet_on_cpu", False)
        )
        self._dual_stream_unet_device = torch.device(
            "cpu" if self._dual_stream_unet_on_cpu else str(config.device)
        )
        self._dual_stream_unet_apply = str(
            getattr(config, "dual_stream_unet_apply", "agent_only_rgb_hard")
        )
        self._debug_last_raw_image = None
        self._debug_last_proc_image = None
        self._debug_last_pred_expert = None
        self._debug_last_used_expert = None
        if self._use_dual_stream_unet_restore:
            if self._use_moe_restore or self._use_single_unet_restore:
                raise ValueError(
                    "use_dual_stream_unet_restore cannot be combined with other restore modes."
                )
            ckpt_path = getattr(config, "dual_stream_unet_checkpoint", None)
            if not ckpt_path:
                ckpt_path = getattr(config, "unet_checkpoint", None)
            if not ckpt_path:
                raise ValueError(
                    "use_dual_stream_unet_restore=True but dual_stream_unet_checkpoint is not set"
                )

            try:
                ckpt = torch.load(ckpt_path, map_location="cpu", weights_only=False)
            except TypeError:
                ckpt = torch.load(ckpt_path, map_location="cpu")
            ckpt_args = ckpt.get("args", {}) if isinstance(ckpt, dict) else {}
            state = (
                ckpt["model_state_dict"]
                if isinstance(ckpt, dict) and "model_state_dict" in ckpt
                else ckpt
            )

            degradations = list(ckpt.get("degradations") or [])
            if not degradations:
                degradations = _parse_csv(ckpt_args.get("degradation_types", ""))
            # Label-free checkpoints store architecture capacity, not labels.
            num_experts = int(ckpt_args.get("num_experts", 0) or len(degradations))
            if num_experts <= 0:
                raise ValueError("Checkpoint must specify args.num_experts or legacy degradations.")

            task_conditioned_mask = bool(
                ckpt_args.get("task_conditioned_mask", False)
            ) or (_infer_num_task_heads(state) > 0)
            num_tasks = int(ckpt_args.get("num_tasks", 0) or _infer_num_task_heads(state))

            tasks_override = getattr(config, "dual_stream_unet_tasks", None)
            tasks = _parse_csv(tasks_override) if tasks_override else _parse_csv(ckpt_args.get("tasks", ""))
            if task_conditioned_mask:
                if not tasks:
                    raise ValueError(
                        "Checkpoint uses task-conditioned mask; set dual_stream_unet_tasks or include tasks in ckpt."
                    )
                if num_tasks and len(tasks) != num_tasks:
                    raise ValueError(
                        f"task-conditioned checkpoint expects num_tasks={num_tasks}, but got {len(tasks)} tasks."
                    )

            base_channels = int(
                getattr(config, "dual_stream_unet_base_channels", 0)
                or ckpt_args.get("base_channels", 64)
            )
            router_hidden = int(
                getattr(config, "dual_stream_unet_router_hidden", 0)
                or ckpt_args.get("router_hidden", 256)
            )

            from aco_moe.moe_unet import DualStreamMoEUNet

            model = DualStreamMoEUNet(
                base_channels=base_channels,
                num_experts=num_experts,
                router_hidden=router_hidden,
                learn_residual_rgb=True,
                task_conditioned_mask=bool(task_conditioned_mask),
                num_tasks=int(num_tasks) if task_conditioned_mask else 0,
            )
            model.load_state_dict(state, strict=True)
            model.to(self._dual_stream_unet_device)
            model.eval()
            for p in model.parameters():
                p.requires_grad = False

            self._dual_stream_unet = model
            self._dual_stream_unet_ref = model
            self._dual_stream_unet_task_conditioned = bool(task_conditioned_mask)

            if self._dual_stream_unet_task_conditioned:
                task_key = _normalize_task_key(getattr(config, "task", ""))
                task_to_id = {str(t): int(i) for i, t in enumerate(tasks)}
                if task_key not in task_to_id and str(getattr(config, "task", "")) in task_to_id:
                    task_key = str(getattr(config, "task", ""))
                if task_key not in task_to_id:
                    raise ValueError(
                        f"Task '{task_key}' not in dual_stream_unet_tasks: {list(task_to_id.keys())}"
                    )
                self._dual_stream_unet_task_id = int(task_to_id[task_key])

            allowed_apply = {
                "agent_only_rgb_hard",
                "agent_only_rgb",
                "agent_only_input_hard",
                "restored_rgb",
            }
            if self._dual_stream_unet_apply not in allowed_apply:
                raise ValueError(
                    f"dual_stream_unet_apply must be one of {sorted(allowed_apply)}, got {self._dual_stream_unet_apply}"
                )
            print(f"[DualStream U-Net Restore] Checkpoint: {ckpt_path}")
            print(f"[DualStream U-Net Restore] Apply: {self._dual_stream_unet_apply}")
            if self._dual_stream_unet_on_cpu:
                print("[DualStream U-Net Restore] Running on CPU to save VRAM (slower).")
                # Keep the U-Net on CPU even if the parent module moves to GPU.
                # Move the module reference out of nn.Module tracking.
                self._modules.pop("_dual_stream_unet", None)
                self.__dict__["_dual_stream_unet_ref"] = model
        if self._use_moe_restore or self._use_single_unet_restore:
            raise ValueError(
                "use_moe_restore / use_single_unet_restore are legacy baselines and "
                "are not supported in this anonymized release. Use "
                "use_dual_stream_unet_restore for ACO-MoE."
            )

        self.dynamics = networks.RSSM(
            config.dyn_stoch,
            config.dyn_deter,
            config.dyn_hidden,
            config.dyn_rec_depth,
            config.dyn_discrete,
            config.act,
            config.norm,
            config.dyn_mean_act,
            config.dyn_std_act,
            config.dyn_min_std,
            config.unimix_ratio,
            config.initial,
            config.num_actions,
            self.embed_size,
            config.device,
        )
        self.heads = nn.ModuleDict()
        if config.dyn_discrete:
            feat_size = config.dyn_stoch * config.dyn_discrete + config.dyn_deter
        else:
            feat_size = config.dyn_stoch + config.dyn_deter
        self.heads["decoder"] = networks.MultiDecoder(
            feat_size, shapes, **config.decoder
        )
        self.heads["reward"] = networks.MLP(
            feat_size,
            (255,) if config.reward_head["dist"] == "symlog_disc" else (),
            config.reward_head["layers"],
            config.units,
            config.act,
            config.norm,
            dist=config.reward_head["dist"],
            outscale=config.reward_head["outscale"],
            device=config.device,
            name="Reward",
        )
        self.heads["cont"] = networks.MLP(
            feat_size,
            (),
            config.cont_head["layers"],
            config.units,
            config.act,
            config.norm,
            dist="binary",
            outscale=config.cont_head["outscale"],
            device=config.device,
            name="Cont",
        )
        for name in config.grad_heads:
            assert name in self.heads, name
        self._model_opt = tools.Optimizer(
            "model",
            self.parameters(),
            config.model_lr,
            config.opt_eps,
            config.grad_clip,
            config.weight_decay,
            opt=config.opt,
            use_amp=self._use_amp,
            amp_dtype=self._amp_dtype,
        )
        print(
            f"Optimizer model_opt has {sum(param.numel() for param in self.parameters())} variables."
        )
        # other losses are scaled by 1.0.
        self._scales = dict(
            reward=config.reward_head["loss_scale"],
            cont=config.cont_head["loss_scale"],
        )

    def _train(self, data):
        # action (batch_size, batch_length, act_dim)
        # image (batch_size, batch_length, h, w, ch)
        # reward (batch_size, batch_length)
        # discount (batch_size, batch_length)
        data = self.preprocess(data)

        with tools.RequiresGrad(self):
            with torch.amp.autocast("cuda", enabled=self._use_amp, dtype=self._amp_dtype):
                embed = self.encoder(data)
                post, prior = self.dynamics.observe(
                    embed, data["action"], data["is_first"]
                )
                kl_free = self._config.kl_free
                dyn_scale = self._config.dyn_scale
                rep_scale = self._config.rep_scale
                kl_loss, kl_value, dyn_loss, rep_loss = self.dynamics.kl_loss(
                    post, prior, kl_free, dyn_scale, rep_scale
                )
                assert kl_loss.shape == embed.shape[:2], kl_loss.shape
                preds = {}
                for name, head in self.heads.items():
                    grad_head = name in self._config.grad_heads
                    feat = self.dynamics.get_feat(post)
                    feat = feat if grad_head else feat.detach()
                    pred = head(feat)
                    if type(pred) is dict:
                        preds.update(pred)
                    else:
                        preds[name] = pred
                losses = {}
                for name, pred in preds.items():
                    loss = -pred.log_prob(data[name])
                    assert loss.shape == embed.shape[:2], (name, loss.shape)
                    losses[name] = loss
                scaled = {
                    key: value * self._scales.get(key, 1.0)
                    for key, value in losses.items()
                }
                model_loss = sum(scaled.values()) + kl_loss
            metrics = self._model_opt(torch.mean(model_loss), self.parameters())

        metrics.update({f"{name}_loss": to_np(loss) for name, loss in losses.items()})
        metrics["kl_free"] = kl_free
        metrics["dyn_scale"] = dyn_scale
        metrics["rep_scale"] = rep_scale
        metrics["dyn_loss"] = to_np(dyn_loss)
        metrics["rep_loss"] = to_np(rep_loss)
        metrics["kl"] = to_np(torch.mean(kl_value))
        with torch.amp.autocast("cuda", enabled=self._use_amp, dtype=self._amp_dtype):
            metrics["prior_ent"] = to_np(
                torch.mean(self.dynamics.get_dist(prior).entropy())
            )
            metrics["post_ent"] = to_np(
                torch.mean(self.dynamics.get_dist(post).entropy())
            )
            context = dict(
                embed=embed,
                feat=self.dynamics.get_feat(post),
                kl=kl_value,
                postent=self.dynamics.get_dist(post).entropy(),
            )
        post = {k: v.detach() for k, v in post.items()}
        return post, context, metrics

    # this function is called during both rollout and training
    def preprocess(self, obs):
        def ensure_expected_image_shape():
            if self._expected_image_shape is None or "image" not in obs:
                return
            exp_h, exp_w = int(self._expected_image_shape[0]), int(self._expected_image_shape[1])
            img = obs["image"]
            if img.dim() == 4:
                # (B, H, W, C) -> (B, C, H, W)
                if int(img.shape[1]) != exp_h or int(img.shape[2]) != exp_w:
                    x = img.permute(0, 3, 1, 2)
                    x = F.interpolate(x, size=(exp_h, exp_w), mode="bilinear", align_corners=False)
                    obs["image"] = x.permute(0, 2, 3, 1)
            elif img.dim() == 5:
                # (B, T, H, W, C) -> (B*T, C, H, W)
                if int(img.shape[2]) != exp_h or int(img.shape[3]) != exp_w:
                    b, t, _, _, c = img.shape
                    x = img.reshape(b * t, img.shape[2], img.shape[3], c).permute(0, 3, 1, 2)
                    x = F.interpolate(x, size=(exp_h, exp_w), mode="bilinear", align_corners=False)
                    obs["image"] = x.permute(0, 2, 3, 1).reshape(b, t, exp_h, exp_w, c)

        obs = {
            k: torch.tensor(v, device=self._config.device, dtype=torch.float32)
            for k, v in obs.items()
        }
        obs["image"] = obs["image"] / 255.0
        self._debug_last_raw_image = obs["image"].detach()

        # Enforce expected H/W early (before any restoration) to stabilize encoder shapes.
        ensure_expected_image_shape()

        dual_enabled = bool(
            getattr(self._config, "dual_stream_unet_restore_enabled", True)
        )

        if self._use_dual_stream_unet_restore and dual_enabled:
            unet = self._dual_stream_unet_ref
            if unet is None:
                unet = self._dual_stream_unet
            image = obs["image"]
            single_time = False
            if image.dim() == 4:
                image = image[:, None, ...]
                single_time = True

            b, t, h, w, c = image.shape
            x = image.permute(0, 1, 4, 2, 3).reshape(b * t, c, h, w)
            x = x * 2.0 - 1.0

            task_ids = None
            if self._dual_stream_unet_task_conditioned:
                task_ids = torch.full(
                    (b * t,),
                    int(self._dual_stream_unet_task_id),
                    device=x.device,
                    dtype=torch.int64,
                )

            with torch.inference_mode():
                if self._dual_stream_unet_device.type == "cpu":
                    if unet is not None:
                        try:
                            p0 = next(unet.parameters())
                            if p0.device.type != "cpu":
                                unet.to("cpu")
                        except StopIteration:
                            pass
                    x_cpu = x.to("cpu")
                    task_ids_cpu = task_ids.to("cpu") if task_ids is not None else None
                    out = unet(x_cpu, task_ids=task_ids_cpu, router_topk=1)
                    restored = out[self._dual_stream_unet_apply]
                    if "router_probs" in out:
                        pred = torch.argmax(out["router_probs"], dim=-1)
                    else:
                        pred = None
                    restored = restored.to(obs["image"].device)
                    pred = pred.to(obs["image"].device) if pred is not None else None
                else:
                    with torch.amp.autocast(
                        "cuda", enabled=self._use_amp, dtype=self._amp_dtype
                    ):
                        out = unet(x, task_ids=task_ids, router_topk=1)
                    restored = out[self._dual_stream_unet_apply]
                    pred = torch.argmax(out["router_probs"], dim=-1) if "router_probs" in out else None

            restored = (restored + 1.0) * 0.5
            restored = torch.clamp(restored, 0.0, 1.0)
            restored = restored.reshape(b, t, c, h, w).permute(0, 1, 3, 4, 2)
            if single_time:
                restored = restored[:, 0]
            obs["image"] = restored

            if pred is not None:
                pred = pred.reshape(b, t)
                if single_time:
                    pred = pred[:, 0]
                self._debug_last_pred_expert = pred.detach()
                self._debug_last_used_expert = pred.detach()
            else:
                self._debug_last_pred_expert = None
                self._debug_last_used_expert = None
        else:
            self._debug_last_pred_expert = None
            self._debug_last_used_expert = None

        # Enforce expected H/W again in case a restoration model changes spatial size.
        ensure_expected_image_shape()

        self._debug_last_proc_image = obs["image"].detach()
        if "discount" in obs:
            obs["discount"] *= self._config.discount
            # (batch_size, batch_length) -> (batch_size, batch_length, 1)
            obs["discount"] = obs["discount"].unsqueeze(-1)
        # 'is_first' is necesarry to initialize hidden state at training
        assert "is_first" in obs
        # 'is_terminal' is necesarry to train cont_head
        assert "is_terminal" in obs
        obs["cont"] = (1.0 - obs["is_terminal"]).unsqueeze(-1)
        return obs

    def video_pred(self, data):
        data = self.preprocess(data)
        embed = self.encoder(data)

        states, _ = self.dynamics.observe(
            embed[:6, :5], data["action"][:6, :5], data["is_first"][:6, :5]
        )
        recon = self.heads["decoder"](self.dynamics.get_feat(states))["image"].mode()[
            :6
        ]
        reward_post = self.heads["reward"](self.dynamics.get_feat(states)).mode()[:6]
        init = {k: v[:, -1] for k, v in states.items()}
        prior = self.dynamics.imagine_with_action(data["action"][:6, 5:], init)
        openl = self.heads["decoder"](self.dynamics.get_feat(prior))["image"].mode()
        reward_prior = self.heads["reward"](self.dynamics.get_feat(prior)).mode()
        # observed image is given until 5 steps
        model = torch.cat([recon[:, :5], openl], 1)
        truth = data["image"][:6]
        model = model
        error = (model - truth + 1.0) / 2.0

        return torch.cat([truth, model, error], 2)


class ImagBehavior(nn.Module):
    def __init__(self, config, world_model):
        super(ImagBehavior, self).__init__()
        self._use_amp = True if config.precision == 16 else False
        self._amp_dtype = torch.bfloat16 if self._use_amp else None
        self._config = config
        self._world_model = world_model
        if config.dyn_discrete:
            feat_size = config.dyn_stoch * config.dyn_discrete + config.dyn_deter
        else:
            feat_size = config.dyn_stoch + config.dyn_deter
        self.actor = networks.MLP(
            feat_size,
            (config.num_actions,),
            config.actor["layers"],
            config.units,
            config.act,
            config.norm,
            config.actor["dist"],
            config.actor["std"],
            config.actor["min_std"],
            config.actor["max_std"],
            absmax=1.0,
            temp=config.actor["temp"],
            unimix_ratio=config.actor["unimix_ratio"],
            outscale=config.actor["outscale"],
            name="Actor",
        )
        self.value = networks.MLP(
            feat_size,
            (255,) if config.critic["dist"] == "symlog_disc" else (),
            config.critic["layers"],
            config.units,
            config.act,
            config.norm,
            config.critic["dist"],
            outscale=config.critic["outscale"],
            device=config.device,
            name="Value",
        )
        if config.critic["slow_target"]:
            self._slow_value = copy.deepcopy(self.value)
            self._updates = 0
        kw = dict(
            wd=config.weight_decay,
            opt=config.opt,
            use_amp=self._use_amp,
            amp_dtype=self._amp_dtype,
        )
        self._actor_opt = tools.Optimizer(
            "actor",
            self.actor.parameters(),
            config.actor["lr"],
            config.actor["eps"],
            config.actor["grad_clip"],
            **kw,
        )
        print(
            f"Optimizer actor_opt has {sum(param.numel() for param in self.actor.parameters())} variables."
        )
        self._value_opt = tools.Optimizer(
            "value",
            self.value.parameters(),
            config.critic["lr"],
            config.critic["eps"],
            config.critic["grad_clip"],
            **kw,
        )
        print(
            f"Optimizer value_opt has {sum(param.numel() for param in self.value.parameters())} variables."
        )
        if self._config.reward_EMA:
            # register ema_vals to nn.Module for enabling torch.save and torch.load
            self.register_buffer(
                "ema_vals", torch.zeros((2,), device=self._config.device)
            )
            self.reward_ema = RewardEMA(device=self._config.device)

    def _train(
        self,
        start,
        objective,
    ):
        self._update_slow_target()
        metrics = {}

        with tools.RequiresGrad(self.actor):
            with torch.amp.autocast("cuda", enabled=self._use_amp, dtype=self._amp_dtype):
                imag_feat, imag_state, imag_action = self._imagine(
                    start, self.actor, self._config.imag_horizon
                )
                reward = objective(imag_feat, imag_state, imag_action)
                actor_ent = self.actor(imag_feat).entropy()
                state_ent = self._world_model.dynamics.get_dist(imag_state).entropy()
                # this target is not scaled by ema or sym_log.
                target, weights, base = self._compute_target(
                    imag_feat, imag_state, reward
                )
                actor_loss, mets = self._compute_actor_loss(
                    imag_feat,
                    imag_action,
                    target,
                    weights,
                    base,
                )
                actor_loss -= self._config.actor["entropy"] * actor_ent[:-1, ..., None]
                actor_loss = torch.mean(actor_loss)
                metrics.update(mets)
                value_input = imag_feat

        with tools.RequiresGrad(self.value):
            with torch.amp.autocast("cuda", enabled=self._use_amp, dtype=self._amp_dtype):
                value = self.value(value_input[:-1].detach())
                target = torch.stack(target, dim=1)
                # (time, batch, 1), (time, batch, 1) -> (time, batch)
                value_loss = -value.log_prob(target.detach())
                slow_target = self._slow_value(value_input[:-1].detach())
                if self._config.critic["slow_target"]:
                    value_loss -= value.log_prob(slow_target.mode().detach())
                # (time, batch, 1), (time, batch, 1) -> (1,)
                value_loss = torch.mean(weights[:-1] * value_loss[:, :, None])

        metrics.update(tools.tensorstats(value.mode(), "value"))
        metrics.update(tools.tensorstats(target, "target"))
        metrics.update(tools.tensorstats(reward, "imag_reward"))
        if self._config.actor["dist"] in ["onehot"]:
            metrics.update(
                tools.tensorstats(
                    torch.argmax(imag_action, dim=-1).float(), "imag_action"
                )
            )
        else:
            metrics.update(tools.tensorstats(imag_action, "imag_action"))
        metrics["actor_entropy"] = to_np(torch.mean(actor_ent))
        with tools.RequiresGrad(self):
            metrics.update(self._actor_opt(actor_loss, self.actor.parameters()))
            metrics.update(self._value_opt(value_loss, self.value.parameters()))
        return imag_feat, imag_state, imag_action, weights, metrics

    def _imagine(self, start, policy, horizon):
        dynamics = self._world_model.dynamics
        flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))
        start = {k: flatten(v) for k, v in start.items()}

        def step(prev, _):
            state, _, _ = prev
            feat = dynamics.get_feat(state)
            inp = feat.detach()
            action = policy(inp).sample()
            succ = dynamics.img_step(state, action)
            return succ, feat, action

        succ, feats, actions = tools.static_scan(
            step, [torch.arange(horizon)], (start, None, None)
        )
        states = {k: torch.cat([start[k][None], v[:-1]], 0) for k, v in succ.items()}

        return feats, states, actions

    def _compute_target(self, imag_feat, imag_state, reward):
        if "cont" in self._world_model.heads:
            inp = self._world_model.dynamics.get_feat(imag_state)
            discount = self._config.discount * self._world_model.heads["cont"](inp).mean
        else:
            discount = self._config.discount * torch.ones_like(reward)
        value = self.value(imag_feat).mode()
        target = tools.lambda_return(
            reward[1:],
            value[:-1],
            discount[1:],
            bootstrap=value[-1],
            lambda_=self._config.discount_lambda,
            axis=0,
        )
        weights = torch.cumprod(
            torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0
        ).detach()
        return target, weights, value[:-1]

    def _compute_actor_loss(
        self,
        imag_feat,
        imag_action,
        target,
        weights,
        base,
    ):
        metrics = {}
        inp = imag_feat.detach()
        policy = self.actor(inp)
        # Q-val for actor is not transformed using symlog
        target = torch.stack(target, dim=1)
        if self._config.reward_EMA:
            offset, scale = self.reward_ema(target, self.ema_vals)
            normed_target = (target - offset) / scale
            normed_base = (base - offset) / scale
            adv = normed_target - normed_base
            metrics.update(tools.tensorstats(normed_target, "normed_target"))
            metrics["EMA_005"] = to_np(self.ema_vals[0])
            metrics["EMA_095"] = to_np(self.ema_vals[1])

        if self._config.imag_gradient == "dynamics":
            actor_target = adv
        elif self._config.imag_gradient == "reinforce":
            actor_target = (
                policy.log_prob(imag_action)[:-1][:, :, None]
                * (target - self.value(imag_feat[:-1]).mode()).detach()
            )
        elif self._config.imag_gradient == "both":
            actor_target = (
                policy.log_prob(imag_action)[:-1][:, :, None]
                * (target - self.value(imag_feat[:-1]).mode()).detach()
            )
            mix = self._config.imag_gradient_mix
            actor_target = mix * target + (1 - mix) * actor_target
            metrics["imag_gradient_mix"] = mix
        else:
            raise NotImplementedError(self._config.imag_gradient)
        actor_loss = -weights[:-1] * actor_target
        return actor_loss, metrics

    def _update_slow_target(self):
        if self._config.critic["slow_target"]:
            if self._updates % self._config.critic["slow_target_update"] == 0:
                mix = self._config.critic["slow_target_fraction"]
                for s, d in zip(self.value.parameters(), self._slow_value.parameters()):
                    d.data = mix * s.data + (1 - mix) * d.data
            self._updates += 1
