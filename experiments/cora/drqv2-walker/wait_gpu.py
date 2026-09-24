"""Detached, locked GPU queue. Never kill workloads or exceed the fixed budget."""
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
C = json.loads((ROOT/'config.json').read_text())
DATA = Path(C['data_root'])
DATA.mkdir(parents=True, exist_ok=True)


def status(kind, **kw):
    p = DATA/'queue-status.json'
    tmp = p.with_suffix('.tmp')
    tmp.write_text(json.dumps(dict(status=kind, pid=os.getpid(), timestamp=time.time(), **kw), indent=2))
    os.replace(tmp, p)
    print(json.dumps(dict(status=kind, **kw)), flush=True)


def run():
    lock = open(DATA/'queue.lock', 'w')
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print('Existing queue owns lock; exiting.', flush=True)
        return
    if (DATA/C['run']/'report.json').exists():
        status('complete', reason='Report already exists; no restart')
        return
    idle = {}
    while True:
        try:
            lines = subprocess.check_output(['nvidia-smi',
                '--query-gpu=index,uuid,memory.used,utilization.gpu', '--format=csv,noheader,nounits'],
                text=True, timeout=20).strip().splitlines()
            apps = subprocess.check_output(['nvidia-smi','--query-compute-apps=gpu_uuid',
                    '--format=csv,noheader'],text=True,timeout=20).splitlines()
            busy = {s.strip() for s in apps}
            snapshot, ready = [], []
            for line in lines:
                index, uuid, mem, util = [s.strip() for s in line.split(',')]
                free = (uuid not in busy and int(mem)<=C['gpu_max_memory_mib']
                        and int(util)<=C['gpu_max_utilization'])
                idle[uuid] = idle.get(uuid,0)+1 if free else 0
                snapshot.append(dict(index=index, uuid=uuid, memory_mib=int(mem),
                                     utilization=int(util), idle_checks=idle[uuid]))
                if idle[uuid]>=C['gpu_idle_checks']:
                    ready.append((index,uuid))
            status('waiting_gpu', gpus=snapshot)
            if ready:
                index, uuid = ready[0]
                # Cooperative reservation with other runs of this project.
                reservation = open(DATA/f'gpu-{index}.lock','w')
                try:
                    fcntl.flock(reservation,fcntl.LOCK_EX | fcntl.LOCK_NB)
                except BlockingIOError:
                    time.sleep(C['gpu_poll_seconds'])
                    continue
                env = dict(os.environ, CUDA_VISIBLE_DEVICES=uuid, MUJOCO_GL='egl',
                           MUJOCO_EGL_DEVICE_ID=index,
                           OMP_NUM_THREADS='4', MKL_NUM_THREADS='4',
                           XDG_CACHE_HOME=str(DATA/'cache'), TMPDIR=str(DATA/'tmp'))
                for sub in ['cache','tmp']:
                    (DATA/sub).mkdir(exist_ok=True)
                smoke_report = DATA/(C['run']+'_smoke')/'report.json'
                if not smoke_report.exists():
                    status('smoke', gpu=index)
                    with open(DATA/'smoke.log','a') as log:
                        rc = subprocess.call([sys.executable,'-u','runner.py','--smoke'],
                            cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT)
                    if rc:
                        status('failed', stage='smoke', returncode=rc)
                        return
                # The gap between checking and launch is unavoidable on a shared server;
                # no other users' processes are stopped or modified.
                status('training', gpu=index)
                with open(DATA/'train.log','a') as log:
                    rc = subprocess.call([sys.executable,'-u','runner.py'],cwd=ROOT,
                                         env=env, stdout=log, stderr=subprocess.STDOUT)
                report = DATA/C['run']/'report.json'
                status('complete' if rc==0 and report.exists() else 'failed',
                       returncode=rc, report=str(report))
                return
        except (subprocess.SubprocessError, ValueError) as exc:
            status('waiting_gpu', query_error=str(exc))
        time.sleep(C['gpu_poll_seconds'])


if __name__=='__main__':
    run()
