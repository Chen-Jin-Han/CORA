"""
Train ACO-MoE adapter on the offline VDCS H5 dataset.

LABEL-FREE CONTRACT
-------------------
By default this script trains ACO-MoE WITHOUT any corruption-type label
supervision and WITHOUT any corruption-count prior:

  * The router receives no cross-entropy supervision against degradation
    labels (`lambda_router = 0`).
  * The model is called WITHOUT `degradation_ids`; teacher forcing is OFF.
    Routing is therefore learned purely end-to-end through the soft expert
    mixture and the downstream RGB / mask / agent-only-composition losses.
  * The number of experts `num_experts` is an ARCHITECTURAL hyperparameter
    -- it does NOT have to equal the number of degradation directories on
    disk and is not interpreted as a corruption-mode count.
  * At inference time the network only consumes corrupted RGB. No label,
    count, or task metadata is required.

The optional ablation flag `--use_label_supervision` turns the router-CE
loss and teacher forcing back on (this reproduces the supervised-router
ablation reported in the paper). It is OFF by default.

H5 sample layout:
  - haze          uint8 [3, H, W]  (corrupted RGB)
  - gt            uint8 [3, H, W]  (clean RGB)
  - gt_agent_only uint8 [3, H, W]  (clean foreground on black background)
  - mask          uint8 [1, H, W]  (0/1 foreground mask)

Files are read recursively from each `data_root/{train,val}/`. The
on-disk subdirectory layout is irrelevant to the loss; corruption labels
are inferred only for analysis logging and only used as supervision when
`--use_label_supervision` is passed.
"""

from __future__ import annotations

import argparse
import glob
import sys
import time
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from torch.utils.tensorboard import SummaryWriter

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from aco_moe.moe_unet import DualStreamMoEUNet


DEFAULT_DEGRADATION_HINTS = [
    "rain_medium",
    "fog_medium",
    "snow_medium",
    "motion_blur",
    "gaussian_noise",
    "low_light",
    "jpeg_compression",
]


class RandomHorizontalFlipAll:
    def __init__(self, p: float = 0.5):
        self.p = float(p)

    def __call__(self, degraded, clean, agent_only, mask):
        if np.random.rand() < self.p:
            degraded = np.flip(degraded, axis=2).copy()
            clean = np.flip(clean, axis=2).copy()
            agent_only = np.flip(agent_only, axis=2).copy()
            mask = np.flip(mask, axis=1).copy()
        return degraded, clean, agent_only, mask


class VDCSH5Dataset(Dataset):
    """Loads (degraded, clean, agent_only, mask) tuples from H5 samples.

    The dataset emits a degradation-name string per sample (parsed from the
    parent directory name) but DOES NOT use it for supervision -- it is
    only attached to the batch so that downstream analytics can group
    samples for diagnostic logging.
    """

    def __init__(
        self,
        root_dirs: Sequence[str],
        *,
        normalize: bool = True,
        transform=None,
    ):
        self.normalize = bool(normalize)
        self.transform = transform
        self.files: List[Tuple[str, str]] = []  # (h5_path, deg_name_for_logging)
        for root in [Path(r) for r in root_dirs]:
            for path in sorted(glob.glob(str(root / "**" / "*.h5"), recursive=True)):
                deg_name = Path(path).parent.name
                self.files.append((path, deg_name))

        if not self.files:
            raise ValueError(f"No .h5 files found under any of: {list(root_dirs)}")

        # Derive a deterministic name->id table for analysis ONLY.
        seen: List[str] = []
        for _, name in self.files:
            if name not in seen:
                seen.append(name)
        self.deg_names: List[str] = seen
        self._deg_to_id = {n: i for i, n in enumerate(seen)}

    def __len__(self) -> int:
        return len(self.files)

    def __getitem__(self, idx: int):
        import h5py

        path, deg_name = self.files[idx]
        with h5py.File(path, "r") as f:
            degraded = f["haze"][:]
            clean = f["gt"][:]
            agent_only = f["gt_agent_only"][:]
            mask = f["mask"][:]

        degraded = degraded.astype(np.float32) / 255.0
        clean = clean.astype(np.float32) / 255.0
        agent_only = agent_only.astype(np.float32) / 255.0
        mask = mask[0].astype(np.int64)

        if self.transform:
            degraded, clean, agent_only, mask = self.transform(
                degraded, clean, agent_only, mask
            )

        if self.normalize:
            degraded = degraded * 2.0 - 1.0
            clean = clean * 2.0 - 1.0
            agent_only = agent_only * 2.0 - 1.0

        # `deg_meta` is metadata only -- the model never sees it in the
        # default label-free configuration.
        deg_meta = int(self._deg_to_id.get(deg_name, -1))
        return (
            torch.from_numpy(degraded),
            torch.from_numpy(clean),
            torch.from_numpy(agent_only),
            torch.from_numpy(mask),
            torch.tensor(deg_meta, dtype=torch.long),
        )


