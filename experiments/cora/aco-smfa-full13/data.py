import json,os,time,hashlib
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor,as_completed
import numpy as np
import torch
from common import DEGS,save_json,root,fingerprint
from checkpoint_io import digest
from perturbations import static_pair
SIZES={'train':4500,'val':500,'test':1000}

def generate_shard(c,task,split):
    import cv2
    cv2.setNumThreads(1)
    src=Path(c['source_dataset_root'])/task/split;out=Path(c['dataset_root'])/task/split
    out.mkdir(parents=True,exist_ok=True);done=out/'complete.json'
    signature=fingerprint(dict(dataset_seed=c['dataset_seed'],ood=c['ood'],types=DEGS,source=str(src),version=1))
    if done.exists():
        m=json.loads(done.read_text());assert m['signature']==signature
        assert all(digest(out/k)==v for k,v in m['hashes'].items());return m
    old=json.loads((src/'complete.json').read_text());assert digest(src/'clean.npy')==old['hashes']['clean.npy']
    assert digest(src/'metadata.npz')==old['hashes']['metadata.npz']
    clean=np.load(src/'clean.npy',mmap_mode='r');assert clean.shape==(SIZES[split],64,64,3)
    if not (out/'clean.npy').exists():os.link(src/'clean.npy',out/'clean.npy')
    assert digest(out/'clean.npy')==old['hashes']['clean.npy']
    n=len(clean);count=n*13;index=np.repeat(np.arange(n),13);kind=np.tile(np.arange(13),n)
    offset=c['tasks'].index(task)*1000000+list(SIZES).index(split)*100000
    seeds=c['dataset_seed']+offset+np.arange(count,dtype=np.int64)
    target=out/'input.npy.partial';x=np.lib.format.open_memmap(target,mode='w+',dtype=np.uint8,shape=(count,64,64,3))
    begin=time.perf_counter();by_kind=np.zeros(13)
    bench=Path(c['dataset_root'])/'benchmark/input.npy'
    cached=np.load(bench,mmap_mode='r') if task==c['tasks'][0] and split=='train' and bench.exists() else None
    for j in range(count):
        start=time.perf_counter()
        x[j]=cached[j] if cached is not None and j<len(cached) else static_pair(clean[index[j]],int(kind[j]),int(seeds[j]),c)
        by_kind[kind[j]]+=time.perf_counter()-start
        if j and j%13000==0:print(json.dumps(dict(task=task,split=split,pairs=j,seconds=time.perf_counter()-begin)),flush=True)
    x.flush();del x;os.replace(target,out/'input.npy')
    z=np.load(src/'metadata.npz')
    np.savez(out/'metadata.npz',index=index,kind=kind,corruption_seed=seeds,episode=z['episode'],frame=z['frame'],policy_source=z['policy_source'])
    m=dict(signature=signature,task=task,split=split,clean=n,pairs=count,seconds=time.perf_counter()-begin,seconds_by_kind=by_kind.tolist(),
           source_clean_sha256=old['hashes']['clean.npy'],hashes={k:digest(out/k) for k in ['clean.npy','input.npy','metadata.npz']})
    save_json(done,m);return m

def generate(c):
    jobs=[(c,t,s) for t in c['tasks'] for s in SIZES];start=time.perf_counter()
    with ProcessPoolExecutor(max_workers=c['data_workers']) as pool:
        fs=[pool.submit(generate_shard,*j) for j in jobs]
        for f in as_completed(fs):
            m=f.result();print(json.dumps(dict(generated=m['task'],split=m['split'],seconds=m['seconds'])),flush=True)
    audit(c);save_json(root(c)/'generation_timing.json',dict(seconds=time.perf_counter()-start,pairs=780000,workers=c['data_workers']))

