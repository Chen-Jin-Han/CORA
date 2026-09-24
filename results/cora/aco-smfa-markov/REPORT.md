# Three-seed ID Markov control report

Seven ID types switch within each episode; stay probability 0.8. No OOD. Each model training seed has 10 evaluation episodes per task. Raw/Clean are shared baselines.

## Across training seeds

ACO/SMFA: mean and sample SD of the three seed means. Raw/Clean: mean and episode sample SD.

| Task | Clean | Raw | ACO | SMFA |
|---|---:|---:|---:|---:|
| walker_walk | 958.88 ± 8.98 | 363.16 ± 166.38 | 436.30 ± 227.26 | 932.29 ± 18.63 |
| walker_run | 728.38 ± 28.82 | 201.93 ± 41.39 | 229.14 ± 104.47 | 641.46 ± 15.30 |
| walker_stand | 970.95 ± 28.65 | 799.14 ± 120.22 | 839.46 ± 116.33 | 969.60 ± 0.11 |
| hopper_stand | 838.00 ± 295.43 | 288.21 ± 122.69 | 494.25 ± 147.57 | 636.03 ± 22.13 |
| quadruped_run | 492.93 ± 77.16 | 482.04 ± 74.20 | 374.78 ± 87.54 | 498.27 ± 14.38 |
| finger_turn_hard | 782.80 ± 305.41 | 409.50 ± 431.39 | 376.23 ± 91.51 | 748.43 ± 39.14 |
| cartpole_swingup_sparse | 829.30 ± 11.88 | 36.30 ± 29.34 | 314.13 ± 244.24 | 665.97 ± 19.55 |
| cup_catch | 973.90 ± 8.69 | 791.60 ± 271.56 | 913.07 ± 90.41 | 962.47 ± 12.79 |
| reacher_easy | 974.00 ± 16.05 | 958.30 ± 31.10 | 949.30 ± 13.05 | 973.23 ± 0.12 |
| reacher_hard | 103.20 ± 300.63 | 76.30 ± 229.02 | 35.13 ± 29.25 | 6.20 ± 0.52 |

## Individual seed means ± episode SD

| Task | Model | Seed1 | Seed2 | Seed3 |
|---|---|---:|---:|---:|
| walker_walk | aco | 698.34 ± 102.92 | 317.43 ± 167.71 | 293.12 ± 94.01 |
| walker_walk | smfa | 935.34 ± 28.11 | 912.33 ± 98.96 | 949.21 ± 17.77 |
| walker_run | aco | 346.97 ± 42.09 | 192.62 ± 45.19 | 147.84 ± 48.90 |
| walker_run | smfa | 627.34 ± 71.03 | 639.32 ± 83.14 | 657.71 ± 54.02 |
| walker_stand | aco | 935.23 ± 59.87 | 873.14 ± 78.65 | 710.00 ± 93.89 |
| walker_stand | smfa | 969.71 ± 22.51 | 969.59 ± 24.04 | 969.49 ± 23.04 |
| hopper_stand | aco | 534.28 ± 205.52 | 617.67 ± 230.97 | 330.79 ± 165.32 |
| hopper_stand | smfa | 659.66 ± 262.84 | 632.63 ± 255.52 | 615.80 ± 252.11 |
| quadruped_run | aco | 438.67 ± 113.73 | 275.00 ± 261.28 | 410.68 ± 111.58 |
| quadruped_run | smfa | 484.81 ± 66.70 | 513.42 ± 34.49 | 496.57 ± 62.51 |
| finger_turn_hard | aco | 465.80 ± 418.23 | 380.00 ± 425.12 | 282.90 ± 408.19 |
| finger_turn_hard | smfa | 720.70 ± 382.79 | 793.20 ± 288.33 | 731.40 ± 335.75 |
| cartpole_swingup_sparse | aco | 467.80 ± 230.43 | 442.10 ± 218.05 | 32.50 ± 28.15 |
| cartpole_swingup_sparse | smfa | 643.70 ± 162.02 | 680.30 ± 110.52 | 673.90 ± 116.93 |
| cup_catch | aco | 974.10 ± 7.84 | 955.90 ± 30.47 | 809.20 ± 154.53 |
| cup_catch | smfa | 948.10 ± 71.02 | 972.60 ± 12.84 | 966.70 ± 20.07 |
| reacher_easy | aco | 964.00 ± 30.48 | 944.80 ± 71.61 | 939.10 ± 73.53 |
| reacher_easy | smfa | 973.10 ± 16.60 | 973.30 ± 16.45 | 973.30 ± 16.45 |
| reacher_hard | aco | 68.90 ± 207.37 | 18.80 ± 46.32 | 17.70 ± 44.29 |
| reacher_hard | smfa | 6.80 ± 10.45 | 5.90 ± 9.99 | 5.90 ± 8.66 |