def _to_uint8(img: torch.Tensor) -> np.ndarray:
    x = (img.detach().float().cpu() + 1.0) * 0.5
    x = torch.clamp(x, 0.0, 1.0)
    x = (x * 255.0).round().to(torch.uint8).numpy()
    return np.transpose(x, (1, 2, 0))


def _prob_to_uint8(prob: torch.Tensor) -> np.ndarray:
    p = (prob.detach().float().cpu().clamp(0, 1) * 255.0).to(torch.uint8).numpy()[0]
    return np.stack([p, p, p], axis=-1)


def _save_vis(out_path: Path, degraded, restored, gt, pred_mask_prob, agent_only):
    from PIL import Image

    out_path.parent.mkdir(parents=True, exist_ok=True)
    cols = [
        _to_uint8(degraded),
        _to_uint8(restored),
        _to_uint8(gt),
        _prob_to_uint8(pred_mask_prob),
        _to_uint8(agent_only),
    ]
    Image.fromarray(np.concatenate(cols, axis=1)).save(out_path)


def parse_args():
    p = argparse.ArgumentParser(
        description=(
            "Train ACO-MoE. The default configuration is LABEL-FREE: no "
            "corruption labels are passed to the model and no router-CE "
            "loss is applied. Use --use_label_supervision to reproduce the "
            "supervised-router ablation."
        )
    )
    p.add_argument(
        "--data_roots",
        type=str,
        required=True,
        help="Comma-separated dataset roots, each containing train/ and val/.",
    )
    p.add_argument(
        "--num_experts",
        type=int,
        default=7,
        help=(
            "Architectural number of experts. NOT a corruption-mode count: "
            "it does not have to equal the number of degradation types in "
            "your dataset and is never used as a class label."
        ),
    )
    p.add_argument("--base_channels", type=int, default=64)
    p.add_argument("--router_hidden", type=int, default=256)

    p.add_argument("--batch_size", type=int, default=64)
    p.add_argument("--val_batch_size", type=int, default=64)
    p.add_argument(
        "--grad_accum_steps",
        type=int,
        default=1,
        help="Accumulate this many micro-batches per optimizer step.",
    )
    p.add_argument(
        "--amp",
        action="store_true",
        help="Use CUDA automatic mixed precision (bfloat16 on supported GPUs).",
    )
    p.add_argument("--lr", type=float, default=1e-4)
    p.add_argument("--weight_decay", type=float, default=1e-4)
    p.add_argument("--num_workers", type=int, default=4)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--cuda", action="store_true", default=True)

    p.add_argument("--steps", type=int, default=20000)
    p.add_argument("--print_freq", type=int, default=100)
    p.add_argument("--val_freq", type=int, default=500)
    p.add_argument("--save_freq", type=int, default=1000)
    p.add_argument("--vis_freq", type=int, default=500)

    p.add_argument("--lambda_rgb", type=float, default=1.0)
    p.add_argument("--lambda_mask", type=float, default=1.0)
    p.add_argument("--lambda_final", type=float, default=0.5)
    p.add_argument(
        "--use_label_supervision",
        action="store_true",
        default=False,
        help=(
            "ABLATION ONLY. Enable router cross-entropy loss against "
            "degradation labels AND teacher-force the router with the "
            "ground-truth label during training. OFF by default; the main "
            "paper setting and the default below NEVER use corruption labels."
        ),
    )
    p.add_argument(
        "--lambda_router",
        type=float,
        default=1.0,
        help=(
            "Router CE weight. Only takes effect when --use_label_supervision "
            "is set; otherwise the loss term is identically zero."
        ),
    )
    p.add_argument(
        "--router_topk",
        type=int,
        default=0,
        help="0 = soft mix during training; 1 = hard top-1 routing.",
    )

    p.add_argument("--output_dir", type=str, required=True)
    p.add_argument("--log_dir", type=str, required=True)
    p.add_argument(
        "--resume",
        type=str,
        default="",
        help="Resume model and optimizer state from a training checkpoint.",
    )
    return p.parse_args()


def set_seed(seed: int) -> None:
    import random

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def _model_forward(model, degraded, *, deg_meta, args):
    """Single point of control for what the adapter is allowed to see.

    In the default LABEL-FREE mode, neither `degradation_ids` nor
    `teacher_force_router` is forwarded to the model.
    """
    if bool(args.use_label_supervision):
        return model(
            degraded,
            degradation_ids=deg_meta,
            teacher_force_router=True,
            router_topk=int(args.router_topk),
        )
    return model(degraded, router_topk=int(args.router_topk))


