"""Linux supervisor. One pipeline, no duplicate jobs, resume only matching source/config."""
import argparse
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
    p=argparse.ArgumentParser()
    p.add_argument('--config',default='config.json')
    p.add_argument('--gpu',default='auto',help='auto or a physical GPU index; always waits for idle')
    p.add_argument('--control-workers',type=int,default=1,choices=[1,2,3,4])
    a=p.parse_args(); c=read_config(a.config); r=bind(c)
    lock=(r/'pipeline.lock').open('a+')
    fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    lock.seek(0); lock.truncate(); lock.write(str(os.getpid())); lock.flush()
    src=Path(__file__).resolve().parent
    config=str(Path(a.config).resolve())
    sources={str(q.relative_to(src)):hashlib.sha256(q.read_bytes()).hexdigest()
             for q in sorted(src.rglob('*.py')) if '__pycache__' not in str(q)}
    source_file=r/'source_hashes.json'
    if source_file.exists():
        assert json.loads(source_file.read_text())==sources, 'Source changed since run started: use a new experiment ID, do not mix results'
    else: save_json(source_file,sources)
    (r/'logs').mkdir(exist_ok=True); (r/'stages').mkdir(exist_ok=True)
    cache=Path(c['data_root'])/'cache'; (cache/'tmp').mkdir(parents=True,exist_ok=True)
    os.environ.update(MUJOCO_GL='egl',XLA_PYTHON_CLIENT_PREALLOCATE='false',
        OMP_NUM_THREADS=str(c['torch_threads']),OPENBLAS_NUM_THREADS=str(c['torch_threads']),
        MKL_NUM_THREADS=str(c['torch_threads']),XDG_CACHE_HOME=str(cache),TMPDIR=str(cache/'tmp'))
    children=[]

    def status(stage,**kw):
        save_json(r/'status.json',dict(pid=os.getpid(),time=time.time(),stage=stage,**kw))

    def gpu():
        while True:
            try:
                out=subprocess.check_output(['nvidia-smi','--query-gpu=index,memory.used,utilization.gpu',
                    '--format=csv,noheader,nounits'],text=True,timeout=10)
                for line in out.splitlines():
                    k,mem,util=map(int,line.split(','))
                    if (a.gpu=='auto' or str(k)==a.gpu) and mem<2000 and util<15:
                        return str(k)
                status('waiting_for_gpu',requested=a.gpu,poll_seconds=10)
            except (OSError,ValueError,subprocess.SubprocessError) as e:
                status('waiting_for_gpu',error=str(e),poll_seconds=10)
            time.sleep(10)

    def launch(key,args,device=None):
        marker=r/'stages'/(key+'.json')
        if marker.exists(): return None
        env=os.environ.copy()
        if device is not None: env['CUDA_VISIBLE_DEVICES']=device
        cmd=[sys.executable,'-u',str(src/'experiment.py'),*args,'--config',config]
        log=(r/'logs'/(key+'.log')).open('a')
        proc=subprocess.Popen(cmd,cwd=src,env=env,stdout=log,stderr=subprocess.STDOUT)
        job=(proc,log,marker,key,cmd); children.append(job)
        status('running',job=key,child_pid=proc.pid)
        return job

    def finish(job):
        if job is None: return
        proc,log,marker,key,cmd=job
        code=proc.wait(); log.close(); children.remove(job)
        if code: raise RuntimeError(f'{key} failed with exit {code}; inspect logs/{key}.log')
        save_json(marker,dict(completed=time.time(),config_hash=fingerprint(c),command=cmd))

    def run(key,args,on_gpu=False):
        if (r/'stages'/(key+'.json')).exists(): return
        device=gpu() if on_gpu else None
        finish(launch(key,args,device))

    def controls(conditions):
        queue=[(f'control_{t}_{k}',['control','--task',t,'--condition',k]) for t in c['tasks'] for k in conditions]
        active=[]
        while queue or active:
            while queue and len(active)<a.control_workers:
                key,args=queue.pop(0); job=launch(key,args)
                if job: active.append(job)
            ready=[j for j in active if j[0].poll() is not None]
            for job in ready: finish(job); active.remove(job)
            if active:
                status('control',active=[dict(job=j[3],pid=j[0].pid) for j in active],queued=len(queue))
                time.sleep(2)

    try:
        # Always recheck external policy files before trusting old markers.
        subprocess.run([sys.executable,str(src/'experiment.py'),'preflight','--config',config],check=True)
        for task in c['tasks']: run('collect_'+task,['collect','--task',task])
        run('audit',['audit'])
        controls(['clean','raw'])
        for name in ['aco','smfa']:
            run('train_'+name,['train','--model',name],True)
            run('images_'+name,['images','--model',name],True)
            run('benchmark_'+name,['benchmark','--model',name],True)
            controls([name])
        run('report',['report'])
        status('complete',control_episodes=400,train_seeds_per_model=1)
    except BaseException as e:
        for job in children:
            if job[0].poll() is None: job[0].terminate()
        for job in children:
            try: job[0].wait(timeout=30)
            except subprocess.TimeoutExpired: job[0].kill(); job[0].wait()
            job[1].close()
        status('failed',error=repr(e))
        raise


if __name__=='__main__': main()
