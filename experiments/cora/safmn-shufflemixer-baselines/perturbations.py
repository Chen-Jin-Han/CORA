"""ID7 random walk; added6 fixed strength/pattern per segment except shot noise."""
import numpy as np
from common import DEGS
from corruptions import corrupt
from ood import OOD

def static_pair(image,kind,seed,c):
    if kind<7:
        rng=np.random.RandomState(seed)
        v=DEGS[kind][1]*rng.uniform(.9,1.1)
        return corrupt(image,kind,v,int(rng.randint(2**31-1)))
    return OOD(DEGS[kind][0],int(seed),c['ood'])(image)

class Stream:
    def __init__(self,seed,c,kind=None):
        self.rng=np.random.RandomState(seed);self.c=c;self.fixed=kind is not None;self.first=True
        self.kind=[n for n,_ in DEGS].index(kind) if self.fixed else int(self.rng.randint(13))
        self.enter()
    def bounds(self):
        b=DEGS[self.kind][1];return max(.1,.9*b),min(1.,1.1*b)
    def enter(self):
        if self.kind<7:self.intensity=float(self.rng.uniform(*self.bounds()));self.operator=None
        else:self.operator=OOD(DEGS[self.kind][0],int(self.rng.randint(2**31-1)),self.c['ood'])
    def __call__(self,image):
        if not self.first:
            switch=not self.fixed and self.rng.rand()>=self.c['markov_stay_prob']
            if switch:
                self.kind=int(self.rng.choice([k for k in range(13) if k!=self.kind]));self.enter()
            elif self.kind<7:self.intensity=float(np.clip(self.intensity+self.rng.normal(0,.02),*self.bounds()))
        self.first=False
        if self.kind<7:return corrupt(image,self.kind,self.intensity,int(self.rng.randint(2**31-1)))
        return self.operator(image)
