import argparse,os,time,json
p=argparse.ArgumentParser();p.add_argument('--id',type=int,default=0);p.add_argument('--batch',type=int,default=16);p.add_argument('--group',required=True);p.add_argument('--platform',default='cpu');p.add_argument('--seconds',type=int,default=15);p.add_argument('--cores',default='');a=p.parse_args()
if a.cores:os.sched_setaffinity(0,{int(x) for x in a.cores.split(',')})
import numpy as np
from common import ROOT,KINDS,save
from diagnostic import Diagnostic
folder=ROOT/'benchmark'/a.group;folder.mkdir(parents=True,exist_ok=True)
d=Diagnostic(a.platform,f'bench_{a.group}_{a.id}');cache=dict(np.load(ROOT/'trajectory.npz'));inputs={m:dict(np.load(ROOT/(m+'.npz'))) for m in ['raw','aco','smfa']}
# Independent replay and cross-device numerical audit, excluded from timing.
check_ids=np.array([103,129,202,417]);check=d.infer(cache,check_ids,inputs['raw'][KINDS[0]][check_ids])
refpath=ROOT/'cpu_check_reference_float32.npz'
if a.platform=='cpu' and a.id==0 and not refpath.exists():np.savez(refpath,**{k:np.asarray(v,dtype=np.float32) for k,v in check.items()})
if a.platform=='gpu' and refpath.exists():
 ref=dict(np.load(refpath));delta={k:float(np.max(np.abs(check[k].astype(float)-ref[k].astype(float)))) for k in ref}
 save(folder/f'{a.id}.numerical.json',dict(cpu_gpu_max_deltas=delta,equivalence_passed=delta['probs']<.01,threshold=.01,note='GPU performance-only when equivalence fails. Formal diagnostic metrics remain CPU-only; no relaxation of the numerical acceptance threshold.'))
if a.id==0:
 clean1=d.infer(cache,check_ids,cache['obs_image'][check_ids]);clean2=d.infer(cache,check_ids,cache['obs_image'][check_ids])
 assert all(np.array_equal(clean1[k],clean2[k]) for k in clean1)
 save(folder/'replay_check.json',dict(independent_clean_replay_exact=True))
ids=100+np.arange(a.batch)%400
def cycle():
 d.infer(cache,ids,cache['obs_image'][ids])
 for kind in KINDS:
  for m in ['raw','aco','smfa']:d.infer(cache,ids,inputs[m][kind][ids])
start=time.perf_counter();cycle();save(folder/f'{a.id}.ready.json',dict(warmup_seconds=time.perf_counter()-start,pid=os.getpid()))
while not (folder/'go').exists():time.sleep(.1)
start=time.perf_counter();started_at=time.time();cycles=0
while time.perf_counter()-start<a.seconds:cycle();cycles+=1
elapsed=time.perf_counter()-start;save(folder/f'{a.id}.json',dict(seconds=elapsed,started_at=started_at,finished_at=time.time(),positions=cycles*a.batch*2,positions_per_second=cycles*a.batch*2/elapsed,batch=a.batch,platform=a.platform))
