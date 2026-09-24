# ACO-RGB versus SMFA-RGB: seed1, L1 + FFT, six OOD families

Only seed1 is trained, 15000 updates per model, batch/microbatch128, AdamW1e-4,
weight_decay1e-4, AMP, 64x64 complete RGB. Architecture and seven-family ID dataset
are unchanged. Existing data/checkpoints of other experiments are never overwritten.
Loss = pixel mean L1 + .05 * mean L1 on stacked real/imag rfft2 (float32 FFT).
Log train_l1, train_fft, train_fft_weighted, train_total separately.
Use final step15000 for all evaluation, never select via OOD results.
There is no old/new-loss comparison, seed0 retraining, DrQ or actor-critic diagnostics.

## Frozen OOD fallback v1

ACO paper F.7 specifies six families, fixed type per episode, +-10% intensity jitter.
The public inspected code has defocus implementation but does not provide full
six-family OOD settings. These explicit fallback settings were authorized by user:

- Each episode draws u~Uniform(.9,1.1) ONCE, independent of image/model outputs.
- Defocus: ACO Gaussian kernel implementation, base intensity .5 times u.
- Frost: supplementary procedural blue-white texture, alpha .25*u modulated by
  seeded coarse noise and thin streaks. Fixed per episode; no external assets.
- Occlusion: black square, target area fraction .1*u, rounded integer side,
  uniformly sampled position, fixed per episode, no agent-aware targeting.
- Saturation: HSV S multiplied by 1-.5*u.
- Shadow: seeded oriented half-plane near image center, sigmoid edge width2px,
  brightness reduction .4*u, fixed per episode.
- Shot noise: independent Poisson draws each frame, effective levels60/u.

These are supplementary implementations/strengths, NOT exact ACO reproduction.
No strength tuning based on policy returns or which model wins.
Each image test pair uses a separate deterministic seed/strength; the control
evaluation retains one operator instance throughout each episode.

## Data and evaluation

Reuse /data1/CST/CORA/aco-smfa-rgb/rgb10_seed0_b128_s15000_ep10_v1/datasets
without changes: 4500 train+500 val+1000 test clean images per task, 10 tasks.
The original data audit reports natural exact-image duplicates across splits;
the new audit is preserved and no claim of zero pixel overlap is made.
ID test70000 pairs + clean10000; OOD test60000 pairs per model.
PSNR/SSIM-Y and RGB use unchanged metrics.py. CSV keeps per-image metrics/seeds.
Control: frozen existing Dreamer checkpoints, 10 tasks * 6 OOD * 3 conditions *
5 episodes =900; fresh Clean 10*5=50. Total950. Same environment/policy/corruption
seeds across conditions; full episodes required. Dreamer action sampling unchanged.
Report episode mean/sample SD, all raw returns, paired differences and exploratory
bootstrap CI (5 paired episodes, not training-seed uncertainty; no multiplicity claim).

## Execution, monitoring and recovery

Code /home/gpuadmin/CST/CORA/aco-smfa-ood.
Outputs /data1/CST/CORA/aco-smfa-ood/rgb10_seed1_fft_b128_s15000_ood_ep5_v1.
Runtime /data1/CST/CORA/aco-smfa-pilot/env/bin/python, reused without modification.
`bash launch.sh` detaches a locked supervisor. First preflight policies and audit
all data checksums, then wait every30s for GPU with no compute processes, memory
<=1024MiB and utilization<=5% three times. Shares the existing DrQ reservation
lock so these two queued experiments cannot intentionally claim the same GPU.
Run full-batch CUDA loss smoke, then train/evaluate ACO and SMFA sequentially.
After GPU work release reservation, run two CPU Dreamer control workers (EGL rendering).
All checkpoints/replay/data/cache/logs are on /data1. No auto extra seeds/steps.

Read status.json, logs/, stages/, checkpoints/*/history.json, results.json, REPORT.md.
Launch repeats cannot create concurrent supervisors. Resume requires identical
source/config, completed stages skipped, controls resume per completed episode.
Failures stop children and write failed status; inspect/fix locally before rerun.
Local checks: `python test_ood.py` and `python -m compileall -q .`.
Output CSVs/panels and report are newly produced; do not use first-round report.py.
Use supervisor.py / run_ood.py for this protocol. Legacy pipeline.py is unused.
