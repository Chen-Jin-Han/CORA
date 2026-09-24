# Full13 seeds7–8

Same seed6 protocol, except restoration training seed/output directory. Shared
585000/65000/130000 pairs read-only; no generation or source-data writes.
Each seed: ACO+SMFA from scratch, 15000 steps batch128 L1+0.05FFT; full images
130000 disturbed +10000 clean per model. Markov10 and single13x5 episodes per
task/model: 1500 newly evaluated episodes per seed, 3000 total.
800 Raw/Clean seed6 episodes are verified/copied with provenance, never treated
as independent new trials. Per-seed reports still contain2300 rows including
shared baseline. All13 perturbations training-seen, not OOD.

Launch `python -u launch_all.py` from this directory. GPU phases seed7 then8,
each ACO/SMFA independently schedules on relatively idle GPUs; same thresholds
and CUDA batch128 smoke as seed6. GPU work may overlap seed6 CPU evaluation.
After both GPU phases wait for seed6 verification, then control seed7 followed
by seed8, keeping8 workers total, 4threads/worker. No old tasks are stopped.
Checkpoint/stage resume, single-owner locks, source hashes; failed state logged.
Output root /data1/CST/CORA/aco-smfa-full13-seed78; per-seed subdirectories.
Final aggregate report distinguishes episode SD from training-seed SD across6–8.