def _losses(out, *, clean, agent_only, mask, deg_meta, args):
    """Compute losses, gating the router CE behind --use_label_supervision."""
    l1 = F.l1_loss
    restored = out["restored_rgb"]
    fg = out["foreground_prob"]
    black = -torch.ones_like(restored)
    pred_agent = torch.clamp(restored * fg + black * (1.0 - fg), -1.0, 1.0)

    loss_rgb = l1(restored, clean)
    loss_mask = F.cross_entropy(out["mask_logits"], mask)
    loss_final = l1(pred_agent, agent_only)

    if bool(args.use_label_supervision):
        loss_router = F.cross_entropy(out["router_logits"], deg_meta)
        router_term = float(args.lambda_router) * loss_router
    else:
        loss_router = torch.zeros((), device=restored.device)
        router_term = torch.zeros((), device=restored.device)

    total = (
        float(args.lambda_rgb) * loss_rgb
        + float(args.lambda_mask) * loss_mask
        + float(args.lambda_final) * loss_final
        + router_term
    )
    return {
        "total": total,
        "rgb": loss_rgb,
        "mask": loss_mask,
        "router": loss_router,
        "final": loss_final,
        "pred_agent": pred_agent,
    }


@torch.no_grad()
def run_val(model, loader, device, *, args):
    model.eval()
    sums = {"rgb": 0.0, "mask": 0.0, "router": 0.0, "final": 0.0, "total": 0.0, "n": 0}
    for batch in loader:
        degraded, clean, agent_only, mask, deg_meta = [x.to(device) for x in batch]
        out = _model_forward(model, degraded, deg_meta=deg_meta, args=args)
        L = _losses(
            out,
            clean=clean,
            agent_only=agent_only,
            mask=mask,
            deg_meta=deg_meta,
            args=args,
        )
        bs = degraded.shape[0]
        for k in ("rgb", "mask", "router", "final", "total"):
            sums[k] += float(L[k].item()) * bs
        sums["n"] += bs
    n = max(1, sums["n"])
    return {k: sums[k] / n for k in ("rgb", "mask", "router", "final", "total")}


