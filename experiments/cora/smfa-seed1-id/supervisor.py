import os,sys,json,time,fcntl,subprocess,hashlib
from pathlib import Path
from common import read_config,bind,root,save_json,DEGS

def main():
 src=Path(__file__).resolve().parent;os.chdir(src);c=read_config('config.json');r=bind(c)
 lock=open(r/'supervisor.lock','a+')
 try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 except BlockingIOError:return
 for n in ['logs','stages','cache/tmp']:(r/n).mkdir(parents=True,exist_ok=True)
 os.environ.update(CUDA_VISIBLE_DEVICES='',MUJOCO_GL='egl',MUJOCO_EGL_DEVICE_ID='0',XLA_PYTHON_CLIENT_PREALLOCATE='false',OMP_NUM_THREADS='4',OPENBLAS_NUM_THREADS='4',MKL_NUM_THREADS='4',XDG_CACHE_HOME=str(r/'cache'),TMPDIR=str(r/'cache/tmp'))
 hashes={str(p.relative_to(src)):hashlib.sha256(p.read_bytes()).hexdigest() for p in src.rglob('*.py') if '__pycache__' not in str(p)}
 manifest=r/'source_hashes.json'
 if manifest.exists():assert json.loads(manifest.read_text())==hashes
 else:save_json(manifest,hashes)
 from checkpoint_io import digest
 ck=Path(c['checkpoint_source'])/'checkpoints/smfa/last.pt';stamp=dict(path=str(ck),sha256=digest(ck))
 cp=r/'checkpoint_source.json'
 if cp.exists():assert json.loads(cp.read_text())==stamp
 else:save_json(cp,stamp)
 from engine import load_model
 load_model(c,'smfa','cpu');print('Strict seed1 SMFA checkpoint check passed',flush=True)
 from parallel_tuning import Tuner
 tuner=Tuner(r)
 queue=[(t,k) for t in c['tasks'] for k,_ in DEGS if not (r/'stages'/f'{t}_{k}.json').exists()];active=[]
 def status(stage,**kw):save_json(r/'status.json',dict(stage=stage,time=time.time(),pid=os.getpid(),queued=len(queue),active=[dict(pid=p.pid,task=t,kind=k) for p,f,t,k in active],**kw))
 try:
  while queue or active:
   limit=tuner.tick(len(active),len(queue))
   for j in list(active):
    p,f,t,k=j
    if p.poll() is None:continue
    f.close();active.remove(j)
    if p.returncode:raise RuntimeError(f'{t}/{k} exit {p.returncode}')
    save_json(r/'stages'/f'{t}_{k}.json',dict(completed=time.time()))
   while queue and len(active)<limit:
    t,k=queue.pop(0)
    if (r/'stages'/f'{t}_{k}.json').exists():continue
    f=open(r/'logs'/f'{t}_{k}.log','a');p=subprocess.Popen([sys.executable,'-u','run.py','--task',t,'--kind',k],stdout=f,stderr=subprocess.STDOUT)
    active.append((p,f,t,k))
   status('running',workers=limit)
   if queue or active:time.sleep(10)
  subprocess.run([sys.executable,'summarize.py'],check=True);status('complete',episodes=700)
 except BaseException as e:
  for p,f,t,k in active:
   if p.poll() is None:p.terminate()
  for p,f,t,k in active:
   try:p.wait(timeout=30)
   except subprocess.TimeoutExpired:p.kill();p.wait()
   f.close()
  status('failed',error=repr(e));raise

if __name__=='__main__':main()
