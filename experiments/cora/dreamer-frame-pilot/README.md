# Shared-history diagnostic pilot

walker_walk, seed6 ACO/SMFA, gaussian_noise and motion_blur, one500-decision
clean reference trajectory (seed860000). First100 frames calibration only;
last400 formal evaluation. Preserve all500 frame metrics with split labels.
No training/new policy checkpoints. Four common-random posterior draws/frame.
All histories/actions shared; only clean trajectory updates history. Current h
is an invariant. Next h uses actual clean policy output action for every branch.
Frozen full Dreamer params include val and valnorm; Ninjax create/modify=False.
Actor symmetric KL compares pre-clipping Normal distributions per action dim;
value MAE divided by calibration clean value std; posterior JS averaged over
categorical factors after unimix; next-h RMSE divided by clean h RMS std.
Relative Raw error reduction is calculated after frame aggregation.

CPU sweep batches1/4/16/32/64 then workers2/4/8/12/16, bounded by CPU affinity
(4cores/worker) and RAM reserve. GPU waits>=12000MiB free and util<=60% three
30s polls; then batches1/4/16/32/64/128, workers2/4/8 with2GiB GPU reserve.
Each measurement follows model loading/JIT warmup and a shared start barrier,
lasts>=15s, and synchronizes outputs to host. Tests include clean self zero,
history invariant, batch numerical differences and branch/order determinism.
The maximum successfully tested concurrency and throughput optimum differ.
Shared-machine sweep does not prove a universal device hardware maximum.
Stop only own children on error, preserve logs. Source developed locally first.

Output /data1/CST/CORA/dreamer-frame-pilot/walker_seed6_two_v1. Run server Python
/data1/CST/CORA/aco-smfa-pilot/env/bin/python -u supervisor.py from project dir.
CPU pilot runs immediately; GPU sweep may queue behind existing workloads.
