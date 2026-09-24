import argparse
import json
from pathlib import Path
import yaml
from checkpoint_io import digest, load_checkpoint, resolve, signature

p = argparse.ArgumentParser()
p.add_argument('--root', type=Path, required=True)
p.add_argument('--output', type=Path, required=True)
args = p.parse_args()
reports = []
for task in ['walker_walk', 'walker_run', 'finger_turn_hard']:
    run = args.root / f'dmc_{task}/seed0/run'
    config = yaml.safe_load((run / 'config.yaml').read_text())
    path = resolve(run)
    data = load_checkpoint(path)
    report = dict(task=task, checkpoint=str(path), sha256=digest(path),
                  config_sha256=digest(run / 'config.yaml'),
                  image_config=config['env']['dmc'],
                  leaves=len(data['params']), signature=signature(data['params']),
                  counters={k: int(v) for k, v in data.get('counters', {}).items()})
    reports.append(report)
    print(task, report['leaves'], report['counters'], flush=True)
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(reports, indent=2))
