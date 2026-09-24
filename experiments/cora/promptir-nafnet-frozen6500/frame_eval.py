"""Evaluate only the 13-type Markov stream with the validated clean history."""
import json,time
from pathlib import Path
import numpy as np
from common import root,read_config,save_json
from diagnostic_frame import Diagnostic
from math_metrics import symkl,js,rmse

BASE=Path('/data1/CST/CORA/promptir-nafnet-frozen6500')
REFERENCE=Path('/data1/CST/CORA/dreamer-frame-full/seed678_id13_shared_history_v1')
METRICS=['actor_symmetric_kl','value_normalized_mae','posterior_js','hnext_normalized_rmse']

def infer_all(d,cache,images,ids=None):
 ids=np.arange(len(images)) if ids is None else np.asarray(ids);out={}
 for start in range(0,len(ids),64):
  sub=ids[start:start+64];padded=np.pad(sub,(0,64-len(sub)),mode='edge')
  value=d.infer(cache,padded,images[padded])
  for k,v in value.items():out.setdefault(k,[]).append(np.asarray(v,dtype=np.float32)[:len(sub)])
 return {k:np.concatenate(v) for k,v in out.items()}

def evaluate(model,task):
 c=read_config('config_'+model+'.json');d=Diagnostic(task,label=f'{model}_{task}')
 s=json.loads((REFERENCE/'scales'/f'{task}.json').read_text());assert s['value_valid'] and s['h_valid']
 restored=np.load(BASE/'frame_inputs'/model/(task+'.npy'),mmap_mode='r')
 assert restored.shape==(5,500,64,64,3)
 dest=BASE/'frame_metrics'/model/(task+'.npz');dest.parent.mkdir(parents=True,exist_ok=True)
 errors=np.empty((5,500,4),np.float64);start=time.perf_counter();checks=[]
 for ep in range(5):
  cache=dict(np.load(REFERENCE/'trajectories'/task/f'evaluation_{ep}.npz'))
  ref=infer_all(d,cache,cache['obs_image']);x=infer_all(d,cache,restored[ep]);delta=float(np.max(np.abs(x['h']-ref['h'])));assert delta<1e-4
  if ep==0:
   idx=np.array([0,103,202,417]);again=infer_all(d,cache,cache['obs_image'],idx)
   audit={k:float(np.max(np.abs(again[k]-ref[k][idx]))) for k in ref};assert max(audit.values())<1e-4
  errors[ep]=np.stack([symkl(x['mu'],x['std'],ref['mu'],ref['std']).mean(axis=1),
      np.abs(x['value']-ref['value']).mean(axis=1)/s['value_std'],js(x['probs'],ref['probs']),
      rmse(x['hnext'],ref['hnext']).mean(axis=1)/s['h_rms_std']],axis=-1)
  checks.append(delta);print(model,task,ep,'done',flush=True)
 assert np.isfinite(errors).all()
 temp=dest.with_suffix('.partial.npz');np.savez(temp,errors=errors);temp.replace(dest)
 save_json(dest.with_suffix('.json'),dict(model=model,task=task,shape=list(errors.shape),metrics=METRICS,current_h_max_delta=max(checks),clean_repeat=audit,seconds=time.perf_counter()-start,reference=str(REFERENCE)))

if __name__=='__main__':
 import sys
 evaluate(sys.argv[1],sys.argv[2])
