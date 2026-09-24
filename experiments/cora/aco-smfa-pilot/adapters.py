import sys
from pathlib import Path
import torch
from torch import nn
from smfa_blocks import FMB
sys.path.insert(0, str(Path(__file__).parent / 'vendor/aco'))
from moe_unet import DualStreamMoEUNet


class SMFAAdapter(nn.Module):
    def __init__(self, dim=36, blocks=8):
        super().__init__()
        self.to_feat = nn.Conv2d(3, dim, 3, padding=1)
        self.feats = nn.Sequential(*[FMB(dim) for _ in range(blocks)])
        self.rgb = nn.Conv2d(dim, 3, 3, padding=1)
        self.mask = nn.Conv2d(dim, 2, 3, padding=1)

    def forward(self, x):
        feat = self.to_feat(x)
        feat = self.feats(feat) + feat
        rgb = (x + self.rgb(feat).tanh()).clamp(-1, 1)
        logits = self.mask(feat)
        prob = logits.softmax(1)[:, 1:2]
        hard = (prob >= .5).to(rgb.dtype)
        return dict(restored_rgb=rgb, mask_logits=logits, foreground_prob=prob,
                    agent_only_rgb=(rgb + 1) * prob - 1,
                    agent_only_rgb_hard=(rgb + 1) * hard - 1)


def build(name):
    if name == 'aco':
        return DualStreamMoEUNet(base_channels=9, num_experts=9)
    if name == 'smfa':
        return SMFAAdapter()
    raise ValueError(name)


def forward(model, x, name, training=False):
    return model(x, router_topk=0 if training else 1) if name == 'aco' else model(x)
