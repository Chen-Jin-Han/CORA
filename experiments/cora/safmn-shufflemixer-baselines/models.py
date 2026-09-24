"""Official standard trunks with scale=1 RGB reconstruction heads."""
import torch
from torch import nn
from safmn_arch import SAFMN
from shufflemixer_arch import ShuffleMixer


class Adapter(nn.Module):
    def __init__(self, core):
        super().__init__()
        self.core = core

    def forward(self, x):
        assert x.shape[1:] == (3, 64, 64)
        return (2 * self.core((x + 1) / 2) - 1).clamp(-1, 1)


def build(name):
    if name == 'safmn':
        return Adapter(SAFMN(dim=36, n_blocks=8, ffn_scale=2.0, upscaling_factor=1))
    if name == 'shufflemixer':
        return Adapter(ShuffleMixer(n_feats=64, kernel_size=7, n_blocks=5,
                                    mlp_ratio=2, upscaling_factor=1))
    raise ValueError(name)
