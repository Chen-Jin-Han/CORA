# CORA ablation, seed6

One restoration training seed. Full is reused from the verified original seed6 run. No training-seed uncertainty is estimated. 13 training-seen types; same data/loss/15000-step budget. Fixed type: 650 episodes per variant; Markov: 100. All tasks/types equally weighted. Benchmark episodes excluded.

| Version | Parameters | PSNR-Y | SSIM-Y | Fixed-type return | Markov return |
|---|---:|---:|---:|---:|---:|
| full | 182703 | 34.689 | 0.9293 | 641.44 | 640.65 |
| no_context | 168591 | 31.519 | 0.9058 | 630.17 | 630.33 |
| no_local | 103215 | 34.821 | 0.9308 | 649.58 | 662.17 |
| full_channel | 533055 | 35.813 | 0.9378 | 656.41 | 655.71 |

Removing the local branch also reduces capacity. These experiments do not isolate capacity from architecture. Full-channel costs should be interpreted using measured throughput, not parameter ratios alone.