import argparse
import functools
import os
import pathlib
import sys

# Respect an existing renderer choice (e.g. `MUJOCO_GL=glfw` with Xvfb).
os.environ.setdefault("MUJOCO_GL", "egl")

import io

import numpy as np
import ruamel.yaml as yaml


def _yaml_load(text: str):
    """Load YAML in a way that works with both ruamel.yaml 0.17 and 0.18+."""
    try:
        return yaml.safe_load(text)
    except (AttributeError, TypeError):
        y = yaml.YAML(typ="safe", pure=True)
        return y.load(io.StringIO(text))

sys.path.append(str(pathlib.Path(__file__).parent))

import exploration as expl
import models
import tools
import envs.wrappers as wrappers
from parallel import Parallel, Damy

import torch
from torch import nn
from torch import distributions as torchd


to_np = lambda x: x.detach().float().cpu().numpy()


def _resolve_device(requested):
    requested = str(requested)
    if requested.startswith("cuda"):
        if not torch.cuda.is_available():
            print(
                f"Requested CUDA device '{requested}' but CUDA is not available. "
                "Falling back to CPU."
            )
            return "cpu"
        device = torch.device(requested)
        index = device.index
        if index is None:
            index = torch.cuda.current_device()
        if index >= torch.cuda.device_count():
            print(
                f"Requested CUDA device index {index} is out of range "
                f"(only {torch.cuda.device_count()} visible). Falling back to CPU."
            )
            return "cpu"
        try:
            props = torch.cuda.get_device_properties(index)
            arch = f"sm_{props.major}{props.minor}"
        except Exception as exc:
            print(
                "Could not inspect the requested CUDA device "
                f"({exc}). Falling back to CPU."
            )
            return "cpu"
        get_arch_list = getattr(torch.cuda, "get_arch_list", None)
        supported = []
        if callable(get_arch_list):
            try:
                supported = get_arch_list()
            except Exception:
                supported = []
        if supported and arch not in supported:
            # Exact architecture membership is too strict: compatible cubins
            # and PTX can run on newer minor architectures (e.g. sm_89).
            try:
                probe = torch.ones((8, 8), device=device)
                (probe @ probe).sum().item()
                torch.cuda.synchronize(device)
                del probe
                print(f"CUDA {arch}: runtime kernel probe passed on {requested}.")
            except RuntimeError as exc:
                print(f"CUDA runtime probe failed ({exc}). Falling back to CPU.")
                return "cpu"
    return requested


def _maybe_init_wandb(config, logdir):
    if not bool(getattr(config, "use_wandb", False)):
        return None
    try:
        import wandb
    except Exception as exc:
        raise RuntimeError(
            "wandb is required for --use_wandb. Install with: pip install wandb"
        ) from exc
    entity = str(getattr(config, "wandb_entity", "")).strip() or None
    project = str(getattr(config, "wandb_project", "")).strip() or None
    run_name = pathlib.Path(logdir).name
    return wandb.init(
        entity=entity,
        project=project,
        name=run_name,
        config=vars(config),
        dir=str(logdir),
        job_type="train",
    )


