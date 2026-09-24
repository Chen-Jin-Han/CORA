import argparse,os
p=argparse.ArgumentParser();p.add_argument('--model',required=True);p.add_argument('--task',required=True);p.add_argument('--mode',choices=['single','markov'],required=True);p.add_argument('--kind');p.add_argument('--cores',required=True);p.add_argument('--benchmark');p.add_argument('--index',type=int,default=0);a=p.parse_args()
cores=[int(i) for i in a.cores.split(',')];os.sched_setaffinity(0,set(cores));n=len(cores)
os.environ.update(CUDA_VISIBLE_DEVICES='',JAX_PLATFORMS='cpu',MUJOCO_GL='egl',MUJOCO_EGL_DEVICE_ID='0',OMP_NUM_THREADS=str(n),MKL_NUM_THREADS=str(n),OPENBLAS_NUM_THREADS=str(n),CORA_THREADS=str(n),XLA_PYTHON_CLIENT_PREALLOCATE='false')
from common import read_config,root,bind
c=read_config('config_'+a.model+'.json')
if a.benchmark:
 c['checkpoint_source']=str(root(c))
 c['experiment']='benchmark/'+a.benchmark+'/'+str(a.index)
 c['control_seed']=940000;c['single_episodes']=c['control_episodes']=1
bind(c)
from control import evaluate
evaluate(c,a.task,a.model,a.mode,a.kind)
