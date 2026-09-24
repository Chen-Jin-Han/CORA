import argparse
import json
import time
from pathlib import Path
import numpy as np
import torch
from skimage.metrics import structural_similarity
from adapters import build, forward
from train_adapter import Pairs
from dreamer_bridge import DEGRADATIONS

p = argparse.ArgumentParser()
p.add_argument('--data', type=Path, required=True)
p.add_argument('--checkpoint', type=Path, required=True)
p.add_argument('--output', type=Path, required=True)
p.add_argument('--split', choices=['val', 'test'], default='test')
p.add_argument('--device', default='cuda')
args = p.parse_args()
torch.set_num_threads(4)
state = torch.load(args.checkpoint, map_location='cpu', weights_only=False)
model = build(state['name']).to(args.device).eval()
model.load_state_dict(state['model'], strict=True)
data = Pairs(args.data, args.split)
rows = []
for i in range(len(data)):
    x, clean, mask = data[i]
    x = x[None].to(args.device)
    if args.device.startswith('cuda'):
        torch.cuda.synchronize()
    start = time.perf_counter()
    with torch.inference_mode():
        pred = forward(model, x, state['name'])
    if args.device.startswith('cuda'):
        torch.cuda.synchronize()
    latency = (time.perf_counter() - start) * 1000
    rgb = ((pred['restored_rgb'][0].cpu().numpy().transpose(1, 2, 0) + 1) / 2).clip(0, 1)
    gt = (clean.numpy().transpose(1, 2, 0) + 1) / 2
    raw = (x[0].cpu().numpy().transpose(1, 2, 0) + 1) / 2
    m = mask.numpy().astype(bool)
    pm = pred['foreground_prob'][0, 0].cpu().numpy() >= .5
    mse = float(np.mean((rgb - gt)**2))
    raw_mse = float(np.mean((raw - gt)**2))
    row = dict(index=i, degradation=DEGRADATIONS[i % 7][0],
        psnr=float(-10*np.log10(max(mse, 1e-12))),
        raw_psnr=float(-10*np.log10(max(raw_mse, 1e-12))),
        ssim=float(structural_similarity(gt, rgb, channel_axis=2, data_range=1)),
        roi_l1=float(np.mean(np.abs(rgb-gt)[m])) if m.any() else None,
        iou=float((pm & m).sum() / max((pm | m).sum(), 1)), latency_ms=latency)
    rows.append(row)
    if (i+1) % 1000 == 0:
        print(i+1, '/', len(data), flush=True)
args.output.mkdir(parents=True, exist_ok=True)
(args.output / 'images.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in rows))
summary = dict(model=state['name'], step=state['step'], params=state['params'], n=len(rows),
    **{k: float(np.mean([r[k] for r in rows if r[k] is not None])) for k in ['psnr', 'raw_psnr', 'ssim', 'roi_l1', 'iou']},
    latency_ms_median=float(np.median([r['latency_ms'] for r in rows[20:]])),
    latency_ms_p95=float(np.percentile([r['latency_ms'] for r in rows[20:]], 95)),
    metric_protocol='RGB [0,1], full frame no crop; PSNR per image; skimage SSIM; supplement to control returns')
(args.output / 'summary.json').write_text(json.dumps(summary, indent=2))
print(json.dumps(summary), flush=True)
