# Server experiment inventory

This inventory maps the CORA code to its saved experiment results. The repository uses `experiments/cora/` for source and `results/cora/` for compact outputs. Personal directory labels and paths in text files were normalized for the project. Paths beginning `/home/gpuadmin/CST/CORA` or `/data1/CST/CORA` in the snapshot are **templates**, not verified locations on the original server. Set the relevant JSON paths to the actual data, policy, and output directories before running a pipeline.

The normalization changes config bytes and source hashes. Existing server supervisors may reject these files as a resume source; use the original run snapshot to resume an existing output, or start a fresh output directory after configuring the published copy.

## Experiment groups

| Experiment | Source | Saved output | Scope |
| --- | --- | --- | --- |
| CORA / ACO main pipeline | `aco-smfa-full13`, `aco-smfa-full13-seed78` | Same-named output directories | Thirteen training-seen corruptions, fixed-type and Markov control, image metrics; seed 6 and additional seeds 7–8 |
| Earlier Markov series | `aco-smfa-markov`, `aco-smfa-markov45` | Same-named output directories | Seeds 1–5; consult each config before combining with the final full-13 series |
| Fixed-history diagnostics | `dreamer-frame-full` | `dreamer-frame-full/seed678_id13_shared_history_v1` | Frozen DreamerV3, common clean recurrent history and actions, posterior/latent/value/actor metrics |
| CORA ablation | `cora-ablation` | `cora-ablation` | Context removal, local removal, full-channel refinement, compared with the reused full seed-6 run |
| PromptIR / NAFNet | `promptir-nafnet-baselines`, `promptir-nafnet-frozen6500` | Same-named output directories | Restoration and frozen-policy baselines; read both reports for checkpoint and diagnostic scope |
| DrQ-v2 | `drqv2-walker` | `drqv2-walker` | Separate RL agent, not a restoration adapter for the frozen DreamerV3 policy |
| Restoration comparison images | `restoration-comparison-figure`, `aco-smfa-full13/make_four_model_figures.py` | `restoration-comparison-figure` | Matched-frame comparison assets and figure metadata |

Auxiliary directories include `aco-moe-reproduction`, `aco-smfa-pilot`, `aco-smfa-rgb`, `aco-smfa-ood`, `dreamer-frame-pilot`, `smfa-seed1-id`, and `safmn-shufflemixer-baselines`. They show the development and comparison work but should not be silently pooled with the final thirteen-corruption tables.

## Main experiment in detail

The server's [`aco-smfa-full13/README.md`](../experiments/cora/aco-smfa-full13/README.md) describes a seed-6, 64 × 64 RGB run: ten tasks; 4,500/500/1,000 clean images per task for train/validation/test; thirteen paired corruptions; batch 128; 15,000 AdamW updates at learning rate and weight decay `1e-4`; pixel L1 plus `0.05` Fourier L1; frozen DreamerV3. It evaluates 2,300 episodes: 300 Markov, 1,950 fixed type, and 50 clean. Each episode has 500 decisions and action repeat 2. The final `last.pt` at step 15,000 is used for formal evaluation.

The thirteen types are rain, fog, snow, motion blur, Gaussian noise, low light, JPEG, defocus blur, frost, patch occlusion, reduced saturation, shadow, and shot noise. In Markov mode the type persists with probability `0.8`; otherwise a different type is drawn. The first seven severities use a bounded random walk within ±10% of base strength. The other six hold their sampled strength or pattern for a same-type segment, except shot noise, which is redrawn per frame.

The seed-6 run, seed extensions, and ablation use different aggregation scopes. The ablation's full-CORA reference reuses a single seed-6 result. Check each run's `REPORT.md`, `results.json`, and `verification.json` before combining values across experiments.

### Ablation result consistency

The supplied ablation image and the saved server report differ on several values. Numeric results were not recalculated; personal path labels in text files were normalized. Examples checked directly:

| Metric | Ablation image | Saved report |
| --- | ---: | ---: |
| No-context Markov return | 607.33 | 630.33 |
| No-local PSNR-Y | 30.821 | 34.821 |
| No-local Markov return | 582.17 | 662.17 |

Treat the [saved ablation report](../results/cora/cora-ablation/REPORT.md) and the [ablation image](../assets/tables/cora-component-ablation.png) as distinct artifacts until their derivations are reconciled.

## Data and checkpoints

| Published path template | Approximate size at inspection | Contents |
| --- | ---: | --- |
| `/data1/CST/CORA/aco-smfa-full13` | 11 GB | Main seed-6 run, including ~9.8 GB generated paired dataset and ~1.1 GB checkpoint history |
| `/data1/CST/CORA/aco-smfa-full13-seed78` | 2.2 GB | Additional full-13 runs and their checkpoints |
| `/data1/CST/CORA/dreamer-frame-full` | 30 GB | Fixed-history input arrays (~29 GB), trajectories, metrics and reports |
| `/data1/CST/CORA/cora-ablation` | 401 MB | Three ablation checkpoints, control records, images and reports |
| `/data1/CST/CORA/promptir-nafnet-baselines` | 13 GB | Baseline training and checkpoints |
| `/data1/CST/CORA/promptir-nafnet-frozen6500` | 628 MB | Frozen-checkpoint follow-up, frame diagnostics and reports |
| `/data1/CST/CORA/aco-smfa-rgb/policies` | ~906 MB tar at parent | Frozen DreamerV3 policies used by the RGB experiments |

The original experiment output tree occupied approximately 76 GB at inspection. The Git repository contains source and compact result files. Generated frame arrays, model checkpoint histories, policy weights, and large trajectories remain on the server. The published paths above follow a project-name convention and must be mapped to the actual server paths. This separation keeps the public Git history usable and avoids presenting large artifacts as if they were included.

## Reproduction sequence

1. Prepare the frozen DreamerV3 policies and clean frames. Set `data_root`, `policy_root`, `dataset_root`, and `source_dataset_root` in each relevant `config*.json` for the target machine.
2. Use Linux, CUDA PyTorch for restoration, and the JAX/DreamerV3 environment for frozen policy evaluation. The published interpreter path `/data1/CST/CORA/aco-smfa-pilot/env/bin/python` is a template; select the actual environment on the target host.
3. Run `tests.py` in the desired source directory. For the main experiment, `supervisor.py` is the end-to-end owner of generation, training, image metrics, control, and report stages. Read the directory README first and use its resume rules; never launch the same supervisor twice.
4. Run additional seed, diagnostic, baseline, and ablation supervisors from their own directories. Each has its own config, output root, and README. Keep matched policy and corruption seeds when comparing methods.
5. Use the output `verification.json`, `REPORT.md`, and `results.json` to confirm completeness and calculate summaries. Fixed-history diagnostics assess one-frame input sensitivity; episode returns assess closed-loop effects.

The retained scripts use absolute server paths and some vendored third-party modules. No numerical experiment was rerun when this repository was assembled.
