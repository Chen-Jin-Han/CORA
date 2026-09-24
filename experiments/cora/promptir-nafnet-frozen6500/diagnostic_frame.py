"""Read-only Ninjax calls with full checkpoint (including critic/valnorm).
Explicit per-frame common categorical noise makes sampling batch-order invariant.
"""
import numpy as np
from pathlib import Path
ROOT=Path('/data1/CST/CORA/promptir-nafnet-frozen6500/frame')
def policy(task):return Path('/data1/CST/CORA/aco-smfa-rgb/policies')/('dmc_'+task)/'seed0/run'

class Diagnostic:
 def __init__(self,task,platform='cpu',label='diagnostic'):
  import jax,jax.numpy as jnp,ninjax as nj
  from dreamer_bridge import make_agent
  import embodied.jax.nets as nn
  self.jax=jax;self.jnp=jnp
  assert platform=='cpu','Formal metrics use the validated CPU path only'
  self.agent,self.cfg=make_agent(policy(task),ROOT/'loading'/task/label,platform)
  self.model=m=self.agent.model
  assert self.cfg['agent']['policy_dist_cont']=='bounded_normal'
  assert set(self.agent.act_space)=={'action'}
  assert m.enc.initial(1)=={} and m.dec.initial(1)=={}
  self.params=self.agent.params
  assert any(k.startswith('val/') for k in self.params)
  assert self.cfg['env']['dmc']['repeat']==2
  def posterior(h,z,prevact,obs):
   _,_,tokens=m.enc({},obs,obs['is_first'],training=False,single=True)
   _,_,feat=m.dyn.observe(dict(deter=h,stoch=z),tokens,dict(action=prevact),obs['is_first'],training=False,single=True)
   probs=jax.nn.softmax(m.dyn._dist(feat['logit']).output.dist.logits,axis=-1)
   return feat['deter'],probs
  def heads(h,z,action):
   feat=dict(deter=nn.cast(h),stoch=nn.cast(z));inp=m.feat2tensor(feat)
   dist=m.pol(inp,bdims=1)['action'].output
   offset,scale=m.valnorm.stats();v=m.val(inp,bdims=1).pred()*scale+offset
   act=nn.DictConcat(m.act_space,1)(dict(action=action))
   hn=m.dyn._core(feat['deter'],feat['stoch'],act)
   return dict(mu=dist.mean,std=dist.stddev,value=v,hnext=hn.astype(jnp.float32))
  ppost=nj.pure(posterior);pheads=nj.pure(heads)
  self.post=jax.jit(lambda h,z,a,o:ppost(self.params,h,z,a,o,seed=0,create=False,modify=False)[1])
  self.head=jax.jit(lambda h,z,a:pheads(self.params,h,z,a,seed=0,create=False,modify=False)[1])
  def sampled(h,probs,act,frame_ids):
   keys=jax.vmap(lambda i:jax.random.PRNGKey(i))(frame_ids)
   # K=4 independent draws per frame, same keys across input branches.
   def draws(key,p):
    keys=jax.random.split(key,4)
    return jax.vmap(lambda k:jax.nn.one_hot(jax.random.categorical(k,jnp.log(p),axis=-1),p.shape[-1]))(keys)
   z=jax.vmap(draws)(keys,probs)
   hh=jnp.repeat(h,4,axis=0);aa=jnp.repeat(act,4,axis=0)
   zz=z.reshape((-1,*z.shape[-2:]));out=pheads(self.params,hh,zz,aa,seed=0,create=False,modify=False)[1]
   return jax.tree.map(lambda x:x.reshape((len(h),4,*x.shape[1:])),out)
  self.sampled=jax.jit(sampled)
 def infer(self,cache,ids,images):
  jnp=self.jnp;obs={k[4:]:jnp.asarray(v[ids]) for k,v in cache.items() if k.startswith('obs_')};obs['image']=jnp.asarray(images)
  h,p=self.post(jnp.asarray(cache['prev_h'][ids]),jnp.asarray(cache['prev_z'][ids]),jnp.asarray(cache['prev_action'][ids]),obs)
  out=self.sampled(h,p,jnp.asarray(cache['action'][ids]),jnp.asarray(cache['frame_seed'][ids],dtype=jnp.uint32))
  return self.jax.device_get(dict(h=h,probs=p,**out))