class Dreamer(nn.Module):
    def __init__(self, obs_space, act_space, config, logger, dataset):
        super(Dreamer, self).__init__()
        self._config = config
        self._logger = logger
        self._should_log = tools.Every(config.log_every)
        batch_steps = config.batch_size * config.batch_length
        self._should_train = tools.Every(batch_steps / config.train_ratio)
        self._should_pretrain = tools.Once()
        self._should_reset = tools.Every(config.reset_every)
        self._should_expl = tools.Until(int(config.expl_until / config.action_repeat))
        self._metrics = {}
        # this is update step
        self._step = logger.step // config.action_repeat
        self._update_count = 0
        self._dataset = dataset
        if getattr(config, "use_dib_wm", False):
            raise ValueError(
                "use_dib_wm is not supported in this anonymized release. "
                "Only the vanilla DreamerV3 + ACO-MoE adapter pipeline is provided."
            )
        self._wm = models.WorldModel(obs_space, act_space, self._step, config)
        self._task_behavior = models.ImagBehavior(config, self._wm)
        if (
            config.compile and os.name != "nt"
        ):  # compilation is not supported on windows
            self._wm = torch.compile(self._wm)
            self._task_behavior = torch.compile(self._task_behavior)
        reward = lambda f, s, a: self._wm.heads["reward"](f).mean()
        self._expl_behavior = dict(
            greedy=lambda: self._task_behavior,
            random=lambda: expl.Random(config, act_space),
            plan2explore=lambda: expl.Plan2Explore(config, self._wm, reward),
        )[config.expl_behavior]().to(self._config.device)

    def __call__(self, obs, reset, state=None, training=True):
        step = self._step
        if training:
            steps = (
                self._config.pretrain
                if self._should_pretrain()
                else self._should_train(step)
            )
            for _ in range(steps):
                self._train(next(self._dataset))
                self._update_count += 1
                self._metrics["update_count"] = self._update_count
            if self._should_log(step):
                for name, values in self._metrics.items():
                    self._logger.scalar(name, float(np.mean(values)))
                    self._metrics[name] = []
                if self._config.video_pred_log:
                    openl = self._wm.video_pred(next(self._dataset))
                    self._logger.video("train_openl", to_np(openl))
                self._logger.write(fps=True)

        policy_output, state = self._policy(obs, state, training)

        if training:
            self._step += len(reset)
            self._logger.step = self._config.action_repeat * self._step
        return policy_output, state

    def _policy(self, obs, state, training):
        if state is None:
            latent = action = None
        else:
            latent, action = state
        obs = self._wm.preprocess(obs)
        embed = self._wm.encoder(obs)

        # DIB-WM: extract content bottleneck for dynamics
        if hasattr(self._wm, 'dual_bottleneck'):
            c_t, _ = self._wm.dual_bottleneck(embed)
            latent, _ = self._wm.dynamics.obs_step(latent, action, c_t, obs["is_first"])
        else:
            latent, _ = self._wm.dynamics.obs_step(latent, action, embed, obs["is_first"])
        if self._config.eval_state_mean:
            latent["stoch"] = latent["mean"]
        feat = self._wm.dynamics.get_feat(latent)
        if not training:
            actor = self._task_behavior.actor(feat)
            action = actor.mode()
        elif self._should_expl(self._step):
            actor = self._expl_behavior.actor(feat)
            action = actor.sample()
        else:
            actor = self._task_behavior.actor(feat)
            action = actor.sample()
        logprob = actor.log_prob(action)
        latent = {k: v.detach() for k, v in latent.items()}
        action = action.detach()
        if self._config.actor["dist"] == "onehot_gumble":
            action = torch.one_hot(
                torch.argmax(action, dim=-1), self._config.num_actions
            )
        policy_output = {"action": action, "logprob": logprob}
        state = (latent, action)
        return policy_output, state

    def _train(self, data):
        metrics = {}
        post, context, mets = self._wm._train(data)
        metrics.update(mets)
        start = post
        reward = lambda f, s, a: self._wm.heads["reward"](
            self._wm.dynamics.get_feat(s)
        ).mode()
        metrics.update(self._task_behavior._train(start, reward)[-1])
        if self._config.expl_behavior != "greedy":
            mets = self._expl_behavior.train(start, context, data)[-1]
            metrics.update({"expl_" + key: value for key, value in mets.items()})
        for name, value in metrics.items():
            if not name in self._metrics.keys():
                self._metrics[name] = [value]
            else:
                self._metrics[name].append(value)


def count_steps(folder):
    return sum(int(str(n).split("-")[-1][:-4]) - 1 for n in folder.glob("*.npz"))


def make_dataset(episodes, config):
    generator = tools.sample_episodes(episodes, config.batch_length)
    dataset = tools.from_generator(generator, config.batch_size)
    return dataset


