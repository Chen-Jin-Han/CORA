import json,csv
import numpy as np
import torch
from common import *
from models import build
BASE=Path('/data1/CST/CORA/cora-ablation');VARIANTS=['no_context','no_local','full_channel']
def main():
 baseline=Path('/data1/CST/CORA/aco-smfa-full13/rgb10_seed6_fft_b128_s15000_full13_v1')
 full=json.loads((baseline/'results.json').read_text());assert full['config']['seed']==6
 records=[];detail={}
 def summarize(v,images,episodes,params):
  assert len(episodes)==750
  assert len({(x['task'],x['mode'],x['kind'],x['seed']) for x in episodes})==750
  for x in episodes:assert x['terminal'] and x['decisions']==500 and x['action_repeat']==2 and np.isfinite(x['return_'])
  single=[x['return_'] for x in episodes if x['mode']=='single'];markov=[x['return_'] for x in episodes if x['mode']=='markov'];assert len(single)==650 and len(markov)==100
  assert images['all']['n']==130000 and images['clean_input']['n']==10000
  records.append(dict(variant=v,parameters=params,psnr_y=images['all']['psnr_y'],ssim_y=images['all']['ssim_y'],single_return=float(np.mean(single)),markov_return=float(np.mean(markov)),seed=6))
  detail[v]=dict(images=images,episodes=episodes)
 fullck=torch.load(baseline/'checkpoints/smfa/last.pt',map_location='cpu',weights_only=False)
 assert fullck['step']==15000 and fullck['config_hash']==fingerprint(full['config'])
 model=build('smfa','full');model.load_state_dict(fullck['model'],strict=True)
 summarize('full',full['images']['smfa'],[x for x in full['episodes'] if x['condition']=='smfa'],sum(p.numel() for p in model.parameters()))
 for v in VARIANTS:
  c=read_config('config_'+v+'.json');r=root(c);episodes=[]
  for task in TASKS:
   for mode,kind in [('markov',None)]+[('single',k) for k,_ in DEGS]:
    d=r/'control'/mode/task/(kind or mode)/'smfa'
    assert json.loads((d/'protocol.json').read_text())==dict(config=fingerprint(c),task=task,condition='smfa',mode=mode,kind=kind)
    rr=[json.loads(x) for x in (d/'episodes.jsonl').read_text().splitlines()];n=10 if mode=='markov' else 5
    assert len(rr)==n and {x['seed'] for x in rr}=={c['control_seed']+TASKS.index(task)*1000+i for i in range(n)}
    assert all(x['task']==task and x['mode']==mode and x['kind']==kind and x['condition']=='smfa' for x in rr)
    episodes+=rr
  ck=torch.load(r/'checkpoints/smfa/last.pt',map_location='cpu',weights_only=False)
  assert ck['step']==15000 and ck['name']=='smfa' and ck['config_hash']==fingerprint(c)
  m=build('smfa',v);m.load_state_dict(ck['model'],strict=True)
  images=json.loads((r/'images/smfa/summary.json').read_text())
  with (r/'images/smfa/per_image.csv').open() as f:
   indices=[int(x['index']) for x in csv.DictReader(f)];assert sorted(indices)==list(range(130000))
  summarize(v,images,episodes,sum(p.numel() for p in m.parameters()))
 save_json(BASE/'results.json',dict(seed=6,summary=records,details=detail,baseline_source=str(baseline),parallelism=json.loads((BASE/'parallelism.json').read_text())))
 lines=['# CORA ablation, seed6','','One restoration training seed. Full is reused from the verified original seed6 run. No training-seed uncertainty is estimated. 13 training-seen types; same data/loss/15000-step budget. Fixed type: 650 episodes per variant; Markov: 100. All tasks/types equally weighted. Benchmark episodes excluded.','','| Version | Parameters | PSNR-Y | SSIM-Y | Fixed-type return | Markov return |','|---|---:|---:|---:|---:|---:|']
 for a in records:lines.append(f"| {a['variant']} | {a['parameters']} | {a['psnr_y']:.3f} | {a['ssim_y']:.4f} | {a['single_return']:.2f} | {a['markov_return']:.2f} |")
 lines+=['','Removing the local branch also reduces capacity. These experiments do not isolate capacity from architecture. Full-channel costs should be interpreted using measured throughput, not parameter ratios alone.']
 (BASE/'REPORT.md').write_text('\n'.join(lines),encoding='utf8')
 save_json(BASE/'verification.json',dict(complete=True,new_checkpoints=3,steps=15000,new_formal_episodes=2250,image_pairs_per_variant=130000,seed=6,full_reused=True))
if __name__=='__main__':main()
