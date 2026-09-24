"""Continue GPU-complete models through empirically selected CPU evaluations."""
import os,sys,time,json,subprocess,fcntl,signal
from pathlib import Path
from common import TASKS,DEGS,save_json,read_config,root
BASE=Path('/data1/CST/CORA/promptir-nafnet-frozen6500');MODELS=['promptir','nafnet']
os.chdir(Path(__file__).resolve().parent);BASE.mkdir(parents=True,exist_ok=True)
lock=open(BASE/'master.lock','a+');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
for d in ['logs','done','cache/tmp','benchmark']:(BASE/d).mkdir(parents=True,exist_ok=True)
os.environ.update(TMPDIR=str(BASE/'cache/tmp'),XDG_CACHE_HOME=str(BASE/'cache'))
cores=sorted(os.sched_getaffinity(0));assert len(cores)>=64
active={};prep={}
def stop(sig,frame):raise RuntimeError('Master interrupted')
signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
def status(stage,**kw):save_json(BASE/'status.json',dict(stage=stage,pid=os.getpid(),time=time.time(),active=[dict(job=k,pid=p.pid) for k,(p,f) in active.items()],prepare=[dict(model=k,pid=p.pid) for k,(p,f) in prep.items()],**kw))
def launch(key,args,store=active,env=None):
 f=open(BASE/'logs'/(key+'.log'),'a');p=subprocess.Popen([sys.executable,'-u',*args],env=env,stdout=f,stderr=subprocess.STDOUT,start_new_session=True);store[key]=(p,f)
def reap():
 for key,(p,f) in list(active.items()):
  if p.poll() is None:continue
  f.close();del active[key]
  if p.returncode:raise RuntimeError(f'{key} failed {p.returncode}; see logs')
  save_json(BASE/'done'/(key+'.json'),dict(completed=time.time()))
def pool(jobs,n,threads,label):
 queue=[x for x in jobs if not (BASE/'done'/(x[0]+'.json')).exists()];slots={};started=time.perf_counter()
 while queue or active:
  reap();slots={s:k for s,k in slots.items() if k in active}
  for slot in range(n):
   if not queue:break
   if slot in slots:continue
   key,args=queue.pop(0);aff=cores[slot*threads:(slot+1)*threads];assert len(aff)==threads
   launch(key,args+['--cores',','.join(map(str,aff))]);slots[slot]=key
  status(label,queued=len(queue),workers=n,threads=threads);time.sleep(3)
 return time.perf_counter()-started
try:
 while True:
  stages={}
  for model in MODELS:
   c=read_config('config_'+model+'.json');path=root(c)/'images'/model/'summary.json'
   stages[model]='images_complete' if path.exists() and json.loads(path.read_text())['all']['n']==130000 else 'waiting_images'
  if all(x=='images_complete' for x in stages.values()):break
  status('waiting_images',model_stages=stages);time.sleep(30)
 for model,gpu in [('promptir',0),('nafnet',1)]:
  prepare_status=BASE/f'frame_prepare_{model}_status.json'
  if prepare_status.exists() and json.loads(prepare_status.read_text())['stage']=='complete':continue
  launch(model,['frame_prepare_supervisor.py',model,str(gpu)],prep)
 candidates=[(8,4),(16,4),(32,2),(64,1)];times=[]
 for workers,threads in candidates:
  label=f'w{workers}_t{threads}';record=BASE/'benchmark'/label/'timing.json'
  if record.exists():times.append(json.loads(record.read_text()));continue
  run=label+'_'+str(int(time.time()));jobs=[]
  for i in range(64):
   model=MODELS[i%2];task=TASKS[i%10];kind=DEGS[i%13][0]
   jobs.append((f'bench_{run}_{i}',['control_worker.py','--model',model,'--task',task,'--mode','single','--kind',kind,'--benchmark',run,'--index',str(i)]))
  seconds=pool(jobs,workers,threads,'benchmark_'+label)
  rec=dict(workers=workers,threads=threads,seconds=seconds,episodes=64,episodes_per_hour=64*3600/seconds,attempt=run,scope='end-to-end complete episode including policy/model loading',excluded_from_formal=True)
  save_json(record,rec);times.append(rec)
 best=min(times,key=lambda x:x['seconds']);save_json(BASE/'parallelism.json',dict(candidates=times,chosen=best,scope='tested CPU settings only, 64 identical complete episodes each'))
 jobs=[]
 for model in MODELS:
  for task in TASKS:
   for mode,kind in [('markov',None)]+[('single',k) for k,_ in DEGS]:
    key=f'formal_{model}_{task}_{kind or mode}';args=['control_worker.py','--model',model,'--task',task,'--mode',mode]
    if kind:args+=['--kind',kind]
    jobs.append((key,args))
 pool(jobs,best['workers'],best['threads'],'formal_control')
 for model,(p,f) in prep.items():
  while p.poll() is None:status('waiting_frame_inputs',model=model);time.sleep(10)
  f.close()
  if p.returncode:raise RuntimeError(f'frame preparation {model} failed {p.returncode}')
 jobs=[(f'frame_{m}_{t}',['frame_worker.py','--model',m,'--task',t]) for m in MODELS for t in TASKS]
 pool(jobs,best['workers'],best['threads'],'fixed_history_markov')
 subprocess.run([sys.executable,'report_baselines.py'],check=True)
 status('complete',formal_episodes=1500,frame_files=20)
except BaseException as e:
 for k,(p,f) in list(active.items())+list(prep.items()):
  if p.poll() is None:os.killpg(p.pid,signal.SIGTERM)
  f.close()
 status('failed',error=repr(e));raise
