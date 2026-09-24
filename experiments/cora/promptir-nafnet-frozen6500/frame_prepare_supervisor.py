import json,os,sys,time,subprocess,fcntl,signal
from pathlib import Path
from common import TASKS,save_json
BASE=Path('/data1/CST/CORA/promptir-nafnet-frozen6500');MODEL=sys.argv[1];GPU=int(sys.argv[2]);assert MODEL in ['promptir','nafnet']
lock=open(BASE/f'frame_prepare_{MODEL}.lock','a+');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
(BASE/'logs').mkdir(exist_ok=True);(BASE/'done').mkdir(exist_ok=True)
def stop(sig,frame):raise RuntimeError('Interrupted')
signal.signal(signal.SIGTERM,stop)
child=None
try:
 for task in TASKS:
  key=f'frame_prepare_{MODEL}_{task}';mark=BASE/'done'/(key+'.json')
  if mark.exists():continue
  streak=0
  while streak<3:
   line=subprocess.check_output(['nvidia-smi','--query-gpu=index,memory.free,utilization.gpu','--format=csv,noheader,nounits'],text=True).splitlines()[GPU]
   idx,free,util=map(int,line.split(','));assert idx==GPU
   streak=streak+1 if free>=14000 and util<=65 else 0
   save_json(BASE/f'frame_prepare_{MODEL}_status.json',dict(stage='waiting_gpu',gpu=GPU,task=task,free=free,util=util,streak=streak,time=time.time()))
   if streak<3:time.sleep(20)
  f=open(BASE/'logs'/(key+'.log'),'a')
  env=dict(os.environ,CUDA_VISIBLE_DEVICES=str(GPU),OMP_NUM_THREADS='4',MKL_NUM_THREADS='4',OPENBLAS_NUM_THREADS='4',XLA_PYTHON_CLIENT_PREALLOCATE='false')
  child=subprocess.Popen([sys.executable,'-u','frame_prepare.py',MODEL,task],stdout=f,stderr=subprocess.STDOUT,env=env,start_new_session=True)
  save_json(BASE/f'frame_prepare_{MODEL}_status.json',dict(stage='working',gpu=GPU,task=task,pid=child.pid,time=time.time()))
  rc=child.wait();child=None;f.close()
  if rc:raise RuntimeError(f'{key} failed {rc}')
  save_json(mark,dict(completed=time.time()))
 save_json(BASE/f'frame_prepare_{MODEL}_status.json',dict(stage='complete',gpu=GPU,time=time.time()))
except BaseException as e:
 if child is not None and child.poll() is None:os.killpg(child.pid,signal.SIGTERM)
 save_json(BASE/f'frame_prepare_{MODEL}_status.json',dict(stage='failed',error=repr(e),time=time.time()))
 raise
