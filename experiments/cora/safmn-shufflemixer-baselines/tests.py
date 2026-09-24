import types
from pathlib import Path
import torch
from models import build
from losses import restoration_loss
from common import read_config
torch.set_num_threads(2)
for name,repo,cls,kwargs in [('safmn','SAFMN','SAFMN',dict(dim=36,n_blocks=8,ffn_scale=2.,upscaling_factor=1)),('shufflemixer','ShuffleMixer','ShuffleMixer',dict(n_feats=64,kernel_size=7,n_blocks=5,mlp_ratio=2,upscaling_factor=1))]:
 read_config('config_'+name+'.json');text=(Path('vendor')/repo/(name+'_arch.py')).read_text();text=text.replace('from torchvision import ops','').replace('from basicsr.utils.registry import ARCH_REGISTRY','').replace('@ARCH_REGISTRY.register()','')
 official=types.ModuleType('official_'+name);exec(compile(text,'official_'+name,'exec'),official.__dict__);core=getattr(official,cls)(**kwargs);model=build(name);model.core.load_state_dict(core.state_dict())
 x=torch.rand(2,3,64,64)*2-1;y=torch.rand_like(x)*2-1;out=model(x);assert out.shape==x.shape;assert torch.equal(out,(2*core((x+1)/2)-1).clamp(-1,1));loss,_,_=restoration_loss(out,y,.05);loss.backward();assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in model.parameters());print(name,'official scale1 parity and gradients PASS',sum(p.numel() for p in model.parameters()))
