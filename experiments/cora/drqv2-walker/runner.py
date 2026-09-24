"""50万环境帧固定预算。官方 DrQ-v2 算法 + 显式 RGB 环境/可恢复 replay。"""
import argparse
import collections
import hashlib
import json
import os
from pathlib import Path
import random
import sys
import time

import numpy as np
import torch

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'vendor/drqv2'))
import drqv2
import utils


def atomic_json(path, value):
    path = Path(path)
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(value, indent=2), encoding='utf-8')
    os.replace(tmp, path)


def append(path, value):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(json.dumps(value) + '\n')


class Env:
    def __init__(self, size=64):
        from dm_control import suite
        self.env = suite.load('walker', 'walk', task_kwargs={'random': 0},
                              visualize_reward=False)
        self.size = size
        spec = self.env.action_spec()
        self.low, self.high = spec.minimum, spec.maximum
        self.action_shape = spec.shape
        self.history = collections.deque(maxlen=3)

    def image(self):
        return self.env.physics.render(height=self.size, width=self.size,
                                       camera_id=0).transpose(2, 0, 1).copy()

    def reset(self, seed):
        self.env.task.random.seed(seed)
        self.env.reset()
        im = self.image()
        self.history.clear()
        self.history.extend([im] * 3)
        return np.concatenate(self.history), im

    def step(self, action):
        a = self.low + (np.clip(action, -1, 1) + 1) * .5 * (self.high-self.low)
        reward, discount, frames = 0., 1., 0
        for _ in range(2):
            ts = self.env.step(a)
            reward += discount * float(ts.reward or 0.)
            discount *= float(ts.discount if ts.discount is not None else 1.)
            frames += 1
            if ts.last():
                break
        im = self.image()
        self.history.append(im)
        return np.concatenate(self.history), im, reward, discount, ts.last(), frames

    def close(self):
        self.env.close()


class Replay:
    """Store each RGB frame once. Stack only within its episode (nstep=1).

    Logical lengths are checkpointed. Extra writes after a checkpoint are ignored
    on resume, then overwritten. No replay eviction within the fixed budget.
    """
    def __init__(self, directory, capacity, action_dim, size=64, resume=False):
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        mode = 'r+' if resume else 'w+'
        self.arrays = {}
        for name, shape, dtype in [
            ('images', (capacity, 3, size, size), np.uint8),
            ('start', (capacity,), np.int64),
            ('index', (capacity,), np.int64),
            ('action', (capacity, action_dim), np.float32),
            ('reward', (capacity, 1), np.float32),
            ('discount', (capacity, 1), np.float32),
        ]:
            p = directory / (name + '.npy')
            a = np.lib.format.open_memmap(p, mode=mode, dtype=dtype, shape=shape)
            if a.shape != shape or a.dtype != dtype:
                raise ValueError(f'Replay mismatch: {p}')
            self.arrays[name] = a
            setattr(self, name, a)
        self.n = self.frames = 0
        self.episode_start = 0

    def begin(self, im):
        self.episode_start = self.frames
        self.images[self.frames] = im
        self.start[self.frames] = self.episode_start
        self.frames += 1

    def add(self, im, action, reward, discount):
        self.index[self.n] = self.frames - 1
        self.action[self.n] = action
        self.reward[self.n] = reward
        self.discount[self.n] = discount
        self.images[self.frames] = im
        self.start[self.frames] = self.episode_start
        self.frames += 1
        self.n += 1

    def stack(self, ids):
        idx = np.maximum(ids[:, None] + np.array([-2, -1, 0]),
                         self.start[ids, None])
        return np.asarray(self.images[idx]).reshape(len(ids), 9, *self.images.shape[-2:])

    def batches(self, batch_size, gamma):
        while True:
            ids = np.random.randint(self.n, size=batch_size)
            t = self.index[ids]
            yield (self.stack(t), np.asarray(self.action[ids]),
                   np.asarray(self.reward[ids]), np.asarray(self.discount[ids])*gamma,
                   self.stack(t+1))

    def flush(self):
        for a in self.arrays.values():
            a.flush()


