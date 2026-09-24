"""One-time deployment gate: verify complete policy upload, then launch supervisor.
Used for this deployment only. Does not start until the initial collector exits
successfully (all three split manifests present); no timeout-based duplicate jobs.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tarfile
import time

DATA=Path('/data1/CST/CORA/aco-smfa-rgb')
CODE=Path('/home/gpuadmin/CST/CORA/aco-smfa-rgb')
ARCHIVE=DATA/'policies.tar'
EXPECTED_SIZE=905512960
EXPECTED_SHA='6e8c4f135db3003af7e2b167f0aa0a0f370c34a65be011f1b66ad66865c826b0'
COLLECT_PID=3507151
PY='/data1/CST/CORA/aco-smfa-pilot/env/bin/python'


def state(stage,**extra):
    tmp=DATA/'deployment-status.tmp'
    tmp.write_text(json.dumps(dict(stage=stage,time=time.time(),pid=os.getpid(),**extra),indent=2))
    tmp.replace(DATA/'deployment-status.json')


try:
    while not ARCHIVE.exists() or ARCHIVE.stat().st_size<EXPECTED_SIZE:
        state('waiting_for_policy_upload',bytes=ARCHIVE.stat().st_size if ARCHIVE.exists() else 0)
        time.sleep(10)
    assert ARCHIVE.stat().st_size==EXPECTED_SIZE
    with ARCHIVE.open('rb') as f: actual=hashlib.file_digest(f,'sha256').hexdigest()
    assert actual==EXPECTED_SHA, 'Uploaded policy archive hash mismatch'
    with tarfile.open(ARCHIVE) as tar:
        dest=(DATA/'policies').resolve()
        for m in tar.getmembers():
            assert (dest/m.name).resolve().is_relative_to(dest) and m.isfile()
        tar.extractall(dest,filter='data')
    state('policies_verified_waiting_for_initial_collection')
    proc=Path(f'/proc/{COLLECT_PID}/cmdline')
    while proc.exists() and b'experiment.py\x00collect' in proc.read_bytes(): time.sleep(10)
    cfg=json.loads((CODE/'config.json').read_text())
    run=DATA/cfg['experiment']
    assert all((run/'datasets/walker_walk'/s/'complete.json').exists() for s in ['train','val','test']), 'Initial collection failed; inspect initial-collect.log'
    subprocess.run([PY,'experiment.py','preflight','--config','config.json'],cwd=CODE,check=True)
    env=os.environ.copy(); env['RGB_PYTHON']=PY
    subprocess.run(['bash','launch.sh','--gpu','auto','--control-workers','2'],cwd=CODE,env=env,check=True)
    state('supervisor_launch_requested')
except BaseException as e:
    state('failed',error=repr(e))
    raise
