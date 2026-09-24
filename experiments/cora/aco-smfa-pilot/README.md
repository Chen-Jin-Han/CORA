# ACO–SMFA pilot

This is an exploratory comparison, not an exact reproduction of ACO's training protocol.
The frozen policies were supplied as JAX checkpoints, with 64×64 full RGB inputs.
Their original General-WM source and foreground-training provenance are unavailable.

## Checkpoint validation

`audit_checkpoints.py` uses a restricted NumPy unpickler and records hashes.
`dreamer_bridge.make_agent` constructs public DreamerV3 using the supplied architecture
and compute dtype, strictly checks every key/shape/dtype, loads the complete state,
and reads it back to confirm exact equality. JAX execution settings disable training
precompilation and memory preallocation. No Dreamer training is performed.
The public policy samples actions in `eval` mode; paired conditions reset the policy
RNG action counter to the same episode-specific value.

## Planned experiments

- Three tasks: walker_walk, walker_run, finger_turn_hard, supplied seed0 policies.
- P0: clean RGB, clean foreground oracle, seven-mode Markov corruption; 10 full episodes each.
- Data: 2000/300/500 clean frames per task, disjoint train/validation/test episode seeds;
  alternating frozen-policy/random trajectories, stride 5. Seven corruptions per frame.
- ACO: local reproduction snapshot, base9, 9 experts, soft training/top1 evaluation.
- SMFA: official FMB modules, dim36, 8 blocks; scale1 RGB residual and 2-class mask heads.
- Both adapters: 10,000 updates, effective batch64, AdamW 1e-4, weight decay1e-4,
  equally weighted RGB L1, segmentation CE, foreground L1. One adapter seed.
- P2: restored RGB and soft foreground composition (paper Algorithm 3) for each adapter,
  10 full episodes/task/condition. Hard masks remain available as an optional ablation.
- Metrics: per-episode undiscounted return; RGB PSNR/SSIM, foreground L1, mask IoU,
  parameter counts, adapter latency and bridge latency. Image metrics are supplementary,
  not claimed as metrics explicitly reported by ACO. Foreground results require the P0
  compatibility diagnostic; severe oracle degradation indicates input distribution shift.

Pixel metrics use [0,1] full RGB without crop. Foreground targets use ACO's non-world
geom-body rule plus target/tip sites. This correction is necessary because finger's
target is a site attached to the world body. It is applied identically to both adapters;
rendered masks must be visually checked for task target coverage.
Checkpoint integrity does not prove the original environment implementation is identical.

## Execution and storage

Code: `/home/gpuadmin/CST/CORA/aco-smfa-pilot`.
All data, env, caches, archives and outputs: `/data1/CST/CORA/aco-smfa-pilot`.
`run_smoke.sh` runs 5-step CPU policy checks; these returns are not full-episode scores.
`run_pipeline.py` holds an exclusive lock, runs CPU policy evaluation/data collection,
then waits for a practically idle GPU for adapter training and comparison. It runs stages
sequentially and stops on any failed stage. Completion markers support stage resumption.
Training resume preserves model/optimizer/scaler/step, but is not bitwise exact across
prefetched augmented minibatches. Do not change stage commands under existing markers.

Local validation: `../aco-moe-code/.venv/Scripts/python.exe test_local.py`.
Source snapshots and SHA256 provenance: `source_manifest.json`.
License for imported SMFA modules: `vendor/SMFANet/LICENSE.txt`.
