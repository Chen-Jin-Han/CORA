import csv
import json
import numpy as np
from common import root, save_json


def make_report(c):
    r=root(c); results=[]; count=0
    for task in c['tasks']:
        rows={}
        for condition in ['clean','raw','aco','smfa']:
            s=json.loads((r/'control'/task/condition/'summary.json').read_text())
            assert s['n']==10 and all(e['terminal'] for e in s['episodes'])
            rows[condition]=s; count+=s['n']
        a={e['seed']:e['return_'] for e in rows['aco']['episodes']}
        b={e['seed']:e['return_'] for e in rows['smfa']['episodes']}
        assert a.keys()==b.keys()
        diff=np.array([b[k]-a[k] for k in sorted(a)])
        rng=np.random.RandomState(42)
        boots=rng.choice(diff,(10000,len(diff)),replace=True).mean(1)
        results.append(dict(task=task,conditions=rows,paired_smfa_minus_aco=float(diff.mean()),
                            paired_bootstrap_ci95=np.percentile(boots,[2.5,97.5]).tolist()))
    assert count==400
    imgs={name:json.loads((r/'images'/name/'summary.json').read_text()) for name in ['aco','smfa']}
    assert all(v['all']['n']==70000 and v['clean_input']['n']==10000 for v in imgs.values())
    from engine import load_model
    params={name:sum(p.numel() for p in load_model(c,name,'cpu').parameters()) for name in ['aco','smfa']}
    efficiency={name:json.loads((r/'efficiency'/f'{name}.json').read_text()) for name in ['aco','smfa']}
    macro={k:float(np.mean([x['conditions'][k]['mean'] for x in results])) for k in ['clean','raw','aco','smfa']}
    for x in results:
        clean=x['conditions']['clean']['mean']
        x['clean_return_retention']={k:x['conditions'][k]['mean']/clean if clean>1e-6 else None for k in ['raw','aco','smfa']}
    curves={}
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axes=plt.subplots(1,2,figsize=(11,4))
    for name in ['aco','smfa']:
        h=json.loads((r/'checkpoints'/name/'history.json').read_text())
        v=[x for x in h if 'validation' in x]
        assert len(v)==30 and v[-1]['step']==15000
        # Trends are descriptive, not an automatic claim of convergence or a trigger for extra training.
        earlier=np.mean([x['validation']['psnr_y'] for x in v if 10000<=x['step']<=12000])
        later=np.mean([x['validation']['psnr_y'] for x in v if 13000<=x['step']<=15000])
        curves[name]=dict(last=v[-1],late_psnr_y_change_db=float(later-earlier),
            comparison='mean of steps 13000..15000 minus 10000..12000; descriptive only')
        axes[0].plot([x['step'] for x in v],[x['validation']['l1'] for x in v],label=name)
        axes[1].plot([x['step'] for x in v],[x['validation']['psnr_y'] for x in v],label=name)
        train=[x for x in h if 'train_l1' in x]
        axes[0].plot([x['step'] for x in train],[x['train_l1'] for x in train],alpha=.25,label=name+' train soft/AMP')
    axes[0].set_ylabel('RGB L1 [-1,1]'); axes[1].set_ylabel('PSNR Y (dB)')
    for ax in axes: ax.set_xlabel('Optimizer updates'); ax.legend(); ax.grid(alpha=.2)
    fig.tight_layout(); fig.savefig(r/'curves.png',dpi=160); plt.close(fig)
    save_json(r/'comparison.json',dict(control=results,macro_return=macro,images=imgs,efficiency=efficiency,convergence=curves,params=params,total_episodes=count))
    lines=['# RGB-only ACO–SMFA results','',
        '10 tasks; one adapter training seed; fixed supplied policy per task; 10 paired episodes per condition.',
        '400 full control episodes verified. No masks, DMC-GB, OOD, extra seeds or automatic continuation.', '',
        '|Task|Clean|Raw VDCS|ACO-RGB|SMFA-RGB|Paired difference [95% bootstrap CI]|',
        '|---|---:|---:|---:|---:|---:|']
    for x in results:
        values=[f"{x['conditions'][k]['mean']:.2f} ± {x['conditions'][k]['std']:.2f}" for k in ['clean','raw','aco','smfa']]
        lo,hi=x['paired_bootstrap_ci95']
        lines.append('|'+x['task']+'|'+'|'.join(values)+f"|{x['paired_smfa_minus_aco']:.2f} [{lo:.2f}, {hi:.2f}]|")
    lines.append('|Equal-task mean|'+'|'.join(f'{macro[k]:.2f}' for k in ['clean','raw','aco','smfa'])+'|—|')
    lines+=['','Intervals describe episode randomness conditional on these trained models, not training-seed uncertainty.',
            '', '|Model|Parameters|PSNR-Y|SSIM-Y|PSNR-RGB|SSIM-RGB|','|---|---:|---:|---:|---:|---:|']
    for name in ['aco','smfa']:
        m=imgs[name]['all']
        lines.append(f"|{name}|{params[name]}|{m['psnr_y']:.4f}|{m['ssim_y']:.4f}|{m['psnr_rgb']:.4f}|{m['ssim_rgb']:.4f}|")
    lines+=['','## Measured efficiency (FP32 batch 1, 64x64)',
            '|Model|Median ms|P95 ms|Peak allocated MiB|Conv/Linear MACs|',
            '|---|---:|---:|---:|---:|']
    for name,e in efficiency.items():
        lines.append(f"|{name}|{e['median_ms']:.3f}|{e['p95_ms']:.3f}|{e['peak_allocated_bytes']/2**20:.1f}|{e['conv_linear_macs']}|")
    lines.append('MACs exclude non-Conv/Linear operations. GPU availability check is not exclusive reservation; shared-load timings may need repetition.')
    lines+=['','## Validation trend (no automatic extension)']
    for name,v in curves.items(): lines.append(f"- {name}: late-window PSNR-Y change {v['late_psnr_y_change_db']:+.4f} dB. Inspect curves.png before deciding convergence.")
    lines+=['','This is an RGB-only adaptation, not full ACO reproduction. 64x64, batch 128 differ from the paper.',
            'Main results always use step 15000, never best_validation.pt.']
    (r/'REPORT.md').write_text('\n'.join(lines),encoding='utf8')
