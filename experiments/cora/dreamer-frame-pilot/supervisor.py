import os,sys,time,subprocess,fcntl,signal,json
from pathlib import Path
from common import ROOT,save

def main():
 os.chdir(Path(__file__).resolve().parent);ROOT.mkdir(parents=True,exist_ok=True)
 lock=open(ROOT/'lock','a+')
 try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 except BlockingIOError:return
 (ROOT/'logs').mkdir(exist_ok=True);(ROOT/'tmp').mkdir(exist_ok=True)
 env=dict(os.environ,CUDA_VISIBLE_DEVICES='',MUJOCO_GL='egl',MUJOCO_EGL_DEVICE_ID='0',OMP_NUM_THREADS='4',MKL_NUM_THREADS='4',OPENBLAS_NUM_THREADS='4',XLA_PYTHON_CLIENT_PREALLOCATE='false',TMPDIR=str(ROOT/'tmp'))
 child=None
 def status(stage,**kw):save(ROOT/'status.json',dict(stage=stage,pid=os.getpid(),time=time.time(),**kw))
 def run(stage,command):
  nonlocal child
  marker=ROOT/(stage+'.done.json')
  if marker.exists():return
  with (ROOT/'logs'/f'{stage}.log').open('a') as f:
   child=subprocess.Popen([sys.executable,'-u',*command],stdout=f,stderr=subprocess.STDOUT,env=env,start_new_session=True)
   while child.poll() is None:status(stage,child_pid=child.pid);time.sleep(5)
   assert child.returncode==0,f'{stage} failed ({child.returncode})'
  child=None;save(marker,dict(completed=time.time()))
 def terminate(sig,frame):raise RuntimeError('supervisor interrupted')
 signal.signal(signal.SIGTERM,terminate)
 try:
  run('prepare',['prepare.py']);run('evaluate',['evaluate.py']);run('cpu_benchmark',['benchmark.py'])
  run('report_cpu',['report.py'])
  streak={}
  while True:
   gpu=None
   for line in subprocess.check_output(['nvidia-smi','--query-gpu=index,memory.free,utilization.gpu','--format=csv,noheader,nounits'],text=True).splitlines():
    i,free,util=map(int,line.split(','));streak[i]=streak.get(i,0)+1 if free>=12000 and util<=60 else 0
    if streak[i]>=3:gpu=i;break
   if gpu is not None:break
   status('waiting_gpu_benchmark',cpu_results_complete=True);time.sleep(30)
  run('gpu_benchmark',['benchmark.py','--platform','gpu','--gpu',str(gpu)])
  run('report_final',['report.py']);status('complete')
 except BaseException as e:
  if child is not None and child.poll() is None:os.killpg(child.pid,signal.SIGTERM);child.wait(timeout=60)
  status('failed',error=repr(e));raise
if __name__=='__main__':main()
