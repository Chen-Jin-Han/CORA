"""Render simulator-derived mask QA panels and explicit target coverage counts."""
import os
os.environ.setdefault('MUJOCO_GL', 'egl')
import argparse
import json
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
from dreamer_bridge import config_for, make_env, reset, foreground

p = argparse.ArgumentParser()
p.add_argument('--root', type=Path, required=True)
p.add_argument('--output', type=Path, required=True)
args = p.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
rows = []
canvas = Image.new('RGB', (768, 3*282), 'white')
draw = ImageDraw.Draw(canvas)
for row, task in enumerate(['walker_walk', 'walker_run', 'finger_turn_hard']):
    cfg = config_for(args.root/f'dmc_{task}/seed0/run')
    env, dm, cam = make_env(cfg, 123)
    obs = reset(env)
    mask = foreground(dm, (64, 64), cam)
    seg = dm.physics.render(64, 64, camera_id=cam, segmentation=True)
    target = [(i, dm.physics.model.id2name(i, 'site')) for i in range(dm.physics.model.nsite)
              if dm.physics.model.id2name(i, 'site') in ('target', 'tip')]
    import mujoco
    visible = (seg[..., 1] == int(mujoco.mjtObj.mjOBJ_SITE)) & np.isin(seg[..., 0], [i for i, _ in target])
    assert np.all(mask[visible])
    rows.append(dict(task=task, foreground_pixels=int(mask.sum()), target_sites=target,
                     visible_target_pixels=int(visible.sum()), kept_target_pixels=int((visible & mask).sum())))
    draw.text((5,row*282), task + ' | RGB / mask / foreground', fill='black')
    for col, img in enumerate([obs['image'], np.repeat(mask[..., None], 3, -1)*255,
                                obs['image']*mask[..., None]]):
        canvas.paste(Image.fromarray(np.uint8(img)).resize((256, 256), Image.Resampling.NEAREST), (col*256, row*282+24))
    env.close()
canvas.save(args.output/'mask_qa.png')
(args.output/'mask_qa.json').write_text(json.dumps(rows, indent=2))
print(json.dumps(rows), flush=True)
