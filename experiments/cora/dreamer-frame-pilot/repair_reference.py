import numpy as np
from common import ROOT,KINDS
from diagnostic import Diagnostic
d=Diagnostic('cpu','reference_float32')
cache=dict(np.load(ROOT/'trajectory.npz'));raw=dict(np.load(ROOT/'raw.npz'));ids=np.array([103,129,202,417])
out=d.infer(cache,ids,raw[KINDS[0]][ids])
np.savez(ROOT/'cpu_check_reference_float32.npz',**{k:np.asarray(v,dtype=np.float32) for k,v in out.items()})
print('Float32 reference saved',flush=True)
