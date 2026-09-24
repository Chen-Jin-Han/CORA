import json,statistics as st
from pathlib import Path
from common import read_config,root
from engine import load_model
base=Path('/data1/CST/CORA/aco-smfa-markov45');rows=json.loads(Path('/data1/CST/CORA/aco-smfa-markov/results.json').read_text())['episodes'];means={}
assert len(rows)==800
for e in rows:
 means.setdefault((e['training_seed'] or 1,e['task'],e['condition']),[]).append(e['return_'])
for s in [4,5]:
 c=read_config(f'config_seed{s}.json')
 for n in ['aco','smfa']:load_model(c,n,'cpu')
 for t in c['tasks']:
  for n in ['aco','smfa']:
   es=[json.loads(l) for l in (root(c)/'control'/t/n/'episodes.jsonl').read_text().splitlines()]
   assert len(es)==10 and sorted(e['seed'] for e in es)==[c['control_seed']+c['tasks'].index(t)*1000+i for i in range(10)]
   assert all(e['terminal'] and e['decisions']==500 and e['action_repeat']==2 for e in es)
   means[s,t,n]=[e['return_'] for e in es];rows.extend(dict(e,training_seed=s if n in ['aco','smfa'] else None) for e in es)
assert len(rows)==1200
assert len({(e['training_seed'],e['task'],e['condition'],e['seed']) for e in rows})==1200
L=['# Five-seed ID Markov control report','','Seven ID types switch within each episode; stay probability 0.8. No OOD. Each model training seed has 10 evaluation episodes per task. Raw/Clean are shared baselines.','','## Across training seeds','','ACO/SMFA: mean and sample SD of the five seed means. Raw/Clean: mean and episode sample SD.','','| Task | Clean | Raw | ACO | SMFA |','|---|---:|---:|---:|---:|']
fmt=lambda v:f'{st.mean(v):.2f} +/- {st.stdev(v):.2f}'
for t in c['tasks']:L.append('| '+' | '.join([t,fmt(means[1,t,'clean']),fmt(means[1,t,'raw'])]+[fmt([st.mean(means[s,t,n]) for s in [1,2,3,4,5]]) for n in ['aco','smfa']])+' |')
L+=['','## Individual seed means +/- episode SD','','| Task | Model | Seed1 | Seed2 | Seed3 | Seed4 | Seed5 |','|---|---|---:|---:|---:|---:|---:|']
for t in c['tasks']:
 for n in ['aco','smfa']:L.append('| '+' | '.join([t,n]+[fmt(means[s,t,n]) for s in [1,2,3,4,5]])+' |')
L+=['','## Final validation restoration quality','','Same 5000 validation pairs; not independent test results. PSNR/SSIM higher is better; L1 lower is better.','','| Model | Seed | PSNR-Y | SSIM-Y | PSNR-RGB | SSIM-RGB | L1 |','|---|---|---:|---:|---:|---:|---:|']
for s in [1,2,3,4,5]:
 for n in ['aco','smfa']:
  if s==1: folder=Path('/data1/CST/CORA/aco-smfa-ood/rgb10_seed1_fft_b128_s15000_ood_ep5_v1')
  elif s in [2,3]: folder=Path('/data1/CST/CORA/aco-smfa-markov')/f'rgb10_seed{s}_fft_b128_s15000_markov_ep10_v1'
  else: folder=root(read_config(f'config_seed{s}.json'))
  h=json.loads((folder/'checkpoints'/n/'history.json').read_text())
  v=[x['validation'] for x in h if x['step']==15000 and 'validation' in x][-1]
  L.append('| '+' | '.join([n,str(s)]+[f'{v[k]:.4f}' for k in ['psnr_y','ssim_y','psnr_rgb','ssim_rgb','l1']])+' |')
(base/'REPORT.md').write_text('\n'.join(L)+'\n',encoding='utf8');(base/'results.json').write_text(json.dumps(dict(episodes=rows,total=1200),indent=2))
print('Verified 1200 unique complete episodes and four new final checkpoints, and saved report')
