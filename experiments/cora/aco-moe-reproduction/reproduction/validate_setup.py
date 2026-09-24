#!/usr/bin/env python3
"""Fail-fast validation for the paper-oriented experiment package."""

from __future__ import annotations

import importlib
from pathlib import Path
import sys

import torch
from ruamel.yaml import YAML

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from aco_moe.moe_unet import DualStreamMoEUNet


REQUIRED_CONFIGS = {
    "paper_dmc_vision",
    "paper_vdcs_markov",
    "paper_vdcs_static",
    "paper_aco",
    "paper_agent_oracle",
    "paper_dmcgb_color_hard",
    "paper_dmcgb_video_hard",
}


def parameter_count(model: torch.nn.Module) -> int:
    return sum(p.numel() for p in model.parameters())


def main() -> int:
    for module in ("dm_control", "gym", "cv2", "h5py", "PIL"):
        importlib.import_module(module)
        print(f"[OK] import {module}")

    from envs.dmc import DeepMindControl

    env = DeepMindControl("cartpole_swingup", action_repeat=2, size=(84, 84), seed=0)
    observation = env.reset()
    if tuple(observation["image"].shape) != (84, 84, 3):
        raise RuntimeError(f"Unexpected rendered image shape: {observation['image'].shape}")
    env.close()
    print("[OK] EGL/MuJoCo 84x84 render")

    configs = YAML(typ="safe").load(Path("configs.yaml").read_text(encoding="utf-8"))
    missing = sorted(REQUIRED_CONFIGS.difference(configs))
    if missing:
        raise RuntimeError(f"Missing reproduction config profiles: {missing}")

    full = DualStreamMoEUNet(base_channels=9, num_experts=9, router_hidden=256)
    full_params = parameter_count(full)
    if full_params != 4_884_961:
        raise RuntimeError(f"Unexpected full ACO parameter count: {full_params}")
    with torch.inference_mode():
        output = full(torch.zeros(1, 3, 84, 84), router_topk=1)
    expected = (1, 3, 84, 84)
    for key in ("restored_rgb", "agent_only_rgb_hard", "agent_only_input_hard"):
        if tuple(output[key].shape) != expected:
            raise RuntimeError(f"Unexpected {key} shape: {tuple(output[key].shape)}")
    del full, output

    single = DualStreamMoEUNet(base_channels=21, num_experts=1, router_hidden=256)
    single_params = parameter_count(single)
    ratio = single_params / full_params
    if not 0.95 <= ratio <= 1.05:
        raise RuntimeError(
            f"Single-expert capacity mismatch: {single_params} vs {full_params} ({ratio:.3f})"
        )

    print(f"[OK] full ACO parameters:   {full_params:,}")
    print(f"[OK] single parameters:     {single_params:,} ({ratio:.2%} of full)")
    print(f"[OK] torch:                 {torch.__version__}")
    print(f"[OK] CUDA available:        {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"[OK] visible CUDA devices:  {torch.cuda.device_count()}")
        for index in range(torch.cuda.device_count()):
            props = torch.cuda.get_device_properties(index)
            print(f"     cuda:{index}: {props.name}, {props.total_memory / 2**30:.1f} GiB")
    print("Preflight validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
