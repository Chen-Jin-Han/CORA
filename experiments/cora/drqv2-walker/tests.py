"""Local checks: replay alignment, boundary masking, resume, 64px actor/critic."""
import tempfile
import unittest
from pathlib import Path
import numpy as np
import torch
from runner import Replay, make_agent, ROOT
import json


class Tests(unittest.TestCase):
    def test_replay_boundaries_and_resume(self):
        with tempfile.TemporaryDirectory() as d:
            r = Replay(d,20,2,size=4)
            im = lambda n: np.full((3,4,4),n,dtype=np.uint8)
            r.begin(im(10)); r.add(im(11),[.1,.2],1.,1.)
            r.add(im(12),[.3,.4],2.,0.)
            r.begin(im(30)); r.add(im(31),[.5,.6],3.,1.)
            self.assertEqual(r.index[:3].tolist(), [0,1,3])
            self.assertEqual(r.stack(np.array([0,1,2,3,4]))[:,::3,0,0].tolist(),
                             [[10,10,10],[10,10,11],[10,11,12],[30,30,30],[30,30,31]])
            b = next(r.batches(128,.99))
            for obs,act,reward,discount,nxt in zip(*b):
                v=int(reward[0]); self.assertAlmostEqual(float(act[0]),{1:.1,2:.3,3:.5}[v],places=5)
                self.assertEqual(int(nxt[-1,0,0]),{1:11,2:12,3:31}[v])
                self.assertAlmostEqual(float(discount[0]),0. if v==2 else .99,places=5)
            r.flush()
            s=Replay(d,20,2,size=4,resume=True)
            self.assertEqual(int(s.images[4,0,0,0]),31)
            # Close memmaps before TemporaryDirectory cleanup on Windows.
            for item in [r,s]:
                for a in item.arrays.values(): a._mmap.close()

    def test_network_update_and_restore(self):
        torch.set_num_threads(2)
        c=json.loads((ROOT/'config.json').read_text())
        agent=make_agent(c,(6,),'cpu')
        self.assertEqual(agent.encoder.repr_dim,32*25*25)
        obs=np.zeros((9,64,64),dtype=np.uint8)
        with torch.no_grad():
            action=agent.act(obs,2000,True)
        self.assertEqual(action.shape,(6,))
        b=(np.zeros((2,9,64,64),np.uint8),np.zeros((2,6),np.float32),
           np.ones((2,1),np.float32),np.full((2,1),.99,np.float32),
           np.ones((2,9,64,64),np.uint8))
        metrics=agent.update(iter([b]),2000)
        self.assertTrue(all(np.isfinite(v) for v in metrics.values()))
        with torch.no_grad(): expected=agent.act(obs,2000,True)
        weights={k:getattr(agent,k).state_dict() for k in ['encoder','actor','critic']}
        other=make_agent(c,(6,),'cpu')
        for k,v in weights.items(): getattr(other,k).load_state_dict(v)
        with torch.no_grad(): actual=other.act(obs,2000,True)
        np.testing.assert_array_equal(expected,actual)


if __name__=='__main__': unittest.main()
