import os,sys,time,json,subprocess,fcntl,traceback,signal
from common import *
ROOT.mkdir(parents=True,exist_ok=True)
os.chdir(Path(__file__).resolve().parent)
def interrupted(sig,frame):raise RuntimeError('Supervisor interrupted')
signal.signal(signal.SIGTERM,interrupted)
lock=open(ROOT/'supervisor.lock','w');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
protocol=ROOT/'protocol.json'
if protocol.exists():assert json.loads(protocol.read_text())==CONFIG
else:save(protocol,CONFIG)
cores=sorted(os.sched_getaffinity(0));assert len(cores)>=64
slots=[cores[i*4:i*4+4] for i in range(16)]
(ROOT/'logs').mkdir(exist_ok=True);(ROOT/'done').mkdir(exist_ok=True)
os.environ['TMPDIR']=str(ROOT/'tmp');(ROOT/'tmp').mkdir(exist_ok=True)
active={}
def stage(name,jobs):
 pending=[]
 for task,extra in jobs:
  ident='_'.join([name,task]+extra);marker=ROOT/'done'/(ident+'.json')
  if not marker.exists():pending.append((task,extra,ident,marker))
 while pending or active:
  for slot in list(active):
   proc,f,ident,marker=active[slot];rc=proc.poll()
   if rc is not None:
    f.close();del active[slot]
    if rc:raise RuntimeError(f'{ident} failed exit {rc}; see logs')
    save(marker,dict(completed=time.time(),returncode=rc))
  for slot in range(16):
   if not pending:break
   if slot in active:continue
   task,extra,ident,marker=pending.pop(0);cmd=[sys.executable,'run.py',name,'--cores',','.join(map(str,slots[slot]))]
   if task:cmd+=['--task',task]
   cmd+=extra;f=open(ROOT/'logs'/(ident+'.log'),'a');proc=subprocess.Popen(cmd,stdout=f,stderr=subprocess.STDOUT,env=dict(os.environ,PYTHONUNBUFFERED='1',MUJOCO_EGL_DEVICE_ID='0',XLA_PYTHON_CLIENT_PREALLOCATE='false'))
   active[slot]=(proc,f,ident,marker)
  save(ROOT/'status.json',dict(state='running',stage=name,pending=len(pending),active=[dict(pid=v[0].pid,job=v[2]) for v in active.values()],updated=time.time(),workers=16))
  time.sleep(3)
try:
 stage('collect',[(t,[]) for t in TASKS])
 stage('corrupt',[(t,[]) for t in TASKS])
 stage('calibrate',[(t,[]) for t in TASKS])
 stage('restore',[(t,['--method',m]) for t in TASKS for m in METHODS[1:]])
 stage('evaluate',[(t,['--episode',str(e)]) for t in TASKS for e in range(5)])
 stage('report',[('',[])])
 save(ROOT/'status.json',dict(state='complete',updated=time.time()))
except BaseException as e:
 for proc,f,_,_ in active.values():
  if proc.poll() is None:proc.terminate()
 save(ROOT/'status.json',dict(state='failed',error=str(e),updated=time.time()));traceback.print_exc();raise