def make_agent(c, action_shape, device):
    # Preserve official convolutions; derive the flattened dimension for 64x64.
    class SizedEncoder(drqv2.Encoder):
        def __init__(self, obs_shape):
            super().__init__(obs_shape)
            with torch.no_grad():
                self.repr_dim = int(self.convnet(torch.zeros(1, *obs_shape)).numel())
    drqv2.Encoder = SizedEncoder
    return drqv2.DrQV2Agent(
        obs_shape=(9, c['image_size'], c['image_size']), action_shape=action_shape,
        device=device, lr=c['lr'], feature_dim=c['feature_dim'],
        hidden_dim=c['hidden_dim'], critic_target_tau=c['critic_target_tau'],
        num_expl_steps=c['seed_frames']//2, update_every_steps=c['update_every_steps'],
        stddev_schedule=c['stddev_schedule'], stddev_clip=c['stddev_clip'], use_tb=True)


def evaluate(agent, env, step, seeds):
    rows = []
    for seed in seeds:
        obs, _ = env.reset(seed)
        total, frames, done = 0., 0, False
        while not done:
            with torch.no_grad(), utils.eval_mode(agent):
                action = agent.act(obs, step, eval_mode=True)
            obs, _, r, _, done, n = env.step(action)
            total += r
            frames += n
        rows.append(dict(seed=seed, reward=total, frames=frames))
    rewards = [r['reward'] for r in rows]
    return dict(mean=float(np.mean(rewards)), std=float(np.std(rewards, ddof=1)),
                minimum=float(np.min(rewards)), episodes=rows)


MODULES = ['encoder', 'actor', 'critic', 'critic_target',
           'encoder_opt', 'actor_opt', 'critic_opt']


