import json,statistics as st
from common import read_config,root,DEGS,save_json
c=read_config('config.json');r=root(c);rows=[]
for ti,t in enumerate(c['tasks']):
 for k,_ in DEGS:
  es=[json.loads(l) for l in (r/'control'/t/k/'smfa/episodes.jsonl').read_text().splitlines()]
  assert len(es)==10 and sorted(e['seed'] for e in es)==[400000+ti*1000+i for i in range(10)]
  assert all(e['terminal'] and e['decisions']==500 and e['condition']=='smfa' and e['kind']==k for e in es)
  rows+=es
assert len({(e['task'],e['kind'],e['seed']) for e in rows})==700
def vals(t=None,k=None):return [e['return_'] for e in rows if (t is None or e['task']==t) and (k is None or e['kind']==k)]
def fmt(v):return f'{st.mean(v):.2f} +/- {st.stdev(v):.2f}'
L=['# Seed1 SMFA: seven fixed-family ID control tests','','Fixed corruption family, severity random walk in base +/-10% band. Ten episodes per task/type. Only SMFA; no new training or OOD.','','## Across tasks','','SD below pools100 episodes and includes task differences.','','| Type | Mean +/- SD |','|---|---:|']
L += ['| '+k+' | '+fmt(vals(k=k))+' |' for k,_ in DEGS]
L+=['','## Per-task returns (10 episodes per cell)','','| Task | '+' | '.join(k for k,_ in DEGS)+' |','|---|'+'---:|'*7]
L+=['| '+t+' | '+' | '.join(fmt(vals(t,k)) for k,_ in DEGS)+' |' for t in c['tasks']]
save_json(r/'results.json',dict(config=c,episodes=rows,total=700));(r/'REPORT.md').write_text('\n'.join(L)+'\n',encoding='utf8')
print('Verified700 unique complete episodes')
