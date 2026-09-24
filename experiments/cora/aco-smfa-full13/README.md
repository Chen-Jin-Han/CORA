# Full13 / seed6

Authorized protocol: ACO-RGB and SMFA-RGB from scratch, seed6, RGB64, batch128,
15000 updates, AdamW lr=1e-4 wd=1e-4, L1+0.05FFT. DreamerV3 is frozen.
Ten existing tasks. No mask, DrQ, actor-critic frame metrics or extra seeds.

All 13 types are now training-seen. ID7 operators/strengths and former OOD6
fallback_v1 strengths are preserved. This is not a zero-shot OOD experiment.
ACO still has 9 RGB experts; no architecture changes.

Data: 4500/500/1000 clean images per task, original episode-disjoint splits,
13 versions each: 585000 train / 65000 validation / 130000 test pairs. Source
clean arrays are read-only hardlinks. All large data resides under /data1.
Fixed dataset_seed=130600, unique corruption seeds by task/split/index.
13000-pair generation benchmark is reused in the first training shard.
Generate once with 4 processes; per-shard hashes and completion markers.
Balanced task/type sampling; 15k updates do not guarantee every pair is seen.
Fixed 5200 validation subset every500 steps; full65000 at final step. The
final full-validation point has a different scope and is labeled in history.
Formal evaluation uses last.pt at step15000, never best-validation selection.

Markov13: stay=.8, otherwise uniform other12. Original7 severity random walk
sigma=.02 bounded base+-10%. Added6 strength/pattern sampled on entering a
segment, fixed until switching; shot noise changes per frame. Single tests
never change type; original7 keep random walk, added6 keep per-episode pattern.
No simultaneous multi-type composition. Initial frame uses initial mode.

Control: 10 tasks x3 methods(raw/aco/smfa)x10 Markov episodes=300;
10x13x3x5 single episodes=1950; 10x5 clean=50. Total2300, each500 decisions
action_repeat2. CPU inference, 8 workers, 4 threads each; GPU0 used for EGL
rendering only. Same policy/env/corruption seeds across paired methods.
Do not pool overlapping Markov and single trials as independent samples.

Image metrics: PSNR-Y, SSIM-Y, PSNR-RGB, SSIM-RGB using existing uint8,
BT.601 and valid-window SSIM implementation. 130000 disturbed +10000 clean
inputs per model. Store per-image CSV, per-task/type summaries, raw metrics.

Execution: local `py -3.10 tests.py`; server Python
`/data1/CST/CORA/aco-smfa-pilot/env/bin/python -u supervisor.py`.
Supervisor single-owner flock, source manifest, 30s GPU polling. Each model
smoke->train->images on GPU with free>=8GiB ACO/12GiB SMFA and utilization<=60%
three consecutive samples; sharing allowed without stopping others. If only
one device qualifies, models run sequentially. Eight CPU control workers follow.
Failure is recorded and stops only this project's child process groups; restart
resumes checkpoints/completed episodes. Completed JSONL records are never rerun.
Outputs: status.json, logs/, generation_benchmark.json, data_audit.json,
checkpoints/, images/, control/, results.json, report.md, verification.json.

Keep original projects/data unchanged. Monitor existing experiments separately.
GPU-dependent smoke and real Dreamer/environment checks run on the server.
