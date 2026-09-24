import argparse
import json
import os
from pathlib import Path
os.environ.setdefault('MUJOCO_GL', 'egl')
import numpy as np
from dreamer_bridge import make_agent, make_env, foreground, reset, act

p = argparse.ArgumentParser()
p.add_argument('--run', type=Path, required=True)
p.add_argument('--output', type=Path, required=True)
p.add_argument('--platform', default='cpu')
p.add_argument('--counts', nargs=3, type=int, default=[2000, 300, 500])
args = p.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
agent, config = make_agent(args.run, args.output / 'loading', args.platform)
for split_id, (split, count) in enumerate(zip(['train', 'val', 'test'], args.counts)):
    path = args.output / f'{split}.npz'
    if path.exists():
        data = np.load(path)
        assert len(data['image']) == count
        continue
    images, masks, seeds, frames, sources = [], [], [], [], []
    episode = 0
    # Split by disjoint environment seeds, before corruption; no rollout crosses splits.
    while len(images) < count:
        seed = 1000 + split_id * 10000 + episode
        env, dm, camera = make_env(config, seed)
        obs = reset(env)
        carry = agent.init_policy(1)
        with agent.n_actions.lock:
            agent.n_actions.value = seed * 10000
        rng = np.random.RandomState(seed)
        use_policy = episode % 2 == 0
        step = 0
        while len(images) < count:
            # Subsample to avoid near-identical consecutive frames; cap 100 frames/episode.
            if step % 5 == 0:
                images.append(obs['image'])
                masks.append(foreground(dm, tuple(config['env']['dmc']['size']), camera))
                seeds.append(seed)
                frames.append(step)
                sources.append('policy' if use_policy else 'random')
            if use_policy:
                carry, action = act(agent, carry, obs)
            else:
                action = {k: rng.uniform(-1, 1, s.shape).astype(s.dtype)
                          for k, s in env.act_space.items() if k != 'reset'}
                action['reset'] = False
            obs = env.step(action)
            step += 1
            if obs['is_last'] or step >= 500:
                break
        env.close()
        episode += 1
        print(split, len(images), '/', count, flush=True)
    np.savez_compressed(path, image=np.stack(images), mask=np.stack(masks),
                        episode_seed=seeds, frame=frames, source=sources)
    print('SAVED', path, flush=True)
(args.output / 'manifest.json').write_text(json.dumps(dict(task=config['task'],
    counts=args.counts, frame_stride=5, max_frames_per_episode=100,
    mask_rule='non-world geom bodies plus target/tip sites; task target coverage visually checked'), indent=2))
