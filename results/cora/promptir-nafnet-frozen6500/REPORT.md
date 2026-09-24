# PromptIR and NAFNet baselines, seed6 · frozen checkpoint

PromptIR was stopped by user request at 6500 updates; NAFNet, ACO and CORA use 15000 updates. Comparisons are therefore not compute-matched. One adapter seed per new model. All 13 perturbation types occurred in training; no OOD claim. ACO/CORA/Raw values are reused from seed6 results. Fixed-type return averages 650 episodes per new adapter; Markov averages 100. Image metrics use 130000 test pairs per adapter. All values below are single-seed, with no seed SD.

## Table 1 · Fixed-type control return

| Controller | Adapter | Mean return ↑ |
|---|---|---:|
| DreamerV3 | Raw | 460.57 |
| DreamerV3 | ACO | 316.72 |
| DreamerV3 | CORA | 641.44 |
| DreamerV3 | promptir | 721.56 |
| DreamerV3 | nafnet | 718.38 |

## Table 2 · Markov-switching return

| Controller | Adapter | Mean return ↑ |
|---|---|---:|
| DreamerV3 | Raw | 483.41 |
| DreamerV3 | ACO | 319.03 |
| DreamerV3 | CORA | 640.65 |
| DreamerV3 | promptir | 746.12 |
| DreamerV3 | nafnet | 750.36 |

## Table 3 · Restoration quality

| Method | Params (M) | PSNR-Y ↑ | SSIM-Y ↑ | PSNR-RGB ↑ | SSIM-RGB ↑ |
|---|---:|---:|---:|---:|---:|
| Raw | — | 23.96 | 0.7480 | 21.42 | 0.6688 |
| ACO | 2.649 | 23.30 | 0.7670 | 19.67 | 0.6416 |
| CORA | 0.183 | 34.69 | 0.9293 | 32.26 | 0.9042 |
| promptir | 35.592 | 44.68 | 0.9902 | 42.16 | 0.9857 |
| nafnet | 17.112 | 43.48 | 0.9856 | 40.49 | 0.9785 |

## Table 4 · Fixed-history Markov diagnostics

| Method | Posterior JS ↓ | Next-h NRMSE ↓ | Value NMAE ↓ | Actor KL ↓ |
|---|---:|---:|---:|---:|
| Raw | 0.2226 | 0.2010 | 0.1340 | 0.2386 |
| ACO | 0.2803 | 0.2354 | 0.1712 | 0.3184 |
| CORA | 0.0782 | 0.1048 | 0.0879 | 0.1020 |
| promptir | 0.0114 | 0.0418 | 0.0478 | 0.0308 |
| nafnet | 0.0160 | 0.0484 | 0.0544 | 0.0347 |

## Table 5 · Per-task fixed-type return

Each task averages its thirteen fixed corruption types equally (65 complete episodes per method). All entries below are seed6 means only.

| Task | Raw | ACO | CORA | promptir | nafnet |
|---|---:|---:|---:|---:|---:|
| walker_walk | 624.6 | 314.4 | 873.5 | 952.0 | 937.9 |
| walker_run | 328.3 | 149.0 | 625.4 | 716.8 | 705.7 |
| walker_stand | 842.4 | 691.8 | 962.0 | 967.4 | 966.4 |
| hopper_stand | 397.4 | 161.7 | 578.5 | 698.3 | 669.6 |
| quadruped_run | 441.9 | 348.8 | 473.7 | 495.6 | 501.1 |
| finger_turn_hard | 422.0 | 241.8 | 495.6 | 627.0 | 689.8 |
| cartpole_swingup_sparse | 152.2 | 122.7 | 593.1 | 820.1 | 800.4 |
| cup_catch | 623.9 | 660.2 | 913.2 | 977.4 | 977.2 |
| reacher_easy | 758.9 | 464.3 | 891.0 | 952.2 | 927.4 |
| reacher_hard | 14.1 | 12.4 | 8.4 | 8.9 | 8.3 |
| Mean | 460.6 | 316.7 | 641.4 | 721.6 | 718.4 |

## Table 6 · Per-type fixed-type return

Each corruption averages ten tasks equally (50 complete episodes per method). All entries below are seed6 means only.

| Corruption | Raw | ACO | CORA | promptir | nafnet |
|---|---:|---:|---:|---:|---:|
| rain | 519.1 | 279.3 | 722.0 | 733.2 | 734.9 |
| fog | 568.6 | 329.0 | 732.8 | 730.1 | 745.3 |
| snow | 98.9 | 231.0 | 714.5 | 729.4 | 740.0 |
| motion_blur | 365.1 | 499.6 | 349.1 | 716.8 | 703.8 |
| gaussian_noise | 649.2 | 130.1 | 745.6 | 736.6 | 753.3 |
| low_light | 105.8 | 88.9 | 694.9 | 743.9 | 722.0 |
| jpeg | 646.2 | 188.0 | 605.3 | 719.0 | 713.1 |
| defocus_blur | 356.6 | 615.3 | 434.3 | 713.9 | 716.0 |
| frost | 627.3 | 335.7 | 739.0 | 743.1 | 747.5 |
| occlusion_patch | 337.1 | 483.4 | 490.6 | 629.0 | 567.2 |
| saturation | 638.0 | 277.8 | 730.3 | 744.7 | 744.5 |
| shadow | 561.9 | 566.7 | 660.5 | 717.0 | 739.8 |
| shot_noise | 513.8 | 92.5 | 719.9 | 723.4 | 711.7 |

Fixed-history metrics reuse the completed clean trajectories and calibration scales, but the new adapters are evaluated on their own restored Markov observations. The reused ACO/CORA/Raw diagnostic values are seed6 only. Complete per-episode, per-task, and benchmark timing data are in results.json and parallelism.json.