"""RGB-only adaptations. No mask modules, labels or foreground composition."""
import sys
from pathlib import Path
import torch
from torch import nn
sys.path.insert(0, str(Path(__file__).parent / 'vendor/aco'))
from moe_unet import UNetEncoder, UNetDecoder, BottleneckRouter
from smfa_blocks import FMB


class ACORGB(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = UNetEncoder(base_channels=9)
        self.router = BottleneckRouter(self.encoder.out_channels, 9, 256)
        self.rgb_experts = nn.ModuleList([UNetDecoder(3, 9) for _ in range(9)])

    def forward(self, x):
        f = self.encoder(x)
        weights = self.router(f.bottleneck).softmax(-1)
        if self.training:
            delta = sum(w[:, None, None, None] * e(f.bottleneck, f.skips)
                        for w, e in zip(weights.unbind(1), self.rgb_experts))
        else:
            chosen = weights.argmax(1)
            delta = torch.empty_like(x)
            for k, expert in enumerate(self.rgb_experts):
                idx = (chosen == k).nonzero(as_tuple=True)[0]
                if len(idx):
                    delta[idx] = expert(f.bottleneck[idx], [s[idx] for s in f.skips]).to(delta.dtype)
        return (x + delta.tanh()).clamp(-1, 1)


class SMFARGB(nn.Module):
    def __init__(self):
        super().__init__()
        self.to_feat = nn.Conv2d(3, 36, 3, padding=1)
        self.feats = nn.Sequential(*[FMB(36) for _ in range(8)])
        self.rgb = nn.Conv2d(36, 3, 3, padding=1)

    def forward(self, x):
        f = self.to_feat(x)
        return (x + self.rgb(self.feats(f) + f).tanh()).clamp(-1, 1)


def build(name):
    return {'aco': ACORGB, 'smfa': SMFARGB}[name]()
