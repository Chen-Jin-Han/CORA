# Shared-history diagnostic pilot

walker_walk, seed6 ACO/SMFA; gaussian_noise and motion_blur. One clean trajectory, seed860000. First100 frames calibrate scales; last400 are evaluated. Four paired posterior samples/frame.

Actor symmetric KL is per-action-dimension and before environment clipping; value and next h errors use fixed clean calibration scales. Current h must be identical across inputs. Next h uses the same clean action. No claim of true value accuracy or population statistical significance.

| Type | Metric | Raw | ACO | ACO reduction % | SMFA | SMFA reduction % |
|---|---|---:|---:|---:|---:|---:|
| gaussian_noise | actor_symmetric_kl | 0.207441 | 0.419483 | -102.21798086943542 | 0.0456788 | 77.97984154785026 |
| gaussian_noise | value_normalized_mae | 0.0208601 | 0.0258795 | -24.062182008195595 | 0.0161359 | 22.64714191778904 |
| gaussian_noise | posterior_js | 0.168094 | 0.428654 | -155.0080139589693 | 0.0235616 | 85.98310843983376 |
| gaussian_noise | hnext_normalized_rmse | 0.161815 | 0.291729 | -80.28543963023182 | 0.0690543 | 57.3251751524077 |
| motion_blur | actor_symmetric_kl | 0.355242 | 0.331196 | 6.768941673303155 | 0.312254 | 12.10093317818178 |
| motion_blur | value_normalized_mae | 0.0216035 | 0.0210133 | 2.732163876204097 | 0.0203215 | 5.934508078586581 |
| motion_blur | posterior_js | 0.314854 | 0.23687 | 24.768103019734347 | 0.283731 | 9.88464228954623 |
| motion_blur | hnext_normalized_rmse | 0.245962 | 0.205636 | 16.395175491989395 | 0.231304 | 5.95923442870283 |

## Parallel benchmarks

Steady-state diagnostic throughput only. Compilation/loading, restoration inference, collection and I/O are separate. Hardware maximum is not inferred from a bounded shared-server sweep.

### cpu

This checkpoint/task and current shared server load; steady-state excludes compilation, loading and restoration inference. Not a universal hardware maximum.

| Workers | Batch/frame positions | Positions/s |
|---:|---:|---:|
| 1 | 1 | 17.201 |
| 1 | 4 | 35.905 |
| 1 | 16 | 51.390 |
| 1 | 32 | 58.611 |
| 1 | 64 | 60.295 |
| 2 | 64 | 120.054 |
| 4 | 64 | 240.785 |
| 8 | 64 | 476.861 |
| 12 | 64 | 594.140 |
| 16 | 64 | 784.634 |

Best: 16 workers, batch 64; maximum successfully tested workers 16. Stop reason: configured resource ceiling reached

GPU measurements are PERFORMANCE ONLY: CPU/GPU posterior differences exceeded the preset0.01 tolerance. Do not mix GPU metrics with the CPU formal results.

### gpu

This checkpoint/task and current shared server load; steady-state excludes compilation, loading and restoration inference. Not a universal hardware maximum.

| Workers | Batch/frame positions | Positions/s |
|---:|---:|---:|
| 1 | 1 | 54.793 |
| 1 | 4 | 211.403 |
| 1 | 16 | 817.676 |
| 1 | 32 | 1521.877 |
| 1 | 64 | 2627.151 |
| 1 | 128 | 4218.165 |
| 2 | 128 | 8015.309 |
| 4 | 128 | 15302.694 |
| 8 | 128 | 21159.839 |

Best: 8 workers, batch 128; maximum successfully tested workers 8. Stop reason: configured resource ceiling reached
