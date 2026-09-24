import json,os,hashlib
from pathlib import Path
ROOT=Path('/data1/CST/CORA/dreamer-frame-pilot/walker_seed6_two_v1')
POLICY=Path('/data1/CST/CORA/aco-smfa-rgb/policies/dmc_walker_walk/seed0/run')
RESTORE=Path('/data1/CST/CORA/aco-smfa-full13/rgb10_seed6_fft_b128_s15000_full13_v1')
DEGS=[('rain',.6),('fog',.6),('snow',.6),('motion_blur',.35),('gaussian_noise',.5),('low_light',.7),('jpeg',.7)]
KINDS=['gaussian_noise','motion_blur']
SEED=860000
def save(path,obj):
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(obj,indent=2),encoding='utf8');os.replace(tmp,path)
def fingerprint(c):return hashlib.sha256(json.dumps(c,sort_keys=True).encode()).hexdigest()
