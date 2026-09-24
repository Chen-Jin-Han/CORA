import csv
import json
import os
import time
from pathlib import Path
import numpy as np
import torch
from common import root, fingerprint, save_json, DEGS
from data import Pairs, ValidationSubset, balanced_indices
from models import build
from metrics import measure, uint8
from losses import restoration_loss


def torch_setup(c):
    torch.set_num_threads(int(os.environ.get('CORA_THREADS',c['torch_threads'])))
    torch.manual_seed(c['seed']); np.random.seed(c['seed'])
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True


def atomic_checkpoint(path, state):
    tmp=path.with_suffix('.tmp'); torch.save(state,tmp); os.replace(tmp,path)


def load_model(c, name, device):
    source=Path(c.get('checkpoint_source', str(root(c))))
    source_config=json.loads((source/'protocol.json').read_text()) if 'checkpoint_source' in c else c
    if 'checkpoint_source' in c:
        assert c['seed']==source_config['seed']==6 and c['model']==source_config['model']
        for key in ['steps','batch_size','lr','weight_decay','fft_weight','dataset_root','tasks']:
            assert c[key]==source_config[key]
    state=torch.load(source/'checkpoints'/name/'last.pt',map_location='cpu',weights_only=False)
    assert state['step']==c['frozen_checkpoint_step'] and state['config_hash']==fingerprint(source_config) and state['name']==name
    model=build(name).to(device); model.load_state_dict(state['model'],strict=True); model.eval()
    return model


@torch.inference_mode()
def validate(c, model, dataset, device):
    model.eval()  # ACO deploys hard top-1 during validation, not its soft training mixture.
    losses=[]; stats=[]; grouped={}; usage=np.zeros(9,dtype=np.int64)
    def route_hook(module,args,out):
        usage[:]+=np.bincount(out.argmax(-1).cpu().numpy(),minlength=9)
    hook=model.router.register_forward_hook(route_hook) if hasattr(model,'router') else None
    for start in range(0,len(dataset),c['eval_batch']):
        ids=np.arange(start,min(start+c['eval_batch'],len(dataset)))
        x,y=dataset.batch(ids); x=x.to(device); y=y.to(device)
        pred=model(x)
        losses.extend((pred-y).abs().mean((1,2,3)).cpu().tolist())
        batch_stats=[measure(a,b) for a,b in zip(uint8(pred),uint8(y))]
        stats.extend(batch_stats)
        for idx,s in zip(ids,batch_stats):
            _,_,task,kind=dataset.get(idx)
            for key in ['task/'+task,'degradation/'+DEGS[kind][0]]:
                grouped.setdefault(key,[]).append(s)
    if hook: hook.remove()
    return dict(l1=float(np.mean(losses)), **{k:float(np.mean([s[k] for s in stats])) for k in stats[0]},
                groups={k:{m:float(np.mean([a[m] for a in v])) for m in v[0]} for k,v in grouped.items()},
                router_top1_counts=usage.tolist() if hook else None)


