# ACO–SMFA preliminary results

All 210 planned control episodes completed; both adapters trained for 10,000 updates.

| Task | Clean | Raw VDCS | Oracle FG | ACO RGB | SMFA RGB | ACO FG | SMFA FG |
|---|---:|---:|---:|---:|---:|---:|---:|
| walker_walk | 954.68 ± 22.37 | 409.71 ± 92.16 | 124.17 ± 46.99 | 905.58 ± 35.58 | 941.58 ± 33.04 | 110.99 ± 31.64 | 104.87 ± 28.60 |
| walker_run | 736.14 ± 26.35 | 190.93 ± 66.70 | 41.19 ± 11.27 | 475.54 ± 66.28 | 612.37 ± 58.89 | 43.25 ± 11.72 | 44.20 ± 13.31 |
| finger_turn_hard | 747.30 ± 394.60 | 497.30 ± 359.11 | 474.50 ± 295.71 | 918.00 ± 43.98 | 816.60 ± 294.38 | 579.90 ± 362.21 | 356.30 ± 255.61 |

Return values are mean ± sample standard deviation over 10 episodes; they are not five independent training seeds.

| Adapter | Parameters | Test PSNR | SSIM | Foreground L1 | Mask IoU | Median latency ms |
|---|---:|---:|---:|---:|---:|---:|
| aco | 4884961 | 28.913 | 0.8715 | 0.0628 | 0.9451 | 4.709 |
| smfa | 183353 | 30.636 | 0.8758 | 0.0445 | 0.9098 | 2.737 |

Pixel metrics are supplementary, measured on identical held-out corruptions. Foreground L1 above is RGB error inside the reference mask.

- One adapter seed and one supplied policy per task; exploratory only
- 64x64 JAX policies differ from ACO paper policy architecture and 84x84 input
- Foreground performance includes distribution shift; interpret oracle comparison first
