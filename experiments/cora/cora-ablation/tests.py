"""Local non-GPU correctness checks; fixtures never enter formal output."""
import json,tempfile,unittest,types,sys
from pathlib import Path
import numpy as np
import torch
from common import read_config,DEGS,save_json
from perturbations import Stream,static_pair
from data import balanced_indices,ValidationSubset

class Tests(unittest.TestCase):
    def setUp(self):
        self.c=read_config('config_seed7.json');self.im=np.random.RandomState(9).randint(0,256,(64,64,3),dtype=np.uint8)
    def test_operators_and_stream(self):
        for k,(name,_) in enumerate(DEGS):
            a=static_pair(self.im,k,33,self.c);b=static_pair(self.im,k,33,self.c)
            self.assertTrue(np.array_equal(a,b));self.assertEqual(a.shape,self.im.shape);self.assertEqual(a.dtype,np.uint8)
            s=Stream(19,self.c,name);t=Stream(19,self.c,name)
            for _ in range(8):
                self.assertTrue(np.array_equal(s(self.im),t(self.im)));self.assertEqual(s.kind,k)
        a=Stream(22,self.c);b=Stream(22,self.c);seen=set();stay=0;prev=a.kind
        for _ in range(1000):
            self.assertTrue(np.array_equal(a(self.im),b(self.im)));seen.add(a.kind);stay+=a.kind==prev;prev=a.kind
            if a.kind<7:self.assertTrue(a.bounds()[0]<=a.intensity<=a.bounds()[1])
        self.assertEqual(len(seen),13);self.assertTrue(.73<stay/1000<.87)
    def test_balanced_sampling(self):
        ds=types.SimpleNamespace(n=4500);hist=np.zeros(130,int)
        for step in range(1,131):
            ids=balanced_indices(ds,np.random.RandomState(step),128,step)
            self.assertEqual(len(set(ids)),128);self.assertTrue(np.all(ids<585000))
            groups=ids//(4500*13)*13+ids%13;hist+=np.bincount(groups,minlength=130)
        self.assertTrue(np.all(hist==128))
        sub=ValidationSubset(None,self.c);self.assertEqual(len(set(sub.ids)),5200)
        self.assertTrue(np.all(np.bincount(np.array(sub.ids)//6500*13+np.array(sub.ids)%13,minlength=130)==40))
    def test_models_loss(self):
        from models import build
        from losses import restoration_loss
        torch.set_num_threads(2)
        for name in ['aco','smfa']:
            m=build(name).train();x=torch.rand(2,3,64,64)*2-1;y=m(x)
            loss,_,_=restoration_loss(y,x,.05);loss.backward()
            self.assertTrue(torch.isfinite(loss));self.assertTrue(all(torch.isfinite(p.grad).all() for p in m.parameters() if p.grad is not None))
            with torch.no_grad():out=m.eval()(x)
            self.assertEqual(out.shape,x.shape);self.assertTrue(out.min()>=-1 and out.max()<=1)
    def test_dataset_resume(self):
        import data
        from checkpoint_io import digest
        with tempfile.TemporaryDirectory() as tmp:
            c=dict(self.c,source_dataset_root=str(Path(tmp)/'src'),dataset_root=str(Path(tmp)/'dst'))
            task=c['tasks'][0];src=Path(c['source_dataset_root'])/task/'train';src.mkdir(parents=True)
            np.save(src/'clean.npy',np.stack([self.im,self.im[::-1]]))
            np.savez(src/'metadata.npz',episode=[1,1],frame=[0,5],policy_source=[1,1])
            save_json(src/'complete.json',dict(hashes={n:digest(src/n) for n in ['clean.npy','metadata.npz']}))
            old=data.SIZES['train'];data.SIZES['train']=2
            try:
                m=data.generate_shard(c,task,'train');m2=data.generate_shard(c,task,'train');self.assertEqual(m,m2)
                x=np.load(Path(c['dataset_root'])/task/'train/input.npy');self.assertEqual(x.shape,(26,64,64,3))
                for k in range(13):self.assertTrue(np.array_equal(x[k],static_pair(self.im,k,c['dataset_seed']+k,c)))
            finally:data.SIZES['train']=old
    def test_control_resume(self):
        import control
        class Env:
            def step(self,action):self.i+=1;return dict(image=np.zeros((64,64,3),np.uint8),reward=1.,is_last=self.i==500)
            def close(self):pass
        class Lock:
            def __enter__(self):pass
            def __exit__(self,*args):pass
        agent=types.SimpleNamespace(init_policy=lambda n:None,n_actions=types.SimpleNamespace(lock=Lock(),value=0))
        cfg={'task':'dmc_walker_walk','env':{'dmc':{'size':[64,64],'repeat':2}}}
        def reset(env):env.i=0;return dict(image=np.zeros((64,64,3),np.uint8))
        fake=types.SimpleNamespace(make_agent=lambda *a:(agent,cfg),make_env=lambda *a:(Env(),None,None),reset=reset,act=lambda *a:(None,{}))
        old=sys.modules.get('dreamer_bridge');sys.modules['dreamer_bridge']=fake
        try:
            with tempfile.TemporaryDirectory() as tmp:
                c=dict(self.c,data_root=tmp);control.evaluate(c,'walker_walk','raw','single','shadow');control.evaluate(c,'walker_walk','raw','single','shadow')
                path=Path(tmp)/c['experiment']/'control/single/walker_walk/shadow/raw/episodes.jsonl'
                rows=[json.loads(x) for x in path.read_text().splitlines()];self.assertEqual(len(rows),5);self.assertTrue(all(a['return_']==500 for a in rows))
        finally:
            if old is None:sys.modules.pop('dreamer_bridge',None)
            else:sys.modules['dreamer_bridge']=old
    def test_report_fixture(self):
        from protocol import jobs
        from common import root,fingerprint
        from summarize import summarize
        with tempfile.TemporaryDirectory() as tmp:
            c=dict(self.c,data_root=tmp);r=root(c)
            self.assertEqual(len(jobs(c)),430)
            for task,mode,kind,method in jobs(c):
                d=r/'control'/mode/task/(kind or mode)/method
                save_json(d/'protocol.json',dict(config=fingerprint(c),task=task,condition=method,mode=mode,kind=kind))
                n=10 if mode=='markov' else 5
                rr=[dict(task=task,condition=method,mode=mode,kind=kind,seed=c['control_seed']+c['tasks'].index(task)*1000+i,return_=float(i),terminal=True,decisions=500,action_repeat=2) for i in range(n)]
                (d/'episodes.jsonl').write_text(''.join(json.dumps(a)+'\n' for a in rr))
            for model in ['aco','smfa']:
                d=r/'checkpoints'/model;d.mkdir(parents=True)
                torch.save(dict(step=15000,config_hash=fingerprint(c),name=model,elapsed=1.,history=[dict(validation=dict(scope='full_65000'))]),d/'last.pt')
                score=dict(psnr_y=25.,ssim_y=.8,psnr_rgb=24.,ssim_rgb=.7)
                ss={"all":dict(n=130000,**score),"clean_input":dict(n=10000,**score)}
                ss.update({'degradation/'+k:dict(n=10000,**score) for k,_ in DEGS})
                d=r/'images'/model;save_json(d/'summary.json',ss)
                (d/'per_image.csv').write_text('index\n'+''.join(str(i)+'\n' for i in range(130000)))
            summarize(c)
            self.assertEqual(json.loads((r/'verification.json').read_text())['unique_episodes'],2300)
if __name__=='__main__':unittest.main()
