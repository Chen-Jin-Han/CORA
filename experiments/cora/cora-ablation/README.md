# CORA ablation seed6

Three new variants, same seed6 data sequence, same 585000/65000/130000 shared pairs, RGB64, batch128, 15000 optimizer steps, AdamW 1e-4/weight_decay1e-4, L1+0.05FFT. No Full retraining. Each variant has 650 fixed-type and 100 Markov evaluation episodes. Full seed6 results are read-only reused, not the three-seed average.

no_context: replace contextual multiplicative gate by identity on x; remove gate-only parameters. no_local: delete DMlp local branch and its unused input projection. full_channel: PCFN 3x3 convolution on 72/72 hidden channels instead of 18/72. Eight blocks and width36 stay unchanged. Expected parameters: Full182703, no_context168591, no_local103215, full_channel533055.

Train from scratch. Training batch/augmentation RNG is stateless per step and independent of model initialization. Smoke runs separately and is not reused for training. Final15000 checkpoints evaluated. Shared dataset never regenerated. All13 perturbations are training-seen.

Run master.py from /home/gpuadmin/CST/CORA/cora-ablation with /data1/CST/CORA/aco-smfa-pilot/env/bin/python. Large files/logs/results under /data1/CST/CORA/cora-ablation. GPU0/2/3 independently poll for resource availability; GPU1 excluded. Three GPU pipelines execute smoke/train/images and then terminate. CPU benchmarks run8x4,16x4,32x2 on identical32 complete episodes across tasks/variants with separate seeds/outputs. Choose fastest measured end-to-end setting automatically for420 formal jobs (2250 episodes). Benchmark includes initialization overhead; optimality is restricted to tested settings. Preserve detailed timings. CPU affinity and thread count are execution overrides only.

Master and per-variant locks prevent duplicate runs. Complete stages and completed control episodes resume. Failures stop only this project's managed processes; investigate logs and fix locally before upload. Source manifest forbids silent code changes on resume. No automatic seed expansion or extra training. REPORT.md contains the four-row ablation summary, results.json all episodes/images, verification.json checks completeness. One seed cannot establish training-seed statistical significance.
