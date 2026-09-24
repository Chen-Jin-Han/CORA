"""Two new seeds; overlap GPU work with seed6, keep control at 8 total workers."""
import os,sys,json,time,fcntl,subprocess,signal
from pathlib import Path
from common import save_json

def main():
    src=Path(__file__).resolve().parent;os.chdir(src)
    r=Path('/data1/CST/CORA/aco-smfa-full13-seed78');r.mkdir(parents=True,exist_ok=True)
    lock=open(r/'launcher.lock','a+')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:return
    child=None
    def status(stage,**kw):save_json(r/'status.json',dict(stage=stage,pid=os.getpid(),time=time.time(),**kw))
    def run(seed,phase):
        nonlocal child
        env=dict(os.environ,EXPERIMENT_CONFIG=f'config_seed{seed}.json',PHASE=phase)
        with (r/f'seed{seed}_{phase}.log').open('a') as f:
            child=subprocess.Popen([sys.executable,'-u','supervisor.py'],stdout=f,stderr=subprocess.STDOUT,env=env)
            while child.poll() is None:
                status(phase,seed=seed,child_pid=child.pid);time.sleep(30)
            assert child.returncode==0,f'seed{seed} {phase} failed: {child.returncode}'
        child=None
    try:
        for seed in [7,8]:run(seed,'gpu')
        baseline=Path('/data1/CST/CORA/aco-smfa-full13/rgb10_seed6_fft_b128_s15000_full13_v1')
        while True:
            s=json.loads((baseline/'status.json').read_text())
            if s['stage']=='complete' and (baseline/'verification.json').exists():break
            status('waiting_seed6_control',seed6_stage=s['stage']);time.sleep(30)
        for seed in [7,8]:run(seed,'control')
        subprocess.run([sys.executable,'aggregate.py'],check=True)
        status('complete',new_training_runs=4,new_control_episodes=3000,reused_baseline_episodes=800)
    except BaseException as e:
        if child is not None and child.poll() is None:child.terminate();child.wait(timeout=60)
        status('failed',error=repr(e));raise
if __name__=='__main__':main()
