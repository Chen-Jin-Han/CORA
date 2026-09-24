import time
import numpy as np
from common import *

def collect(task):
 from dreamer_bridge import make_agent,make_env,reset,act
 from checkpoint_io import digest
 agent,cfg=make_agent(policy(task),ROOT/'loading'/task/'collection','cpu')
 assert not agent.init_policy(1)[0] and not agent.init_policy(1)[2]
 for split,count in [('calibration',2),('evaluation',5)]:
  for ep in range(count):
   path=trajectory(task,split,ep);marker=path.with_suffix('.json')
   if marker.exists():assert digest(path)==__import__('json').loads(marker.read_text())['sha256'];continue
   seed=trajectory_seed(task,split,ep);env,_,_=make_env(cfg,seed);obs=reset(env);carry=agent.init_policy(1);records={};score=0.;start=time.perf_counter()
   with agent.n_actions.lock:agent.n_actions.value=seed*10000
   def add(k,v):records.setdefault(k,[]).append(np.asarray(v))
   try:
    for t in range(500):
     for k,v in obs.items():
      if not k.startswith('log/'):add('obs_'+k,v)
     add('prev_h',carry[1]['deter'][0]);add('prev_z',carry[1]['stoch'][0]);add('prev_action',carry[3]['action'][0])
     carry,action=act(agent,carry,obs);add('action',action['action']);add('clean_h',carry[1]['deter'][0])
     obs=env.step(action);score+=float(obs['reward']);assert bool(obs['is_last'])==(t==499)
    arrays={k:np.asarray(v,dtype=np.float32) if k in ['prev_h','prev_z','clean_h'] else np.asarray(v) for k,v in records.items()}
    arrays['frame_seed']=np.arange(500,dtype=np.uint32)+seed*1000
    atomic_npz(path,**arrays);save(marker,dict(task=task,split=split,episode=ep,seed=seed,decisions=500,return_=score,seconds=time.perf_counter()-start,sha256=digest(path)))
    print(task,split,ep,score,flush=True)
   finally:env.close()
