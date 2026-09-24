import json,time
from pathlib import Path

class Tuner:
 def __init__(self,root):
  self.root=root;self.levels=[2,4,6,8,12];self.i=0;self.limit=2;self.started=None;self.baseline=None;self.results=[];self.finished=False;self.previous_cpu=None;self.idle=[]
 def count(self):
  count=0
  for p in self.root.glob('control/**/episodes.jsonl'):
   for line in p.read_text().splitlines():
    try:
     row=json.loads(line)
     assert row['terminal'] and row['decisions']==500
     count+=1
    except json.JSONDecodeError: pass
  return count
 def resources(self):
  cpu=list(map(int,Path('/proc/stat').read_text().splitlines()[0].split()[1:9]));total=sum(cpu);idle=cpu[3]+cpu[4]
  fraction=None
  if self.previous_cpu:
   dt=total-self.previous_cpu[0]
   if dt:fraction=(idle-self.previous_cpu[1])/dt
  self.previous_cpu=(total,idle)
  mem={line.split(':')[0]:int(line.split()[1]) for line in Path('/proc/meminfo').read_text().splitlines() if line.startswith(('MemAvailable:','MemTotal:'))}
  return fraction,mem['MemAvailable']/1024**2
 def tick(self,active,queued):
  from common import save_json
  now=time.time();idle,free=self.resources()
  if self.finished:return self.limit
  if free<32 or (idle is not None and idle<.10):
   self.limit=max(2,self.limit//2);self.finished=True;self.reason='resource_guard';self.save();return self.limit
  if active<self.limit and queued:
   self.started=None;self.baseline=None;return self.limit
  if self.started is None:self.started=now;self.idle=[]
  if idle is not None:self.idle.append(idle)
  if now-self.started>=120 and self.baseline is None:self.baseline=(now,self.count())
  if self.baseline and now-self.baseline[0]>=300:
   duration=now-self.baseline[0];n=self.count()-self.baseline[1]
   row=dict(workers=self.limit,episodes=n,seconds=duration,episodes_per_hour=n*3600/duration,cpu_idle_fraction=sum(self.idle)/len(self.idle) if self.idle else None,available_gib=free,time=now)
   self.results.append(row)
   stop=(len(self.results)>1 and row['episodes_per_hour']<self.results[-2]['episodes_per_hour']*1.10) or self.i==len(self.levels)-1 or not queued
   if stop:
    best=max(self.results,key=lambda x:x['episodes_per_hour']);self.limit=best['workers'];self.finished=True;self.reason='measured_plateau_or_safe_cap'
   else:
    self.i+=1;self.limit=self.levels[self.i];self.started=None;self.baseline=None
  self.save();return self.limit
 def save(self):
  from common import save_json
  save_json(self.root/'parallel_benchmark.json',dict(time=time.time(),workers=self.limit,finished=self.finished,reason=getattr(self,'reason',None),results=self.results,warmup_seconds=120,measurement_seconds=300,safe_cap=12,note='Operational throughput across remaining formal jobs; task mix varies. Not an isolated hardware maximum.'))
