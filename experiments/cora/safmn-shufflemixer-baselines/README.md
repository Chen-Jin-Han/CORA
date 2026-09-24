# SAFMN and ShuffleMixer RGB64 comparison, seed6

Two adapters, seed6 each, 15000 optimizer updates, physical/effective batch128,
AdamW lr=1e-4 weight_decay=1e-4, AMP, L1+0.05FFT. Deterministic balanced sampling
and horizontal flips match the existing pipeline. Final checkpoint evaluation.
Read-only shared pairs: 585000 train / 65000 validation / 130000 test.
All thirteen corruption types occur in training; no OOD claim.

## Sources and adaptation

- SAFMN: https://github.com/sunny2109/SAFMN at
  1a412066e927da640bc7e2a53ea60f9ffc134241: dim36, 8 blocks, expansion2.
- ShuffleMixer: https://github.com/sunny2109/ShuffleMixer at
  9173c4b2c0bb12fc8258008b51d83468fd8c243b: width64, 5 blocks, kernel7, expansion2.
- Original files/licenses are preserved in vendor. Local copies only remove
  BasicSR registry and unused torchvision import. Both instantiate scale=1.
- SAFMN head outputs three channels and PixelShuffle(1) is identity.
  ShuffleMixer retains its 1x1 projection, SiLU, RGB tail and input residual;
  PixelShuffle(1) and scale1 interpolation preserve resolution. No extra
  input residual is added to SAFMN. The same [-1,1]/[0,1] wrapper and output
  clamp as the previous baselines is used. These are RGB restoration adaptations.

## Execution and outputs

Run local `python tests.py` for source parity and gradients. Server supervisors
perform dataset hash audit, independent full-batch CUDA smoke, train and images.
SAFMN polls GPU0, ShuffleMixer GPU2; no peer processes are stopped.
Code/data roots are /home/gpuadmin/CST/CORA/safmn-shufflemixer-baselines and
/data1/CST/CORA/safmn-shufflemixer-baselines respectively.
Python: /data1/CST/CORA/aco-smfa-pilot/env/bin/python.

Master tests 8x4,16x4,32x2,64x1 CPU processes x cores, with the same 64 complete
episodes per setting and both models spanning ten tasks. It selects shortest
wall time among these settings, not an absolute maximum claim. Benchmark seeds
are independent of formal evaluation, whose model jobs are interleaved.
Per model: 650 fixed-type episodes (10 tasks x 13 types x 5) plus 100 Markov
episodes (10 tasks x 10), each 500 decisions / repeat2. Total1500.
Fixed-history diagnostics reuse validated Clean histories/calibration, physical
JAX batch64 and four common posterior draws. Twenty files, 25000 frames/model.

REPORT.md contains six tables after verification; results.json has all episodes
and aggregates. Existing Raw/ACO/CORA/PromptIR/NAFNet seed6 results are reused.
PromptIR was stopped at6500 updates, all others use15000. Report this limitation.
No training-seed SD is reported for single-seed results. No automatic extension.
