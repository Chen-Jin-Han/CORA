import json
import time
import numpy as np
import torch
from common import root, policy, fingerprint, save_json
from perturbations import Stream
from engine import load_model, torch_setup
from metrics import uint8


def evaluate(c,task,condition,mode,kind=None):
    from dreamer_bridge import make_agent,make_env,reset,act
    assert condition in ['clean','raw','promptir','nafnet']
    torch_setup(c)
    label=mode if kind is None else kind
    count=c['control_episodes'] if mode=='markov' else c['clean_episodes'] if mode=='clean' else c['single_episodes']
    out=root(c)/'control'/mode/task/label/condition; out.mkdir(parents=True,exist_ok=True)
    signature=dict(config=fingerprint(c),task=task,condition=condition,mode=mode,kind=kind)
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
    expected={c['control_seed']+c['tasks'].index(task)*1000+i for i in range(count)}
    assert all(r['seed'] in expected and r['task']==task and r['condition']==condition and r['mode']==mode and r['kind']==kind and r['terminal'] and r['decisions']==500 and r['action_repeat']==2 for r in rows)
    done={r['seed'] for r in rows}
    agent,cfg=make_agent(policy(c,task),out/'loading','cpu')
    assert cfg['task']=='dmc_'+task and list(cfg['env']['dmc']['size'])==[64,64]
    adapter=load_model(c,condition,'cpu') if condition in ['promptir','nafnet'] else None
    for ep in range(count):
        seed=c['control_seed']+c['tasks'].index(task)*1000+ep
        if seed in done: continue
        env,dm,camera=make_env(cfg,seed); obs=reset(env); carry=agent.init_policy(1)
        with agent.n_actions.lock: agent.n_actions.value=seed*10000
        degrader=Stream(seed+10000000,c,kind if mode=='single' else None); score=0.; steps=0; adapter_times=[]
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
        assert steps==500 and cfg['env']['dmc']['repeat']==2
        row=dict(task=task,condition=condition,mode=mode,kind=kind,corruption_seed=seed+10000000,seed=seed,return_=score,decisions=steps,
                 action_repeat=cfg['env']['dmc']['repeat'],seconds=time.perf_counter()-start,
                 adapter_seconds_mean=float(np.mean(adapter_times)) if adapter_times else 0.,terminal=True)
        with path.open('a') as f:
            f.write(json.dumps(row)+'\n'); f.flush()
        rows.append(row); print(json.dumps(row),flush=True)
    assert len(rows)==count
    save_json(out/'summary.json',dict(n=len(rows),mean=float(np.mean([r['return_'] for r in rows])),
        std=float(np.std([r['return_'] for r in rows],ddof=1)),episodes=rows))
