import csv,json
from pathlib import Path
import numpy as np,torch
from common import read_config,root,fingerprint,save_json,TASKS,DEGS
from models import build

BASE=Path('/data1/CST/CORA/promptir-nafnet-frozen6500')
FULL=Path('/data1/CST/CORA/aco-smfa-full13/rgb10_seed6_fft_b128_s15000_full13_v1')
MODELS=['promptir','nafnet']

def report():
 original=json.loads((FULL/'results.json').read_text());assert original['config']['seed']==6
 rows=[];episodes={};frames={}
 for model in MODELS:
  c=read_config('config_'+model+'.json');r=root(c)
  source=Path(c['checkpoint_source'])
  source_config=json.loads((source/'protocol.json').read_text())
  ck=torch.load(source/'checkpoints'/model/'last.pt',map_location='cpu',weights_only=False)
  assert ck['step']==c['frozen_checkpoint_step'] and ck['name']==model and ck['config_hash']==fingerprint(source_config)
  m=build(model);m.load_state_dict(ck['model'],strict=True);count=sum(x.numel() for x in m.parameters())
  images=json.loads((r/'images'/model/'summary.json').read_text());assert images['all']['n']==130000 and images['clean_input']['n']==10000
  with (r/'images'/model/'per_image.csv').open() as file:
   indices=[int(x['index']) for x in csv.DictReader(file)];assert sorted(indices)==list(range(130000))
  ee=[]
  for task in TASKS:
   for mode,kind in [('markov',None)]+[('single',k) for k,_ in DEGS]:
    d=r/'control'/mode/task/(kind or mode)/model
    assert json.loads((d/'protocol.json').read_text())==dict(config=fingerprint(c),task=task,condition=model,mode=mode,kind=kind)
    items=[json.loads(x) for x in (d/'episodes.jsonl').read_text().splitlines()];n=10 if mode=='markov' else 5
    assert len(items)==n and {x['seed'] for x in items}=={c['control_seed']+TASKS.index(task)*1000+i for i in range(n)}
    assert all(x['terminal'] and x['decisions']==500 and x['action_repeat']==2 and np.isfinite(x['return_']) for x in items)
    ee.extend(items)
  assert len(ee)==750 and len({(x['task'],x['mode'],x['kind'],x['seed']) for x in ee})==750
  fm=[]
  for task in TASKS:
   p=BASE/'frame_metrics'/model/(task+'.npz');meta=json.loads(p.with_suffix('.json').read_text());assert meta['current_h_max_delta']<1e-4 and max(meta['clean_repeat'].values())<1e-4
   a=np.load(p)['errors'];assert a.shape==(5,500,4) and np.isfinite(a).all();fm.append(a)
  frame=np.stack(fm);frames[model]=dict(metrics=['actor_symmetric_kl','value_normalized_mae','posterior_js','hnext_normalized_rmse'],mean=frame.mean((0,1,2)).tolist(),per_task={task:frame[i].mean((0,1)).tolist() for i,task in enumerate(TASKS)},reference='shared clean history, independent calibration, four common posterior draws')
  row=dict(method=model,seed=6,checkpoint_step=ck['step'],parameters=count,psnr_y=images['all']['psnr_y'],ssim_y=images['all']['ssim_y'],psnr_rgb=images['all']['psnr_rgb'],ssim_rgb=images['all']['ssim_rgb'],fixed_return=float(np.mean([x['return_'] for x in ee if x['mode']=='single'])),markov_return=float(np.mean([x['return_'] for x in ee if x['mode']=='markov'])),frame_metrics=frames[model]['mean'])
  rows.append(row);episodes[model]=ee
 raw=original['images']['smfa']['all'];base=[]
 diag=json.loads(Path('/data1/CST/CORA/dreamer-frame-full/seed678_id13_shared_history_v1/results.json').read_text())
 frame_names=['actor_symmetric_kl','value_normalized_mae','posterior_js','hnext_normalized_rmse']
 for name,condition in [('Raw','raw'),('ACO','aco'),('CORA','smfa')]:
  g=original['control_groups'];im=original['images'].get(condition)
  fd=next(x for x in diag['rows'] if x['task']=='ALL_TASKS' and x['protocol']=='markov' and x['method']==('raw' if condition=='raw' else condition+'_seed6'))
  base.append(dict(method=name,parameters={'raw':None,'aco':2649000,'smfa':182703}[condition],fixed_return=g['single/all/'+condition]['mean'],markov_return=g['markov/'+condition]['mean'],psnr_y=raw['raw_psnr_y'] if im is None else im['all']['psnr_y'],ssim_y=raw['raw_ssim_y'] if im is None else im['all']['ssim_y'],psnr_rgb=raw['raw_psnr_rgb'] if im is None else im['all']['psnr_rgb'],ssim_rgb=raw['raw_ssim_rgb'] if im is None else im['all']['ssim_rgb'],frame_metrics=[fd['mean'][k] for k in frame_names]))
 all_episodes={name:[x for x in original['episodes'] if x['condition']==condition] for name,condition in [('Raw','raw'),('ACO','aco'),('CORA','smfa')]}
 all_episodes.update(episodes)
 conditions={name:[e for e in items if e['mode']=='single'] for name,items in all_episodes.items()}
 assert all(len(items)==650 for items in conditions.values())
 def avg(items):
  assert items
  return float(np.mean([x['return_'] for x in items]))
 per_task={task:{name:avg([e for e in items if e['task']==task]) for name,items in conditions.items()} for task in TASKS}
 per_type={kind:{name:avg([e for e in items if e['kind']==kind]) for name,items in conditions.items()} for kind,_ in DEGS}
 save_json(BASE/'results.json',dict(configs={m:read_config('config_'+m+'.json') for m in MODELS},new_methods=rows,baseline_seed6=base,episodes=episodes,frame=frames,parallelism=json.loads((BASE/'parallelism.json').read_text()),per_task_fixed=per_task,per_type_fixed=per_type))
 allrows=base+rows
 lines=['# PromptIR and NAFNet baselines, seed6 · frozen checkpoint','','PromptIR was stopped by user request at 6500 updates; NAFNet, ACO and CORA use 15000 updates. Comparisons are therefore not compute-matched. One adapter seed per new model. All 13 perturbation types occurred in training; no OOD claim. ACO/CORA/Raw values are reused from seed6 results. Fixed-type return averages 650 episodes per new adapter; Markov averages 100. Image metrics use 130000 test pairs per adapter. All values below are single-seed, with no seed SD.','','## Table 1 · Fixed-type control return','','| Controller | Adapter | Mean return ↑ |','|---|---|---:|']
 for x in allrows:lines.append(f"| DreamerV3 | {x['method']} | {x['fixed_return']:.2f} |")
 lines+=['','## Table 2 · Markov-switching return','','| Controller | Adapter | Mean return ↑ |','|---|---|---:|']
 for x in allrows:lines.append(f"| DreamerV3 | {x['method']} | {x['markov_return']:.2f} |")
 lines+=['','## Table 3 · Restoration quality','','| Method | Params (M) | PSNR-Y ↑ | SSIM-Y ↑ | PSNR-RGB ↑ | SSIM-RGB ↑ |','|---|---:|---:|---:|---:|---:|']
 for x in allrows:
  p='—' if x['parameters'] is None else f"{x['parameters']/1e6:.3f}"
  lines.append(f"| {x['method']} | {p} | {x['psnr_y']:.2f} | {x['ssim_y']:.4f} | {x['psnr_rgb']:.2f} | {x['ssim_rgb']:.4f} |")
 lines+=['','## Table 4 · Fixed-history Markov diagnostics','','| Method | Posterior JS ↓ | Next-h NRMSE ↓ | Value NMAE ↓ | Actor KL ↓ |','|---|---:|---:|---:|---:|']
 for x in allrows:
  v=x['frame_metrics'];lines.append(f"| {x['method']} | {v[2]:.4f} | {v[3]:.4f} | {v[1]:.4f} | {v[0]:.4f} |")
 names=list(conditions)
 lines+=['','## Table 5 · Per-task fixed-type return','','Each task averages its thirteen fixed corruption types equally (65 complete episodes per method). All entries below are seed6 means only.','','| Task | '+' | '.join(names)+' |','|---|'+'---:|'*len(names)]
 for task in TASKS:lines.append('| '+task+' | '+' | '.join(f'{per_task[task][name]:.1f}' for name in names)+' |')
 lines+=['| Mean | '+' | '.join(f'{np.mean([per_task[t][name] for t in TASKS]):.1f}' for name in names)+' |']
 lines+=['','## Table 6 · Per-type fixed-type return','','Each corruption averages ten tasks equally (50 complete episodes per method). All entries below are seed6 means only.','','| Corruption | '+' | '.join(names)+' |','|---|'+'---:|'*len(names)]
 for kind,_ in DEGS:lines.append('| '+kind+' | '+' | '.join(f'{per_type[kind][name]:.1f}' for name in names)+' |')
 lines+=['','Fixed-history metrics reuse the completed clean trajectories and calibration scales, but the new adapters are evaluated on their own restored Markov observations. The reused ACO/CORA/Raw diagnostic values are seed6 only. Complete per-episode, per-task, and benchmark timing data are in results.json and parallelism.json.']
 (BASE/'REPORT.md').write_text('\n'.join(lines),encoding='utf8')
 save_json(BASE/'verification.json',dict(complete=True,models=MODELS,seed=6,checkpoint_steps={'promptir':6500,'nafnet':15000},image_pairs_each=130000,formal_control_episodes=1500,markov_frame_files=20,markov_frame_positions=50000,baseline_full_reused=True))
if __name__=='__main__':report()
