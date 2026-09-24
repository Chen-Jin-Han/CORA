"""Copy verified seed6 policy-only baselines; preserve provenance, no new trials."""
import json,shutil
from pathlib import Path
from common import root,fingerprint,save_json
from checkpoint_io import digest
from protocol import jobs

def reuse(c):
    src=Path(c['baseline_source']);old=json.loads((src/'protocol.json').read_text())
    omit={'seed','experiment','data_root','baseline_source'}
    assert {k:v for k,v in c.items() if k not in omit}=={k:v for k,v in old.items() if k not in omit}
    assert json.loads((src/'verification.json').read_text())['valid']
    provenance=[];total=0
    for task,mode,kind,method in jobs(c):
        if method not in ['raw','clean']:continue
        rel=Path('control')/mode/task/(kind or mode)/method;s=src/rel;d=root(c)/rel
        expected=dict(config=fingerprint(old),task=task,condition=method,mode=mode,kind=kind)
        assert json.loads((s/'protocol.json').read_text())==expected
        rows=[json.loads(x) for x in (s/'episodes.jsonl').read_text().splitlines()];count=10 if mode=='markov' else 5
        assert len(rows)==count and len({x['seed'] for x in rows})==count
        assert all(x['terminal'] and x['decisions']==500 and x['action_repeat']==2 for x in rows)
        d.mkdir(parents=True,exist_ok=True)
        for name in ['episodes.jsonl','summary.json']:
            if (d/name).exists():assert digest(d/name)==digest(s/name)
            else:shutil.copy2(s/name,d/name)
        expected['config']=fingerprint(c);save_json(d/'protocol.json',expected)
        provenance.append(dict(source=str(s/'episodes.jsonl'),sha256=digest(s/'episodes.jsonl'),destination=str(d/'episodes.jsonl'),episodes=count))
        total+=count
    assert total==800
    save_json(root(c)/'baseline_provenance.json',dict(reused_episodes=total,not_independent_repeats=True,source=str(src),files=provenance))