def benchmark(c):
    import cv2
    cv2.setNumThreads(1)
    d=Path(c['dataset_root'])/'benchmark';d.mkdir(parents=True,exist_ok=True)
    a=np.load(Path(c['source_dataset_root'])/c['tasks'][0]/'train/clean.npy',mmap_mode='r')
    x=np.lib.format.open_memmap(d/'input.npy.partial',mode='w+',dtype=np.uint8,shape=(13000,64,64,3));times=[]
    for k in range(13):
        start=time.perf_counter()
        for i in range(1000):x[i*13+k]=static_pair(a[i],k,c['dataset_seed']+i*13+k,c)
        x.flush();times.append(time.perf_counter()-start)
    del x;os.replace(d/'input.npy.partial',d/'input.npy')
    save_json(root(c)/'generation_benchmark.json',dict(pairs=13000,seconds_by_kind=dict(zip([n for n,_ in DEGS],times)),serial_seconds=sum(times),projected_serial_train_hours=sum(times)*45/3600,note='Single-process; parallel contention not measured'))

def audit(c):
    result=[];seeds_seen=set()
    for t in c['tasks']:
        eps_seen=set();pixels_seen=set()
        for s,n in SIZES.items():
            d=Path(c['dataset_root'])/t/s;m=json.loads((d/'complete.json').read_text());assert all(digest(d/k)==v for k,v in m['hashes'].items())
            z=np.load(d/'metadata.npz');y=np.load(d/'clean.npy',mmap_mode='r');x=np.load(d/'input.npy',mmap_mode='r')
            assert x.shape==(n*13,64,64,3) and x.dtype==y.dtype==np.uint8
            assert np.array_equal(z['index'],np.repeat(np.arange(n),13)) and np.array_equal(z['kind'],np.tile(np.arange(13),n))
            eps=set(z['episode'].tolist());assert not eps&eps_seen;eps_seen|=eps
            assert len(set(zip(z['episode'].tolist(),z['frame'].tolist())))==n
            seeds=set(z['corruption_seed'].tolist());assert len(seeds)==13*n and not seeds&seeds_seen;seeds_seen|=seeds
            hashes={hashlib.sha256(im.tobytes()).hexdigest() for im in y};duplicates=len(hashes&pixels_seen);pixels_seen|=hashes
            result.append(dict(task=t,split=s,clean=n,pairs=n*13,counts=np.bincount(z['kind']).tolist(),cross_split_exact_pixel_duplicates=duplicates))
    save_json(root(c)/'data_audit.json',result);return result

class Pairs:
    def __init__(self,c,split):
        self.shards=[];self.ends=[];count=0;self.n=SIZES[split]
        for task in c['tasks']:
            d=Path(c['dataset_root'])/task/split;assert (d/'complete.json').exists()
            z=np.load(d/'metadata.npz');x=np.load(d/'input.npy',mmap_mode='r');y=np.load(d/'clean.npy',mmap_mode='r')
            self.shards.append((task,x,y,z['index'],z['kind']));count+=len(x);self.ends.append(count)
    def __len__(self):return self.ends[-1]
    def get(self,idx):
        s=int(np.searchsorted(self.ends,idx,side='right'));j=idx-(self.ends[s-1] if s else 0)
        task,x,y,index,kind=self.shards[s];return x[j],y[index[j]],task,int(kind[j])
    def batch(self,indices,flips=None):
        pairs=[self.get(int(i)) for i in indices];x=np.stack([p[0] for p in pairs]);y=np.stack([p[1] for p in pairs])
        if flips is not None:x[flips]=x[flips,:,::-1,:];y[flips]=y[flips,:,::-1,:]
        cv=lambda a:torch.from_numpy(a.copy()).permute(0,3,1,2).float()/127.5-1
        return cv(x),cv(y)

class ValidationSubset(Pairs):
    def __init__(self,full,c):
        self.full=full;self.ids=[]
        for t in range(10):
            for k in range(13):
                rng=np.random.RandomState(c['dataset_seed']+90000000+t*13+k)
                self.ids.extend((t*500*13+rng.choice(500,40,replace=False)*13+k).tolist())
    def __len__(self):return len(self.ids)
    def get(self,idx):return self.full.get(self.ids[idx])

def balanced_indices(dataset,rng,size,step):
    groups=(np.arange(size)+(step-1)*size)%130;rng.shuffle(groups)
    return (groups//13*dataset.n+rng.randint(dataset.n,size=size))*13+groups%13
