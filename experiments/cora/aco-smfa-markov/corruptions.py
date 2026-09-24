import sys
from pathlib import Path
import numpy as np
from common import DEGS
sys.path.insert(0, str(Path(__file__).parent / 'vendor/aco'))
from visual_degradations import get_degradation


def corrupt(image, kind, intensity, seed):
    return get_degradation(DEGS[int(kind)][0], intensity=float(intensity), seed=int(seed))(image)


class VDCS:
    """Separate schedule RNG from pixel RNG; initial frame uses initial mode.
    Matched random streams remain independent of policy-induced image contents.
    """
    def __init__(self, seed):
        self.rng = np.random.RandomState(seed)
        self.kind = int(self.rng.randint(7))
        self.intensity = self.sample()
        self.first = True

    def bounds(self):
        b = DEGS[self.kind][1]
        return max(.1, .9*b), min(1., 1.1*b)

    def sample(self):
        return float(self.rng.uniform(*self.bounds()))

    def __call__(self, image):
        if not self.first:
            if self.rng.rand() < .8:
                self.intensity = float(np.clip(self.intensity + self.rng.normal(0, .02), *self.bounds()))
            else:
                self.kind = int(self.rng.choice([k for k in range(7) if k != self.kind]))
                self.intensity = self.sample()
        self.first = False
        return corrupt(image, self.kind, self.intensity, self.rng.randint(2**31-1))
