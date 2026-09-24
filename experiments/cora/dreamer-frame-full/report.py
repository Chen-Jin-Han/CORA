import numpy as np
from common import *
def report():
 rows=[];data=[];seeds=[]
 for task in TASKS:
  for split,n in [('calibration',2),('evaluation',5)]:
   for e in range(n):
    meta=json.loads(trajectory(task,split,e).with_suffix('.json').read_text());assert meta['decisions']==500;seeds.append(meta['seed'])
  for m in METHODS[1:]:
   meta=json.loads((ROOT/'inputs'/task/(m+'.json')).read_text());assert meta['images']==35000
  episodes=[]
  for e in range(5):
   x=np.load(ROOT/'metrics'/task/f'episode_{e}.npz')['errors'];assert x.shape==(14,7,500,4);episodes.append(x)
  data.append(np.stack(episodes))
 assert len(set(seeds))==70
 data=np.stack(data) # task, episode, protocol, method, frame, metric
 def val(x):return None if not np.isfinite(x) else float(x)
 for ti,task in enumerate(TASKS+['ALL_TASKS']):
  block=data[ti:ti+1] if ti<len(TASKS) else data
  for pi,protocol in enumerate(PROTOCOLS):
   for mi,method in enumerate(METHODS):
    means=block[:,:,pi,mi].mean(axis=(0,1,2));raw=block[:,:,pi,0].mean(axis=(0,1,2))
    row=dict(task=task,protocol=protocol,method=method,mean=dict(zip(CONFIG['frame_metrics'],map(val,means))),reduction_percent=dict(zip(CONFIG['frame_metrics'],[val(100*(1-a/b)) if b>1e-12 else None for a,b in zip(means,raw)])))
    rows.append(row)
 summary=[]
 for pi,protocol in enumerate(PROTOCOLS):
  for model in ['aco','smfa']:
   indices=[METHODS.index(f'{model}_seed{s}') for s in [6,7,8]]
   a=np.stack([data[:,:,pi,i].mean(axis=(0,1,2)) for i in indices]);raw=data[:,:,pi,0].mean(axis=(0,1,2));mean=a.mean(0)
   summary.append(dict(protocol=protocol,model=model,mean=list(map(val,mean)),seed_std=list(map(val,a.std(0,ddof=1))),raw_reduction_percent=[val(100*(1-x/y)) if y>1e-12 else None for x,y in zip(mean,raw)]))
 save(ROOT/'results.json',dict(config=CONFIG,rows=rows,summary=summary))
 save(ROOT/'verification.json',dict(complete=True,trajectories=70,evaluation_frames=25000,protocol_frame_positions=350000,method_frame_records=2450000,restored_images=2100000,metric_files=50,unique_seeds=70))
 lines=['# Unified clean-history diagnostics','', 'Four metrics: action symmetric KL (per action dimension), normalized value MAE, categorical posterior JS, normalized next-h RMSE. Lower is better. SD is across restoration seeds 6/7/8, not across frames. Raw is shared, not three independent baselines. Calibration trajectories are disjoint. All calculations use CPU and common random posterior draws.','', '| Protocol | Model | Action KL | Value NMAE | Posterior JS | Next-h NRMSE |','|---|---|---:|---:|---:|---:|']
 for r in summary:
  cells=[f'{v:.6g} ± {s:.3g}' if v is not None and s is not None else 'NA' for v,s in zip(r['mean'],r['seed_std'])];lines.append('| '+' | '.join([r['protocol'],r['model']]+cells)+' |')
 lines+=['','Full task/protocol/seed means and relative Raw reductions are in results.json. Undefined calibration scales or zero Raw denominators are reported as null, never silently clipped.']
 (ROOT/'REPORT.md').write_text('\n'.join(lines),encoding='utf8')
if __name__=='__main__':report()
