import os,time,json
import numpy as np
from common import ROOT,POLICY,RESTORE,SEED,KINDS,DEGS,save,fingerprint

def main():
 ROOT.mkdir(parents=True,exist_ok=True)
 import jax,torch
 from dreamer_bridge import make_agent,make_env,reset,act
 from checkpoint_io import digest
 if not (ROOT/'trajectory.npz').exists():
  agent,cfg=make_agent(POLICY,ROOT/'loading/collection','cpu')
  env,_,_=make_env(cfg,SEED);obs=reset(env);carry=agent.init_policy(1)
  assert not carry[0] and not carry[2]
  with agent.n_actions.lock:agent.n_actions.value=SEED*10000
  records={};score=0;begin=time.perf_counter()
  def add(k,v):records.setdefault(k,[]).append(np.asarray(v))
  try:
   for t in range(500):
    for k,v in obs.items():
     if not k.startswith('log/'):add('obs_'+k,v)
    add('prev_h',carry[1]['deter'][0]);add('prev_z',carry[1]['stoch'][0]);add('prev_action',carry[3]['action'][0])
    carry,action=act(agent,carry,obs);add('action',action['action']);add('clean_h',carry[1]['deter'][0]);add('clean_z',carry[1]['stoch'][0])
    obs=env.step(action);score+=float(obs['reward'])
    assert bool(obs['is_last'])==(t==499)
   records['frame_seed']=np.arange(500,dtype=np.uint32)+SEED*10
   np.savez(ROOT/'trajectory.npz',**{k:np.asarray(v,dtype=np.float32) if k in ['prev_h','prev_z','clean_h','clean_z'] else np.asarray(v) for k,v in records.items()})
   save(ROOT/'trajectory.json',dict(seed=SEED,decisions=500,return_=score,seconds=time.perf_counter()-begin,calibration_frames=[0,100],evaluation_frames=[100,500],policy_sampled_actions=True))
  finally:env.close()
 cache=dict(np.load(ROOT/'trajectory.npz'));clean=cache['obs_image']
 from corruptions import corrupt
 from models import build
 from metrics import uint8
 inputs={};meta={}
 for kind in KINDS:
  rng=np.random.RandomState(SEED+10000000+KINDS.index(kind));k=[n for n,_ in DEGS].index(kind);base=DEGS[k][1];intensity=rng.uniform(.9*base,1.1*base);out=[];strengths=[]
  for i,im in enumerate(clean):
   if i:intensity=float(np.clip(intensity+rng.normal(0,.02),.9*base,1.1*base))
   strengths.append(float(intensity));out.append(corrupt(im,k,intensity,int(rng.randint(2**31-1))))
  inputs[kind]=np.stack(out);meta[kind]=strengths
 np.savez(ROOT/'raw.npz',**inputs);save(ROOT/'strengths.json',meta)
 torch.set_num_threads(4);config=json.loads((RESTORE/'protocol.json').read_text());sources={}
 for name in ['aco','smfa']:
  path=RESTORE/'checkpoints'/name/'last.pt';ck=torch.load(path,map_location='cpu',weights_only=False)
  assert ck['step']==15000 and ck['config_hash']==fingerprint(config) and config['seed']==6
  model=build(name).eval();model.load_state_dict(ck['model'],strict=True);result={};start=time.perf_counter()
  with torch.inference_mode():
   for kind in KINDS:
    outputs=[]
    for i in range(0,500,16):
     x=torch.from_numpy(inputs[kind][i:i+16]).permute(0,3,1,2).float()/127.5-1
     outputs.append(uint8(model(x)))
    result[kind]=np.concatenate(outputs)
  np.savez(ROOT/(name+'.npz'),**result);sources[name]=dict(sha256=digest(path),seconds=time.perf_counter()-start)
 save(ROOT/'preparation.json',dict(complete=True,model_sources=sources,trajectory_sha256=digest(ROOT/'trajectory.npz')))
if __name__=='__main__':main()