def make_env(config, mode, id):
    suite, task = config.task.split("_", 1)
    if suite == "dmc":
        # Check if VDCS (Visual Degraded Control Suite) is enabled
        vdcs_enabled = getattr(config, 'vdcs_enabled', False)

        if vdcs_enabled:
            # Use Visual Degraded Control Suite
            import envs.visual_degraded_control as vdcs

            vdcs_degradation_configs = getattr(config, 'vdcs_degradation_configs', None)
            if isinstance(vdcs_degradation_configs, str):
                # CLI passes strings; allow Python-literal list/tuple of dicts.
                import ast
                try:
                    parsed = ast.literal_eval(vdcs_degradation_configs)
                    if isinstance(parsed, (list, tuple)):
                        vdcs_degradation_configs = list(parsed)
                except Exception as exc:
                    raise ValueError(
                        f"Failed to parse vdcs_degradation_configs: {vdcs_degradation_configs!r}"
                    ) from exc

            # Gather VDCS configuration
            vdcs_kwargs = {
                'action_repeat': config.action_repeat,
                'size': tuple(config.size),
                'seed': config.seed + id,
                'base_env': getattr(config, 'vdcs_base_env', 'dmc'),
                'degradation_type': getattr(config, 'vdcs_degradation_type', None),
                'degradation_preset': getattr(config, 'vdcs_degradation_preset', None),
                'degradation_configs': vdcs_degradation_configs,
                'intensity': getattr(config, 'vdcs_intensity', 0.7),
                'composition_mode': getattr(config, 'vdcs_composition_mode', 'sequential'),
                'composition_probability': getattr(config, 'vdcs_composition_probability', 1.0),
                'intensity_jitter': getattr(config, 'vdcs_intensity_jitter', 0.1),
                'markov_stay_prob': getattr(config, 'vdcs_markov_stay_prob', 0.95),
            }

            # If base_env is 'dcs', pass DCS parameters
            if vdcs_kwargs['base_env'] == 'dcs':
                vdcs_kwargs['difficulty'] = getattr(config, 'dcs_difficulty', 'easy')
                vdcs_kwargs['dynamic'] = getattr(config, 'dcs_dynamic', True)
                vdcs_kwargs['background_dataset_path'] = getattr(config, 'dcs_background_path', None)
                vdcs_kwargs['distraction_types'] = getattr(config, 'dcs_distraction_types', None)

            env = vdcs.VisualDegradedControl(task, **vdcs_kwargs)
            env = wrappers.NormalizeActions(env)
        else:
            # Use standard DMC
            import envs.dmc as dmc

            env = dmc.DeepMindControl(
                task, config.action_repeat, config.size, seed=config.seed + id
            )
            env = wrappers.NormalizeActions(env)
    elif suite == "dcs":
        # Distracting Control Suite
        import envs.dcs as dcs

        # Gather DCS-specific configuration
        dcs_kwargs = {
            'difficulty': getattr(config, 'dcs_difficulty', 'easy'),
            'intensity': getattr(config, 'dcs_intensity', None),
            'dynamic': getattr(config, 'dcs_dynamic', True),
            'background_dataset_path': getattr(config, 'dcs_background_path', None),
            'background_dataset_videos': getattr(config, 'dcs_background_videos', 'train'),
            'distraction_types': getattr(config, 'dcs_distraction_types', None),
        }

        env = dcs.DistractingControl(
            task,
            config.action_repeat,
            config.size,
            seed=config.seed + id,
            **dcs_kwargs
        )
        env = wrappers.NormalizeActions(env)
    elif suite == "dmcgb":
        # DMControl Generalization Benchmark (DMC-GB style test distributions)
        import envs.dmcgb as dmcgb

        # Allow separate train/eval distributions (train defaults to clean DMC).
        default_mode = getattr(config, "dmcgb_mode", "train")
        train_mode = getattr(config, "dmcgb_mode_train", default_mode)
        eval_mode = getattr(config, "dmcgb_mode_eval", default_mode)
        dmcgb_mode = train_mode if mode == "train" else eval_mode

        env = dmcgb.DMCGBControl(
            task,
            action_repeat=config.action_repeat,
            size=tuple(config.size),
            seed=config.seed + id,
            mode=dmcgb_mode,
            background_dataset_path=getattr(config, "dmcgb_background_path", None),
            background_dataset_videos=getattr(config, "dmcgb_background_videos", "train"),
            dynamic=getattr(config, "dmcgb_dynamic", True),
            video_alpha=getattr(config, "dmcgb_video_alpha", 1.0),
            video_update_every=getattr(config, "dmcgb_video_update_every", 2),
            num_videos_easy=getattr(config, "dmcgb_num_videos_easy", 10),
            num_videos_hard=getattr(config, "dmcgb_num_videos_hard", 100),
            color_mode=getattr(config, "dmcgb_color_mode", "random_walk"),
            color_palette_root=getattr(config, "dmcgb_color_palette_root", None),
        )
        env = wrappers.NormalizeActions(env)
    elif suite == "metaworld":
        import envs.metaworld as metaworld

        # Get camera names from config, default to ['corner']
        camera_names = getattr(config, 'camera_names', ['corner'])

        env = metaworld.MetaWorld(
            task, config.action_repeat, config.size, camera_names=camera_names, seed=config.seed + id
        )
        env = wrappers.NormalizeActions(env)
    elif suite == "robosuite":
        import envs.robosuite as robosuite

        # Get camera names from config, default to ['agentview']
        camera_names = getattr(config, 'camera_names', ['agentview'])

        # Get camera rotations from config (optional)
        camera_rotations = getattr(config, 'camera_rotations', None)

        # Get RoboSuite-specific configuration
        robots = getattr(config, 'robosuite_robots', 'Panda')
        gripper_types = getattr(config, 'robosuite_gripper_types', 'default')
        reward_shaping = getattr(config, 'robosuite_reward_shaping', True)
        control_freq = getattr(config, 'robosuite_control_freq', 20)

        # Episode horizon: ensure inner robosuite horizon isn't shorter than TimeLimit.
        robosuite_horizon = getattr(config, 'robosuite_horizon', None)
        if robosuite_horizon is None:
            try:
                robosuite_horizon = int(config.time_limit * config.action_repeat)
            except Exception:
                robosuite_horizon = None

        # DAVIS video background (DMC-GB style) for RoboSuite.
        video_background_default = getattr(config, "robosuite_video_background", False)
        video_background_train = getattr(config, "robosuite_video_background_train", video_background_default)
        video_background_eval = getattr(config, "robosuite_video_background_eval", video_background_default)
        video_background = bool(video_background_train if mode == "train" else video_background_eval)

        background_path = getattr(config, "robosuite_background_path", None)
        if background_path is None:
            background_path = getattr(config, "davis_path", None)

        background_videos = getattr(config, "robosuite_background_videos", None)
        if background_videos is None:
            background_videos = getattr(config, "davis_split", "train")

        background_mask_mode = getattr(config, "robosuite_background_mask_mode", "segmentation")
        camera_segmentations = getattr(config, "robosuite_camera_segmentations", None)
        if video_background and camera_segmentations is None and str(background_mask_mode).lower() == "segmentation":
            # Best-effort default: request segmentation so we can mask background pixels.
            camera_segmentations = "element"

        # Controller configs can be None to use defaults, or customized
        # For custom controllers:
        # from robosuite.controllers import load_part_controller_config
        # controller_type = getattr(config, 'robosuite_controller', 'OSC_POSE')
        # controller_configs = load_part_controller_config(default_controller=controller_type)
        controller_configs = None  # Use defaults

        env = robosuite.RoboSuite(
            task,
            action_repeat=config.action_repeat,
            size=config.size,
            camera_names=camera_names,
            camera_rotations=camera_rotations,
            seed=config.seed + id,
            robots=robots,
            gripper_types=gripper_types,
            controller_configs=controller_configs,
            reward_shaping=reward_shaping,
            control_freq=control_freq,
            horizon=robosuite_horizon,
            camera_segmentations=camera_segmentations,
            video_background=video_background,
            background_dataset_path=background_path,
            background_dataset_videos=background_videos,
            background_num_videos=getattr(config, "robosuite_background_num_videos", None),
            background_dynamic=getattr(config, "robosuite_background_dynamic", True),
            background_update_every=getattr(config, "robosuite_background_update_every", 2),
            background_alpha=getattr(config, "robosuite_background_alpha", 1.0),
            background_mask_mode=background_mask_mode,
            background_key_color=getattr(config, "robosuite_background_key_color", (0, 0, 0)),
            background_key_tolerance=getattr(config, "robosuite_background_key_tolerance", 0),
            background_mask_geoms=getattr(config, "robosuite_background_mask_geoms", None),
        )
        env = wrappers.NormalizeActions(env)
    elif suite == "atari":
        import envs.atari as atari

        env = atari.Atari(
            task,
            config.action_repeat,
            config.size,
            gray=config.grayscale,
            noops=config.noops,
            lives=config.lives,
            sticky=config.stickey,
            actions=config.actions,
            resize=config.resize,
            seed=config.seed + id,
        )
        env = wrappers.OneHotAction(env)
    elif suite == "dmlab":
        import envs.dmlab as dmlab

        env = dmlab.DeepMindLabyrinth(
            task,
            mode if "train" in mode else "test",
            config.action_repeat,
            seed=config.seed + id,
        )
        env = wrappers.OneHotAction(env)
    elif suite == "memorymaze":
        from envs.memorymaze import MemoryMaze

        env = MemoryMaze(task, seed=config.seed + id)
        env = wrappers.OneHotAction(env)
    elif suite == "crafter":
        import envs.crafter as crafter

        env = crafter.Crafter(task, config.size, seed=config.seed + id)
        env = wrappers.OneHotAction(env)
    elif suite == "minecraft":
        import envs.minecraft as minecraft

        env = minecraft.make_env(task, size=config.size, break_speed=config.break_speed)
        env = wrappers.OneHotAction(env)
    else:
        raise NotImplementedError(suite)

    if getattr(config, "agent_only_pixels", False):
        env = wrappers.AgentOnlyPixels(
            env,
            background_color=getattr(config, "agent_only_bg_color", (0, 0, 0)),
            agent_body=getattr(config, "agent_only_body", None),
            extra_sites=getattr(config, "agent_only_extra_sites", None),
            extra_geoms=getattr(config, "agent_only_extra_geoms", None),
            keep_target_sites=getattr(config, "agent_only_keep_target_sites", True),
            keep_target_geoms=getattr(config, "agent_only_keep_target_geoms", True),
            strict=getattr(config, "agent_only_strict", False),
        )
    env = wrappers.TimeLimit(env, config.time_limit)
    env = wrappers.SelectAction(env, key="action")
    env = wrappers.UUID(env)
    if suite == "minecraft":
        env = wrappers.RewardObs(env)
    return env


