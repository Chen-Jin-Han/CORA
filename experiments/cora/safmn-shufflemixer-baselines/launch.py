"""Start independently locked GPU supervisors and the evaluation master once."""
import os,sys,subprocess,fcntl,json,time
from pathlib import Path
from common import save_json
base=Path('/data1/CST/CORA/safmn-shufflemixer-baselines')
base.mkdir(parents=True,exist_ok=True)
os.chdir(Path(__file__).resolve().parent)
lock=open(base/'launch.lock','a+')
fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
assert not (base/'launch.json').exists(), 'Already deployed: inspect processes/status before resuming'
jobs=[]
for model,gpu in [('safmn',0),('shufflemixer',2)]:
 env=dict(os.environ,EXPERIMENT_CONFIG='config_'+model+'.json',ALLOWED_GPU=str(gpu),PHASE='gpu',OMP_NUM_THREADS='4',MKL_NUM_THREADS='4',OPENBLAS_NUM_THREADS='4')
 with open(base/(model+'-supervisor.log'),'a') as log:
  p=subprocess.Popen([sys.executable,'-u','supervisor.py'],env=env,stdout=log,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL,start_new_session=True)
 jobs.append(dict(role=model,pid=p.pid,gpu=gpu))
with open(base/'master.log','a') as log:
 p=subprocess.Popen([sys.executable,'-u','master.py'],stdout=log,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL,start_new_session=True)
jobs.append(dict(role='master',pid=p.pid));save_json(base/'launch.json',dict(time=time.time(),jobs=jobs));print(jobs)
