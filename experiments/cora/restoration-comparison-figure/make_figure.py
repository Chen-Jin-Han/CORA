"""Render matched full13 test images through CORA, PromptIR, and NAFNet.

All images are from the same episode-disjoint test split. The contact sheet is
used only to choose frames with a visible agent; it does not run any model.
"""
from __future__ import annotations

import argparse
import gc
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


DATA = Path('/data1/CST/CORA/aco-smfa-full13/datasets/full13_v1')
ROOT = Path('/data1/CST/CORA/restoration-comparison-figure')
FULL_CODE = Path('/home/gpuadmin/CST/CORA/aco-smfa-full13')
BASE_CODE = Path('/home/gpuadmin/CST/CORA/promptir-nafnet-baselines')
ROWS = [('walker_walk', 'low_light', 5), ('quadruped_run', 'motion_blur', 3)]
CANDIDATES = (42, 171, 294, 417, 682, 901)
CHECKPOINTS = {
    'CORA': Path('/data1/CST/CORA/aco-smfa-full13/rgb10_seed6_fft_b128_s15000_full13_v1/checkpoints/smfa/last.pt'),
    'PromptIR': Path('/data1/CST/CORA/promptir-nafnet-baselines/promptir_seed6_b128_s15000_full13_v1/checkpoints/promptir/last.pt'),
    'NAFNet': Path('/data1/CST/CORA/promptir-nafnet-baselines/nafnet_seed6_b128_s15000_full13_v1/checkpoints/nafnet/last.pt'),
}


