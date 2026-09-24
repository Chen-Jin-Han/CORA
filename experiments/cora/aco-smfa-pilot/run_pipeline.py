"""One foreground supervisor; persisted stage state, exclusive process lock."""
import fcntl
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = Path('/data1/CST/CORA/aco-smfa-pilot')
OUT = DATA / 'outputs'
OUT.mkdir(parents=True, exist_ok=True)
lock = (OUT / 'pipeline.lock').open('a+')
fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
lock.seek(0)
lock.truncate()
lock.write(str(os.getpid()))
lock.flush()
os.chdir(ROOT)
os.environ.update(XDG_CACHE_HOME=str(DATA/'cache'), TMPDIR=str(DATA/'cache/tmp'),
    MUJOCO_GL='egl', OMP_NUM_THREADS='4', OPENBLAS_NUM_THREADS='4', MKL_NUM_THREADS='4',
    XLA_PYTHON_CLIENT_PREALLOCATE='false')


def status(stage, **extra):
    row = dict(pid=os.getpid(), stage=stage, timestamp=time.time(), **extra)
    tmp = OUT / 'pipeline_status.tmp'
    tmp.write_text(json.dumps(row, indent=2))
    tmp.replace(OUT / 'pipeline_status.json')
    print(json.dumps(row), flush=True)


def available_gpu():
    result = subprocess.check_output(['nvidia-smi', '--query-gpu=index,memory.used,utilization.gpu', '--format=csv,noheader,nounits'], text=True, timeout=10)
    for line in result.splitlines():
        index, used, util = [int(v.strip()) for v in line.split(',')]
        if used < 2000 and util < 15:
            return index
    return None


def run(stage, command):
    marker = OUT / f'{stage}.complete.json'
    if marker.exists():
        return
    status(stage, command=command)
    with (OUT / f'{stage}.log').open('a') as log:
        code = subprocess.call([sys.executable, '-u', *command], stdout=log, stderr=subprocess.STDOUT)
    if code:
        status('failed', failed_stage=stage, exit_code=code)
        sys.exit(code)
    marker.write_text(json.dumps(dict(command=command, completed=time.time())))


def run_gpu(stage, command):
    if (OUT / f'{stage}.complete.json').exists():
        return
    while True:
        try:
            gpu = available_gpu()
            if gpu is not None:
                break
            status('waiting_for_gpu', next_stage=stage, poll_seconds=10,
                   reason='Waiting for memory<2000MiB and utilization<15%')
        except (subprocess.SubprocessError, OSError, ValueError) as exc:
            status('waiting_for_gpu', next_stage=stage, poll_seconds=10, query_error=str(exc))
        time.sleep(10)
    os.environ['CUDA_VISIBLE_DEVICES'] = str(gpu)
    status('gpu_selected', gpu=gpu, next_stage=stage)
    run(stage, command)


try:
    # CPU policy inference measured ~40 ms/step. Make useful progress while GPUs are busy.
    tasks = ['walker_walk', 'walker_run', 'finger_turn_hard']
    for task in tasks:
        runpath = str(DATA / f'checkpoints/dmc_{task}/seed0/run')
        run('p0_'+task, ['evaluate_control.py', '--run', runpath,
            '--output', str(OUT/'p0'/task), '--platform', 'cpu'])
        run('data_'+task, ['collect_data.py', '--run', runpath,
            '--output', str(DATA/'datasets'/task), '--platform', 'cpu'])
    for model in ['aco', 'smfa']:
        modeldir = DATA/'checkpoints'/model
        run_gpu('train_'+model, ['train_adapter.py', '--data', str(DATA/'datasets'),
            '--output', str(modeldir), '--model', model])
        for split in ['val', 'test']:
            run_gpu(f'images_{model}_{split}', ['evaluate_images.py', '--data', str(DATA/'datasets'),
                '--checkpoint', str(modeldir/'last.pt'), '--output', str(OUT/'images'/model/split), '--split', split])
        for task in tasks:
            run(f'p2_{model}_{task}', ['evaluate_control.py',
                '--run', str(DATA/f'checkpoints/dmc_{task}/seed0/run'),
                '--output', str(OUT/'p2'/model/task), '--platform', 'cpu',
                '--adapter', model, '--adapter-checkpoint', str(modeldir/'last.pt'),
                '--torch-device', 'cpu', '--conditions', 'restored_rgb', 'agent_only_rgb'])
    run('data_integrity', ['validate_data.py', '--root', str(DATA/'datasets'),
        '--output', str(OUT/'data_integrity_all.json')])
    run('final_report', ['summarize_results.py', '--root', str(OUT)])
    status('complete')
except Exception as exc:
    status('failed', error=repr(exc))
    raise
