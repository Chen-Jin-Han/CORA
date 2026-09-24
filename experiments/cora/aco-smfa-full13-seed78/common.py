import hashlib
import json
import os
from pathlib import Path

TASKS = ['walker_walk', 'walker_run', 'walker_stand', 'hopper_stand',
         'quadruped_run', 'finger_turn_hard', 'cartpole_swingup_sparse',
         'cup_catch', 'reacher_easy', 'reacher_hard']
DEGS = [('rain', .6), ('fog', .6), ('snow', .6), ('motion_blur', .35),
        ('gaussian_noise', .5), ('low_light', .7), ('jpeg', .7),
        ('defocus_blur', .5), ('frost', .25), ('occlusion_patch', .1),
        ('saturation', .5), ('shadow', .4), ('shot_noise', 60.)]


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def save_json(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf8')
    os.replace(tmp, path)


def read_config(path):
    c = json.loads(Path(path).read_text(encoding='utf8'))
    assert c['tasks'] == TASKS, 'This protocol requires exactly the agreed ten tasks/order'
    assert c['seed'] in [7,8] and c['image_size'] == 64
    assert (c['train_pairs_per_task'], c['val_pairs_per_task'], c['test_clean_per_task']) == (4500, 500, 1000)
    assert c['steps'] == 15000 and c['batch_size'] == 128 and c['control_episodes'] == 10
    assert 0 < c['micro_batch'] <= 128 and 128 % c['micro_batch'] == 0
    assert c['validate_every'] == 500
    assert c['single_episodes']==c['clean_episodes']==5 and len(DEGS)==13
    assert c['loss']=='l1_fft' and c['fft_weight']==.05
    assert c['validation_subset_per_task_kind']==40 and c['markov_stay_prob']==.8
    return c


def root(c):
    return Path(c['data_root']) / c['experiment']


def policy(c, task):
    return Path(c['policy_root']) / ('dmc_' + task) / 'seed0' / 'run'


def bind(c):
    r = root(c)
    r.mkdir(parents=True, exist_ok=True)
    p = r / 'protocol.json'
    if p.exists():
        assert json.loads(p.read_text()) == c, 'Existing output belongs to a different config; use a new experiment name'
    else:
        save_json(p, c)
    return r
