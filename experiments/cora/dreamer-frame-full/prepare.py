import json,time
import numpy as np
from common import *

def corrupt_task(task):
 from perturbations import Stream
 from checkpoint_io import digest
 d=ROOT/'inputs'/task;d.mkdir(parents=True,exist_ok=True);path=d/'raw.npy';out=np.lib.format.open_memmap(d/'raw.partial.npy',mode='w+',dtype=np.uint8,shape=(14,5,500,64,64,3));kinds=np.zeros((14,5,500),np.int16)
 for ep in range(5):
  clean=np.load(trajectory(task,'evaluation',ep))['obs_image'];seed=trajectory_seed(task,'evaluation',ep)
  for j,protocol in enumerate(PROTOCOLS):
   stream=Stream(seed+10000000,CONFIG,None if protocol=='markov' else protocol)
   for t,im in enumerate(clean):out[j,ep,t]=stream(im);kinds[j,ep,t]=stream.kind
 out.flush();del out;os.replace(d/'raw.partial.npy',path);atomic_npz(d/'metadata.npz',kind=kinds)
 save(d/'raw.json',dict(shape=[14,5,500,64,64,3],sha256=digest(path),protocols=PROTOCOLS))

def restore_task(task,method):
 import torch
 from models import build
 from metrics import uint8
 from checkpoint_io import digest
 modelname,seedtext=method.split('_seed');seed=int(seedtext);source=restoration(seed);cfg=json.loads((source/'protocol.json').read_text())
 ckpath=source/'checkpoints'/modelname/'last.pt';ck=torch.load(ckpath,map_location='cpu',weights_only=False)
 assert cfg['seed']==seed and ck['step']==15000 and ck['config_hash']==fingerprint(cfg) and ck['name']==modelname
 torch.set_num_threads(4);model=build(modelname).eval();model.load_state_dict(ck['model'],strict=True)
 d=ROOT/'inputs'/task;raw=np.load(d/'raw.npy',mmap_mode='r');x=raw.reshape((-1,64,64,3))
 output=np.lib.format.open_memmap(d/(method+'.partial.npy'),mode='w+',dtype=np.uint8,shape=raw.shape);flat=output.reshape((-1,64,64,3));start=time.perf_counter()
 with torch.inference_mode():
  for i in range(0,len(x),64):
   a=torch.from_numpy(np.array(x[i:i+64])).permute(0,3,1,2).float()/127.5-1;flat[i:i+64]=uint8(model(a))
   if i%6400==0:print(task,method,i,len(x),flush=True)
 output.flush();del flat,output;os.replace(d/(method+'.partial.npy'),d/(method+'.npy'))
 save(d/(method+'.json'),dict(task=task,method=method,images=len(x),seconds=time.perf_counter()-start,checkpoint=str(ckpath),checkpoint_sha256=digest(ckpath),output_sha256=digest(d/(method+'.npy'))))
