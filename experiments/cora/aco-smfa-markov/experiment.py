"""Isolated subcommands; pipeline starts each task in a fresh process to release JAX state."""
import argparse
import json
import os
from pathlib import Path
os.environ.setdefault('MUJOCO_GL','egl')
os.environ.setdefault('XLA_PYTHON_CLIENT_PREALLOCATE','false')
from common import read_config,bind,policy,save_json,root


def preflight(c):
    from dreamer_bridge import config_for
    from checkpoint_io import resolve,digest
    rows=[]
    for task in c['tasks']:
        run=policy(c,task); cfg=config_for(run); p=resolve(run)
        assert cfg['task']=='dmc_'+task and list(cfg['env']['dmc']['size'])==[64,64]
        rows.append(dict(task=task,checkpoint=str(p),checkpoint_sha256=digest(p),
                         config_sha256=digest(run/'config.yaml'),env=cfg['env']['dmc']))
    manifest=root(c)/'policy_manifest.json'
    if manifest.exists():
        assert json.loads(manifest.read_text())==rows, 'Policy files/configs changed; use a new experiment ID'
    else:
        save_json(manifest,rows)
    print('PREFLIGHT: all 10 policy files/configs found; strict live loading is performed by collect/control stages',flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('stage',choices=['preflight','collect','audit','train','images','control','report','benchmark'])
    p.add_argument('--config',default='config.json'); p.add_argument('--task'); p.add_argument('--model',choices=['aco','smfa'])
    p.add_argument('--condition',choices=['clean','raw','aco','smfa']); p.add_argument('--device',default='cuda')
    a=p.parse_args(); c=read_config(a.config); bind(c)
    if a.stage=='preflight': preflight(c)
    elif a.stage=='collect':
        assert a.task in c['tasks']
        from data import generate
        generate(c,a.task)
    elif a.stage=='audit':
        from data import audit
        audit(c)
    elif a.stage in ['train','images','benchmark']:
        assert a.model
        from engine import train,image_eval,benchmark
        {'train':train,'images':image_eval,'benchmark':benchmark}[a.stage](c,a.model,a.device)
    elif a.stage=='control':
        assert a.task in c['tasks'] and a.condition
        from control import evaluate
        evaluate(c,a.task,a.condition)
    elif a.stage=='report':
        from report import make_report
        make_report(c)
