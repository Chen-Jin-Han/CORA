"""GPU-batch restore cached Markov observations from the completed diagnostic run."""
import sys,time,hashlib
from pathlib import Path
import numpy as np,torch
from common import read_config,root,save_json
from engine import load_model,torch_setup
from metrics import uint8
BASE=Path('/data1/CST/CORA/safmn-shufflemixer-baselines')
REF=Path('/data1/CST/CORA/dreamer-frame-full/seed678_id13_shared_history_v1')
model=sys.argv[1];task=sys.argv[2];c=read_config('config_'+model+'.json');torch_setup(c)
adapter=load_model(c,model,'cuda');source=np.load(REF/'inputs'/task/'raw.npy',mmap_mode='r')[13]
assert source.shape==(5,500,64,64,3)
dest=BASE/'frame_inputs'/model/(task+'.npy');dest.parent.mkdir(parents=True,exist_ok=True)
tmp=dest.with_suffix('.partial.npy');out=np.lib.format.open_memmap(tmp,'w+',dtype=np.uint8,shape=source.shape)
a=source.reshape((-1,64,64,3));b=out.reshape((-1,64,64,3));start=time.perf_counter()
with torch.inference_mode():
 for i in range(0,len(a),c['eval_batch']):
  x=torch.from_numpy(np.array(a[i:i+c['eval_batch']])).permute(0,3,1,2).float().cuda()/127.5-1
  b[i:i+len(x)]=uint8(adapter(x))
out.flush();del b,out;tmp.replace(dest)
save_json(dest.with_suffix('.json'),dict(model=model,task=task,images=2500,shape=[5,500,64,64,3],seconds=time.perf_counter()-start,sha256=hashlib.sha256(dest.read_bytes()).hexdigest()))
