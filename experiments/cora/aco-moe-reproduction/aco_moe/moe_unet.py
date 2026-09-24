"""
Dual-stream MoE-UNet (the ACO-MoE adapter) for visual restoration +
foreground segmentation.

Architecture:
  - Shared U-Net encoder (multi-scale feature pyramid)
  - Router on bottleneck features -> soft routing weights over experts
  - Stream 1: RGB decoder experts -> restored RGB
  - Stream 2: Mask decoder experts -> foreground mask logits (2-way)
  - Final: agent_only_rgb = restored_rgb * foreground_prob

LABEL-FREE INTERFACE
--------------------
The forward signature exposes a few optional knobs (`degradation_ids`,
`teacher_force_router`, `router_override_probs`, `task_ids`) that exist
purely so that *ablation* runs can reproduce the supervised-router
baseline. None of them is required.

In particular:

  * The DEFAULT call signature is `model(degraded)`. With this call the
    network needs ONLY the corrupted RGB tensor; it never sees a
    corruption type, a corruption count, a clean reference, or a task id.
  * `num_experts` is an architectural capacity hyperparameter. It is not
    interpreted as the number of corruption modes and the experts are
    never assigned to fixed corruption categories.
  * At inference time inside the DreamerV3 backbone (see `models.py`) we
    again call the adapter with RGB only -- the inference path does not
    pass `degradation_ids` and never can.

All tensors are expected in [-1, 1] range for RGB streams.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F


class DoubleConv(nn.Module):
    def __init__(self, in_channels: int, out_channels: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.SiLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.SiLU(inplace=True),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


class Down(nn.Module):
    def __init__(self, in_channels: int, out_channels: int):
        super().__init__()
        self.net = nn.Sequential(nn.MaxPool2d(2), DoubleConv(in_channels, out_channels))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


class Up(nn.Module):
    def __init__(self, in_channels: int, out_channels: int):
        super().__init__()
        self.up = nn.Upsample(scale_factor=2, mode="bilinear", align_corners=True)
        self.conv = DoubleConv(in_channels, out_channels)

    def forward(self, x: torch.Tensor, skip: torch.Tensor) -> torch.Tensor:
        x = self.up(x)
        diff_y = skip.size(2) - x.size(2)
        diff_x = skip.size(3) - x.size(3)
        x = F.pad(x, [diff_x // 2, diff_x - diff_x // 2, diff_y // 2, diff_y - diff_y // 2])
        x = torch.cat([skip, x], dim=1)
        return self.conv(x)


@dataclass(frozen=True)
class EncoderFeatures:
    skips: List[torch.Tensor]
    bottleneck: torch.Tensor


class UNetEncoder(nn.Module):
    def __init__(self, in_channels: int = 3, base_channels: int = 64, depth: int = 4):
        super().__init__()
        if depth != 4:
            raise ValueError("Only depth=4 is supported for now (64x64 -> 4x4 bottleneck).")
        c1 = base_channels
        c2 = base_channels * 2
        c3 = base_channels * 4
        c4 = base_channels * 8
        c5 = base_channels * 16

        self.inc = DoubleConv(in_channels, c1)
        self.down1 = Down(c1, c2)
        self.down2 = Down(c2, c3)
        self.down3 = Down(c3, c4)
        self.down4 = Down(c4, c5)

        self.out_channels = c5
        self.skip_channels = [c1, c2, c3, c4]

    def forward(self, x: torch.Tensor) -> EncoderFeatures:
        x1 = self.inc(x)
        x2 = self.down1(x1)
        x3 = self.down2(x2)
        x4 = self.down3(x3)
        x5 = self.down4(x4)
        return EncoderFeatures(skips=[x1, x2, x3, x4], bottleneck=x5)


class UNetDecoder(nn.Module):
    def __init__(self, out_channels: int, base_channels: int = 64):
        super().__init__()
        c1 = base_channels
        c2 = base_channels * 2
        c3 = base_channels * 4
        c4 = base_channels * 8
        c5 = base_channels * 16

        self.up1 = Up(c5 + c4, c4)
        self.up2 = Up(c4 + c3, c3)
        self.up3 = Up(c3 + c2, c2)
        self.up4 = Up(c2 + c1, c1)
        self.outc = nn.Conv2d(c1, out_channels, kernel_size=1)

    def forward(self, bottleneck: torch.Tensor, skips: List[torch.Tensor]) -> torch.Tensor:
        x1, x2, x3, x4 = skips
        x = self.up1(bottleneck, x4)
        x = self.up2(x, x3)
        x = self.up3(x, x2)
        x = self.up4(x, x1)
        return self.outc(x)


class UNetDecoderFeatures(nn.Module):
    def __init__(self, base_channels: int = 64):
        super().__init__()
        c1 = base_channels
        c2 = base_channels * 2
        c3 = base_channels * 4
        c4 = base_channels * 8
        c5 = base_channels * 16

        self.up1 = Up(c5 + c4, c4)
        self.up2 = Up(c4 + c3, c3)
        self.up3 = Up(c3 + c2, c2)
        self.up4 = Up(c2 + c1, c1)

    def forward(self, bottleneck: torch.Tensor, skips: List[torch.Tensor]) -> torch.Tensor:
        x1, x2, x3, x4 = skips
        x = self.up1(bottleneck, x4)
        x = self.up2(x, x3)
        x = self.up3(x, x2)
        x = self.up4(x, x1)
        return x


class BottleneckRouter(nn.Module):
    def __init__(self, in_channels: int, num_experts: int, hidden: int = 256):
        super().__init__()
        self.num_experts = int(num_experts)
        self.pool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc1 = nn.Linear(int(in_channels), int(hidden))
        self.fc2 = nn.Linear(int(hidden), int(num_experts))

    def forward(self, bottleneck: torch.Tensor) -> torch.Tensor:
        x = self.pool(bottleneck).flatten(1)
        x = F.silu(self.fc1(x))
        return self.fc2(x)


class DualStreamMoEUNet(nn.Module):
    def __init__(
        self,
        *,
        in_channels: int = 3,
        base_channels: int = 64,
        num_experts: int = 7,
        router_hidden: int = 256,
        learn_residual_rgb: bool = True,
        task_conditioned_mask: bool = False,
        num_tasks: int = 0,
        special_rgb_expert_id: Optional[int] = None,
        special_rgb_checkpoint: Optional[str] = None,
        freeze_special_rgb_expert: bool = True,
    ):
        super().__init__()
        self.num_experts = int(num_experts)
        self.learn_residual_rgb = bool(learn_residual_rgb)
        self.special_rgb_expert_id = int(special_rgb_expert_id) if special_rgb_expert_id is not None else None
        self.task_conditioned_mask = bool(task_conditioned_mask)
        self.num_tasks = int(num_tasks)
        if self.task_conditioned_mask and self.num_tasks <= 0:
            raise ValueError("num_tasks must be > 0 when task_conditioned_mask=True")

        self.encoder = UNetEncoder(in_channels=in_channels, base_channels=base_channels, depth=4)
        self.router = BottleneckRouter(
            in_channels=self.encoder.out_channels, num_experts=self.num_experts, hidden=router_hidden
        )

        self.rgb_experts = nn.ModuleList(
            [UNetDecoder(out_channels=3, base_channels=base_channels) for _ in range(self.num_experts)]
        )
        if self.task_conditioned_mask:
            # Task-conditioned mask head: share mask decoder features; only last 1x1 is per-task.
            self.mask_experts = nn.ModuleList(
                [UNetDecoderFeatures(base_channels=base_channels) for _ in range(self.num_experts)]
            )
            self.task_mask_heads = nn.ModuleList(
                [nn.Conv2d(int(base_channels), 2, kernel_size=1) for _ in range(self.num_tasks)]
            )
            self.mask_out = None
        else:
            # Default behavior: each expert predicts its own mask logits (original design).
            self.mask_experts = nn.ModuleList(
                [UNetDecoder(out_channels=2, base_channels=base_channels) for _ in range(self.num_experts)]
            )
            self.task_mask_heads = None
            self.mask_out = None

        # Optional: a full U-Net expert for a specific degradation (e.g., motion_blur),
        # without sharing the encoder/decoder with the MoE backbone.
        self.special_rgb_unet: Optional[nn.Module] = None
        if self.special_rgb_expert_id is not None:
            if not (0 <= self.special_rgb_expert_id < self.num_experts):
                raise ValueError(f"special_rgb_expert_id must be in [0,{self.num_experts}), got {self.special_rgb_expert_id}")
            if special_rgb_checkpoint:
                self._init_special_rgb_unet(str(special_rgb_checkpoint), freeze=bool(freeze_special_rgb_expert))

    def _init_special_rgb_unet(self, checkpoint_path: str, *, freeze: bool) -> None:
        from aco_moe.simple_unet import get_unet

        unet = get_unet(n_channels=3, n_classes=3, learn_residual=True)
        ckpt = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
        if isinstance(ckpt, dict) and "model_state_dict" in ckpt:
            state = ckpt["model_state_dict"]
        else:
            state = ckpt
        unet.load_state_dict(state, strict=True)
        if freeze:
            for p in unet.parameters():
                p.requires_grad = False
            unet.eval()
        self.special_rgb_unet = unet

    def forward(
        self,
        degraded: torch.Tensor,
        router_override_probs: torch.Tensor | None = None,
        degradation_ids: torch.Tensor | None = None,
        teacher_force_router: bool = False,
        task_ids: torch.Tensor | None = None,
        router_topk: int = 0,
    ):
        """
        The DEFAULT call is `forward(degraded)` -- the network requires
        ONLY the corrupted RGB tensor. The remaining keyword arguments
        exist for ablations and are NOT used in the paper's main
        configuration:

        Args:
            degraded: [B, 3, H, W] in [-1, 1]. The only required input.
            router_override_probs: optional explicit routing weights
                (analysis / debugging only; takes precedence over the
                learned router output).
            degradation_ids: [B] integer corruption-type ids. Used ONLY
                when `teacher_force_router=True`; the label-free main
                config never passes this.
            teacher_force_router: ABLATION ONLY. When True, replaces the
                learned router output with one-hot(degradation_ids).
            task_ids: optional task ids for the (off-by-default) task-
                conditioned mask head. Not used at downstream inference.
            router_topk: 0 = soft mixture (training default), 1 = hard
                top-1 selection (inference default).

        Returns dict:
            agent_only_rgb: [B, 3, H, W] in [-1, 1]
            restored_rgb:   [B, 3, H, W] in [-1, 1]
            mask_logits:    [B, 2, H, W] (unnormalized)
            router_logits:  [B, K]
            router_probs:   [B, K]
            foreground_prob:[B, 1, H, W] in [0, 1]
        """
        feats = self.encoder(degraded)
        router_logits = self.router(feats.bottleneck)
        router_probs = F.softmax(router_logits, dim=-1)
        routing_weights = router_probs
        if bool(teacher_force_router) and degradation_ids is not None:
            if degradation_ids.ndim != 1 or degradation_ids.shape[0] != router_logits.shape[0]:
                raise ValueError(f"degradation_ids must have shape [B], got {tuple(degradation_ids.shape)}")
            if degradation_ids.dtype not in (torch.int32, torch.int64) or degradation_ids.device != router_logits.device:
                degradation_ids = degradation_ids.to(device=router_logits.device, dtype=torch.int64)
            routing_weights = F.one_hot(degradation_ids, num_classes=self.num_experts).to(router_logits.dtype)
        if router_override_probs is not None:
            if router_override_probs.shape != router_probs.shape:
                raise ValueError(
                    f"router_override_probs must have shape {tuple(router_probs.shape)}, got {tuple(router_override_probs.shape)}"
                )
            routing_weights = router_override_probs.to(device=router_logits.device, dtype=router_logits.dtype)

        if int(router_topk) == 1:
            chosen = routing_weights.argmax(dim=1)
            routing_weights = F.one_hot(chosen, num_classes=self.num_experts).to(router_logits.dtype)

            rgb_out = None
            mask_out = None
            batch = degraded.shape[0]
            for i in range(self.num_experts):
                idx = (chosen == i).nonzero(as_tuple=True)[0]
                if idx.numel() == 0:
                    continue
                bottleneck_i = feats.bottleneck[idx]
                skips_i = [s[idx] for s in feats.skips]

                # RGB stream
                if self.special_rgb_unet is not None and self.special_rgb_expert_id == i:
                    rgb_i = self.special_rgb_unet(degraded[idx])
                else:
                    rgb_logits_i = self.rgb_experts[i](bottleneck_i, skips_i)
                    rgb_i = torch.tanh(rgb_logits_i)
                    if self.learn_residual_rgb:
                        rgb_i = torch.clamp(degraded[idx] + rgb_i, -1.0, 1.0)

                if rgb_out is None:
                    rgb_out = torch.zeros((batch,) + rgb_i.shape[1:], device=rgb_i.device, dtype=rgb_i.dtype)
                rgb_out[idx] = rgb_i

                mask_i = self.mask_experts[i](bottleneck_i, skips_i)
                if mask_out is None:
                    mask_out = torch.zeros((batch,) + mask_i.shape[1:], device=mask_i.device, dtype=mask_i.dtype)
                mask_out[idx] = mask_i

            restored_rgb = torch.clamp(rgb_out, -1.0, 1.0)
            mask_mix = mask_out
        else:
            rgb_preds: List[torch.Tensor] = []
            mask_outputs: List[torch.Tensor] = []
            for i in range(self.num_experts):
                # RGB stream
                if self.special_rgb_unet is not None and self.special_rgb_expert_id == i:
                    # Full U-Net expert (already returns [-1,1] with residual).
                    rgb_i = self.special_rgb_unet(degraded)
                else:
                    rgb_logits_i = self.rgb_experts[i](feats.bottleneck, feats.skips)
                    rgb_i = torch.tanh(rgb_logits_i)
                    if self.learn_residual_rgb:
                        rgb_i = torch.clamp(degraded + rgb_i, -1.0, 1.0)
                rgb_preds.append(rgb_i)

                mask_outputs.append(self.mask_experts[i](feats.bottleneck, feats.skips))

            rgb_stack_t = torch.stack(rgb_preds, dim=1)  # [B,K,3,H,W] in [-1,1]
            mask_stack_t = torch.stack(mask_outputs, dim=1)  # [B,K,*,H,W]

            w = routing_weights[:, :, None, None, None]
            restored_rgb = torch.sum(w * rgb_stack_t, dim=1)
            restored_rgb = torch.clamp(restored_rgb, -1.0, 1.0)
            mask_mix = torch.sum(w * mask_stack_t, dim=1)  # [B,2,H,W] or [B,C,H,W]

        if self.task_conditioned_mask:
            if task_ids is None:
                raise ValueError("task_ids is required when task_conditioned_mask=True")
            if task_ids.ndim != 1 or task_ids.shape[0] != mask_mix.shape[0]:
                raise ValueError(f"task_ids must have shape [B], got {tuple(task_ids.shape)}")
            if task_ids.dtype not in (torch.int32, torch.int64):
                task_ids = task_ids.to(torch.int64)

            mask_logits = torch.zeros(
                (mask_mix.shape[0], 2, mask_mix.shape[2], mask_mix.shape[3]),
                device=mask_mix.device,
                dtype=mask_mix.dtype,
            )
            for t in torch.unique(task_ids).tolist():
                if not (0 <= int(t) < self.num_tasks):
                    raise ValueError(f"Invalid task id {t}, expected in [0,{self.num_tasks})")
                idx = (task_ids == int(t)).nonzero(as_tuple=True)[0]
                if idx.numel() == 0:
                    continue
                head_out = self.task_mask_heads[int(t)](mask_mix[idx])
                if head_out.dtype != mask_logits.dtype:
                    head_out = head_out.to(mask_logits.dtype)
                mask_logits[idx] = head_out
        else:
            mask_logits = mask_mix

        foreground_prob = F.softmax(mask_logits, dim=1)[:, 1:2]  # [B,1,H,W]
        black_bg = -torch.ones_like(restored_rgb)
        agent_only_rgb = torch.clamp(restored_rgb * foreground_prob + black_bg * (1.0 - foreground_prob), -1.0, 1.0)
        foreground_hard = (foreground_prob >= 0.5).to(restored_rgb.dtype)
        agent_only_rgb_hard = torch.clamp(restored_rgb * foreground_hard + black_bg * (1.0 - foreground_hard), -1.0, 1.0)
        # Ablation used by the paper's "w/o Repair" condition: retain the
        # predicted hard foreground mask but apply it to the corrupted input
        # instead of the restored RGB stream.
        agent_only_input_hard = torch.clamp(
            degraded * foreground_hard + black_bg * (1.0 - foreground_hard),
            -1.0,
            1.0,
        )

        return {
            "agent_only_rgb": agent_only_rgb,
            "agent_only_rgb_hard": agent_only_rgb_hard,
            "agent_only_input_hard": agent_only_input_hard,
            "restored_rgb": restored_rgb,
            "mask_logits": mask_logits,
            "router_logits": router_logits,
            "router_probs": routing_weights,
            "foreground_prob": foreground_prob,
            "foreground_hard": foreground_hard,
        }
