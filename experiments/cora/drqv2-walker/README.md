# walker_walk DrQ-v2: fixed 500,000 environment frames

One seed (0), 64x64 complete RGB, three-frame stack, action repeat 2,
batch 128, Adam 1e-4, gamma .99, nstep 1, hidden width 1024, feature 50.
Official algorithm revision: c0c650b76c6e5d22a7eb5f2edffd1440fe94f8ef.
Vendored drqv2.py and utils.py have only unused Hydra/OmegaConf imports removed.
The runner derives the encoder flattened size (32*25*25 for 64 pixels).
Critic/actor optimization, target update, random shifts and exploration are official.
Replay holds individual uint8 frames on disk and reconstructs episode-bounded stacks.
It samples uniformly over transitions; walker episodes have equal lengths.
Training uses clean observations only, and never uses ACO/SMFA or OOD data.

## Budget and evaluation

- 500,000 underlying environment steps = 250,000 action decisions.
- Random exploration for first 4,000 environment frames; update every two decisions.
- Expected 124,000 updates. No automatic extension or second seed.
- Validation every 50,000 frames, seeds 700000..700004, five episodes.
- Independent final acceptance seeds 800000..800009, ten episodes.
- Criterion: the last two validation means and final acceptance mean all >=900.
- Acceptance failure is a completed experiment, not a reason to auto-train further.
- Validation/acceptance are deterministic mean actions, never train on their data.
- These acceptance episodes are NOT the final held-out OOD test seeds.

## Paths and execution

Code: /home/gpuadmin/CST/CORA/drqv2-walker
Data: /data1/CST/CORA/drqv2-walker
Runtime: /data1/CST/CORA/aco-smfa-pilot/env/bin/python (existing, not modified).
`bash launch.sh` starts a detached queue protected by flock.
It checks every 30s. A GPU must have no compute processes, <=1024 MiB used,
and <=5% utilization for three consecutive checks. It never stops other jobs.
Once available it runs an isolated 2,000-frame GPU smoke test, then the fixed run.
The smoke uses a separate directory and does not contribute to the formal run.
Failures are reported and the supervisor exits; it never loops failed training.

Queue: queue-status.json, queue.log, smoke.log, train.log in the data root.
Run: walker_walk_seed0_b128_f500000_v1/{status.json,config.json,provenance.json,
train.jsonl,validation.jsonl,latest.pt,final.pt,report.json,replay/}.
No videos; replay ~3.1 GB (decimal), plus models/checkpoints.

## Checks and recovery

Local: `python tests.py`, `python -m py_compile runner.py wait_gpu.py`.
Remote CPU tests use the same command. GPU smoke occurs only after a free GPU.
Latest full checkpoint is saved at episode boundaries every 50k frames.
It includes all weights/optimizers/RNG, counters and replay logical lengths.
Replay is flushed before saving. On restart any later replay entries are ignored
and overwritten; the next training episode is regenerated from its explicit seed.
Diagnostic JSONL logs may include an interrupted attempt; use checkpoint counters
and report.json as authority (do not count duplicate frame rows twice).
Never resume on a different config; mismatch raises an error.
A successful final report prevents any retraining on repeated launches.

Load a trusted final.pt with torch.load(..., weights_only=False); use its config
to call runner.make_agent, then load each entry in weights. This stores encoder,
actor, critic and target critic, not just an actor export.
DrQ critic is Q(s,a), unlike the Dreamer state-value head; compare appropriately.

## Known protocol differences

Not an exact original-paper reproduction: 64 rather than 84 pixels, batch128
rather than walker512, 500k rather than 1.1M environment frames, sparse validation.
FP32; CuDNN benchmark enabled (seeded, not guaranteed bitwise across hardware).
Stop at fixed budget regardless of return. This is a one-seed pilot.
