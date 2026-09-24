"""Local CPU checks; no policy weights, server, datasets or formal jobs required."""
import ast
import json
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace
import threading
from pathlib import Path
import cv2
import numpy as np
import torch
from common import read_config,DEGS,save_json
from models import build
from metrics import measure,y_channel
from corruptions import VDCS,corrupt
from data import Pairs


class Checks(unittest.TestCase):
    @classmethod
    def setUpClass(cls): torch.set_num_threads(2)

    def test_latest_protocol(self):
        c=read_config(Path(__file__).parent/'config.json')
        self.assertEqual(len(c['tasks'])*4*c['control_episodes'],400)
        self.assertEqual(c['batch_size']*c['steps'],1920000)

    def test_models_train_and_top1(self):
        for name in ['aco','smfa']:
            torch.manual_seed(0); m=build(name)
            self.assertFalse(any('mask' in k for k in m.state_dict()))
            x=torch.rand(2,3,64,64)*2-1; y=torch.rand_like(x)*2-1
            m.train(); opt=torch.optim.AdamW(m.parameters(),lr=1e-4)
            loss=(m(x)-y).abs().mean(); loss.backward()
            self.assertTrue(all(p.grad is not None and torch.isfinite(p.grad).all() for p in m.parameters()))
            opt.step(); m.eval()
            with torch.no_grad(): out=m(x)
            self.assertEqual(out.shape,x.shape); self.assertTrue(torch.isfinite(out).all())
            self.assertTrue(out.min()>=-1 and out.max()<=1)
            if name=='aco':
                counts=[0]*9
                handles=[e.register_forward_hook(lambda m,i,o,k=k: counts.__setitem__(k,counts[k]+len(i[0]))) for k,e in enumerate(m.rgb_experts)]
                with torch.no_grad(): m(x)
                for h in handles: h.remove()
                self.assertEqual(sum(counts),len(x)) # only the selected expert runs for each image
            print(name,'params',sum(p.numel() for p in m.parameters()),'loss',float(loss.detach()))

    def test_metrics_against_vendor(self):
        vendor=Path(__file__).parent/'vendor/SMFANet/basicsr'
        ns={'np':np,'cv2':cv2,'torch':torch}
        # Execute actual vendored pure functions without importing BasicSR's unrelated torchvision registry.
        for rel in ['utils/color_util.py','metrics/metric_util.py','metrics/psnr_ssim.py']:
            tree=ast.parse((vendor/rel).read_text())
            funcs=[n for n in tree.body if isinstance(n,ast.FunctionDef)]
            for f in funcs: f.decorator_list=[]
            exec(compile(ast.Module(body=funcs,type_ignores=[]),rel,'exec'),ns)
            if rel=='utils/color_util.py': ns['bgr2ycbcr']=ns['bgr2ycbcr']
        rng=np.random.RandomState(2)
        a=rng.randint(0,256,(64,64,3),dtype=np.uint8); b=rng.randint(0,256,a.shape,dtype=np.uint8)
        m=measure(a,b)
        # BasicSR numpy API takes BGR; our public input is RGB.
        for suffix,y in [('y',True),('rgb',False)]:
            self.assertAlmostEqual(m['psnr_'+suffix],ns['calculate_psnr'](a[...,::-1],b[...,::-1],0,test_y_channel=y),places=6)
            self.assertAlmostEqual(m['ssim_'+suffix],ns['calculate_ssim'](a[...,::-1],b[...,::-1],0,test_y_channel=y),places=6)
        self.assertAlmostEqual(measure(a,a)['ssim_y'],1.)

    def test_corruption_streams(self):
        image=np.full((64,64,3),127,np.uint8)
        for k,(_,base) in enumerate(DEGS):
            a=corrupt(image,k,base,15); b=corrupt(image,k,base,15)
            self.assertTrue(np.array_equal(a,b)); self.assertEqual(a.shape,image.shape)
            self.assertEqual(a.dtype,np.uint8)
        a,b=VDCS(17),VDCS(17)
        for _ in range(100):
            self.assertTrue(np.array_equal(a(image),b(image)))
            lo,hi=a.bounds(); self.assertTrue(lo<=a.intensity<=hi)

    def test_fixed_pairs_and_aligned_flip(self):
        with tempfile.TemporaryDirectory() as temp:
            c={'data_root':temp,'experiment':'test','tasks':['fixture']}
            d=Path(temp)/'test/datasets/fixture/train'; d.mkdir(parents=True)
            clean=np.arange(2*64*64*3,dtype=np.uint8).reshape(2,64,64,3)
            np.save(d/'clean.npy',clean); np.save(d/'input.npy',clean[[1,0]])
            np.savez(d/'metadata.npz',index=[1,0],kind=[0,1]); save_json(d/'complete.json',{})
            ds=Pairs(c,'train'); x,y=ds.batch([0,1],np.array([True,False]))
            self.assertTrue(torch.equal(x,y))
            expected=torch.from_numpy(clean[1,:,::-1].copy()).permute(2,0,1).float()/127.5-1
            self.assertTrue(torch.equal(x[0],expected))
            from engine import validate
            stats=validate({'eval_batch':2},build('smfa'),ds,'cpu')
            self.assertTrue(np.isfinite(stats['l1']))
            self.assertIn('task/fixture',stats['groups'])
            for _,a,b,_,_ in ds.shards:
                a._mmap.close(); b._mmap.close()

    def test_control_resume_full_episodes(self):
        from control import evaluate
        c=read_config(Path(__file__).parent/'config.json')
        made=[]
        class Env:
            def __init__(self): self.steps=0; made.append(self)
            def step(self,action):
                self.steps+=1
                return dict(image=np.zeros((64,64,3),np.uint8),reward=2.,is_last=self.steps==3)
            def close(self): pass
        agent=SimpleNamespace(init_policy=lambda n:None,n_actions=SimpleNamespace(lock=threading.Lock(),value=0))
        cfg={'task':'dmc_walker_walk','env':{'dmc':{'size':[64,64],'repeat':2}}}
        initial=dict(image=np.zeros((64,64,3),np.uint8),reward=0.,is_last=False)
        with tempfile.TemporaryDirectory() as tmp:
            c['data_root']=tmp
            with patch('dreamer_bridge.make_agent',return_value=(agent,cfg)), \
                 patch('dreamer_bridge.make_env',side_effect=lambda *a:(Env(),None,0)), \
                 patch('dreamer_bridge.reset',return_value=initial), \
                 patch('dreamer_bridge.act',return_value=(None,{})):
                evaluate(c,'walker_walk','clean')
                path=Path(tmp)/c['experiment']/'control/walker_walk/clean/episodes.jsonl'
                with path.open('a') as f: f.write('{"partial":')
                evaluate(c,'walker_walk','clean')
                self.assertEqual(len(made),10) # completed episodes are not repeated on resume
                rows=[json.loads(x) for x in path.read_text().splitlines()]
                self.assertTrue(all(r['return_']==6 and r['decisions']==3 and r['terminal'] for r in rows))

    def test_report_contract(self):
        from report import make_report
        c=read_config(Path(__file__).parent/'config.json')
        with tempfile.TemporaryDirectory() as tmp:
            c['data_root']=tmp; r=Path(tmp)/c['experiment']
            for task in c['tasks']:
                for condition in ['clean','raw','aco','smfa']:
                    value={'clean':10.,'raw':2.,'aco':6.,'smfa':8.}[condition]
                    save_json(r/'control'/task/condition/'summary.json',dict(n=10,mean=value,std=0.,
                        episodes=[dict(seed=i,return_=value,terminal=True) for i in range(10)]))
            metrics=dict(psnr_y=30.,ssim_y=.9,psnr_rgb=28.,ssim_rgb=.8)
            for name in ['aco','smfa']:
                save_json(r/'images'/name/'summary.json',{'all':dict(n=70000,**metrics),'clean_input':dict(n=10000,**metrics)})
                save_json(r/'checkpoints'/name/'history.json',[dict(step=i,validation=dict(l1=.1,**metrics)) for i in range(500,15001,500)])
                save_json(r/'efficiency'/f'{name}.json',dict(median_ms=1.,p95_ms=2.,peak_allocated_bytes=100,conv_linear_macs=100))
            with patch('engine.load_model',return_value=torch.nn.Linear(1,1)): make_report(c)
            result=json.loads((r/'comparison.json').read_text())
            self.assertEqual(result['total_episodes'],400)
            self.assertEqual(result['macro_return']['smfa'],8.)
            self.assertTrue(all(x['paired_bootstrap_ci95']==[2.,2.] for x in result['control']))
            self.assertTrue((r/'curves.png').exists())


if __name__=='__main__': unittest.main(verbosity=2)
