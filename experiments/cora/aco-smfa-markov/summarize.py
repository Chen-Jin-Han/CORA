import json,statistics as st
from pathlib import Path
from common import read_config,root
from engine import load_model
base=Path('/data1/CST/CORA/aco-smfa-markov');rows=[];means={}
for s in [1,2,3]:
 c=read_config(f'config_seed{s}.json')
 for n in ['aco','smfa']:load_model(c,n,'cpu')
 for t in c['tasks']:
  for n in (['clean','raw','aco','smfa'] if s==1 else ['aco','smfa']):
   es=[json.loads(l) for l in (root(c)/'control'/t/n/'episodes.jsonl').read_text().splitlines()]
   assert len(es)==10 and sorted(e['seed'] for e in es)==[c['control_seed']+c['tasks'].index(t)*1000+i for i in range(10)]
   assert all(e['terminal'] and e['decisions']==500 and e['action_repeat']==2 for e in es)
   means[s,t,n]=[e['return_'] for e in es];rows.extend(dict(e,training_seed=s if n in ['aco','smfa'] else None) for e in es)
assert len(rows)==800
assert len({(e['training_seed'],e['task'],e['condition'],e['seed']) for e in rows})==800
L=['# Three-seed ID Markov control report','','Seven ID types switch within each episode; stay probability 0.8. No OOD. Each model training seed has 10 evaluation episodes per task. Raw/Clean are shared baselines.','','## Across training seeds','','ACO/SMFA: mean and sample SD of the three seed means. Raw/Clean: mean and episode sample SD.','','| Task | Clean | Raw | ACO | SMFA |','|---|---:|---:|---:|---:|']
fmt=lambda v:f'{st.mean(v):.2f} ± {st.stdev(v):.2f}'
for t in c['tasks']:L.append('| '+' | '.join([t,fmt(means[1,t,'clean']),fmt(means[1,t,'raw'])]+[fmt([st.mean(means[s,t,n]) for s in [1,2,3]]) for n in ['aco','smfa']])+' |')
L+=['','## Individual seed means ± episode SD','','| Task | Model | Seed1 | Seed2 | Seed3 |','|---|---|---:|---:|---:|']
for t in c['tasks']:
 for n in ['aco','smfa']:L.append('| '+' | '.join([t,n]+[fmt(means[s,t,n]) for s in [1,2,3]])+' |')
(base/'REPORT.md').write_text('\n'.join(L)+'\n',encoding='utf8');(base/'results.json').write_text(json.dumps(dict(episodes=rows,total=800),indent=2))
print('Verified 800 unique complete episodes, all six final checkpoints, and saved report')