def main():
    args = parse_args()
    set_seed(int(args.seed))

    device = torch.device("cuda" if (args.cuda and torch.cuda.is_available()) else "cpu")
    if int(args.grad_accum_steps) < 1:
        raise ValueError("--grad_accum_steps must be >= 1")
    amp_enabled = bool(args.amp and device.type == "cuda")

    data_roots = [x.strip() for x in args.data_roots.split(",") if x.strip()]
    train_roots = [str(Path(r) / "train") for r in data_roots]
    val_roots = [str(Path(r) / "val") for r in data_roots]

    train_ds = VDCSH5Dataset(
        train_roots, normalize=True, transform=RandomHorizontalFlipAll(0.5)
    )
    val_ds = VDCSH5Dataset(val_roots, normalize=True)

    train_loader = DataLoader(
        train_ds,
        batch_size=int(args.batch_size),
        shuffle=True,
        num_workers=int(args.num_workers),
        pin_memory=True,
        drop_last=True,
    )
    val_loader = DataLoader(
        val_ds,
        batch_size=int(args.val_batch_size),
        shuffle=False,
        num_workers=max(1, int(args.num_workers) // 2),
        pin_memory=True,
    )

    model = DualStreamMoEUNet(
        base_channels=int(args.base_channels),
        num_experts=int(args.num_experts),
        router_hidden=int(args.router_hidden),
        learn_residual_rgb=True,
    ).to(device)

    opt = torch.optim.AdamW(
        model.parameters(), lr=float(args.lr), weight_decay=float(args.weight_decay)
    )

    start_step = 0
    best_val = float("inf")
    if args.resume:
        resume_path = Path(args.resume)
        if not resume_path.is_file():
            raise FileNotFoundError(f"Resume checkpoint not found: {resume_path}")
        checkpoint = torch.load(resume_path, map_location=device, weights_only=False)
        model.load_state_dict(checkpoint["model_state_dict"], strict=True)
        if "optimizer_state_dict" in checkpoint:
            opt.load_state_dict(checkpoint["optimizer_state_dict"])
        start_step = int(checkpoint.get("step", 0))
        best_val = float(checkpoint.get("best_val", float("inf")))
        print(f"Resuming from {resume_path} at optimizer step {start_step}")

    outdir = Path(args.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)
    writer = SummaryWriter(log_dir=args.log_dir)
    vis_dir = outdir / "vis"

    print("=" * 80)
    print("ACO-MoE adapter training")
    print("=" * 80)
    print(f"Device:               {device}")
    print(f"Data roots:           {data_roots}")
    print(f"Train files:          {len(train_ds)}")
    print(f"Val files:            {len(val_ds)}")
    print(f"Steps / micro-batch:  {args.steps} / {args.batch_size}")
    print(f"Gradient accumulation:{args.grad_accum_steps}")
    print(f"Effective batch:      {int(args.batch_size) * int(args.grad_accum_steps)}")
    print(f"AMP (bfloat16):       {amp_enabled}")
    print(f"Num experts (arch):   {args.num_experts}  (NOT a corruption-mode count)")
    print(
        f"Label supervision:    "
        f"{'ON (ablation)' if args.use_label_supervision else 'OFF (default, label-free)'}"
    )
    print(f"Degradation hints:    {train_ds.deg_names}")
    print("                      ^^ analytics only; never used as labels in the default mode")
    print("=" * 80)

    train_iter = iter(train_loader)
    start = time.time()
    for step in range(start_step, int(args.steps)):
        model.train()
        opt.zero_grad(set_to_none=True)
        accum = {"total": 0.0, "rgb": 0.0, "mask": 0.0, "router": 0.0, "final": 0.0}
        last_batch = None
        last_out = None
        last_losses = None
        for _ in range(int(args.grad_accum_steps)):
            try:
                batch = next(train_iter)
            except StopIteration:
                train_iter = iter(train_loader)
                batch = next(train_iter)
            degraded, clean, agent_only, mask, deg_meta = [x.to(device, non_blocking=True) for x in batch]
            with torch.amp.autocast(
                "cuda",
                enabled=amp_enabled,
                dtype=torch.bfloat16 if amp_enabled else None,
            ):
                out = _model_forward(model, degraded, deg_meta=deg_meta, args=args)
                L = _losses(
                    out,
                    clean=clean,
                    agent_only=agent_only,
                    mask=mask,
                    deg_meta=deg_meta,
                    args=args,
                )
                scaled_loss = L["total"] / int(args.grad_accum_steps)
            scaled_loss.backward()
            for key in accum:
                accum[key] += float(L[key].detach().item()) / int(args.grad_accum_steps)
            last_batch = (degraded, clean, agent_only, mask, deg_meta)
            last_out = out
            last_losses = L
        opt.step()

        degraded, clean, agent_only, mask, deg_meta = last_batch
        out = last_out
        L = last_losses

        writer.add_scalar("train/loss_total", accum["total"], step)
        writer.add_scalar("train/loss_rgb", accum["rgb"], step)
        writer.add_scalar("train/loss_mask", accum["mask"], step)
        writer.add_scalar("train/loss_final", accum["final"], step)
        if bool(args.use_label_supervision):
            writer.add_scalar("train/loss_router", accum["router"], step)

        if step % int(args.print_freq) == 0:
            dt = time.time() - start
            print(
                f"step {step:06d}/{args.steps} "
                f"loss {accum['total']:.4f} rgb {accum['rgb']:.4f} "
                f"mask {accum['mask']:.4f} final {accum['final']:.4f} "
                f"({dt:.1f}s)"
            )
            start = time.time()

        if step > 0 and step % int(args.vis_freq) == 0:
            with torch.no_grad():
                _save_vis(
                    vis_dir / f"step_{step:06d}.png",
                    degraded[0],
                    out["restored_rgb"][0],
                    clean[0],
                    out["foreground_prob"][0],
                    L["pred_agent"][0],
                )

        if step > 0 and step % int(args.val_freq) == 0:
            val = run_val(model, val_loader, device, args=args)
            for k, v in val.items():
                writer.add_scalar(f"val/loss_{k}", v, step)
            print(
                f"[val step {step:06d}] total {val['total']:.4f} rgb {val['rgb']:.4f} "
                f"mask {val['mask']:.4f} final {val['final']:.4f}"
            )
            if val["total"] < best_val:
                best_val = float(val["total"])
                torch.save(
                    {
                        "step": step + 1,
                        "model_state_dict": model.state_dict(),
                        "optimizer_state_dict": opt.state_dict(),
                        "best_val": best_val,
                        "args": vars(args),
                        "label_free": not bool(args.use_label_supervision),
                    },
                    outdir / "moe_unet_best.pth",
                )
                print(
                    f"Saved best to {outdir / 'moe_unet_best.pth'} "
                    f"(val_total={best_val:.4f})"
                )

        if step > 0 and step % int(args.save_freq) == 0:
            torch.save(
                {
                    "step": step + 1,
                    "model_state_dict": model.state_dict(),
                    "optimizer_state_dict": opt.state_dict(),
                    "best_val": best_val,
                    "args": vars(args),
                    "label_free": not bool(args.use_label_supervision),
                },
                outdir / "moe_unet_latest.pth",
            )

    torch.save(
        {
            "step": int(args.steps),
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": opt.state_dict(),
            "best_val": best_val,
            "args": vars(args),
            "label_free": not bool(args.use_label_supervision),
        },
        outdir / "moe_unet_latest.pth",
    )
    writer.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
