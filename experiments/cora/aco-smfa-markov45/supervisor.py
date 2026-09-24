"""Single-owner, resumable Markov-only experiment; never trains seed1."""
import os, sys, json, time, subprocess, fcntl, hashlib
from pathlib import Path
from common import read_config, bind, save_json

def main():
 src=Path(__file__).resolve().parent; os.chdir(src)
 base=Path('/data1/CST/CORA/aco-smfa-markov45');base.mkdir(parents=True,exist_ok=True)
 lock=open(base/'supervisor.lock','a+')
 try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 except BlockingIOError:return
 cache=base/'cache';(cache/'tmp').mkdir(parents=True,exist_ok=True)
 os.environ.update(MUJOCO_GL='egl',XLA_PYTHON_CLIENT_PREALLOCATE='false',OMP_NUM_THREADS='4',OPENBLAS_NUM_THREADS='4',MKL_NUM_THREADS='4',XDG_CACHE_HOME=str(cache),TMPDIR=str(cache/'tmp'))
 for s in [4,5]:bind(read_config(f'config_seed{s}.json'))
 for n in ['logs','stages']:(base/n).mkdir(exist_ok=True)
 hashes={str(p.relative_to(src)):hashlib.sha256(p.read_bytes()).hexdigest() for p in src.rglob('*.py') if '__pycache__' not in str(p)}
 manifest=base/'source_hashes.json'
 if manifest.exists():assert json.loads(manifest.read_text())==hashes
 else:save_json(manifest,hashes)
 active=[]
 def runjob(key,args,env=None):
  marker=base/'stages'/f'{key}.json'
  if marker.exists():return None
  f=open(base/'logs'/f'{key}.log','a');p=subprocess.Popen([sys.executable,'-u',*args],stdout=f,stderr=subprocess.STDOUT,env=env)
  j=(p,f,marker,key);active.append(j);return j
 def finish(j):
  if j is None:return
  p,f,m,k=j;rc=p.wait();f.close();active.remove(j)
  if rc:raise RuntimeError(f'{k} exited {rc}; inspect log')
  save_json(m,dict(completed=time.time()))
 def status(stage,**kw):save_json(base/'status.json',dict(stage=stage,time=time.time(),pid=os.getpid(),active=[dict(pid=j[0].pid,job=j[3]) for j in active],**kw))
 try:
  for stage in ['preflight','audit']:
   status(stage);finish(runjob(stage,['experiment.py',stage,'--config','config_seed4.json']))
  lanes={n:dict(gpu=g,job=None,queue=[(f'smoke_{n}',['smoke.py','--model',n])]+[(f'train_{n}_seed{s}',['experiment.py','train','--config',f'config_seed{s}.json','--model',n]) for s in [4,5]]) for n,g in json.loads((src/'gpu_assignment.json').read_text()).items()}
  # Seed1 evaluation can proceed while the new networks train; at most two CPU jobs.
  queue=[(f'control_s{s}_{t}_{n}',['experiment.py','control','--config',f'config_seed{s}.json','--task',t,'--condition',n]) for s in [4,5] for t in read_config('config_seed4.json')['tasks'] for n in ['aco','smfa']]
  cpu=[]
  while lanes or queue or cpu:
   for n,l in list(lanes.items()):
    if l['job'] and l['job'][0].poll() is not None:finish(l['job']);l['job']=None
    while l['job'] is None and l['queue']:
     free=int(subprocess.check_output(['nvidia-smi',f'--id={l["gpu"]}','--query-gpu=memory.free','--format=csv,noheader,nounits'],text=True).strip())
     if free < (6000 if n=='aco' else 10000):break
     key,args=l['queue'].pop(0)
     l['job']=runjob(key,args,dict(os.environ,CUDA_VISIBLE_DEVICES=l['gpu'],MUJOCO_EGL_DEVICE_ID=l['gpu']))
    if not l['queue'] and l['job'] is None:del lanes[n]
   for j in list(cpu):
    if j[0].poll() is not None:finish(j);cpu.remove(j)
   for item in list(queue):
    if len(cpu)>=2:break
    key,args=item;s=int(key.split('_')[1][1:]);n=args[-1]
    if s>1 and not (base/'stages'/f'train_{n}_seed{s}.json').exists():continue
    queue.remove(item);j=runjob(key,args,dict(os.environ,CUDA_VISIBLE_DEVICES='',MUJOCO_EGL_DEVICE_ID='3'))
    if j:cpu.append(j)
   status('running',queued_controls=len(queue),gpu_lanes=list(lanes),poll_seconds=30)
   if lanes or queue or cpu:time.sleep(30)
  finish(runjob('report',['summarize.py']));status('complete',episodes=400)
 except BaseException as exc:
  for p,f,m,k in active:
   if p.poll() is None:p.terminate()
  for p,f,m,k in active:
   try:p.wait(timeout=30)
   except subprocess.TimeoutExpired:p.kill();p.wait()
   f.close()
  status('failed',error=repr(exc));raise

if __name__=='__main__':main()
