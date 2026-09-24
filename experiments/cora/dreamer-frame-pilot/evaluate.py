import json,time
import numpy as np
from common import ROOT,KINDS,save
from math_metrics import symkl,js,rmse

def main():
 from diagnostic import Diagnostic
 d=Diagnostic('cpu','evaluation');cache=dict(np.load(ROOT/'trajectory.npz'))
 images={m:dict(np.load(ROOT/(m+'.npz'))) for m in ['raw','aco','smfa']}
 def batched(im,ids,batch=16):
  out={}
  for pos in range(0,len(ids),batch):
   ii=ids[pos:pos+batch];v=d.infer(cache,ii,im[ii])
   for k,a in v.items():out.setdefault(k,[]).append(a)
  return {k:np.concatenate(v) for k,v in out.items()}
 ids=np.arange(500);start=time.perf_counter();ref=batched(cache['obs_image'],ids)
 herror=float(np.max(np.abs(ref['h'].astype(float)-cache['clean_h'].astype(float))))
 assert herror<.05,('current h must match clean collected carry',herror)
 sv=float(np.std(ref['value'][:100].mean(axis=1),ddof=1))
 sh=float(np.sqrt(np.mean(np.var(ref['h'][:100].astype(float),axis=0,ddof=1))))
 assert sv>1e-6 and sh>1e-6,('Degenerate calibration',sv,sh)
 scales=dict(value_std=sv,h_rms_std=sh,calibration_frames=100,evaluation_frames=400,epsilon=1e-6)
 save(ROOT/'scales.json',scales)
 def error(x,c):
  return dict(actor_symmetric_kl=symkl(x['mu'],x['std'],c['mu'],c['std']).mean(axis=1),
   value_normalized_mae=np.abs(x['value']-c['value']).mean(axis=1)/sv,
   posterior_js=js(x['probs'],c['probs']),hnext_normalized_rmse=rmse(x['hnext'],c['hnext']).mean(axis=1)/sh)
 zero=error(ref,ref);assert all(np.max(np.abs(v))<1e-10 for v in zero.values())
 # Batch/order invariance checks with the exact same frame-keyed sampling.
 ii=np.array([103,129,202,417]);a=batched(images['raw'][KINDS[0]],ii,1);b=batched(images['raw'][KINDS[0]],ii,4)
 reverse=batched(images['raw'][KINDS[0]],ii[::-1],4);batch_delta={k:float(np.max(np.abs(a[k].astype(float)-b[k].astype(float)))) for k in a}
 order_delta={k:float(np.max(np.abs(reverse[k][::-1].astype(float)-b[k].astype(float)))) for k in b}
 # BF16 model precision can cause batch-kernel numerical differences; record all deltas.
 assert max(order_delta.values())<1e-4,order_delta
 assert np.max(np.abs(a['probs']-b['probs']))<.005,batch_delta
 # Read-only helpers reject state creation/modification, no parameter updates possible.
 checks=dict(clean_self_zero=True,current_h_vs_collection_max=herror,batch_deltas=batch_delta,order_deltas=order_delta,parameters_read_only=True,full_critic_loaded=True)
 allrows=[];summaries={}
 for kind in KINDS:
  summaries[kind]={}
  for method in ['raw','aco','smfa']:
   out=batched(images[method][kind],ids);delta=float(np.max(np.abs(out['h'].astype(float)-ref['h'].astype(float))))
   assert delta<1e-4,('Shared history differs',delta)
   ee=error(out,ref)
   for frame in ids:allrows.append(dict(frame=int(frame),split='calibration' if frame<100 else 'evaluation',kind=kind,method=method,**{k:float(v[frame]) for k,v in ee.items()}))
   summaries[kind][method]={k:dict(mean=float(v[100:].mean()),p95=float(np.percentile(v[100:],95))) for k,v in ee.items()}
   print(kind,method,summaries[kind][method],flush=True)
  for method in ['aco','smfa']:
   for metric,v in summaries[kind][method].items():
    raw=summaries[kind]['raw'][metric]['mean'];v['reduction_percent']=100*(raw-v['mean'])/raw if raw>1e-8 else None
 with (ROOT/'per_frame.jsonl').open('w') as f:
  for row in allrows:f.write(json.dumps(row)+'\n')
 save(ROOT/'correctness.json',checks);save(ROOT/'results.json',dict(task='walker_walk',restoration_seed=6,trajectory_seed=860000,kinds=KINDS,scales=scales,posterior_samples=4,statistics=summaries,seconds=time.perf_counter()-start,notes=['One trajectory; first100 calibration, last400 evaluation. No statistical significance claim.','Actor KL is per-action-dimension symmetric KL of pre-clipping Normal policies, averaged over four common-random posterior draws.','Fixed clean action for hnext; no extra environment step or history contamination.']))
if __name__=='__main__':main()