def font(size: int):
    for path in ('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 'C:/Windows/Fonts/arial.ttf'):
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def tile(rgb: np.ndarray, side: int) -> Image.Image:
    assert rgb.shape == (64, 64, 3) and rgb.dtype == np.uint8
    return Image.fromarray(rgb).resize((side, side), Image.Resampling.NEAREST)


def pair(task: str, kind: int, index: int) -> tuple[np.ndarray, np.ndarray]:
    assert 0 <= index < 1000 and 0 <= kind < 13
    source = DATA / task / 'test'
    clean = np.load(source / 'clean.npy', mmap_mode='r')
    corrupt = np.load(source / 'input.npy', mmap_mode='r')
    assert clean.shape == (1000, 64, 64, 3)
    assert corrupt.shape == (13000, 64, 64, 3)
    return np.array(clean[index]), np.array(corrupt[index * 13 + kind])


def contact() -> Path:
    ROOT.mkdir(parents=True, exist_ok=True)
    side, gap, pad = 128, 14, 18
    width = pad * 2 + 6 * (side + gap) - gap
    height = pad * 2 + 2 * (side * 2 + 55) + 26
    canvas = Image.new('RGB', (width, height), '#ffffff')
    draw = ImageDraw.Draw(canvas)
    f, small = font(17), font(14)
    for row, (task, name, kind) in enumerate(ROWS):
        y = pad + row * (side * 2 + 55 + 10)
        draw.text((pad, y), f'{task} / {name} · Clean above, disturbed below', fill='#202533', font=f)
        for col, idx in enumerate(CANDIDATES):
            x = pad + col * (side + gap)
            clean, corrupt = pair(task, kind, idx)
            canvas.paste(tile(clean, side), (x, y + 25))
            canvas.paste(tile(corrupt, side), (x, y + 25 + side))
            draw.text((x, y + 25 + side * 2 + 3), f'index {idx}', fill='#303542', font=small)
    out = ROOT / 'contact_sheet.png'
    canvas.save(out)
    print(out, flush=True)
    return out


def module(path: Path, name: str):
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    item = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(item)
    return item


def restore(method: str, disturbed: list[np.ndarray]) -> tuple[list[np.ndarray], int]:
    import torch

    torch.set_num_threads(4)
    if method == 'CORA':
        builder = module(FULL_CODE / 'models.py', 'cora_figure_models')
        model = builder.build('smfa')
        expected_name = 'smfa'
    else:
        builder = module(BASE_CODE / 'models.py', 'baseline_figure_models')
        model = builder.build(method.lower())
        expected_name = method.lower()
    state = torch.load(CHECKPOINTS[method], map_location='cpu', weights_only=False)
    step = int(state['step'])
    assert state['name'] == expected_name and 0 < step <= 15000
    if method != 'PromptIR':
        assert step == 15000
    model.load_state_dict(state['model'], strict=True)
    del state
    model.eval()
    images = []
    with torch.inference_mode():
        for frame in disturbed:
            x = torch.from_numpy(frame.copy()).permute(2, 0, 1)[None].float() / 127.5 - 1
            y = model(x).clamp(-1, 1)
            images.append(((y[0].permute(1, 2, 0).numpy() + 1) * 127.5).round().clip(0, 255).astype(np.uint8))
    del model
    gc.collect()
    return images, step


def render(indices: tuple[int, int]) -> Path:
    from importlib.util import spec_from_file_location, module_from_spec
    ROOT.mkdir(parents=True, exist_ok=True)
    metric_spec = spec_from_file_location('figure_metrics', FULL_CODE / 'metrics.py')
    assert metric_spec is not None and metric_spec.loader is not None
    metrics = module_from_spec(metric_spec)
    metric_spec.loader.exec_module(metrics)
    samples = [pair(task, kind, idx) for (task, _, kind), idx in zip(ROWS, indices)]
    clean = [p[0] for p in samples]
    raw = [p[1] for p in samples]
    outputs = {'Clean': clean, 'Disturbed': raw}
    steps = {}
    for method in CHECKPOINTS:
        outputs[method], steps[method] = restore(method, raw)
    side, gap, left, top, bottom = 206, 18, 205, 81, 72
    width = left + 5 * side + 4 * gap + 32
    height = top + 2 * (side + 52) + bottom
    canvas = Image.new('RGB', (width, height), '#ffffff')
    draw = ImageDraw.Draw(canvas)
    head, label, small = font(20), font(16), font(13)
    titles = ['Clean', 'Disturbed', 'CORA', f'PromptIR ({steps["PromptIR"]:,} steps)', 'NAFNet']
    for j, name in enumerate(titles):
        x = left + j * (side + gap)
        draw.text((x + side / 2, 32), name, fill='#182235', font=head, anchor='mm')
    details = []
    for i, ((task, kind_name, _), idx) in enumerate(zip(ROWS, indices)):
        y = top + i * (side + 52)
        draw.text((18, y + 15), task.replace('_', ' '), fill='#182235', font=label)
        draw.text((18, y + 39), kind_name.replace('_', ' '), fill='#536073', font=small)
        draw.text((18, y + 61), f'test frame {idx}', fill='#536073', font=small)
        detail = dict(task=task, corruption=kind_name, clean_index=idx, metrics={})
        for j, method in enumerate(outputs):
            x = left + j * (side + gap)
            frame = outputs[method][i]
            canvas.paste(tile(frame, side), (x, y))
            if method != 'Clean':
                score = metrics.measure(frame, clean[i])
                detail['metrics'][method] = score
                draw.text((x + side / 2, y + side + 16),
                          f'PSNR-Y {score["psnr_y"]:.1f} dB  ·  SSIM-Y {score["ssim_y"]:.3f}',
                          fill='#435169', font=small, anchor='mm')
        details.append(detail)
    preview = steps['PromptIR'] != 15000
    note = (f'PREVIEW · PromptIR checkpoint at {steps["PromptIR"]:,} / 15,000 updates; regenerate for final paper figure.'
            if preview else 'All adapters use final 15,000-update checkpoints · matched full13 test pairs.')
    draw.text((width / 2, height - 26), note, fill='#9b3333' if preview else '#536073', font=small, anchor='mm')
    out = ROOT / ('comparison_preview.png' if preview else 'comparison_final.png')
    canvas.save(out)
    (ROOT / 'figure_metadata.json').write_text(json.dumps(dict(checkpoint_steps=steps,rows=details,preview=preview),indent=2),encoding='utf8')
    print(out, flush=True)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['contact', 'render'])
    parser.add_argument('--indices', type=int, nargs=2, default=[294, 417])
    args = parser.parse_args()
    contact() if args.action == 'contact' else render(tuple(args.indices))


if __name__ == '__main__':
    main()
