import numpy as np
def symkl(mu,sigma,ref_mu,ref_sigma):
 a=np.asarray(mu,np.float64);b=np.asarray(ref_mu,np.float64);s=np.asarray(sigma,np.float64);r=np.asarray(ref_sigma,np.float64)
 return np.mean(.25*((s/r)**2+(r/s)**2-2+(a-b)**2*(1/s**2+1/r**2)),axis=-1)
def js(p,q):
 p=np.asarray(p,np.float64);q=np.asarray(q,np.float64);m=(p+q)/2
 return np.mean(.5*np.sum(p*np.log(p/m)+q*np.log(q/m),axis=-1),axis=-1)
def rmse(a,b):return np.sqrt(np.mean((np.asarray(a,np.float64)-np.asarray(b,np.float64))**2,axis=-1))