def train(c,name,device):
    assert c['seed'] == 6
    assert device.startswith('cuda'), 'Formal training requires CUDA; use tests.py for CPU smoke tests'
    torch_setup(c)
    d=root(c)/'checkpoints'/name; d.mkdir(parents=True,exist_ok=True)
    trainset=Pairs(c,'train'); fullval=Pairs(c,'val'); valset=ValidationSubset(fullval,c)
    assert len(trainset)==585000 and len(valset)==5200 and len(fullval)==65000
    model=build(name).to(device)
    opt=torch.optim.AdamW(model.parameters(),lr=c['lr'],weight_decay=c['weight_decay'],betas=(.9,.999),eps=1e-8)
    scaler=torch.amp.GradScaler('cuda',enabled=c['amp'])
    start=0; best=float('inf'); elapsed=0.; history=[]
    last=d/'last.pt'
    if last.exists():
        state=torch.load(last,map_location='cpu',weights_only=False)
        assert state['config_hash']==fingerprint(c) and state['name']==name
        model.load_state_dict(state['model']); opt.load_state_dict(state['optimizer']); scaler.load_state_dict(state['scaler'])
        start=state['step']; best=state['best']; elapsed=state['elapsed']; history=state['history']
        torch.set_rng_state(state['torch_rng']); torch.cuda.set_rng_state_all(state['cuda_rng'])
    # Statelesly seeded batches/flips give both architectures identical samples and resume order.
    begin=time.perf_counter()
    for step in range(start+1,c['steps']+1):
        model.train(); opt.zero_grad(set_to_none=True)
        rng=np.random.RandomState(7000000+c['seed']*100000+step)
        ids=balanced_indices(trainset,rng,c['batch_size'],step)
        flips=rng.rand(c['batch_size'])<.5
        buffers={k:v.clone() for k,v in model.named_buffers()}
        retries=0
        while True:
            opt.zero_grad(set_to_none=True)
            loss_sum=0.; pixel_sum=0.; fft_sum=0.
            for pos in range(0,c['batch_size'],c['micro_batch']):
                sl=slice(pos,pos+c['micro_batch'])
                x,y=trainset.batch(ids[sl],flips[sl]); x=x.to(device); y=y.to(device)
                with torch.autocast('cuda',enabled=c['amp']):
                    pred=model(x)
                loss,pixel,fft=restoration_loss(pred,y,c['fft_weight'])
                if not torch.isfinite(loss):
                    raise FloatingPointError(f'{name} nonfinite loss at {step}')
                scaler.scale(loss*c['micro_batch']/c['batch_size']).backward()
                loss_sum+=float(loss.detach())*c['micro_batch']/c['batch_size']
                pixel_sum+=float(pixel.detach())*c['micro_batch']/c['batch_size']
                fft_sum+=float(fft.detach())*c['micro_batch']/c['batch_size']
            scaler.unscale_(opt)
            finite=torch.stack([torch.isfinite(p.grad).all() for p in model.parameters() if p.grad is not None]).all()
            if finite:
                break
            if not c['amp'] or retries >= 20:
                raise FloatingPointError('Nonfinite gradients persist after AMP scale retries')
            old_scale=scaler.get_scale()
            scaler.update(new_scale=old_scale/2)
            with torch.no_grad():
                for k,v in model.named_buffers(): v.copy_(buffers[k])
            retries+=1
            print(json.dumps(dict(step=step,amp_retry=retries,old_scale=old_scale,new_scale=scaler.get_scale())),flush=True)
        scaler.step(opt); scaler.update()
        if step%c['log_every']==0:
            row=dict(step=step,train_l1=pixel_sum,train_fft=fft_sum,train_fft_weighted=fft_sum*c['fft_weight'],train_total=loss_sum,elapsed=elapsed+time.perf_counter()-begin)
            history.append(row); print(json.dumps(row),flush=True)
        if step%c['validate_every']==0 or step==c['steps']:
            val=validate(c,model,fullval if step==c['steps'] else valset,device)
            val['scope']='full_65000' if step==c['steps'] else 'fixed_subset_5200'
            history.append(dict(step=step,validation=val))
            improved=val['l1']<best; best=min(best,val['l1'])
            state=dict(name=name,step=step,config_hash=fingerprint(c),model=model.state_dict(),
                       optimizer=opt.state_dict(),scaler=scaler.state_dict(),best=best,
                       elapsed=elapsed+time.perf_counter()-begin,history=history,
                       torch_rng=torch.get_rng_state(),cuda_rng=torch.cuda.get_rng_state_all())
            atomic_checkpoint(last,state)
            atomic_checkpoint(d/f'step_{step:05d}.pt',state)
            if improved: atomic_checkpoint(d/'best_validation.pt',state)
            save_json(d/'history.json',history)
            print(json.dumps(dict(step=step,validation=val)),flush=True)
    assert last.exists()
    # Repair a crash between atomic last.pt and its human-readable history export.
    save_json(d/'history.json',history)


