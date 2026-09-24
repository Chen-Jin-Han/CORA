"""Single owner, restartable stages, resource polling independent of Codex quota."""
import os,sys,json,time,fcntl,subprocess,hashlib,signal
from pathlib import Path
from common import read_config,bind,save_json,DEGS
from protocol import jobs

def main():
    src=Path(__file__).resolve().parent;os.chdir(src);c=read_config(os.environ.get('EXPERIMENT_CONFIG','config_seed7.json'));r=bind(c)
    lock=open(r/'supervisor.lock','a+')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:print('Existing owner; exit',flush=True);return
    for d in ['logs','stages','cache/tmp']:(r/d).mkdir(parents=True,exist_ok=True)
    hashes={str(p.relative_to(src)):hashlib.sha256(p.read_bytes()).hexdigest() for p in src.rglob('*.py') if '__pycache__' not in str(p)}
    manifest=r/'source_hashes.json'
    if manifest.exists():assert json.loads(manifest.read_text())==hashes
    else:save_json(manifest,hashes)
    base=dict(os.environ,CUDA_VISIBLE_DEVICES='',MUJOCO_GL='egl',MUJOCO_EGL_DEVICE_ID='0',XLA_PYTHON_CLIENT_PREALLOCATE='false',OMP_NUM_THREADS='4',OPENBLAS_NUM_THREADS='4',MKL_NUM_THREADS='4',XDG_CACHE_HOME=str(r/'cache'),TMPDIR=str(r/'cache/tmp'))
    active={};gpu_streak={};gpu_locks={}
    def status(stage,**kw):
        save_json(r/'status.json',dict(stage=stage,time=time.time(),pid=os.getpid(),active=[dict(id=k,pid=v[0].pid,gpu=v[2]) for k,v in active.items()],**kw))
    def done(k):return (r/'stages'/f'{k}.json').exists()
    def launch(k,args,gpu=None,threads=4):
        env=dict(base,OMP_NUM_THREADS=str(threads),OPENBLAS_NUM_THREADS=str(threads),MKL_NUM_THREADS=str(threads))
        if gpu is not None:env['CUDA_VISIBLE_DEVICES']=str(gpu)
        f=open(r/'logs'/f'{k}.log','a');p=subprocess.Popen([sys.executable,'-u',*args],stdout=f,stderr=subprocess.STDOUT,env=env,start_new_session=True)
        active[k]=(p,f,gpu);print('START',k,p.pid,'GPU',gpu,flush=True)
    def reap():
        for k,(p,f,g) in list(active.items()):
            if p.poll() is None:continue
            f.close();del active[k]
            if g is not None:
                fh=gpu_locks.pop(g);fcntl.flock(fh,fcntl.LOCK_UN);fh.close()
            if p.returncode:raise RuntimeError(f'{k} exited {p.returncode}; see logs/{k}.log')
            save_json(r/'stages'/f'{k}.json',dict(completed=time.time()));print('DONE',k,flush=True)
    def wait_stage(k,args,threads=4):
        if done(k):return
        launch(k,args,threads=threads)
        while k in active:reap();status(k);time.sleep(5)
    def choose_gpu(model):
        # Share only a relatively idle device with a memory reserve; never stop peers.
        raw=subprocess.check_output(['nvidia-smi','--query-gpu=index,memory.free,utilization.gpu','--format=csv,noheader,nounits'],text=True)
        need=8000 if model=='aco' else 12000
        for line in raw.splitlines():
            idx,free,util=[int(x.strip()) for x in line.split(',')]
            if str(idx)!=os.environ.get('ALLOWED_GPU',str(idx)):continue
            ok=free>=need and util<=60 and idx not in gpu_locks
            gpu_streak[(model,idx)]=gpu_streak.get((model,idx),0)+1 if ok else 0
            if gpu_streak[(model,idx)]<3:continue
            fh=open(Path(c['data_root'])/f'gpu{idx}.lock','a+')
            try:fcntl.flock(fh,fcntl.LOCK_EX|fcntl.LOCK_NB)
            except BlockingIOError:fh.close();continue
            gpu_locks[idx]=fh;return idx
        return None
    def stop(signum,frame):raise RuntimeError(f'received signal {signum}')
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    try:
        wait_stage('audit',['run.py','audit'],1)
        # Each model independently queues smoke -> train -> images. No extra seeds.
        while not all(done('images_'+m) for m in ['smfa']):
            reap()
            for m in ['smfa']:
                if any(k.endswith('_'+m) for k in active):continue
                stage=next((s for s in ['smoke','train','images'] if not done(s+'_'+m)),None)
                if stage is None:continue
                gpu=choose_gpu(m)
                if gpu is None:continue
                args=['smoke.py','--model',m] if stage=='smoke' else ['run.py',stage,'--model',m]
                launch(stage+'_'+m,args,gpu)
            status('training_or_gpu_wait',poll_seconds=30)
            if not all(done('images_'+m) for m in ['smfa']):time.sleep(30)
        if os.environ.get('PHASE')=='gpu':
            status('gpu_complete');return
        wait_stage('baseline',['run.py','baseline'],1)
        queue=[]
        for t,mode,k,method in jobs(c):
            if method in ['raw','clean']:continue
            key='_'.join([t,mode,k or 'all',method])
            if not done(key):queue.append((key,t,mode,k,method))
        while queue or active:
            reap()
            while queue and len(active)<c['control_workers']:
                key,t,mode,k,method=queue.pop(0)
                args=['run.py','control','--task',t,'--mode',mode,'--condition',method]
                if k:args+=['--kind',k]
                launch(key,args)
            status('control',queued=len(queue),workers=c['control_workers'])
            if queue or active:time.sleep(10)
        wait_stage('report',['run.py','report']);status('complete',episodes=2300)
    except BaseException as e:
        for p,f,g in active.values():
            if p.poll() is None:os.killpg(p.pid,signal.SIGTERM)
        for p,f,g in active.values():
            try:p.wait(timeout=30)
            except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait()
            f.close()
        status('failed',error=repr(e));raise
if __name__=='__main__':main()
