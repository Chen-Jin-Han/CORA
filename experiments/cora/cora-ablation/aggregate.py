import json
from pathlib import Path
import numpy as np
from common import save_json

def main():
    base=Path('/data1/CST/CORA/aco-smfa-full13-seed78');allresults={}
    for seed in [6,7,8]:
        parent=Path('/data1/CST/CORA/aco-smfa-full13') if seed==6 else base
        r=parent/f'rgb10_seed{seed}_fft_b128_s15000_full13_v1'
        assert json.loads((r/'verification.json').read_text())['valid']
        allresults[seed]=json.loads((r/'results.json').read_text())
    groups={};lines=['# Full13 seeds 6–8','','Three independent restoration training seeds. Raw/Clean are shared seed6 trials, not independent replications.','', '| Group | Mean over seeds | Training-seed SD | Seed6 | Seed7 | Seed8 |','|---|---:|---:|---:|---:|---:|']
    for key in allresults[6]['control_groups']:
        if key.split('/')[-1] not in ['aco','smfa']:continue
        means=[allresults[s]['control_groups'][key]['mean'] for s in [6,7,8]]
        groups[key]=dict(seed_means=means,mean=float(np.mean(means)),training_seed_std=float(np.std(means,ddof=1)))
        lines.append('| '+key+' | '+' | '.join(f'{x:.4f}' for x in [np.mean(means),np.std(means,ddof=1),*means])+' |')
    quality={}
    lines+=['','## Restoration quality','','| Model/group/metric | Mean | Training-seed SD |','|---|---:|---:|']
    for m in ['aco','smfa']:
        for g in allresults[6]['images'][m]:
            for metric in ['psnr_y','ssim_y','psnr_rgb','ssim_rgb']:
                a=[allresults[s]['images'][m][g][metric] for s in [6,7,8]]
                key=m+'/'+g+'/'+metric;quality[key]=dict(mean=float(np.mean(a)),training_seed_std=float(np.std(a,ddof=1)),seed_values=a)
                lines.append(f'| {key} | {np.mean(a):.6f} | {np.std(a,ddof=1):.6f} |')
    save_json(base/'seed6-8_summary.json',dict(control=groups,images=quality,shared_baseline_source=allresults[6]['config']['experiment']))
    (base/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
if __name__=='__main__':main()
