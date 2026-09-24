import json,csv
import numpy as np
from common import root,save_json,DEGS,fingerprint

def summarize(c):
    import torch
    r=root(c);rows=[];seen=set()
    from protocol import jobs
    for task,mode,kind,condition in jobs(c):
        d=r/'control'/mode/task/(kind or mode)/condition
        signature=dict(config=fingerprint(c),task=task,condition=condition,mode=mode,kind=kind)
        assert json.loads((d/'protocol.json').read_text())==signature
        rr=[json.loads(s) for s in (d/'episodes.jsonl').read_text().splitlines()]
        count=10 if mode=='markov' else 5;assert len(rr)==count
        assert {a['seed'] for a in rr}=={c['control_seed']+c['tasks'].index(task)*1000+i for i in range(count)}
        for a in rr:
            assert all(a[k]==v for k,v in dict(task=task,mode=mode,kind=kind,condition=condition).items())
            assert a['terminal'] and a['decisions']==500 and a['action_repeat']==2 and np.isfinite(a['return_'])
            key=(task,mode,kind,condition,a['seed']);assert key not in seen;seen.add(key)
        rows+=rr
    assert len(rows)==2300
    images={};checkpoints={}
    for model in ['aco','smfa']:
        ck=torch.load(r/'checkpoints'/model/'last.pt',map_location='cpu',weights_only=False)
        assert ck['step']==15000 and ck['config_hash']==fingerprint(c) and ck['name']==model
        checkpoints[model]=dict(step=ck['step'],elapsed=ck['elapsed'],final_validation=ck['history'][-1]['validation'])
        assert checkpoints[model]['final_validation']['scope']=='full_65000'
        s=json.loads((r/'images'/model/'summary.json').read_text());assert s['all']['n']==130000 and s['clean_input']['n']==10000
        assert all(s['degradation/'+k]['n']==10000 for k,_ in DEGS)
        for label,kinds in [('original7',DEGS[:7]),('added6',DEGS[7:])]:
            ss=[s['degradation/'+k] for k,_ in kinds]
            s[label]=dict(n=sum(v['n'] for v in ss),**{metric:float(np.mean([v[metric] for v in ss])) for metric in ss[0] if metric!='n'})
        with (r/'images'/model/'per_image.csv').open() as f:
            ii=list(csv.DictReader(f));assert len(ii)==130000 and len({x['index'] for x in ii})==130000
        images[model]=s
    groups={}
    def group(label,rr):
        a=np.array([x['return_'] for x in rr]);groups[label]=dict(n=len(a),mean=float(a.mean()),episode_std=float(a.std(ddof=1)))
    for method in ['raw','aco','smfa']:
        group('markov/'+method,[a for a in rows if a['mode']=='markov' and a['condition']==method])
        group('single/all/'+method,[a for a in rows if a['mode']=='single' and a['condition']==method])
        for label,kinds in [('original7',DEGS[:7]),('added6',DEGS[7:])]:
            group('single/'+label+'/'+method,[a for a in rows if a['kind'] in [k for k,_ in kinds] and a['condition']==method])
        for kind,_ in DEGS:group('single/'+kind+'/'+method,[a for a in rows if a['kind']==kind and a['condition']==method])
        for task in c['tasks']:
            group('task/'+task+'/single_mean/'+method,[a for a in rows if a['mode']=='single' and a['task']==task and a['condition']==method])
            group('task/'+task+'/markov/'+method,[a for a in rows if a['mode']=='markov' and a['task']==task and a['condition']==method])
            for kind,_ in DEGS:group('task/'+task+'/'+kind+'/'+method,[a for a in rows if a['task']==task and a['kind']==kind and a['condition']==method])
    group('clean',[a for a in rows if a['condition']=='clean'])
    result=dict(config=c,episodes=rows,control_groups=groups,images=images,checkpoints=checkpoints)
    save_json(r/'results.json',result)
    lines=['# Full13 seed6 results','','All 13 types are training-seen. Former OOD6 use fallback_v1; this is not a zero-shot OOD experiment.','',
           'One training seed per model. +/- denotes episode SD, not training-seed uncertainty. Pooled cross-task SD also contains task differences.','',
           '## Overall control','','| Protocol | Raw | ACO | SMFA |','|---|---:|---:|---:|']
    fmt=lambda g:f"{g['mean']:.2f} +/- {g['episode_std']:.2f} (n={g['n']})"
    for prefix in ['markov','single/all']:
        lines.append('| '+prefix+' | '+' | '.join(fmt(groups[prefix+'/'+m]) for m in ['raw','aco','smfa'])+' |')
    lines+=['','Clean: '+fmt(groups['clean']),'','## Image restoration','','| Model / group | n | PSNR-Y | SSIM-Y | PSNR-RGB | SSIM-RGB |','|---|---:|---:|---:|---:|---:|']
    for model,s in images.items():
        for key,v in s.items():lines.append(f"| {model}/{key} | {v['n']} | {v['psnr_y']:.4f} | {v['ssim_y']:.6f} | {v['psnr_rgb']:.4f} | {v['ssim_rgb']:.6f} |")
    lines+=['','## All control aggregates','','| Group | Mean +/- episode SD |','|---|---:|']
    lines += ['| '+k+' | '+fmt(v)+' |' for k,v in groups.items()]
    lines+=['','## All episodes','','| Task | Mode | Type | Method | Seed | Return |','|---|---|---|---|---:|---:|']
    lines += [f"| {a['task']} | {a['mode']} | {a['kind'] or '-'} | {a['condition']} | {a['seed']} | {a['return_']:.6f} |" for a in rows]
    (r/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
    save_json(r/'verification.json',dict(valid=True,unique_episodes=len(seen),markov=300,single=1950,clean=50,checkpoint_steps=15000,image_pairs_per_model=130000))
