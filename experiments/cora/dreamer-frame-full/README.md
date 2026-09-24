# Formal shared-history experiment

Frozen DreamerV3, 10 tasks, restoration seeds 6/7/8. No training. 13 fixed-type temporal perturbation protocols plus Markov switching, five clean evaluation trajectories of 500 decisions per task. Two disjoint calibration trajectories per task. Every branch receives the same clean previous latent state/action; only the Clean policy advances the simulator. Four shared categorical draws per frame.

Metrics: symmetric KL between the underlying Normal actor distributions averaged over action dimensions and posterior draws; decoded value absolute deviation divided by task calibration value standard deviation; posterior categorical JS averaged over latent factors; next deterministic state RMSE divided by calibration current-state RMS standard deviation. Next-state comparisons use the same Clean action. Raw-relative error reduction is computed after averaging, with zero denominators undefined. Normal KL describes the pre-clipping distribution, not the clipped executed action distribution.

CPU only due to pilot CPU/GPU numerical mismatch. Up to 16 workers, four affinity-pinned logical CPUs each, batch64. Collection/calibration have ten independent task jobs; restoration has 60; evaluation has 50. Checkpoint load, clean replay, batch-order and shared-history checks must pass. A failure stops the supervisor and its own workers. Restart resumes only completed jobs; partial files are never treated as complete. Do not start a second supervisor.

Numerical audit correction: physical diagnostic batches are always 64, padding short chunks with repeated indices and discarding padding outputs. Common random keys remain tied to original frame indices. The audit tests logical chunking/order consistency under this fixed physical shape, not equivalence of different physical batch sizes. An initial Hopper audit found next-h rounding delta 0.00048828125 between physical batch4 and batch64; thresholds were not relaxed. Completed restoration inputs are reused.

Server code: /home/gpuadmin/CST/CORA/dreamer-frame-full
Outputs: /data1/CST/CORA/dreamer-frame-full/seed678_id13_shared_history_v1
Environment: /data1/CST/CORA/aco-smfa-pilot/env/bin/python
Run supervisor.py from code directory. Logs, status.json, completion markers, results.json and REPORT.md live in the output directory. Expected 70 trajectories, 60 restored input arrays (2.1M images), 50 metric files, 350k protocol-frame positions and 2.45M method-frame records. Raw/Clean are shared across restoration seeds, not independent seed replicates. Three restoration-seed SDs do not quantify policy-training uncertainty.
