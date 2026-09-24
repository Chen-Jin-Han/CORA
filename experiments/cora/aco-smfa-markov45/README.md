# Seed4/5 continuation
Code: /home/gpuadmin/CST/CORA/aco-smfa-markov45
Outputs: /data1/CST/CORA/aco-smfa-markov45
Python: /data1/CST/CORA/aco-smfa-pilot/env/bin/python
Run supervisor.py from the code directory. Single-owner lock, source manifest, 30-second scheduling and resumable checkpoints/episodes.
GPU assignment: ACO on GPU1, SMFA on GPU3, each sequentially seed4 then seed5. CPU controls: two workers, EGL rendering on GPU3.
Ten tasks, RGB64, batch128, 15000 updates, L1+0.05FFT; unchanged dataset, architecture and inference. Validation every500 steps.
Four training runs, 400 new Markov-control episodes. No OOD or full image tests. Read-only reuse prior800 episodes; final1200 unique episodes. No retraining seeds1-3 or repeating Raw/Clean.
Final REPORT.md includes five-seed control means/sampleSD, individual seed means/episodeSD, final validation PSNR-Y/SSIM-Y/PSNR-RGB/SSIM-RGB/L1.
Check status.json, supervisor.log, logs/ and actual PIDs. On failure inspect before resuming; never launch duplicate workers.
Local checks: syntax, exact configuration parity except seed/output paths, exact model/loss/control source parity, reproducible 500-frame Markov schedule.
