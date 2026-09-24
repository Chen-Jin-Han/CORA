import json
from common import ROOT,save

def main():
 r=json.loads((ROOT/'results.json').read_text());lines=['# Shared-history diagnostic pilot','','walker_walk, seed6 ACO/SMFA; gaussian_noise and motion_blur. One clean trajectory, seed860000. First100 frames calibrate scales; last400 are evaluated. Four paired posterior samples/frame.','',
 'Actor symmetric KL is per-action-dimension and before environment clipping; value and next h errors use fixed clean calibration scales. Current h must be identical across inputs. Next h uses the same clean action. No claim of true value accuracy or population statistical significance.','','| Type | Metric | Raw | ACO | ACO reduction % | SMFA | SMFA reduction % |','|---|---|---:|---:|---:|---:|---:|']
 for kind,g in r['statistics'].items():
  for metric in g['raw']:
   lines.append(f"| {kind} | {metric} | {g['raw'][metric]['mean']:.6g} | {g['aco'][metric]['mean']:.6g} | {g['aco'][metric]['reduction_percent']} | {g['smfa'][metric]['mean']:.6g} | {g['smfa'][metric]['reduction_percent']} |")
 lines+=['','## Parallel benchmarks','','Steady-state diagnostic throughput only. Compilation/loading, restoration inference, collection and I/O are separate. Hardware maximum is not inferred from a bounded shared-server sweep.','']
 for platform in ['cpu','gpu']:
  p=ROOT/(platform+'_benchmark_results.json')
  if p.exists():
   b=json.loads(p.read_text())
   if platform=='gpu':
    checks=[json.loads(f.read_text()) for f in (ROOT/'benchmark').glob('gpu*/*.numerical.json')]
    b['cpu_equivalence_passed']=bool(checks) and all(x.get('equivalence_passed',x['cpu_gpu_max_deltas']['probs']<.01) for x in checks)
    if not b['cpu_equivalence_passed']:lines+=['GPU measurements are PERFORMANCE ONLY: CPU/GPU posterior differences exceeded the preset0.01 tolerance. Do not mix GPU metrics with the CPU formal results.','']
   for x in b['tested']:
    name=platform+('_batch'+str(x['batch']) if x['workers']==1 else '_workers'+str(x['workers']))
    folder=ROOT/'benchmark'/name
    if (folder/'go').exists() and all((folder/f'{i}.json').exists() for i in range(x['workers'])):
     elapsed=max((folder/f'{i}.json').stat().st_mtime for i in range(x['workers']))-(folder/'go').stat().st_mtime
     x['sum_individual_rates']=x['throughput'];x['wall_seconds']=elapsed
     x['throughput']=sum(d['positions'] for d in x['details'])/elapsed
   b['best']=max(b['tested'],key=lambda x:x['throughput']);b['throughput_definition']='total positions / wall time from shared go barrier to last completed result'
   save(p,b)
   lines+=['### '+platform,'',b['scope'],'','| Workers | Batch/frame positions | Positions/s |','|---:|---:|---:|']
   for x in b['tested']:lines.append(f"| {x['workers']} | {x['batch']} | {x['throughput']:.3f} |")
   lines+=['',f"Best: {b['best']['workers']} workers, batch {b['best']['batch']}; maximum successfully tested workers {b['max_tested_workers']}. Stop reason: {b['stop_reason']}",'']
  else:lines+=['GPU benchmark pending resource availability.','']
 (ROOT/'report.md').write_text('\n'.join(lines),encoding='utf8')
if __name__=='__main__':main()
