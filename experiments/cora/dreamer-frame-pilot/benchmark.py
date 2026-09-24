import os,sys,json,time,subprocess
from pathlib import Path
from common import ROOT,save

def mem_available():
 return int(next(l.split()[1] for l in Path('/proc/meminfo').read_text().splitlines() if l.startswith('MemAvailable:')))/1024**2
def main():
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument('--platform',default='cpu');parser.add_argument('--gpu',default='');args=parser.parse_args()
 platform=args.platform
 cpus=sorted(os.sched_getaffinity(0));results=[]
 prefix=platform+'_'
 def run(n,b,tag):
  folder=ROOT/'benchmark'/tag;folder.mkdir(parents=True,exist_ok=True)
  # Resume completed measurements; incomplete groups use a new time-stamped tag.
  if all((folder/f'{i}.json').exists() for i in range(n)):return [json.loads((folder/f'{i}.json').read_text()) for i in range(n)]
  if any(folder.iterdir()):return run(n,b,tag+'_'+str(int(time.time())))
  children=[]
  try:
   for i in range(n):
    f=(folder/f'{i}.log').open('w');cores=cpus[i*4:(i+1)*4]
    env=dict(os.environ,CUDA_VISIBLE_DEVICES=args.gpu if platform=='gpu' else '',OMP_NUM_THREADS='4',OPENBLAS_NUM_THREADS='4',MKL_NUM_THREADS='4')
    p=subprocess.Popen([sys.executable,'-u','bench_worker.py','--group',tag,'--id',str(i),'--batch',str(b),'--platform',platform,'--cores',','.join(map(str,cores))],stdout=f,stderr=subprocess.STDOUT,env=env);children.append((p,f))
   deadline=time.time()+600
   while not all((folder/f'{i}.ready.json').exists() for i in range(n)):
    assert all(p.poll() is None for p,f in children),'worker failed during warmup'
    assert time.time()<deadline,'warmup timeout'
    assert mem_available()>24,'RAM safety threshold reached'
    if platform=='gpu':
     free=int(subprocess.check_output(['nvidia-smi','-i',args.gpu,'--query-gpu=memory.free','--format=csv,noheader,nounits'],text=True).strip())
     assert free>2048,'GPU memory reserve reached'
    time.sleep(1)
   (folder/'go').touch()
   for p,f in children:assert p.wait(timeout=180)==0,'worker failed during measurement'
   return [json.loads((folder/f'{i}.json').read_text()) for i in range(n)]
  finally:
   for p,f in children:
    if p.poll() is None:p.terminate()
   for p,f in children:
    if p.poll() is None:
     try:p.wait(timeout=20)
     except subprocess.TimeoutExpired:p.kill();p.wait()
    f.close()
 def record(n,b,tag):
  values=run(n,b,prefix+tag);speed=sum(v['positions_per_second'] for v in values)
  result=dict(workers=n,batch=b,throughput=speed,details=values);results.append(result);save(ROOT/(prefix+'benchmark_progress.json'),results);print(result,flush=True);return speed
 batches=[1,4,16,32,64] if platform=='cpu' else [1,4,16,32,64,128]
 stop='configured resource ceiling reached'
 for b in batches:
  try:record(1,b,'batch'+str(b))
  except Exception as e:stop='batch limit: '+repr(e);break
 assert results,'No benchmark configuration succeeded'
 bestbatch=max(results,key=lambda x:x['throughput'])['batch']
 maxworkers=min(16 if platform=='cpu' else 8,len(cpus)//4)
 for n in [2,4,8,12,16]:
  if n>maxworkers:break
  if mem_available()<32+n*2:stop='insufficient memory reserve for next concurrency level';break
  try:record(n,bestbatch,'workers'+str(n))
  except Exception as e:stop=repr(e);break
 best=max(results,key=lambda x:x['throughput'])
 save(ROOT/(prefix+'benchmark_results.json'),dict(platform=platform,gpu=args.gpu,best=best,tested=results,max_tested_workers=max(x['workers'] for x in results),stop_reason=stop,scope='This checkpoint/task and current shared server load; steady-state excludes compilation, loading and restoration inference. Not a universal hardware maximum.'))
if __name__=='__main__':main()
