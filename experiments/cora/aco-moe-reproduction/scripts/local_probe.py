"""GPU, render, and backward-pass checks for the local preliminary run."""
import json
import os
import time
from pathlib import Path

os.environ.setdefault("MUJOCO_GL", "glfw" if os.name == "nt" else "egl")
import numpy as np
import torch
from PIL import Image
from aco_moe.moe_unet import DualStreamMoEUNet
from envs.dmc import DMC


def main():
    torch.set_num_threads(4)
    assert torch.cuda.is_available(), "CUDA not available"
    outdir = Path("runs/local_initial")
    outdir.mkdir(parents=True, exist_ok=True)
    report = {"torch": torch.__version__, "cuda": torch.version.cuda,
              "gpu": torch.cuda.get_device_name(), "render_backend": os.environ["MUJOCO_GL"]}
    env = DMC("walker_walk", action_repeat=2, size=(64, 64), seed=0)
    obs = env.reset()
    assert obs["image"].shape == (64, 64, 3)
    assert obs["image"].std() > 0
    Image.fromarray(obs["image"]).resize((384, 384)).save(outdir / "walker_render.png")
    for _ in range(10):
        obs, reward, done, info = env.step(np.zeros(env.action_space.shape, np.float32))
    report["render_shape"] = list(obs["image"].shape)
    # Count the default network without allocating hundreds of MB on CPU/GPU.
    with torch.device("meta"):
        full = DualStreamMoEUNet()
    report["default_adapter_parameters"] = sum(p.numel() for p in full.parameters())
    del full
    torch.manual_seed(0)
    model = DualStreamMoEUNet(base_channels=16, num_experts=7).cuda()
    report["local_adapter_parameters"] = sum(p.numel() for p in model.parameters())
    opt = torch.optim.AdamW(model.parameters(), lr=1e-4)
    x = torch.rand(4, 3, 64, 64, device="cuda") * 2 - 1
    torch.cuda.reset_peak_memory_stats()
    start = time.perf_counter()
    for _ in range(3):
        opt.zero_grad(set_to_none=True)
        result = model(x)
        loss = result["restored_rgb"].square().mean() + result["mask_logits"].square().mean()
        assert torch.isfinite(loss)
        loss.backward()
        assert model.router.fc2.weight.grad is not None
        opt.step()
    torch.cuda.synchronize()
    report["three_adapter_updates_seconds"] = time.perf_counter() - start
    report["peak_allocated_MiB"] = torch.cuda.max_memory_allocated() / 2**20
    report["peak_reserved_MiB"] = torch.cuda.max_memory_reserved() / 2**20
    model.eval()
    with torch.no_grad():
        hard = model(x, router_topk=1)
        assert hard["agent_only_rgb"].shape == x.shape
        assert torch.isfinite(hard["agent_only_rgb"]).all()
    (outdir / "probe.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