def image_eval(c,name,device):
    torch_setup(c); model=load_model(c,name,device); dataset=Pairs(c,'test')
    assert len(dataset)==130000
    out=root(c)/'images'/name; out.mkdir(parents=True,exist_ok=True)
    from collections import defaultdict
    groups=defaultdict(list)
    with (out/'per_image.csv.tmp').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['index','task','degradation','psnr_y','ssim_y','psnr_rgb','ssim_rgb','raw_psnr_y','raw_ssim_y','raw_psnr_rgb','raw_ssim_rgb'])
        writer.writeheader()
        with torch.inference_mode():
            for start in range(0,len(dataset),c['eval_batch']):
                ids=np.arange(start,min(start+c['eval_batch'],len(dataset)))
                x,y=dataset.batch(ids); pred=uint8(model(x.to(device)))
                for i,p in zip(ids,pred):
                    raw,gt,task,k=dataset.get(i)
                    scores=measure(p,gt); rawscores={'raw_'+a:b for a,b in measure(raw,gt).items()}
                    row=dict(index=int(i),task=task,degradation=DEGS[k][0],**scores,**rawscores)
                    writer.writerow(row)
                    for key in ['all','task/'+task,'degradation/'+DEGS[k][0],task+'/'+DEGS[k][0]]:
                        groups[key].append({**scores,**rawscores})
                    if i%7000==0:
                        from PIL import Image
                        Image.fromarray(np.concatenate([gt,raw,p],axis=1)).save(out/f'panel_{i:05d}.png')
                if start%7000==0: print(name,'images',start,flush=True)
    os.replace(out/'per_image.csv.tmp',out/'per_image.csv')
    summary={k:dict(n=len(v),**{m:float(np.mean([x[m] for x in v])) for m in v[0]}) for k,v in groups.items()}
    # Clean-input pass (10,000 independent clean images), no extra control conditions.
    clean_stats=[]
    with torch.inference_mode():
        for task,x,y,index,kind in dataset.shards:
            for start in range(0,len(y),c['eval_batch']):
                a=np.array(y[start:start+c['eval_batch']])
                tensor=torch.from_numpy(a).permute(0,3,1,2).float().to(device)/127.5-1
                clean_stats.extend(measure(p,g) for p,g in zip(uint8(model(tensor)),a))
    summary['clean_input']=dict(n=len(clean_stats),**{k:float(np.mean([s[k] for s in clean_stats])) for k in clean_stats[0]})
    save_json(out/'summary.json',summary)


def benchmark(c,name,device):
    assert device.startswith('cuda')
    torch_setup(c); model=load_model(c,name,device)
    dataset=Pairs(c,'test')
    # Fixed, task-balanced real inputs so top-1 costs reflect more than one arbitrary expert.
    inputs=[dataset.batch([i*7000+j*70])[0].to(device) for i in range(10) for j in range(10)]
    samples=[]; macs=[]
    def count_hook(module,args,out):
        if isinstance(module,torch.nn.Conv2d):
            macs.append(out.numel()*(module.in_channels//module.groups)*module.kernel_size[0]*module.kernel_size[1])
        elif isinstance(module,torch.nn.Linear): macs.append(out.numel()*module.in_features)
    handles=[m.register_forward_hook(count_hook) for m in model.modules() if isinstance(m,(torch.nn.Conv2d,torch.nn.Linear))]
    with torch.inference_mode(): model(inputs[0])
    for h in handles: h.remove()
    with torch.inference_mode():
        for i in range(50): model(inputs[i%len(inputs)])
        torch.cuda.synchronize(); torch.cuda.reset_peak_memory_stats()
        for i in range(300):
            torch.cuda.synchronize(); t=time.perf_counter(); model(inputs[i%len(inputs)]); torch.cuda.synchronize()
            samples.append((time.perf_counter()-t)*1000)
    save_json(root(c)/'efficiency'/f'{name}.json',dict(params=sum(p.numel() for p in model.parameters()),
        batch=1,size=64,dtype='float32',median_ms=float(np.median(samples)),p95_ms=float(np.percentile(samples,95)),
        peak_allocated_bytes=torch.cuda.max_memory_allocated(),device=torch.cuda.get_device_name(),
        conv_linear_macs=int(sum(macs)),conv_linear_flops_2xmacs=int(2*sum(macs)),
        mac_scope='executed Conv2d/Linear only; excludes pooling, interpolation, normalization, activations, elementwise math',
        input='100 fixed real images balanced across 10 tasks; shared load must be checked before interpreting'))
