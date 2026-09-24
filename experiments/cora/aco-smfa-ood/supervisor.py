"""Detached single-owner pipeline; stage markers + per-episode resumability."""
import fcntl
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from common import read_config,bind,save_json,fingerprint

def main():
    src=Path(__file__).resolve().parent; os.chdir(src)
    c=read_config('config.json'); r=bind(c)
    lock=open(r/'pipeline.lock','a+')
    try: fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError: print('Already running');return
    lock.seek(0);lock.truncate();lock.write(str(os.getpid()));lock.flush()
    for name in ['logs','stages']: (r/name).mkdir(exist_ok=True)
    cache=Path(c['data_root'])/'cache'; (cache/'tmp').mkdir(parents=True,exist_ok=True)
    os.environ.update(MUJOCO_GL='egl',XLA_PYTHON_CLIENT_PREALLOCATE='false',
        OMP_NUM_THREADS='4',OPENBLAS_NUM_THREADS='4',MKL_NUM_THREADS='4',
        XDG_CACHE_HOME=str(cache),TMPDIR=str(cache/'tmp'))
    hashes={str(p.relative_to(src)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(src.rglob('*.py')) if '__pycache__' not in str(p)}
    manifest=r/'source_hashes.json'
    if manifest.exists(): assert json.loads(manifest.read_text())==hashes,'Source changed: inspect before resume'
    else: save_json(manifest,hashes)
    active=[]
    def status(stage,**kw): save_json(r/'status.json',dict(stage=stage,pid=os.getpid(),time=time.time(),**kw))
    def launch(key,script,args,env=None):
        marker=r/'stages'/(key+'.json')
        if marker.exists(): return None
        f=open(r/'logs'/(key+'.log'),'a')
        p=subprocess.Popen([sys.executable,'-u',script,*args],env=env,cwd=src,stdout=f,stderr=subprocess.STDOUT)
        j=(p,f,marker,key);active.append(j);status('running',job=key,child_pid=p.pid);return j
    def finish(j):
        if j is None:return
        p,f,m,key=j; rc=p.wait();f.close();active.remove(j)
        if rc:raise RuntimeError(f'{key} failed: {rc}')
        save_json(m,dict(config_hash=fingerprint(c),completed=time.time()))
    def run(key,script,args,env=None):finish(launch(key,script,args,env))
    def acquire_gpu():
        consecutive={}
        while True:
            lines=subprocess.check_output(['nvidia-smi','--query-gpu=index,uuid,memory.used,utilization.gpu','--format=csv,noheader,nounits'],text=True,timeout=20).splitlines()
            busy=set(subprocess.check_output(['nvidia-smi','--query-compute-apps=gpu_uuid','--format=csv,noheader'],text=True,timeout=20).splitlines())
            for line in lines:
                i,u,m,v=[x.strip() for x in line.split(',')]
                free=u not in busy and int(m)<=1024 and int(v)<=5
                consecutive[u]=consecutive.get(u,0)+1 if free else 0
                if consecutive[u]>=3:
                    # Shared reservation with the existing DrQ queue, without changing it.
                    claim=open('/data1/CST/CORA/drqv2-walker/gpu-'+i+'.lock','a')
                    try:fcntl.flock(claim,fcntl.LOCK_EX|fcntl.LOCK_NB)
                    except BlockingIOError:claim.close();continue
                    return claim,dict(os.environ,CUDA_VISIBLE_DEVICES=u,MUJOCO_EGL_DEVICE_ID=i)
            status('waiting_for_gpu',poll_seconds=30);time.sleep(30)
    try:
        run('preflight','experiment.py',['preflight'])
        # Reuse exactly the existing dataset; audit verifies hashes and records duplicate pixels.
        run('audit','experiment.py',['audit'])
        # User authorized sharing GPUs 2 and 3. One independent model lane/card.
        lines=subprocess.check_output(['nvidia-smi','--query-gpu=index,uuid,memory.free',
            '--format=csv,noheader,nounits'],text=True,timeout=20).splitlines()
        devices={x.split(',')[0].strip():[v.strip() for v in x.split(',')[1:]] for x in lines}
        lanes={}
        for name,index in [('aco','2'),('smfa','3')]:
            uuid,free=devices[index]
            assert int(free)>=6000, f'GPU {index} has <6GiB available; inspect before restart'
            env=dict(os.environ,CUDA_VISIBLE_DEVICES=uuid,MUJOCO_EGL_DEVICE_ID=index)
            lanes[name]=dict(env=env,gpu=index,job=None,stages=[
                ('smoke_'+name,'run_ood.py',['smoke','--model',name]),
                ('train_'+name,'experiment.py',['train','--model',name]),
                ('images_id_'+name,'experiment.py',['images','--model',name]),
                ('images_ood_'+name,'run_ood.py',['images','--model',name])])
        while lanes:
            for name,lane in list(lanes.items()):
                if lane['job'] is not None and lane['job'][0].poll() is not None:
                    finish(lane['job']);lane['job']=None
                while lane['job'] is None and lane['stages']:
                    key,script,args=lane['stages'].pop(0)
                    lane['job']=launch(key,script,args,lane['env'])
                if lane['job'] is None and not lane['stages']: del lanes[name]
            if lanes:
                status('gpu_parallel',active=[dict(model=n,gpu=v['gpu'],job=v['job'][3],pid=v['job'][0].pid) for n,v in lanes.items()])
                time.sleep(5)
        queue=[(t,k,s) for t in c['tasks'] for k in ['clean']+c['ood_types']
               for s in (['clean'] if k=='clean' else ['raw','aco','smfa'])]
        while queue or active:
            while queue and len(active)<c['control_workers']:
                t,k,s=queue.pop(0)
                launch(f'control_{t}_{k}_{s}','run_ood.py',['control','--task',t,'--kind',k,'--condition',s])
            for j in list(active):
                if j[0].poll() is not None: finish(j)
            if active:
                status('control',active=[dict(job=j[3],pid=j[0].pid) for j in active],queued=len(queue));time.sleep(5)
        run('report','run_ood.py',['report']);status('complete',ood_episodes=900,clean_episodes=50)
    except BaseException as exc:
        for p,f,m,k in active:
            if p.poll() is None:p.terminate()
        for p,f,m,k in active:
            try:p.wait(timeout=30)
            except subprocess.TimeoutExpired:p.kill();p.wait()
            f.close()
        status('failed',error=repr(exc));raise

if __name__=='__main__':main()
