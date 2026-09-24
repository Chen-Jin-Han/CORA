import torch,json
from models import build
torch.set_num_threads(2)
expected={'full':182703,'no_context':168591,'no_local':103215,'full_channel':533055}
for variant,count in expected.items():
 torch.manual_seed(6);m=build('smfa',variant);assert sum(p.numel() for p in m.parameters())==count
 x=torch.rand(2,3,64,64)*2-1;m.train();y=m(x);y.square().mean().backward()
 assert y.shape==x.shape and torch.isfinite(y).all()
 assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in m.parameters())
 m.eval()
 with torch.no_grad():z=m(x)
 assert torch.allclose(y,z,atol=1e-6),float((y-z).abs().max())
 print(variant,count,'all parameters connected; train/eval equivalent')
# Reproduce the original Full computation using the same weights.
from importlib.util import spec_from_file_location,module_from_spec
s=spec_from_file_location('original_blocks','../aco-smfa-full13-seed78/smfa_blocks.py')
if __import__('pathlib').Path(s.origin).exists():
 mod=module_from_spec(s);s.loader.exec_module(mod)
 full=build('smfa','full');original=build('smfa','full');original.feats=torch.nn.Sequential(*[mod.FMB(36) for _ in range(8)]);original.load_state_dict(full.state_dict());full.eval();original.eval()
 with torch.no_grad():assert torch.equal(full(x),original(x))
 print('Full matches original implementation exactly')