def main(config):
    tools.set_seed_everywhere(config.seed)
    if config.deterministic_run:
        tools.enable_deterministic_run()
    config.device = _resolve_device(config.device)
    if getattr(config, "vdcs_mode", None):
        config.vdcs_composition_mode = config.vdcs_mode
    logdir = pathlib.Path(config.logdir).expanduser()
    config.traindir = config.traindir or logdir / "train_eps"
    config.evaldir = config.evaldir or logdir / "eval_eps"
    config.steps //= config.action_repeat
    config.eval_every = max(1, config.eval_every // config.action_repeat)
    config.log_every = max(1, config.log_every // config.action_repeat)
    config.time_limit //= config.action_repeat

    print("Logdir", logdir)
    logdir.mkdir(parents=True, exist_ok=True)
    config.traindir.mkdir(parents=True, exist_ok=True)
    config.evaldir.mkdir(parents=True, exist_ok=True)
    step = count_steps(config.traindir)
    # step in logger is environmental step
    wandb_run = _maybe_init_wandb(config, logdir)
    logger = tools.Logger(logdir, config.action_repeat * step, wandb_run=wandb_run)

    print("Create envs.")
    if config.offline_traindir:
        directory = config.offline_traindir.format(**vars(config))
    else:
        directory = config.traindir
    train_eps = tools.load_episodes(directory, limit=config.dataset_size)
    if config.offline_evaldir:
        directory = config.offline_evaldir.format(**vars(config))
    else:
        directory = config.evaldir
    eval_eps = tools.load_episodes(directory, limit=1)
    make = lambda mode, id: make_env(config, mode, id)
    train_envs = [make("train", i) for i in range(config.envs)]
    eval_envs = [make("eval", i) for i in range(config.envs)]
    if config.parallel:
        train_envs = [Parallel(env, "process") for env in train_envs]
        eval_envs = [Parallel(env, "process") for env in eval_envs]
    else:
        train_envs = [Damy(env) for env in train_envs]
        eval_envs = [Damy(env) for env in eval_envs]
    acts = train_envs[0].action_space
    print("Action Space", acts)
    config.num_actions = acts.n if hasattr(acts, "n") else acts.shape[0]

    state = None
    if not config.offline_traindir and not config.eval_only:
        prefill = max(0, config.prefill - count_steps(config.traindir))
        print(f"Prefill dataset ({prefill} steps).")
        if hasattr(acts, "discrete"):
            random_actor = tools.OneHotDist(
                torch.zeros(config.num_actions).repeat(config.envs, 1)
            )
        else:
            random_actor = torchd.independent.Independent(
                torchd.uniform.Uniform(
                    torch.tensor(acts.low).repeat(config.envs, 1),
                    torch.tensor(acts.high).repeat(config.envs, 1),
                ),
                1,
            )

        def random_agent(o, d, s):
            action = random_actor.sample()
            logprob = random_actor.log_prob(action)
            return {"action": action, "logprob": logprob}, None

        state = tools.simulate(
            random_agent,
            train_envs,
            train_eps,
            config.traindir,
            logger,
            limit=config.dataset_size,
            steps=prefill,
        )
        logger.step += prefill * config.action_repeat
        print(f"Logger: ({logger.step} steps).")

    print("Simulate agent.")
    train_dataset = make_dataset(train_eps, config)
    eval_dataset = make_dataset(eval_eps, config)
    agent = Dreamer(
        train_envs[0].observation_space,
        train_envs[0].action_space,
        config,
        logger,
        train_dataset,
    ).to(config.device)
    agent.requires_grad_(requires_grad=False)
    checkpoint_path = pathlib.Path(config.policy_checkpoint) if config.policy_checkpoint else logdir / "latest.pt"
    if config.eval_only and not checkpoint_path.is_file():
        raise FileNotFoundError(f"Frozen evaluation requires a trained policy: {checkpoint_path}")
    if checkpoint_path.exists():
        checkpoint = torch.load(checkpoint_path, map_location=config.device, weights_only=False)
        try:
            agent.load_state_dict(checkpoint["agent_state_dict"])
        except RuntimeError as e:
            print(f"[WARN] load_state_dict strict=True failed: {str(e).splitlines()[0]}")
            print("[WARN] Retrying with strict=False (expected when adding new modules).")
            res = agent.load_state_dict(checkpoint["agent_state_dict"], strict=False)
            if config.eval_only:
                missing_policy = [k for k in res.missing_keys if "._dual_stream_unet" not in k]
                if missing_policy or res.unexpected_keys:
                    raise RuntimeError(f"Policy checkpoint mismatch: {missing_policy}, {res.unexpected_keys}")
            if res.missing_keys:
                print(f"[WARN] Missing keys (showing up to 20): {res.missing_keys[:20]}")
            if res.unexpected_keys:
                print(f"[WARN] Unexpected keys (showing up to 20): {res.unexpected_keys[:20]}")
        if not config.eval_only:
            try:
                tools.recursively_load_optim_state_dict(agent, checkpoint["optims_state_dict"])
            except Exception as e:
                print(f"[WARN] Failed to load optimizer state dicts: {e}")
        agent._should_pretrain._once = False
        del checkpoint

    if config.eval_only:
        if config.eval_episode_num < 1:
            raise ValueError("eval_only requires eval_episode_num >= 1")
        agent.eval()
        agent.requires_grad_(False)
        try:
            with torch.no_grad():
                tools.simulate(
                    functools.partial(agent, training=False), eval_envs, eval_eps,
                    config.evaldir, logger, is_eval=True, episodes=config.eval_episode_num,
                )
            print("Frozen evaluation complete; no optimizer updates or policy checkpoint writes.")
        finally:
            logger._writer.close()
            for env in train_envs + eval_envs:
                close = getattr(env, "close", None)
                if close is not None:
                    close()
        return

    # Track best eval return for saving best.pt
    best_eval_return = float("-inf")
    if (logdir / "best.pt").exists() and config.save_best:
        try:
            best_ckpt = torch.load(logdir / "best.pt")
            best_eval_return = best_ckpt.get("eval_return", float("-inf"))
            print(f"Loaded best eval_return: {best_eval_return}")
        except Exception:
            pass

    # make sure eval will be executed once after config.steps
    while agent._step < config.steps + config.eval_every:
        logger.write()
        if config.eval_episode_num > 0:
            print("Start evaluation.")
            eval_policy = functools.partial(agent, training=False)
            eval_result = tools.simulate(
                eval_policy,
                eval_envs,
                eval_eps,
                config.evaldir,
                logger,
                is_eval=True,
                episodes=config.eval_episode_num,
            )
            # Handle new return format: (result, eval_return) or just result
            if isinstance(eval_result, tuple) and len(eval_result) == 2 and isinstance(eval_result[1], (int, float)):
                _, eval_return = eval_result
                if config.save_best and eval_return > best_eval_return:
                    best_eval_return = eval_return
                    items_to_save = {
                        "agent_state_dict": agent.state_dict(),
                        "optims_state_dict": tools.recursively_collect_optim_state_dict(agent),
                        "eval_return": eval_return,
                        "step": agent._step,
                    }
                    torch.save(items_to_save, logdir / "best.pt")
                    print(f"Saved best.pt with eval_return={eval_return:.2f} at step {agent._step}")
            if config.video_pred_log:
                video_pred = agent._wm.video_pred(next(eval_dataset))
                logger.video("eval_openl", to_np(video_pred))
            # Save best model if current eval_return is better
            if logger.last_eval_return is not None and logger.last_eval_return > best_eval_return:
                best_eval_return = logger.last_eval_return
                best_items_to_save = {
                    "agent_state_dict": agent.state_dict(),
                    "optims_state_dict": tools.recursively_collect_optim_state_dict(agent),
                    "best_eval_return": best_eval_return,
                    "step": agent._step,
                }
                torch.save(best_items_to_save, logdir / "best.pt")
                print(f"Saved best model with eval_return: {best_eval_return:.2f} at step {agent._step}")
        print("Start training.")
        state = tools.simulate(
            agent,
            train_envs,
            train_eps,
            config.traindir,
            logger,
            limit=config.dataset_size,
            steps=config.eval_every,
            state=state,
        )
        items_to_save = {
            "agent_state_dict": agent.state_dict(),
            "optims_state_dict": tools.recursively_collect_optim_state_dict(agent),
        }
        torch.save(items_to_save, logdir / "latest.pt")
    for env in train_envs + eval_envs:
        try:
            env.close()
        except Exception:
            pass
    if wandb_run is not None:
        try:
            wandb_run.finish()
        except Exception:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--configs", nargs="+")
    args, remaining = parser.parse_known_args()
    configs = _yaml_load(
        (pathlib.Path(sys.argv[0]).parent / "configs.yaml").read_text()
    )

    def recursive_update(base, update):
        for key, value in update.items():
            if isinstance(value, dict) and key in base:
                recursive_update(base[key], value)
            else:
                base[key] = value

    name_list = ["defaults", *args.configs] if args.configs else ["defaults"]
    defaults = {}
    for name in name_list:
        recursive_update(defaults, configs[name])
    parser = argparse.ArgumentParser()
    for key, value in sorted(defaults.items(), key=lambda x: x[0]):
        arg_type = tools.args_type(value)
        parser.add_argument(f"--{key}", type=arg_type, default=arg_type(value))
    main(parser.parse_args(remaining))
