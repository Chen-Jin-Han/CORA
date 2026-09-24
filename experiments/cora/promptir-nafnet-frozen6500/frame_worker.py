import argparse,os
p=argparse.ArgumentParser();p.add_argument('--model',required=True);p.add_argument('--task',required=True);p.add_argument('--cores',required=True);a=p.parse_args()
cores=[int(x) for x in a.cores.split(',')];os.sched_setaffinity(0,set(cores));n=len(cores)
os.environ.update(CUDA_VISIBLE_DEVICES='',JAX_PLATFORMS='cpu',MUJOCO_GL='egl',MUJOCO_EGL_DEVICE_ID='0',OMP_NUM_THREADS=str(n),MKL_NUM_THREADS=str(n),OPENBLAS_NUM_THREADS=str(n),CORA_THREADS=str(n),XLA_PYTHON_CLIENT_PREALLOCATE='false')
from frame_eval import evaluate
evaluate(a.model,a.task)
