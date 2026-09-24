import argparse
import csv
import json
import os
from pathlib import Path
import numpy as np
from common import read_config,bind,root,save_json,fingerprint


def images(c,name,device):
    import torch
    from engine import load_model,torch_setup
    from metrics import measure,uint8
    from ood import OOD
    torch_setup(c); model=load_model(c,name,device)
    out=root(c)/'ood_images'/name; out.mkdir(parents=True,exist_ok=True)
    sums={}; counts={}
    fields=['task','kind','index','seed','psnr_y','ssim_y','psnr_rgb','ssim_rgb',
            'raw_psnr_y','raw_ssim_y','raw_psnr_rgb','raw_ssim_rgb']
    with (out/'per_image.csv.tmp').open('w',newline='') as f,torch.inference_mode():
        writer=csv.DictWriter(f,fieldnames=fields); writer.writeheader()
        for ti,task in enumerate(c['tasks']):
            clean=np.load(Path(c['dataset_root'])/task/'test/clean.npy',mmap_mode='r')
            assert len(clean)==1000
            for ki,kind in enumerate(c['ood_types']):
                for start in range(0,len(clean),c['eval_batch']):
                    gt=np.array(clean[start:start+c['eval_batch']])
                    seeds=[9000000+ti*100000+ki*10000+start+j for j in range(len(gt))]
                    raw=np.stack([OOD(kind,s,c['ood'])(g) for s,g in zip(seeds,gt)])
                    x=torch.from_numpy(raw).permute(0,3,1,2).float().to(device)/127.5-1
                    pred=uint8(model(x))
                    for j,(g,x,p,s) in enumerate(zip(gt,raw,pred,seeds)):
                        scores=dict(**measure(p,g),**{'raw_'+k:v for k,v in measure(x,g).items()})
                        writer.writerow(dict(task=task,kind=kind,index=start+j,seed=s,**scores))
                        for key in ['all','task/'+task,'degradation/'+kind,task+'/'+kind]:
                            if key not in sums: sums[key]={k:0. for k in scores}; counts[key]=0
                            for k,v in scores.items(): sums[key][k]+=v
                            counts[key]+=1
                    if start==0:
                        from PIL import Image
                        Image.fromarray(np.concatenate([gt[0],raw[0],pred[0]],1)).save(out/f'{task}_{kind}.png')
                print(name,task,kind,'1000 images',flush=True)
    os.replace(out/'per_image.csv.tmp',out/'per_image.csv')
    save_json(out/'summary.json',{k:dict(n=counts[k],**{m:v/counts[k] for m,v in s.items()}) for k,s in sums.items()})


def report(c):
    import torch
    r=root(c); rows=[]; pairs=[]
    for name in ['aco','smfa']:
        ck=torch.load(r/'checkpoints'/name/'last.pt',map_location='cpu',weights_only=False)
        assert ck['step']==15000 and ck['config_hash']==fingerprint(c)
        assert json.loads((r/'images'/name/'summary.json').read_text())['all']['n']==70000
        assert json.loads((r/'ood_images'/name/'summary.json').read_text())['all']['n']==60000
    for task in c['tasks']:
        for kind in ['clean']+c['ood_types']:
            summaries={}
            for condition in (['clean'] if kind=='clean' else ['raw','aco','smfa']):
                d=r/'control'/task/kind/condition
                s=json.loads((d/'summary.json').read_text()); assert s['n']==5
                eps=s['episodes']; expected=[c['control_seed']+c['tasks'].index(task)*1000+i for i in range(5)]
                assert sorted(e['seed'] for e in eps)==expected
                assert all(e['terminal'] and e['decisions']==500 for e in eps)
                rows.extend(eps); summaries[condition]=s
            if kind!='clean':
                a={e['seed']:e['return_'] for e in summaries['aco']['episodes']}
                b={e['seed']:e['return_'] for e in summaries['smfa']['episodes']}
                dif=np.array([b[s]-a[s] for s in sorted(a)])
                rng=np.random.RandomState(0)
                boots=dif[rng.randint(0,5,size=(10000,5))].mean(1)
                pairs.append(dict(task=task,kind=kind,delta=float(dif.mean()),
                                  ci95=np.percentile(boots,[2.5,97.5]).tolist(),
                                  **{k:v['mean'] for k,v in summaries.items()}))
    assert len(rows)==950
    save_json(r/'results.json',dict(control_episodes=950,ood_episodes=900,clean_episodes=50,
        comparisons=pairs,episodes=rows,config=c,
        caveat='Single training seed; exploratory episode bootstrap n=5, not training-seed uncertainty. OOD fallback protocol is not exact ACO reproduction.'))
    lines=['# ACO-RGB / SMFA-RGB: seed 1, L1 + 0.05 FFT',
           '', 'Fixed 15000 updates. Six OOD families, 5 episodes per task/condition. No DrQ or framewise actor-critic evaluation.',
           '', 'OOD: supplementary fallback strengths and five supplementary operators; defocus reuses ACO kernel. Not an exact replication of ACO F.7.',
           '', '| Task | OOD | Raw | ACO | SMFA | SMFA-ACO |','|---|---|---:|---:|---:|---:|']
    lines += [f"| {v['task']} | {v['kind']} | {v['raw']:.2f} | {v['aco']:.2f} | {v['smfa']:.2f} | {v['delta']:.2f} |" for v in pairs]
    (r/'REPORT.md').write_text('\n'.join(lines)+'\n')


if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('stage',choices=['images','control','report','smoke'])
    p.add_argument('--config',default='config.json'); p.add_argument('--model'); p.add_argument('--task'); p.add_argument('--kind',default='clean'); p.add_argument('--condition');p.add_argument('--device',default='cuda')
    a=p.parse_args(); c=read_config(a.config); bind(c)
    if a.stage=='images': images(c,a.model,a.device)
    elif a.stage=='control':
        from control import evaluate
        assert a.task in c['tasks'] and a.kind in ['clean']+c['ood_types']
        assert (a.kind=='clean')==(a.condition=='clean')
        evaluate(c,a.task,a.condition,a.kind)
    elif a.stage=='report': report(c)
    else:
        import torch
        from models import build
        from losses import restoration_loss
        from data import Pairs
        from engine import torch_setup
        torch_setup(c); dataset=Pairs(c,'train'); x,y=dataset.batch(range(128)); x=x.cuda();y=y.cuda()
        for name in ([a.model] if a.model else ['aco','smfa']):
            m=build(name).cuda().train(); opt=torch.optim.AdamW(m.parameters(),lr=c['lr'],weight_decay=c['weight_decay'])
            with torch.autocast('cuda'): pred=m(x)
            total,pixel,fft=restoration_loss(pred,y); total.backward()
            assert all(torch.isfinite(p.grad).all() for p in m.parameters() if p.grad is not None)
            opt.step(); torch.cuda.synchronize()
            print(name,'CUDA batch128 finite',float(total),float(pixel),float(fft),
                  'peak_allocated_mib',torch.cuda.max_memory_allocated()/1024**2,
                  'peak_reserved_mib',torch.cuda.max_memory_reserved()/1024**2,flush=True)
            del m,opt,pred,total,pixel,fft; torch.cuda.empty_cache()
