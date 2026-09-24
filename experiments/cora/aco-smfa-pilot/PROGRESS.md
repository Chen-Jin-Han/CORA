# Progress — 2026-09-18

## Verified

- Public DreamerV3 source pinned to e3f02248693a79dc8b0ebd62c93683888ddaccfe.
- Three supplied seed0 checkpoints safely parsed; each has 294 parameter/state leaves.
- walker_walk fully instantiated from supplied config using public JAX implementation:
  strict key/shape/dtype match and exact readback equality for all 294 leaves.
  Initialization and restoration took 7.29 seconds on remote CPU.
- Five-step clean/oracle-foreground/VDCS inference completed. These are smoke checks,
  not full-episode scores. Warm CPU inference+environment stepping around 40 ms/step.
- Subsequently all three tasks passed strict loading and three-condition smoke checks.
- Live supervisor PID 3232107, child P0 evaluator initially PID 3232108, verified running.
  Full walker_walk clean returns for seeds 40000–40003: 964.8438, 959.1670, 952.5289,
  930.1390. Each completed 500 decision steps (action repeat2), about 14–17 seconds.
  These four episodes are an incomplete subset, not the final ten-episode mean.
- Local adapter forward/backward, finite gradients, shape and background checks passed.
  ACO: 4,884,961 parameters; SMFA: 183,353 parameters.
- Remote environment installed; CUDA JAX plugin installed for later GPU stages.
- Simulator mask panels rendered and visually inspected. Finger target/tip sites retained:
  23 visible site pixels in the inspected example, all 23 retained.

## Important protocol decisions

- YAML loaded with ruamel (same parser family as public Dreamer); PyYAML interpreted
  scientific notation such as 1e-08 as text and caused the first initialization failure.
- Finger target is a world-body SITE, so geom-only masks would erase the target. Both
  adapters share the corrected target-preserving mask definition.
- Main foreground P2 uses soft mask composition, matching ACO Algorithm 3. Hard masks
  remain optional ablations. This corrects the earlier preliminary plan's hard-mask default.
- Both adapters use bounded tanh RGB residuals and synchronized horizontal flips.
- Existing policies are 64×64 JAX size12m configurations, not the paper's 84×84 policy.
  Results establish a controlled replacement experiment; they do not reproduce paper numbers.

## Remaining

- Full P0: 90 complete episodes over three tasks and three conditions.
- Dataset: 8,400 clean frames, split by episode before corruption.
- Two adapter runs: 10,000 updates each; image evaluation and 120 P2 episodes.
- Four GPUs were busy at last check. CPU P0/data stages proceed first, then training
  waits for a GPU with <2 GB used and <15% utilization. No other user's job is stopped.
- Current-thread heartbeat runs every 30 minutes. It must inspect live process state,
  logs and artifacts, and stop when the complete experiment and report are delivered.

## Where to inspect

- Remote code: /home/gpuadmin/CST/CORA/aco-smfa-pilot
- Remote outputs: /data1/CST/CORA/aco-smfa-pilot/outputs
- Supervisor: supervisor.log, pipeline_status.json, per-stage logs and completion markers.
- After all stages finish, run summarize_results.py. It requires all 210 full episodes,
  10,000 adapter updates and expected held-out image counts before producing REPORT.md.
- Local evidence: outputs/walker_walk_checkpoint_load.json, outputs/mask_qa.png,
  outputs/local_checkpoint_audit.json.

Do not start another supervisor merely because an SSH observation times out.
Check the existing PID and child process state first. Pipeline stages stop on errors.
