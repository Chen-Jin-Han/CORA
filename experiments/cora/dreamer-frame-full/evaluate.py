import json,time
import numpy as np
from common import *
from math_metrics import symkl,js,rmse
from diagnostic import Diagnostic

def infer_all(d,cache,images,ids=None,batch=64):
 ids=np.arange(len(images)) if ids is None else np.asarray(ids);outputs={}
 for start in range(0,len(ids),batch):
  idx=ids[start:start+batch]
  # BF16 kernels can round differently with different physical batch shapes.
  # Keep the physical shape at 64 even for audit calls and final chunks.
  assert 0<len(idx)<=64
  padded=np.pad(idx,(0,64-len(idx)),mode='edge')
  r=d.infer(cache,padded,images[padded])
  for k,v in r.items():outputs.setdefault(k,[]).append(np.asarray(v,dtype=np.float32)[:len(idx)])
 return {k:np.concatenate(v) for k,v in outputs.items()}

def calibrate(task):
 d=Diagnostic(task,label='calibration');values=[];hs=[];checks=[]
 for ep in range(2):
  cache=dict(np.load(trajectory(task,'calibration',ep)));ref=infer_all(d,cache,cache['obs_image']);values.append(ref['value'].mean(axis=1));hs.append(ref['h'])
  checks.append(float(np.max(np.abs(ref['h']-cache['clean_h']))))
 v=np.concatenate(values).astype(float);h=np.concatenate(hs).astype(float);sv=float(v.std(ddof=1));sh=float(np.sqrt(np.mean(h.var(axis=0,ddof=1))))
 save(ROOT/'scales'/f'{task}.json',dict(value_std=sv,h_rms_std=sh,value_valid=sv>1e-6,h_valid=sh>1e-6,episodes=2,frames=1000,seeds=[trajectory_seed(task,'calibration',i) for i in range(2)],collection_h_max_delta=max(checks)))

def evaluate(task,ep):
 d=Diagnostic(task,label=f'evaluation_{ep}');cache=dict(np.load(trajectory(task,'evaluation',ep)));ref=infer_all(d,cache,cache['obs_image']);sc=json.loads((ROOT/'scales'/f'{task}.json').read_text())
 sv=sc['value_std'] if sc['value_valid'] else np.nan;sh=sc['h_rms_std'] if sc['h_valid'] else np.nan
 def errors(x):
  return np.stack([symkl(x['mu'],x['std'],ref['mu'],ref['std']).mean(axis=1),np.abs(x['value']-ref['value']).mean(axis=1)/sv,js(x['probs'],ref['probs']),rmse(x['hnext'],ref['hnext']).mean(axis=1)/sh],axis=-1)
 outdir=ROOT/'metrics'/task;outdir.mkdir(parents=True,exist_ok=True);start=time.perf_counter()
 # Real independent repeat, not merely subtracting a tensor from itself.
 ii=np.array([0,103,202,417]);rep=infer_all(d,cache,cache['obs_image'],ii,4);orig={k:v[ii] for k,v in ref.items()}
 repeat={k:float(np.max(np.abs(rep[k]-orig[k]))) for k in rep};assert max(repeat.values())<1e-4,repeat
 rev=infer_all(d,cache,cache['obs_image'],ii[::-1],1)
 order={k:float(np.max(np.abs(rev[k][::-1]-rep[k]))) for k in rep};assert max(order.values())<1e-4,order
 zero=errors(ref);assert np.nanmax(np.abs(zero))<1e-10
 arrays=np.empty((14,7,500,4),np.float64);value_abs=np.empty((14,7,500),np.float64);h_abs=np.empty_like(value_abs);max_h=0.
 for j,protocol in enumerate(PROTOCOLS):
  for mi,method in enumerate(METHODS):
   images=np.load(ROOT/'inputs'/task/(method+'.npy'),mmap_mode='r')[j,ep]
   x=infer_all(d,cache,images);delta=float(np.max(np.abs(x['h']-ref['h'])));max_h=max(max_h,delta);assert delta<1e-4
   arrays[j,mi]=errors(x);value_abs[j,mi]=np.abs(x['value']-ref['value']).mean(axis=1);h_abs[j,mi]=rmse(x['hnext'],ref['hnext']).mean(axis=1)
  print(task,ep,protocol,'done',flush=True)
 assert np.isfinite(arrays[:,:,:,0]).all() and np.isfinite(arrays[:,:,:,2]).all()
 if sc['value_valid']:assert np.isfinite(arrays[:,:,:,1]).all()
 if sc['h_valid']:assert np.isfinite(arrays[:,:,:,3]).all()
 atomic_npz(outdir/f'episode_{ep}.npz',errors=arrays,value_absolute_error=value_abs,h_absolute_rmse=h_abs,frame=np.arange(500),kind=np.load(ROOT/'inputs'/task/'metadata.npz')['kind'][:,ep])
 save(outdir/f'episode_{ep}.json',dict(task=task,episode=ep,seed=trajectory_seed(task,'evaluation',ep),shape=list(arrays.shape),protocols=PROTOCOLS,methods=METHODS,metrics=CONFIG['frame_metrics'],seconds=time.perf_counter()-start,current_h_max_delta=max_h,independent_clean_repeat=repeat,batch_order_deltas=order,clean_self_zero=True,read_only=True,scales=sc))
