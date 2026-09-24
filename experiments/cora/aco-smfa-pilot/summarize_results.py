"""Validate the full planned pilot before producing the comparison report."""
import argparse
import json
from pathlib import Path
import numpy as np

p = argparse.ArgumentParser()
p.add_argument('--root', type=Path, default=Path('/data1/CST/CORA/aco-smfa-pilot/outputs'))
args = p.parse_args()
root = args.root
tasks = ['walker_walk', 'walker_run', 'finger_turn_hard']
rows, tables = [], []
for task in tasks:
    paths = [root/'p0'/task/'episodes.jsonl'] + [root/'p2'/m/task/'episodes.jsonl' for m in ['aco','smfa']]
    values = {}
    for path in paths:
        records = [json.loads(line) for line in path.read_text().splitlines()]
        model = path.parts[-3] if 'p2' in path.parts else 'baseline'
        expected = ['clean','oracle_fg','raw'] if model == 'baseline' else ['restored_rgb','agent_only_rgb']
        assert len(records) == 10 * len(expected), path
        for condition in expected:
            group = [r for r in records if r['condition'] == condition]
            assert len(group) == 10 and all(r['full_episode'] for r in group), path
            assert {r['seed'] for r in group} == set(range(40000,40010)), path
            key = condition if model == 'baseline' else f'{model}_{condition}'
            values[key] = np.array([r['return_'] for r in sorted(group,key=lambda r:r['seed'])])
        rows.extend(records)
    summary = {k: dict(mean=float(v.mean()), std=float(v.std(ddof=1))) for k,v in values.items()}
    gap = values['clean'].mean() - values['raw'].mean()
    for key in values:
        if key.startswith(('aco_', 'smfa_')):
            summary[key]['recovery_ratio'] = float((values[key].mean()-values['raw'].mean())/gap) if gap > 0 else None
    tables.append(dict(task=task, conditions=summary,
                       oracle_minus_clean=float(np.mean(values['oracle_fg']-values['clean']))))
assert len(rows) == 210
image_stats = {}
for model in ['aco','smfa']:
    for split, count in [('val',6300),('test',10500)]:
        stats = json.loads((root/'images'/model/split/'summary.json').read_text())
        assert stats['n'] == count and stats['step'] == 10000, stats
        image_stats[f'{model}_{split}'] = stats
result = dict(full_control_episodes=len(rows), control=tables, image=image_stats,
    limitations=['One adapter seed and one supplied policy per task; exploratory only',
                 '64x64 JAX policies differ from ACO paper policy architecture and 84x84 input',
                 'Foreground performance includes distribution shift; interpret oracle comparison first'])
(root/'comparison.json').write_text(json.dumps(result,indent=2))
lines = ['# ACO–SMFA preliminary results', '', 'All 210 planned control episodes completed; both adapters trained for 10,000 updates.', '',
         '| Task | Clean | Raw VDCS | Oracle FG | ACO RGB | SMFA RGB | ACO FG | SMFA FG |',
         '|---|---:|---:|---:|---:|---:|---:|---:|']
keys = ['clean','raw','oracle_fg','aco_restored_rgb','smfa_restored_rgb','aco_agent_only_rgb','smfa_agent_only_rgb']
for task in tables:
    text = [f"{task['conditions'][k]['mean']:.2f} ± {task['conditions'][k]['std']:.2f}" for k in keys]
    lines.append('| '+task['task']+' | '+' | '.join(text)+' |')
lines += ['', 'Return values are mean ± sample standard deviation over 10 episodes; they are not five independent training seeds.', '',
          '| Adapter | Parameters | Test PSNR | SSIM | Foreground L1 | Mask IoU | Median latency ms |',
          '|---|---:|---:|---:|---:|---:|---:|']
for m in ['aco','smfa']:
    s = image_stats[m+'_test']
    lines.append(f"| {m} | {s['params']} | {s['psnr']:.3f} | {s['ssim']:.4f} | {s['roi_l1']:.4f} | {s['iou']:.4f} | {s['latency_ms_median']:.3f} |")
lines += ['', 'Pixel metrics are supplementary, measured on identical held-out corruptions. Foreground L1 above is RGB error inside the reference mask.', '',
          *['- '+x for x in result['limitations']]]
(root/'REPORT.md').write_text('\n'.join(lines)+'\n')
print('Validated complete pilot:', root/'REPORT.md')
