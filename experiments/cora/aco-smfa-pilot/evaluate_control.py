import argparse
import json
import os
import time
from pathlib import Path
os.environ.setdefault('MUJOCO_GL', 'egl')
import numpy as np
from dreamer_bridge import make_agent, make_env, foreground, reset, act, make_degrader

p = argparse.ArgumentParser()
p.add_argument('--run', type=Path, required=True)
p.add_argument('--output', type=Path, required=True)
p.add_argument('--platform', default='cpu')
p.add_argument('--episodes', type=int, default=10)
p.add_argument('--seed', type=int, default=40000)
p.add_argument('--max-steps', type=int, default=0, help='0: full episodes; nonzero smoke only')
p.add_argument('--conditions', nargs='+', default=['clean', 'oracle_fg', 'raw'])
p.add_argument('--adapter', choices=['aco', 'smfa'])
p.add_argument('--adapter-checkpoint', type=Path)
p.add_argument('--torch-device', default='cpu')
args = p.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
agent, config = make_agent(args.run, args.output, args.platform)
adapter = None
if args.adapter:
    import torch
    from adapters import build, forward
    torch.set_num_threads(4)
    adapter = build(args.adapter).to(args.torch_device)
    state = torch.load(args.adapter_checkpoint, map_location='cpu', weights_only=False)
    assert state['name'] == args.adapter
    adapter.load_state_dict(state['model'], strict=True)
    adapter.eval()
rows = []
path = args.output / 'episodes.jsonl'
if path.exists():
    rows = [json.loads(x) for x in path.read_text().splitlines()]
done = {(r['condition'], r['seed']) for r in rows}
for condition in args.conditions:
    assert condition in ['clean', 'oracle_fg', 'raw', 'restored_rgb', 'agent_only_rgb', 'agent_only_rgb_hard']
    for ep in range(args.episodes):
        seed = args.seed + ep
        if (condition, seed) in done:
            continue
        env, dm, camera = make_env(config, seed)
        obs = reset(env)
        carry = agent.init_policy(1)
        # Public policy samples even in eval mode. Reset its PRNG counter for paired runs.
        with agent.n_actions.lock:
            agent.n_actions.value = seed * 10000
        degrader = make_degrader(seed + 100000)
        score, steps = 0., 0
        start = time.perf_counter()
        bridge_seconds = []
        while True:
            image = obs['image']
            if condition == 'oracle_fg':
                mask = foreground(dm, tuple(config['env']['dmc']['size']), camera)
                image = image * mask[..., None]
            elif condition != 'clean':
                image = degrader(image)
                if condition != 'raw':
                    assert adapter is not None
                    t0 = time.perf_counter()
                    x = torch.from_numpy(np.ascontiguousarray(image)).permute(2, 0, 1)[None].to(args.torch_device).float() / 127.5 - 1
                    with torch.inference_mode():
                        pred = forward(adapter, x, args.adapter)[condition]
                    image = ((pred[0].permute(1, 2, 0).cpu().numpy() + 1) * 127.5).round().clip(0, 255).astype(np.uint8)
                    bridge_seconds.append(time.perf_counter() - t0)
            obs = dict(obs, image=np.asarray(image, np.uint8))
            carry, action = act(agent, carry, obs)
            obs = env.step(action)
            score += float(obs['reward'])
            steps += 1
            if obs['is_last'] or (args.max_steps and steps >= args.max_steps):
                break
        row = dict(task=config['task'], condition=condition, seed=seed, return_=score,
                   agent_steps=steps, seconds=time.perf_counter() - start,
                   full_episode=bool(obs['is_last']), terminal=bool(obs['is_terminal']),
                   action_repeat=config['env']['dmc']['repeat'],
                   adapter_bridge_ms=float(np.mean(bridge_seconds) * 1000) if bridge_seconds else None)
        rows.append(row)
        with path.open('a') as f:
            f.write(json.dumps(row) + '\n')
        print(json.dumps(row), flush=True)
        env.close()
summary = {}
for condition in args.conditions:
    values = [r['return_'] for r in rows if r['condition'] == condition]
    summary[condition] = dict(n=len(values), mean=float(np.mean(values)),
                              std=float(np.std(values, ddof=1)) if len(values) > 1 else None)
(args.output / 'summary.json').write_text(json.dumps(summary, indent=2))
