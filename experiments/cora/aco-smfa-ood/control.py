import json
import time
import numpy as np
import torch
from common import root, policy, fingerprint, save_json
from ood import OOD
from engine import load_model, torch_setup
from metrics import uint8


def evaluate(c,task,condition,kind='clean'):
    from dreamer_bridge import make_agent,make_env,reset,act
    assert condition in ['clean','raw','aco','smfa']
    torch_setup(c)
    out=root(c)/'control'/task/kind/condition; out.mkdir(parents=True,exist_ok=True)
    signature=dict(config=fingerprint(c),task=task,condition=condition,kind=kind)
    meta=out/'protocol.json'
    if meta.exists(): assert json.loads(meta.read_text())==signature
    else: save_json(meta,signature)
    rows=[]; path=out/'episodes.jsonl'
    if path.exists():
        # Each flushed line is an independently completed episode. Drop only an interrupted final line.
        lines=path.read_text().splitlines()
        for i,line in enumerate(lines):
            try: rows.append(json.loads(line))
            except json.JSONDecodeError:
                if i!=len(lines)-1: raise
        path.write_text(''.join(json.dumps(r)+'\n' for r in rows))
    assert len({r['seed'] for r in rows})==len(rows)
    done={r['seed'] for r in rows}
    agent,cfg=make_agent(policy(c,task),out/'loading','cpu')
    assert cfg['task']=='dmc_'+task and list(cfg['env']['dmc']['size'])==[64,64]
    adapter=load_model(c,condition,'cpu') if condition in ['aco','smfa'] else None
    for ep in range(c['control_episodes']):
        seed=c['control_seed']+c['tasks'].index(task)*1000+ep
        if seed in done: continue
        env,dm,camera=make_env(cfg,seed); obs=reset(env); carry=agent.init_policy(1)
        with agent.n_actions.lock: agent.n_actions.value=seed*10000
        degrader=OOD(kind,seed+10000000,c['ood']) if kind!='clean' else None; score=0.; steps=0; adapter_times=[]
        start=time.perf_counter()
        try:
            while True:
                image=obs['image']
                if condition!='clean': image=degrader(image)
                if adapter is not None:
                    t=time.perf_counter()
                    x=torch.from_numpy(np.array(image)).permute(2,0,1)[None].float()/127.5-1
                    with torch.inference_mode(): image=uint8(adapter(x))[0]
                    adapter_times.append(time.perf_counter()-t)
                carry,action=act(agent,carry,dict(obs,image=np.asarray(image,np.uint8)))
                obs=env.step(action); score+=float(obs['reward']); steps+=1
                if obs['is_last']: break
                if steps>10000: raise RuntimeError('Environment did not terminate; refusing truncated formal episode')
        finally: env.close()
        row=dict(task=task,condition=condition,kind=kind,seed=seed,return_=score,decisions=steps,
                 action_repeat=cfg['env']['dmc']['repeat'],seconds=time.perf_counter()-start,
                 adapter_seconds_mean=float(np.mean(adapter_times)) if adapter_times else 0.,terminal=True)
        with path.open('a') as f:
            f.write(json.dumps(row)+'\n'); f.flush()
        rows.append(row); print(json.dumps(row),flush=True)
    assert len(rows)==c['control_episodes']
    save_json(out/'summary.json',dict(n=len(rows),mean=float(np.mean([r['return_'] for r in rows])),
        std=float(np.std([r['return_'] for r in rows],ddof=1)),episodes=rows))
