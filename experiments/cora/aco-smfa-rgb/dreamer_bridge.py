import os
import sys
import time
import json
from pathlib import Path
import numpy as np
from ruamel.yaml import YAML
from checkpoint_io import load_checkpoint, resolve, digest, strict_check
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'vendor/dreamerv3'))
sys.path.insert(0, str(ROOT / 'vendor/aco'))


def config_for(run):
    # Match public Dreamer's YAML 1.2 parser (PyYAML misreads 1e-08 as a string).
    return YAML(typ='safe').load((Path(run) / 'config.yaml').read_text())


def make_env(config, seed):
    from dm_control import suite
    from embodied.envs.dmc import DMC
    import embodied
    domain, task = config['task'][4:].split('_', 1)
    dm = suite.load('ball_in_cup' if domain == 'cup' else domain, task,
                    task_kwargs={'random': seed})
    kw = dict(config['env']['dmc'])
    kw['size'] = tuple(kw['size'])
    if kw['camera'] == -1:
        kw['camera'] = DMC.DEFAULT_CAMERAS.get(domain, 0)
    env = DMC(dm, **kw)
    for key, space in env.act_space.items():
        if not space.discrete:
            env = embodied.wrappers.NormalizeAction(env, key)
    env = embodied.wrappers.UnifyDtypes(env)
    env = embodied.wrappers.CheckSpaces(env)
    for key, space in env.act_space.items():
        if not space.discrete:
            env = embodied.wrappers.ClipAction(env, key)
    return env, dm, kw['camera']


def make_agent(run, output, platform='cpu'):
    import elements
    from dreamerv3.agent import Agent
    config = config_for(run)
    env, dm, camera = make_env(config, 0)
    obs = {k: v for k, v in env.obs_space.items() if not k.startswith('log/')}
    acts = {k: v for k, v in env.act_space.items() if k != 'reset'}
    env.close()
    jaxkw = dict(config['jax'])
    # JAX 0.4.33 expands generic 'gpu' to CUDA and ROCm, requiring both backends.
    # This host has NVIDIA GPUs only; request CUDA explicitly.
    jaxkw.update(platform='cuda' if platform == 'gpu' else platform, prealloc=False, precompile=False, profiler=False,
                 transfer_guard=False, policy_devices=[0], train_devices=[0],
                 expect_devices=0, gpuflags=False)
    # Preserve architecture and dtype. Only execution settings are changed.
    kwargs = {k: config[k] for k in ['seed', 'batch_size', 'batch_length',
              'replay_context', 'report_length', 'replica', 'replicas']}
    cfg = elements.Config(**config['agent'], **kwargs, logdir=str(output), jax=jaxkw)
    start = time.perf_counter()
    agent = Agent(obs, acts, cfg)
    path = resolve(run)
    data = load_checkpoint(path)
    report = strict_check(agent.params, data['params'])
    agent.load(data)
    # Read back all leaves to prove exact restoration, including optimizer state.
    restored = agent.save()
    assert all(np.array_equal(restored['params'][k], v) for k, v in data['params'].items())
    report.update(checkpoint=str(path), checkpoint_sha256=digest(path),
                  config_sha256=digest(Path(run) / 'config.yaml'),
                  exact_values_restored=True, seconds=time.perf_counter() - start,
                  platform=platform, execution_overrides=jaxkw,
                  checkpoint_counters=data['counters'])
    Path(output).mkdir(parents=True, exist_ok=True)
    (Path(output) / 'checkpoint_load.json').write_text(json.dumps(report, indent=2))
    return agent, config


def reset(env):
    action = {k: np.zeros(v.shape, v.dtype) for k, v in env.act_space.items()}
    action['reset'] = True
    return env.step(action)


def act(agent, carry, obs):
    batch = {k: np.asarray(v)[None] for k, v in obs.items() if not k.startswith('log/')}
    carry, action, _ = agent.policy(carry, batch, mode='eval')
    return carry, {**{k: v[0] for k, v in action.items()}, 'reset': False}


DEGRADATIONS = [('rain', .6), ('fog', .6), ('snow', .6), ('motion_blur', .35),
                ('gaussian_noise', .5), ('low_light', .7), ('jpeg', .7)]


def make_degrader(seed):
    from markov import MarkovTemporalDegradation
    return MarkovTemporalDegradation([dict(name=k, intensity=v) for k, v in DEGRADATIONS],
                                     seed=seed, markov_stay_prob=.8, intensity_jitter=.1)
