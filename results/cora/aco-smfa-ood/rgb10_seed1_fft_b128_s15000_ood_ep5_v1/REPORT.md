# ACO-RGB / SMFA-RGB: seed 1, L1 + 0.05 FFT

Fixed 15000 updates. Six OOD families, 5 episodes per task/condition. No DrQ or framewise actor-critic evaluation.

OOD: supplementary fallback strengths and five supplementary operators; defocus reuses ACO kernel. Not an exact replication of ACO F.7.

| Task | OOD | Raw | ACO | SMFA | SMFA-ACO |
|---|---|---:|---:|---:|---:|
| walker_walk | defocus_blur | 421.07 | 910.77 | 896.13 | -14.64 |
| walker_walk | frost | 826.03 | 796.08 | 959.43 | 163.35 |
| walker_walk | occlusion_patch | 285.41 | 248.52 | 228.35 | -20.17 |
| walker_walk | saturation | 900.94 | 263.99 | 761.97 | 497.98 |
| walker_walk | shadow | 569.42 | 681.07 | 595.00 | -86.07 |
| walker_walk | shot_noise | 808.64 | 934.33 | 961.32 | 26.99 |
| walker_run | defocus_blur | 269.49 | 496.58 | 401.49 | -95.09 |
| walker_run | frost | 340.26 | 305.99 | 648.97 | 342.99 |
| walker_run | occlusion_patch | 260.56 | 186.66 | 220.07 | 33.42 |
| walker_run | saturation | 669.54 | 188.01 | 436.58 | 248.57 |
| walker_run | shadow | 340.93 | 281.11 | 385.18 | 104.07 |
| walker_run | shot_noise | 265.34 | 570.08 | 738.03 | 167.94 |
| walker_stand | defocus_blur | 867.85 | 948.63 | 939.85 | -8.78 |
| walker_stand | frost | 953.68 | 948.70 | 956.53 | 7.83 |
| walker_stand | occlusion_patch | 932.16 | 943.64 | 936.90 | -6.74 |
| walker_stand | saturation | 956.54 | 858.83 | 967.51 | 108.68 |
| walker_stand | shadow | 956.17 | 969.31 | 932.93 | -36.38 |
| walker_stand | shot_noise | 964.12 | 969.84 | 966.52 | -3.32 |
| hopper_stand | defocus_blur | 67.61 | 181.60 | 99.13 | -82.47 |
| hopper_stand | frost | 701.50 | 595.28 | 710.41 | 115.13 |
| hopper_stand | occlusion_patch | 308.21 | 33.02 | 228.42 | 195.41 |
| hopper_stand | saturation | 696.54 | 176.16 | 716.10 | 539.94 |
| hopper_stand | shadow | 440.38 | 533.68 | 462.47 | -71.20 |
| hopper_stand | shot_noise | 682.86 | 670.91 | 705.96 | 35.05 |
| quadruped_run | defocus_blur | 519.58 | 475.13 | 411.21 | -63.92 |
| quadruped_run | frost | 483.79 | 496.50 | 446.58 | -49.93 |
| quadruped_run | occlusion_patch | 515.56 | 508.31 | 462.33 | -45.98 |
| quadruped_run | saturation | 395.21 | 173.50 | 213.25 | 39.74 |
| quadruped_run | shadow | 342.89 | 386.10 | 426.96 | 40.86 |
| quadruped_run | shot_noise | 501.79 | 521.36 | 520.12 | -1.25 |
| finger_turn_hard | defocus_blur | 72.20 | 315.40 | 193.00 | -122.40 |
| finger_turn_hard | frost | 910.60 | 514.80 | 572.20 | 57.40 |
| finger_turn_hard | occlusion_patch | 369.40 | 185.40 | 373.80 | 188.40 |
| finger_turn_hard | saturation | 367.80 | 185.60 | 563.00 | 377.40 |
| finger_turn_hard | shadow | 92.80 | 90.80 | 216.60 | 125.80 |
| finger_turn_hard | shot_noise | 557.80 | 157.80 | 374.20 | 216.40 |
| cartpole_swingup_sparse | defocus_blur | 14.80 | 40.60 | 0.00 | -40.60 |
| cartpole_swingup_sparse | frost | 157.60 | 739.60 | 828.80 | 89.20 |
| cartpole_swingup_sparse | occlusion_patch | 316.80 | 26.00 | 334.20 | 308.20 |
| cartpole_swingup_sparse | saturation | 374.60 | 58.60 | 717.60 | 659.00 |
| cartpole_swingup_sparse | shadow | 507.00 | 322.60 | 503.80 | 181.20 |
| cartpole_swingup_sparse | shot_noise | 30.80 | 0.00 | 809.60 | 809.60 |
| cup_catch | defocus_blur | 571.40 | 974.20 | 194.60 | -779.60 |
| cup_catch | frost | 977.80 | 975.20 | 977.00 | 1.80 |
| cup_catch | occlusion_patch | 259.60 | 32.20 | 330.00 | 297.80 |
| cup_catch | saturation | 938.80 | 567.00 | 967.00 | 400.00 |
| cup_catch | shadow | 971.40 | 957.80 | 965.80 | 8.00 |
| cup_catch | shot_noise | 489.00 | 362.40 | 977.20 | 614.80 |
| reacher_easy | defocus_blur | 674.40 | 973.80 | 787.80 | -186.00 |
| reacher_easy | frost | 982.00 | 982.40 | 982.40 | 0.00 |
| reacher_easy | occlusion_patch | 417.20 | 780.40 | 715.60 | -64.80 |
| reacher_easy | saturation | 982.00 | 233.60 | 982.20 | 748.60 |
| reacher_easy | shadow | 982.20 | 981.60 | 981.80 | 0.20 |
| reacher_easy | shot_noise | 981.80 | 982.00 | 982.00 | 0.00 |
| reacher_hard | defocus_blur | 104.40 | 1.60 | 4.60 | 3.00 |
| reacher_hard | frost | 7.00 | 11.00 | 7.60 | -3.40 |
| reacher_hard | occlusion_patch | 0.80 | 1.20 | 1.20 | 0.00 |
| reacher_hard | saturation | 7.80 | 0.60 | 8.40 | 7.80 |
| reacher_hard | shadow | 9.40 | 2.40 | 9.40 | 7.00 |
| reacher_hard | shot_noise | 7.60 | 7.40 | 6.40 | -1.00 |
