import numpy as np
from common import DEGS
from corruptions import corrupt

class SingleID:
    """Fixed family per episode; ACO Appendix A severity random walk, no type switches."""
    def __init__(self, kind, seed):
        self.kind=[k for k,_ in DEGS].index(kind)
        self.rng=np.random.RandomState(seed)
        base=DEGS[self.kind][1];self.bounds=(max(.1,.9*base),min(1.,1.1*base))
        self.intensity=float(self.rng.uniform(*self.bounds));self.first=True
    def __call__(self,image):
        if not self.first:self.intensity=float(np.clip(self.intensity+self.rng.normal(0,.02),*self.bounds))
        self.first=False
        return corrupt(image,self.kind,self.intensity,self.rng.randint(2**31-1))
