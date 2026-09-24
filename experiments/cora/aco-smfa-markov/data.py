import hashlib
import json
from pathlib import Path
import numpy as np
import torch
from common import DEGS, root, policy, save_json
from corruptions import corrupt


def generate(c, task):
    raise RuntimeError('Existing datasets are read-only for this experiment')
    from dreamer_bridge import make_agent, make_env, reset, act
    r = root(c)
    agent, cfg = make_agent(policy(c, task), r/'audit'/task, 'cpu')
    assert cfg['task'] == 'dmc_'+task
    assert list(cfg['env']['dmc']['size']) == [64,64]
    ti = c['tasks'].index(task)
    for si, (split, n) in enumerate([('train',4500), ('val',500), ('test',1000)]):
        d = root(c)/'datasets'/task/split
        if (d/'complete.json').exists():
            continue
        d.mkdir(parents=True, exist_ok=True)
        images, episodes, frames, source = [], [], [], []
        episode = 0
        while len(images) < n:
            seed = 1000000 + ti*100000 + si*10000 + episode
            env, dm, camera = make_env(cfg, seed)
            obs = reset(env)
            carry = agent.init_policy(1)
            with agent.n_actions.lock:
                agent.n_actions.value = seed*10000
            rng = np.random.RandomState(seed)
            use_policy = episode % 2 == 0
            step, sampled = 0, 0
            try:
                while len(images) < n:
                    if step % c['frame_stride'] == 0:
                        images.append(obs['image'].copy())
                        episodes.append(seed); frames.append(step); source.append(int(use_policy))
                        sampled += 1
                    if sampled >= 100:
                        break
                    if use_policy:
                        carry, action = act(agent, carry, obs)
                    else:
                        action = {k:rng.uniform(-1,1,s.shape).astype(s.dtype) for k,s in env.act_space.items() if k!='reset'}
                        action['reset'] = False
                    obs = env.step(action)
                    step += 1
                    if obs['is_last']:
                        break
            finally:
                env.close()
            episode += 1
            print(task, split, len(images), '/', n, flush=True)
        clean = np.stack(images)
        np.save(d/'clean.npy', clean)
        meta_rng = np.random.RandomState(3000000+ti*10000+si)
        index = np.repeat(np.arange(n), 7) if split=='test' else np.arange(n)
        kind = np.tile(np.arange(7), n) if split=='test' else np.arange(n)%7
        if split!='test':
            meta_rng.shuffle(kind)
        seeds = meta_rng.randint(0,2**31-1,size=len(index))
        intensity = np.array([DEGS[k][1] for k in kind])*meta_rng.uniform(.9,1.1,size=len(index))
        x = np.lib.format.open_memmap(d/'input.npy', mode='w+', dtype=np.uint8, shape=(len(index),64,64,3))
        for j, (i,k,s,v) in enumerate(zip(index,kind,seeds,intensity)):
            x[j] = corrupt(clean[i], k, v, s)
        x.flush(); del x
        np.savez(d/'metadata.npz', index=index, kind=kind, corruption_seed=seeds, intensity=intensity,
                 episode=np.array(episodes), frame=np.array(frames), policy_source=np.array(source))
        from checkpoint_io import digest
        save_json(d/'complete.json', dict(task=task, split=split, clean=n, pairs=len(index),
            hashes={p.name:digest(p) for p in [d/'clean.npy',d/'input.npy',d/'metadata.npz']}))


def audit(c):
    from checkpoint_io import digest
    result = []
    for task in c['tasks']:
        seen_ep, seen_hash = set(), set()
        for split, n, pairs in [('train',4500,4500),('val',500,500),('test',1000,7000)]:
            d = Path(c['dataset_root'])/task/split
            m = json.loads((d/'complete.json').read_text())
            assert all(digest(d/k)==v for k,v in m['hashes'].items())
            y, x = np.load(d/'clean.npy',mmap_mode='r'), np.load(d/'input.npy',mmap_mode='r')
            z = np.load(d/'metadata.npz')
            assert y.shape==(n,64,64,3) and x.shape==(pairs,64,64,3)
            assert y.dtype==x.dtype==np.uint8
            assert len(z['index']) == pairs and np.all((z['index']>=0)&(z['index']<n))
            assert len(set(zip(z['episode'].tolist(),z['frame'].tolist())))==n
            eps=set(z['episode'].tolist()); assert not eps & seen_ep
            seen_ep |= eps
            counts=np.bincount(z['kind'],minlength=7); assert counts.max()-counts.min()<=1
            hashes={hashlib.sha256(im.tobytes()).hexdigest() for im in y}
            overlap=len(hashes & seen_hash); seen_hash |= hashes
            result.append(dict(task=task,split=split,clean=n,pairs=pairs,episodes=len(eps),
                               cross_split_exact_pixel_duplicates=overlap,counts=counts.tolist()))
    # Identical rendered resets can occur naturally; explicitly report rather than silently discard.
    save_json(root(c)/'data_audit.json', result)
    return result


class Pairs:
    def __init__(self, c, split):
        self.shards=[]; self.ends=[]; count=0
        for task in c['tasks']:
            d=Path(c['dataset_root'])/task/split
            assert (d/'complete.json').exists()
            z=np.load(d/'metadata.npz')
            x=np.load(d/'input.npy',mmap_mode='r'); y=np.load(d/'clean.npy',mmap_mode='r')
            self.shards.append((task,x,y,z['index'],z['kind']))
            count+=len(x); self.ends.append(count)

    def __len__(self):
        return self.ends[-1]

    def get(self, idx):
        s=int(np.searchsorted(self.ends,idx,side='right'))
        j=idx-(self.ends[s-1] if s else 0)
        task,x,y,index,kind=self.shards[s]
        return x[j], y[index[j]], task, int(kind[j])

    def batch(self, indices, flips=None):
        pairs=[self.get(int(i)) for i in indices]
        x=np.stack([p[0] for p in pairs]); y=np.stack([p[1] for p in pairs])
        if flips is not None:
            x[flips]=x[flips,:,::-1,:]; y[flips]=y[flips,:,::-1,:]
        cv=lambda a:torch.from_numpy(a.copy()).permute(0,3,1,2).float()/127.5-1
        return cv(x),cv(y)
