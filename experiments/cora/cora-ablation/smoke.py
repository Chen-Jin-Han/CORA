import argparse,torch
from common import read_config
from engine import torch_setup
from data import Pairs
from models import build
from losses import restoration_loss
p=argparse.ArgumentParser();p.add_argument('--model',required=True);a=p.parse_args()
c=read_config(__import__('os').environ.get('EXPERIMENT_CONFIG','config_seed7.json'));torch_setup(c)
x,y=Pairs(c,'train').batch(range(128));x=x.cuda();y=y.cuda();m=build(a.model,c['variant']).cuda().train()
opt=torch.optim.AdamW(m.parameters(),lr=c['lr'],weight_decay=c['weight_decay'])
with torch.autocast('cuda'):pred=m(x)
loss,_,_=restoration_loss(pred,y,c['fft_weight']);loss.backward()
assert torch.isfinite(loss) and all(torch.isfinite(p.grad).all() for p in m.parameters() if p.grad is not None)
opt.step();torch.cuda.synchronize();print(a.model,'batch128 smoke passed',float(loss),flush=True)
