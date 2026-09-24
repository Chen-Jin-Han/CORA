import unittest,numpy as np
from math_metrics import symkl,js,rmse
class TestMetrics(unittest.TestCase):
 def test_normal(self):
  z=np.zeros((4,6));one=np.ones_like(z)
  self.assertTrue(np.all(symkl(z,one,z,one)==0))
  self.assertTrue(np.allclose(symkl(z,one,one,one),.5))
  self.assertTrue(np.allclose(symkl(z,one,one,one*2),symkl(one,one*2,z,one)))
 def test_js(self):
  p=np.array([[[.8,.2],[.2,.8]]]);q=p[...,::-1]
  self.assertTrue(np.all(js(p,p)==0));self.assertTrue(np.allclose(js(p,q),js(q,p)));self.assertTrue(np.all(js(p,q)<=np.log(2)))
 def test_rmse(self):self.assertEqual(float(rmse([0.,0.],[1.,1.])),1.)
if __name__=='__main__':unittest.main()
