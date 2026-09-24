# Frozen PromptIR/NAFNet evaluation

The user stopped PromptIR training during a 15,000-update run. The last fully
written checkpoint is step 6,500. The 15,000-update NAFNet checkpoint and its
complete 130,000-pair image evaluation are reused read-only. This directory
keeps all new outputs separate from both source runs. It never resumes training.

Run `prepare_eval.py` first. It verifies exact checkpoint SHA-256 hashes and
original config fingerprints, writes `frozen_manifest.json`, and links the
completed NAFNet image results. Then run `EXPERIMENT_CONFIG=config_promptir.json
CUDA_VISIBLE_DEVICES=0 python run.py images --model promptir` on GPU0. Start
`master.py` once: it waits for both image summaries, prepares fixed-history
Markov observations on GPU, empirically compares 8x4, 16x4, 32x2, 64x1 CPU
worker configurations, runs 1,500 formal episodes (750 per new model), then
computes 20 fixed-history files and six report tables.

Protocol: seed6, 10 tasks, RGB64, 13 training-seen perturbations, effective
batch128, L1+0.05FFT, 5 fixed-type episodes/task/type and 10 Markov episodes/
task/model, all 500 decisions with action repeat2. Raw, ACO, and CORA seed6
results are reused from the full13 run. Report tables contain seed6 means only;
there is no training-seed standard deviation for PromptIR or NAFNet. The
PromptIR/NAFNet comparison is **not training-budget matched** (6,500 vs 15,000
updates), which must be stated alongside any comparison of results.
