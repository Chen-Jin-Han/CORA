import argparse,os,time,torch
from common import read_config,root,save_json
from engine import torch_setup
from data import Pairs
from models import build
from losses import restoration_loss
p=argparse.ArgumentParser();p.add_argument('--model',required=True);a=p.parse_args()
c=read_config(os.environ['EXPERIMENT_CONFIG']);torch_setup(c)
x,y=Pairs(c,'train').batch(range(128));x=x.cuda();y=y.cuda();m=build(a.model).cuda().train()
opt=torch.optim.AdamW(m.parameters(),lr=c['lr'],weight_decay=c['weight_decay']);scaler=torch.amp.GradScaler('cuda',enabled=c['amp'],init_scale=1024.)
torch.cuda.reset_peak_memory_stats();timings=[]
for _ in range(5):
  torch.cuda.synchronize();start=time.perf_counter();opt.zero_grad(set_to_none=True)
  with torch.autocast('cuda',enabled=c['amp']):pred=m(x)
  assert pred.shape==x.shape
  loss,_,_=restoration_loss(pred,y,c['fft_weight']);assert torch.isfinite(loss);scaler.scale(loss).backward();scaler.unscale_(opt)
  assert all(torch.isfinite(p.grad).all() for p in m.parameters() if p.grad is not None);scaler.step(opt);scaler.update();torch.cuda.synchronize();timings.append(time.perf_counter()-start)
result=dict(model=a.model,batch=128,steps=5,finite=True,loss=float(loss),step_seconds=timings,peak_allocated_bytes=torch.cuda.max_memory_allocated(),parameters=sum(p.numel() for p in m.parameters()))
save_json(root(c)/'smoke.json',result);print(result,flush=True)
