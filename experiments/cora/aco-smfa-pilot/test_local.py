import numpy as np
import torch
from adapters import build, forward
from checkpoint_io import strict_check

torch.set_num_threads(4)
torch.manual_seed(0)
x = torch.rand(2, 3, 64, 64) * 2 - 1
for name in ['aco', 'smfa']:
    model = build(name)
    out = forward(model, x, name, training=True)
    loss = out['restored_rgb'].square().mean() + out['mask_logits'].square().mean()
    loss.backward()
    assert all(torch.isfinite(p.grad).all() for p in model.parameters() if p.grad is not None)
    model.eval()
    with torch.inference_mode():
        out = forward(model, x, name)
    assert out['restored_rgb'].shape == x.shape
    assert out['mask_logits'].shape == (2, 2, 64, 64)
    masked = out['foreground_prob'] < .5
    assert torch.all(out['agent_only_rgb_hard'][masked.expand_as(x)] == -1)
    print(name, sum(p.numel() for p in model.parameters()), 'forward/backward and black background OK')
strict_check({'x': np.zeros((2,), np.float32)}, {'x': np.ones((2,), np.float32)})
try:
    strict_check({'x': np.zeros((2,), np.float32)}, {'y': np.ones((2,), np.float32)})
except ValueError:
    print('Mismatch correctly rejected')
else:
    raise AssertionError('Mismatch silently accepted')
