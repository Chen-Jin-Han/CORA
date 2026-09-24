"""Persistent GPU queue, empirical CPU scheduler, exact restart markers."""
import os,sys,time,json,subprocess,fcntl,signal,hashlib
from pathlib import Path
from common import read_config,root,save_json,DEGS,TASKS
BASE=Path('/data1/CST/CORA/cora-ablation');VARIANTS=['no_context','no_local','full_channel']
os.chdir(Path(__file__).resolve().parent);BASE.mkdir(parents=True,exist_ok=True)
lock=open(BASE/'master.lock','a+');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
for d in ['logs','cache/tmp','done']:(BASE/d).mkdir(exist_ok=True,parents=True)
os.environ.update(TMPDIR=str(BASE/'cache/tmp'),XDG_CACHE_HOME=str(BASE/'cache'))
manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('.').glob('*.py')}
if (BASE/'source.json').exists():assert json.loads((BASE/'source.json').read_text())==manifest
else:save_json(BASE/'source.json',manifest)
active={};cores=sorted(os.sched_getaffinity(0));assert len(cores)>=64
def interrupted(sig,frame):raise RuntimeError('Master interrupted')
signal.signal(signal.SIGTERM,interrupted);signal.signal(signal.SIGINT,interrupted)
def status(stage,**kw):save_json(BASE/'status.json',dict(stage=stage,updated=time.time(),pid=os.getpid(),active=[dict(job=k,pid=v[0].pid) for k,v in active.items()],**kw))
def reap():
 for k,(p,f) in list(active.items()):
  if p.poll() is None:continue
  f.close();del active[k]
  if p.returncode:raise RuntimeError(f'{k} failed exit {p.returncode}; see logs')
  save_json(BASE/'done'/(k+'.json'),dict(completed=time.time()))
def launch(k,args,env=None):
 f=open(BASE/'logs'/(k+'.log'),'a');p=subprocess.Popen([sys.executable,'-u',*args],stdout=f,stderr=subprocess.STDOUT,env=env,start_new_session=True);active[k]=(p,f)
def pool(jobs,n,threads,label):
 queue=[j for j in jobs if not (BASE/'done'/(j[0]+'.json')).exists()];occupied={};start=time.perf_counter()
 while queue or active:
  reap();occupied={s:k for s,k in occupied.items() if k in active}
  for slot in range(n):
   if not queue:break
   if slot in occupied:continue
   k,args=queue.pop(0);assigned=cores[slot*threads:(slot+1)*threads];assert len(assigned)==threads
   launch(k,args+['--cores',','.join(map(str,assigned))]);occupied[slot]=k
  status(label,queued=len(queue),workers=n,threads=threads);time.sleep(2)
 return time.perf_counter()-start
try:
 for v,gpu in zip(VARIANTS,[0,2,3]):
  k='gpu_'+v
  if not (BASE/'done'/(k+'.json')).exists():launch(k,['supervisor.py'],dict(os.environ,EXPERIMENT_CONFIG='config_'+v+'.json',PHASE='gpu',ALLOWED_GPU=str(gpu)))
 while active:reap();status('gpu_training_or_images');time.sleep(10)
 # Identical 32 independent complete episodes for every setting. Includes all
 # variants/tasks; separate seeds/outputs, never counted as formal evaluation.
 candidates=[(8,4),(16,4),(32,2)];timings=[]
 for n,th in candidates:
  label=f'w{n}_t{th}';record=BASE/'benchmark'/label/'timing.json'
  if record.exists():timings.append(json.loads(record.read_text()));continue
  # A restarted partial benchmark is resumed but its timing is marked invalid;
  # use a fresh attempt to obtain a fair complete makespan.
  attempt=label+'_'+str(int(time.time()));jobs=[]
  for i in range(32):
   v=VARIANTS[i%3];t=TASKS[i%10];kind=DEGS[i%13][0]
   args=['worker.py','--variant',v,'--task',t,'--mode','single','--kind',kind,'--benchmark',attempt,'--index',str(i)]
   jobs.append(('bench_'+attempt+'_'+str(i),args))
  seconds=pool(jobs,n,th,'benchmark_'+label)
  rec=dict(workers=n,threads=th,seconds=seconds,episodes=32,episodes_per_hour=32/seconds*3600,attempt=attempt,scope='end-to-end complete episodes including model load, compilation and scheduling',excluded_from_formal=True)
  save_json(record,rec);timings.append(rec)
 best=min(timings,key=lambda x:x['seconds']);save_json(BASE/'parallelism.json',dict(candidates=timings,chosen=best,note='Fastest measured configuration; not an absolute hardware maximum. Single-episode jobs include more load overhead than formal 5/10-episode jobs.'))
 jobs=[]
 for v in VARIANTS:
  for task in TASKS:
   for mode,kind in [('markov',None)]+[('single',k) for k,_ in DEGS]:
    key='formal_'+v+'_'+task+'_'+(kind or mode);args=['worker.py','--variant',v,'--task',task,'--mode',mode]
    if kind:args+=['--kind',kind]
    jobs.append((key,args))
 pool(jobs,best['workers'],best['threads'],'formal_control')
 subprocess.run([sys.executable,'report_ablation.py'],check=True)
 status('complete',formal_episodes=2250)
except BaseException as e:
 for p,f in active.values():
  if p.poll() is None:os.killpg(p.pid,signal.SIGTERM)
 for p,f in active.values():
  try:p.wait(timeout=30)
  except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL)
  f.close()
 status('failed',error=repr(e));raise
