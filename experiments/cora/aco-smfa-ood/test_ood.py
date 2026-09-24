import unittest
import numpy as np
import torch
from common import read_config
from ood import OOD
from losses import restoration_loss

class Tests(unittest.TestCase):
    def test_models_loss_gradients(self):
        from models import build
        torch.set_num_threads(2)
        for name in ['aco','smfa']:
            torch.manual_seed(1)
            m=build(name).train()
            x=torch.rand(2,3,64,64)*2-1
            total,_,_=restoration_loss(m(x),x)
            total.backward()
            self.assertTrue(torch.isfinite(total))
            self.assertTrue(all(torch.isfinite(p.grad).all() for p in m.parameters() if p.grad is not None))

    def test_fft_matches_official_formula(self):
        torch.manual_seed(1)
        x=torch.rand(2,3,64,64,requires_grad=True); y=torch.rand_like(x)
        a,b=torch.fft.rfft2(x),torch.fft.rfft2(y)
        reference=torch.nn.functional.l1_loss(torch.stack([a.real,a.imag],-1),torch.stack([b.real,b.imag],-1))
        total,pixel,fft=restoration_loss(x,y)
        torch.testing.assert_close(fft,reference)
        torch.testing.assert_close(total,(x-y).abs().mean()+.05*reference)
        total.backward();self.assertTrue(torch.isfinite(x.grad).all())
        self.assertEqual(float(restoration_loss(y,y)[0]),0.)

    def test_ood_streams_and_bounds(self):
        c=read_config('config.json'); image=np.random.RandomState(1).randint(0,256,(64,64,3),dtype=np.uint8)
        for kind in c['ood_types']:
            a,b=OOD(kind,42,c['ood']),OOD(kind,42,c['ood'])
            first=a(image);other=b(image)
            np.testing.assert_array_equal(first,other)
            self.assertEqual(first.dtype,np.uint8);self.assertEqual(first.shape,image.shape)
            self.assertFalse(np.array_equal(first,image))
            second=a(image);np.testing.assert_array_equal(second,b(image))
            if kind=='shot_noise':self.assertFalse(np.array_equal(first,second))
            else:np.testing.assert_array_equal(first,second)
        a=OOD('occlusion_patch',4,c['ood']); a(image)
        area=a.pattern[2]**2/4096;self.assertTrue(.08<area<.12)
        self.assertEqual(len(c['tasks'])*len(c['ood_types'])*3*c['control_episodes'],900)

if __name__=='__main__':unittest.main()
