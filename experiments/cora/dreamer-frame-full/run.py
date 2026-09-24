import argparse,os
p=argparse.ArgumentParser();p.add_argument('stage');p.add_argument('--task');p.add_argument('--method');p.add_argument('--episode',type=int);p.add_argument('--cores');a=p.parse_args()
if a.cores:os.sched_setaffinity(0,{int(x) for x in a.cores.split(',')})
os.environ.update(CUDA_VISIBLE_DEVICES='',JAX_PLATFORMS='cpu',OMP_NUM_THREADS='4',OPENBLAS_NUM_THREADS='4',MKL_NUM_THREADS='4',MUJOCO_GL='egl')
if a.stage=='collect':
 from collect import collect
 collect(a.task)
elif a.stage=='corrupt':
 from prepare import corrupt_task
 corrupt_task(a.task)
elif a.stage=='restore':
 from prepare import restore_task
 restore_task(a.task,a.method)
elif a.stage=='calibrate':
 from evaluate import calibrate
 calibrate(a.task)
elif a.stage=='evaluate':
 from evaluate import evaluate
 evaluate(a.task,a.episode)
elif a.stage=='report':
 from report import report
 report()
else:raise ValueError(a.stage)
