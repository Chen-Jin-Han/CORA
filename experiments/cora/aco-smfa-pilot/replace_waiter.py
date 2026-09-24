"""Replace only the verified idle project waiter; refuse active experiment stages."""
import json
import os
from pathlib import Path
import signal
import subprocess
import time

root = Path('/home/gpuadmin/CST/CORA/aco-smfa-pilot')
out = Path('/data1/CST/CORA/aco-smfa-pilot/outputs')
state = json.loads((out/'pipeline_status.json').read_text())
pid = state['pid']
assert state['stage'] == 'waiting_for_gpu', state
cmd = Path(f'/proc/{pid}/cmdline').read_bytes()
assert b'run_pipeline.py' in cmd, cmd
assert Path(f'/proc/{pid}/cwd').resolve() == root
children = Path(f'/proc/{pid}/task/{pid}/children').read_text().strip()
assert not children, ('Refuse to interrupt active child', children)
os.kill(pid, signal.SIGTERM)
for _ in range(50):
    if not Path(f'/proc/{pid}').exists():
        break
    time.sleep(.1)
else:
    raise RuntimeError('Old waiter still exists; refusing duplicate launch')
with (out/'supervisor.log').open('ab', buffering=0) as log:
    proc = subprocess.Popen(['bash', 'launch_pipeline.sh'], cwd=root,
        stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT,
        start_new_session=True, close_fds=True)
print(json.dumps(dict(replaced_pid=pid, detached_launcher_pid=proc.pid)), flush=True)
