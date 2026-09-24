"""
Generate the VDCS-style segmentation H5 dataset used to pretrain ACO-MoE.

For each (task, degradation) pair, render the clean DMC frame and the
MuJoCo geom segmentation; apply a corruption operator from
envs.visual_degradations to the clean frame; save an H5 sample with the
clean frame, the corrupted frame, the foreground-only frame, and the
binary foreground mask.

Output layout:
  <out>/<task>_vdcs_seg64/<degradation>/*.h5
  <out>/<task>_vdcs_seg64_split/{train,val}/<degradation>/*.h5  (symlinks)
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

os.environ.setdefault("MUJOCO_GL", "egl")

import numpy as np
from tqdm import tqdm

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _expert_degradation_configs():
    from envs.visual_degradations import (
        RainDegradation,
        FogDegradation,
        SnowDegradation,
        MotionBlurDegradation,
        GaussianNoiseDegradation,
        LowLightDegradation,
        JPEGCompressionDegradation,
    )

    return {
        "rain_medium": {"cls": RainDegradation, "intensity": 0.6},
        "fog_medium": {"cls": FogDegradation, "intensity": 0.6},
        "snow_medium": {"cls": SnowDegradation, "intensity": 0.6},
        "motion_blur": {"cls": MotionBlurDegradation, "intensity": 0.35},
        "gaussian_noise": {"cls": GaussianNoiseDegradation, "intensity": 0.5},
        "low_light": {"cls": LowLightDegradation, "intensity": 0.7},
        "jpeg_compression": {"cls": JPEGCompressionDegradation, "intensity": 0.7},
    }


DMC_TASKS_DEFAULT = [
    "cartpole_swingup",
    "finger_spin",
    "hopper_stand",
    "hopper_hop",
    "cheetah_run",
    "walker_walk",
    "walker_run",
]


def _as_chw(img_hwc: np.ndarray) -> np.ndarray:
    return np.transpose(img_hwc, (2, 0, 1))


def _compute_keep_geom_non_world(physics) -> np.ndarray:
    model = physics.model
    try:
        world_body_id = int(model.name2id("world", "body"))
    except Exception:
        world_body_id = 0
    geom_bodyid = np.asarray(model.geom_bodyid, dtype=np.int32)
    return geom_bodyid != int(world_body_id)


def _render_segmentation(env, size: Tuple[int, int]) -> np.ndarray:
    h, w = int(size[0]), int(size[1])
    return env._env.physics.render(h, w, camera_id=int(env._camera), segmentation=True)


def _mask_from_seg_keep_geom(seg: np.ndarray, keep_geom: np.ndarray) -> np.ndarray:
    geom_id = seg[..., 0]
    mask = np.zeros_like(geom_id, dtype=np.uint8)
    valid = geom_id >= 0
    if np.any(valid):
        mask[valid] = keep_geom[geom_id[valid]].astype(np.uint8)
    return mask


def _write_sample_h5(path: Path, *, haze, gt, gt_agent_only, mask01,
                     task, degradation, intensity, seed, action_repeat):
    import h5py

    path.parent.mkdir(parents=True, exist_ok=True)
    with h5py.File(path, "w") as f:
        f.create_dataset("haze", data=_as_chw(haze), dtype=np.uint8)
        f.create_dataset("gt", data=_as_chw(gt), dtype=np.uint8)
        f.create_dataset("gt_agent_only", data=_as_chw(gt_agent_only), dtype=np.uint8)
        f.create_dataset("mask", data=mask01[None, ...], dtype=np.uint8)
        f.attrs["task"] = str(task)
        f.attrs["degradation"] = str(degradation)
        f.attrs["degradation_intensity"] = float(intensity)
        f.attrs["seed"] = int(seed)
        f.attrs["action_repeat"] = int(action_repeat)


def _sample_intensity(base: float, rng: np.random.RandomState, jitter_frac: float = 0.10) -> float:
    scale = float(rng.uniform(1.0 - jitter_frac, 1.0 + jitter_frac))
    return float(np.clip(base * scale, 0.0, 1.0))


def _create_symlink(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() or dst.is_symlink():
        dst.unlink()
    try:
        os.symlink(str(src.resolve()), str(dst))
    except OSError:
        # Windows may require elevated privileges for symlinks. Copies retain
        # the same deterministic split and do not require changing OS settings.
        shutil.copy2(src, dst)


def _split_train_val(base_root: Path, split_root: Path,
                     degradation_types: Sequence[str], train_ratio: float) -> None:
    if split_root.exists():
        shutil.rmtree(split_root)
    for deg in degradation_types:
        files = sorted((base_root / deg).glob("*.h5"))
        n_train = int(len(files) * float(train_ratio))
        for f in files[:n_train]:
            _create_symlink(f, split_root / "train" / deg / f.name)
        for f in files[n_train:]:
            _create_symlink(f, split_root / "val" / deg / f.name)


def _collect_clean_frames(task, *, num_samples, size, action_repeat,
                           seed, max_episode_steps):
    from envs.dmc import DMC

    rng = np.random.RandomState(seed)
    env = DMC(task, action_repeat=action_repeat, size=size, seed=seed)
    keep_geom = _compute_keep_geom_non_world(env._env.physics)

    images, masks = [], []
    obs = env.reset()
    episode_steps = 0
    pbar = tqdm(total=num_samples, desc=f"clean/{task}", unit="frame")
    try:
        while len(images) < num_samples:
            if episode_steps >= max_episode_steps:
                obs = env.reset()
                episode_steps = 0
            img = np.asarray(obs["image"], dtype=np.uint8)
            seg = _render_segmentation(env, size)
            mask01 = _mask_from_seg_keep_geom(seg, keep_geom)
            images.append(img)
            masks.append(mask01)
            pbar.update(1)
            action = rng.uniform(-1, 1, size=env.action_space.shape).astype(np.float32)
            obs, *_ = env.step(action)
            episode_steps += 1
    finally:
        pbar.close()
        if hasattr(env, "close"):
            env.close()
    return np.stack(images, 0), np.stack(masks, 0)


def generate_task_dataset(task, *, out_h5_dir: Path, samples_per_task: int,
                           size, action_repeat, seed, max_episode_steps,
                           train_ratio: float, overwrite: bool):
    configs = _expert_degradation_configs()
    height, width = (int(size[0]), int(size[1]))
    size_tag = f"{height}" if height == width else f"{height}x{width}"
    base_root = out_h5_dir / f"{task}_vdcs_seg{size_tag}"
    split_root = out_h5_dir / f"{task}_vdcs_seg{size_tag}_split"

    if base_root.exists():
        if overwrite:
            shutil.rmtree(base_root)
        else:
            raise FileExistsError(f"Output exists: {base_root} (use --overwrite)")

    clean_imgs, masks01 = _collect_clean_frames(
        task, num_samples=samples_per_task, size=size,
        action_repeat=action_repeat, seed=seed, max_episode_steps=max_episode_steps,
    )

    for deg_idx, (deg_name, cfg) in enumerate(configs.items()):
        deg = cfg["cls"](intensity=cfg["intensity"], seed=seed)
        rng_int = np.random.RandomState(seed + 10007 + deg_idx * 1000)
        out_dir = base_root / deg_name
        out_dir.mkdir(parents=True, exist_ok=True)

        pbar = tqdm(total=samples_per_task, desc=f"write/{task}/{deg_name}", unit="file")
        try:
            for idx in range(samples_per_task):
                gt = clean_imgs[idx]
                mask01 = masks01[idx]
                gt_agent_only = (gt * mask01[..., None]).astype(np.uint8)
                intensity = _sample_intensity(float(cfg["intensity"]), rng_int, 0.10)
                deg.intensity = intensity
                haze = deg.apply(gt)
                _write_sample_h5(
                    out_dir / f"{idx:05d}.h5",
                    haze=haze, gt=gt, gt_agent_only=gt_agent_only, mask01=mask01,
                    task=task, degradation=deg_name, intensity=intensity,
                    seed=seed, action_repeat=action_repeat,
                )
                pbar.update(1)
        finally:
            pbar.close()

    _split_train_val(base_root, split_root,
                     list(configs.keys()), train_ratio)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_h5_dir", type=str, required=True,
                        help="Output root, e.g. data/h5")
    parser.add_argument("--tasks", type=str, default=",".join(DMC_TASKS_DEFAULT))
    parser.add_argument("--samples_per_task", type=int, default=500)
    parser.add_argument("--size", type=int, nargs=2, default=[64, 64])
    parser.add_argument("--action_repeat", type=int, default=2)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--max_episode_steps", type=int, default=100)
    parser.add_argument("--train_ratio", type=float, default=0.9)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    tasks = [t.strip() for t in str(args.tasks).split(",") if t.strip()]
    if not tasks:
        raise ValueError("No tasks provided")

    out_h5_dir = Path(args.out_h5_dir)
    out_h5_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("VDCS Segmentation H5 Dataset Generation")
    print("=" * 80)
    print(f"Out dir:       {out_h5_dir}")
    print(f"Tasks:         {tasks}")
    print(f"Samples/task:  {args.samples_per_task}")
    print(f"Image size:    {tuple(args.size)}")
    print("=" * 80)

    for task in tasks:
        generate_task_dataset(
            task, out_h5_dir=out_h5_dir,
            samples_per_task=int(args.samples_per_task),
            size=tuple(args.size),
            action_repeat=int(args.action_repeat),
            seed=int(args.seed),
            max_episode_steps=int(args.max_episode_steps),
            train_ratio=float(args.train_ratio),
            overwrite=bool(args.overwrite),
        )
        print(f"[OK] {task}")

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
