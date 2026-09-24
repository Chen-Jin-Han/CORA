"""Official architectures with one shared RGB64 input/output contract.

The existing restoration pipeline uses [-1,1]. Both source networks operate on
[0,1] RGB and predict images at the same spatial resolution.
"""
from pathlib import Path
import sys
import torch
from torch import nn

sys.path.insert(0,str(Path(__file__).parent/'vendor'/'PromptIR'))
from net.model import PromptIR
from nafnet_arch import NAFNet


class Adapter(nn.Module):
    def __init__(self, core):
        super().__init__()
        self.core=core

    def forward(self,x):
        assert x.shape[1:]==(3,64,64)
        return (2*self.core((x+1)/2)-1).clamp(-1,1)


def build(name):
    if name=='promptir':
        return Adapter(PromptIR(decoder=True))
    if name=='nafnet':
        return Adapter(NAFNet(img_channel=3,width=32,enc_blk_nums=[1,1,1,28],middle_blk_num=1,dec_blk_nums=[1,1,1,1]))
    raise ValueError(name)