def checkpoint(path, agent, replay, state, c):
    replay.flush()
    payload = dict(config=c, state=state, replay=dict(n=replay.n, frames=replay.frames),
                   weights={k: getattr(agent, k).state_dict() for k in MODULES},
                   rng=dict(python=random.getstate(), numpy=np.random.get_state(),
                            torch=torch.get_rng_state(), cuda=torch.cuda.get_rng_state_all()))
    tmp = path.with_suffix('.tmp')
    torch.save(payload, tmp)
    os.replace(tmp, path)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--config', default=str(ROOT/'config.json'))
    p.add_argument('--smoke', action='store_true')
    args = p.parse_args()
    c = json.loads(Path(args.config).read_text())
    if args.smoke:
        c.update(run=c['run']+'_smoke', frames=2000, seed_frames=1000,
                 eval_every_frames=2000, eval_episodes=2, acceptance_episodes=2)
    out = Path(c['data_root'])/c['run']
    out.mkdir(parents=True, exist_ok=True)
    import fcntl
    lock = open(out/'train.lock', 'w')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    if (out/'report.json').exists():
        print('Already complete; no restart.', flush=True)
        return
    torch.set_num_threads(c['torch_threads'])
    torch.backends.cudnn.benchmark = True
    utils.set_seed_everywhere(c['seed'])
    if not torch.cuda.is_available():
        raise RuntimeError('CUDA required; refusing accidental CPU training')
    env, eval_env = Env(c['image_size']), Env(c['image_size'])
    agent = make_agent(c, env.action_shape, 'cuda')
    cp = out/'latest.pt'
    if (out/'config.json').exists() and not cp.exists():
        raise RuntimeError('Existing incomplete initialization: inspect before restarting')
    replay = Replay(out/'replay', c['frames']//2 + c['frames']//1000 + 1000,
                    env.action_shape[0], c['image_size'], resume=cp.exists())
    state = dict(step=0, frames=0, episode=0, updates=0, elapsed=0., validations=[])
    if cp.exists():
        saved = torch.load(cp, map_location='cpu', weights_only=False)
        if saved['config'] != c:
            raise RuntimeError('Checkpoint config mismatch')
        for k in MODULES:
            getattr(agent, k).load_state_dict(saved['weights'][k])
        state = saved['state']
        replay.n, replay.frames = saved['replay']['n'], saved['replay']['frames']
        rng = saved['rng']
        random.setstate(rng['python']); np.random.set_state(rng['numpy'])
        torch.set_rng_state(rng['torch']); torch.cuda.set_rng_state_all(rng['cuda'])
    else:
        checkpoint(cp, agent, replay, state, c)
    atomic_json(out/'config.json', c)
    atomic_json(out/'provenance.json', dict(
        official_commit='c0c650b76c6e5d22a7eb5f2edffd1440fe94f8ef',
        torch=torch.__version__, gpu=torch.cuda.get_device_name(0),
        source_sha256={str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest()
                       for f in [ROOT/'runner.py', ROOT/'config.json', ROOT/'vendor/drqv2/drqv2.py']}))
    batches = replay.batches(c['batch_size'], c['discount'])
    begin, previous_elapsed = time.monotonic(), state['elapsed']
    metrics = {}
    while state['frames'] < c['frames']:
        obs, im = env.reset(c['seed'] + state['episode'])
        replay.begin(im)
        done, total = False, 0.
        while not done:
            step = state['step']
            with torch.no_grad(), utils.eval_mode(agent):
                action = agent.act(obs, step, eval_mode=False)
            if state['frames'] >= c['seed_frames']:
                m = agent.update(batches, step)
                if m:
                    metrics = {k: float(v) for k,v in m.items()}
                    if not all(np.isfinite(v) for v in metrics.values()):
                        raise FloatingPointError(f'Nonfinite metrics: {metrics}')
                    state['updates'] += 1
            obs, im, r, d, done, n = env.step(action)
            replay.add(im, action, r, d)
            state['step'] += 1
            state['frames'] += n
            total += r
        state['episode'] += 1
        state['elapsed'] = previous_elapsed + time.monotonic()-begin
        row = dict(frames=state['frames'], episode=state['episode'], reward=total,
                   elapsed=state['elapsed'], updates=state['updates'], **metrics)
        append(out/'train.jsonl', row)
        atomic_json(out/'status.json', dict(status='training', pid=os.getpid(), **row))
        print(json.dumps(row), flush=True)
        if state['frames'] % c['eval_every_frames'] == 0:
            ev = evaluate(agent, eval_env, state['step'],
                          range(c['validation_seed'],c['validation_seed']+c['eval_episodes']))
            ev['frames'] = state['frames']
            state['validations'].append(ev)
            append(out/'validation.jsonl', ev)
            state['elapsed'] = previous_elapsed + time.monotonic()-begin
            checkpoint(cp, agent, replay, state, c)
    # Fixed budget: always stop at 500k, irrespective of the acceptance result.
    checkpoint(out/'final.pt', agent, replay, state, c)
    atomic_json(out/'status.json', dict(status='acceptance', frames=state['frames'], pid=os.getpid()))
    acceptance = evaluate(agent, eval_env, state['step'],
                          range(c['acceptance_seed'],c['acceptance_seed']+c['acceptance_episodes']))
    recent = state['validations'][-2:]
    passed = (len(recent)==2 and all(v['mean']>=c['acceptance_threshold'] for v in recent)
              and acceptance['mean']>=c['acceptance_threshold'])
    report = dict(status='complete', frames=state['frames'], updates=state['updates'],
                  seed=c['seed'], training_elapsed_seconds=state['elapsed'],
                  acceptance=acceptance, acceptance_passed=passed,
                  acceptance_rule='Last two validation means and independent acceptance mean >=900',
                  checkpoint=str(out/'final.pt'), auto_extend=False)
    atomic_json(out/'report.json', report)
    atomic_json(out/'status.json', report)
    env.close(); eval_env.close()
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
