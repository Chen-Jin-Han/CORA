# RGB-only ACO–SMFA results

10 tasks; one adapter training seed; fixed supplied policy per task; 10 paired episodes per condition.
400 full control episodes verified. No masks, DMC-GB, OOD, extra seeds or automatic continuation.

|Task|Clean|Raw VDCS|ACO-RGB|SMFA-RGB|Paired difference [95% bootstrap CI]|
|---|---:|---:|---:|---:|---:|
|walker_walk|958.88 ± 8.98|363.16 ± 166.38|695.27 ± 108.21|814.43 ± 145.63|119.16 [-11.17, 240.63]|
|walker_run|728.38 ± 28.82|201.93 ± 41.39|288.20 ± 49.69|581.38 ± 111.40|293.18 [240.62, 350.01]|
|walker_stand|970.95 ± 28.65|799.14 ± 120.22|934.90 ± 69.59|959.43 ± 45.97|24.53 [-17.15, 75.69]|
|hopper_stand|838.00 ± 295.43|288.21 ± 122.69|580.91 ± 225.79|581.32 ± 241.51|0.42 [-84.74, 91.06]|
|quadruped_run|492.93 ± 77.16|482.04 ± 74.20|486.85 ± 41.58|434.62 ± 157.54|-52.23 [-164.06, 33.18]|
|finger_turn_hard|782.80 ± 305.41|409.50 ± 431.39|440.00 ± 464.27|576.10 ± 425.28|136.10 [-173.00, 457.90]|
|cartpole_swingup_sparse|829.30 ± 11.88|36.30 ± 29.34|431.60 ± 203.87|429.40 ± 195.71|-2.20 [-187.41, 179.90]|
|cup_catch|973.90 ± 8.69|791.60 ± 271.56|885.70 ± 138.75|962.50 ± 23.74|76.80 [7.30, 173.40]|
|reacher_easy|974.00 ± 16.05|958.30 ± 31.10|969.20 ± 20.60|972.20 ± 18.47|3.00 [0.50, 6.40]|
|reacher_hard|103.20 ± 300.63|76.30 ± 229.02|20.70 ± 49.08|5.30 ± 9.62|-15.40 [-48.30, 3.60]|
|Equal-task mean|765.23|440.65|573.33|631.67|—|

Intervals describe episode randomness conditional on these trained models, not training-seed uncertainty.

|Model|Parameters|PSNR-Y|SSIM-Y|PSNR-RGB|SSIM-RGB|
|---|---:|---:|---:|---:|---:|
|aco|2649181|24.6074|0.7975|21.3669|0.6439|
|smfa|182703|34.4333|0.9213|31.8937|0.8917|

## Measured efficiency (FP32 batch 1, 64x64)
|Model|Median ms|P95 ms|Peak allocated MiB|Conv/Linear MACs|
|---|---:|---:|---:|---:|
|aco|1.789|2.010|25.0|69822720|
|smfa|3.833|3.879|11.1|677652480|
MACs exclude non-Conv/Linear operations. GPU availability check is not exclusive reservation; shared-load timings may need repetition.

## Validation trend (no automatic extension)
- aco: late-window PSNR-Y change -0.0059 dB. Inspect curves.png before deciding convergence.
- smfa: late-window PSNR-Y change +0.4141 dB. Inspect curves.png before deciding convergence.

This is an RGB-only adaptation, not full ACO reproduction. 64x64, batch 128 differ from the paper.
Main results always use step 15000, never best_validation.pt.