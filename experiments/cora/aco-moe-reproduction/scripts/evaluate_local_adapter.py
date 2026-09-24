"""Held-out image metrics, distinct from downstream control performance."""
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import torch
from PIL import Image, ImageDraw
from torch.utils.data import DataLoader
from aco_moe.moe_unet import DualStreamMoEUNet
from scripts.train_aco_moe import VDCSH5Dataset, run_val, _to_uint8


def main():
    torch.set_num_threads(4)
    device = torch.device('cuda')
    ckpt = torch.load('checkpoints/local_initial/adapter/moe_unet_best.pth', map_location='cpu', weights_only=False)
    args = SimpleNamespace(**ckpt['args'])
    ds = VDCSH5Dataset(['data/local_initial/walker_walk_vdcs_seg64_split/val'])
    loader = DataLoader(ds, batch_size=4, num_workers=0)
    torch.manual_seed(args.seed)
    model = DualStreamMoEUNet(base_channels=args.base_channels, num_experts=args.num_experts,
                             router_hidden=args.router_hidden).to(device)
    metrics = {'validation_samples': len(ds), 'checkpoint_step': ckpt['step']}
    metrics['random_init_soft'] = run_val(model, loader, device, args=args)
    model.load_state_dict(ckpt['model_state_dict'])
    metrics['trained_soft'] = run_val(model, loader, device, args=args)
    args.router_topk = 1
    metrics['trained_top1'] = run_val(model, loader, device, args=args)
    model.eval()
    intersection = union = 0
    raw_l1_sum = 0.0
    expert_counts = [0] * args.num_experts
    with torch.no_grad():
        for x, clean, target, mask, _ in loader:
            out = model(x.to(device), router_topk=1)
            pred = out['foreground_prob'][:, 0].cpu() >= 0.5
            truth = mask.bool()
            intersection += (pred & truth).sum().item()
            union += (pred | truth).sum().item()
            raw_l1_sum += (x-clean).abs().mean().item() * len(x)
            for i in out['router_probs'].argmax(-1).tolist():
                expert_counts[i] += 1
    metrics['top1_mask_iou_global'] = intersection / max(1, union)
    metrics['raw_corrupted_rgb_l1'] = raw_l1_sum / len(ds)
    metrics['top1_expert_counts'] = expert_counts
    root = Path('runs/local_initial')
    root.mkdir(parents=True, exist_ok=True)
    (root / 'adapter_validation.json').write_text(json.dumps(metrics, indent=2), encoding='utf-8')
    headers = ['Corrupted', 'Restored top-1', 'Clean', 'Predicted mask', 'Agent-centric', 'Target foreground']
    canvas = Image.new('RGB', (180*6, 38 + 148*7), 'white')
    draw = ImageDraw.Draw(canvas)
    for col, title in enumerate(headers):
        draw.text((col*180+5, 12), title, fill='black')
    with torch.no_grad():
        for row, deg in enumerate(ds.deg_names):
            index = next(i for i, (_, name) in enumerate(ds.files) if name == deg)
            x, clean, target, mask, _ = ds[index]
            out = model(x[None].to(device), router_topk=1)
            probability = out['foreground_prob'][0].repeat(3, 1, 1) * 2 - 1
            images = [x, out['restored_rgb'][0], clean, probability, out['agent_only_rgb_hard'][0], target]
            for col, tensor in enumerate(images):
                canvas.paste(Image.fromarray(_to_uint8(tensor)).resize((128, 128)), (col*180+5, 38+row*148))
            draw.text((5, 38+row*148+129), deg, fill='black')
    canvas.save(root / 'adapter_comparison.png')
    print(json.dumps(metrics, indent=2))


if __name__ == '__main__':
    main()
