# Seed1 SMFA fixed-family ID control
700 episodes = 10 tasks x 7 ID families x 10 evaluation seeds. No training.
Checkpoint source: /data1/CST/CORA/aco-smfa-ood/rgb10_seed1_fft_b128_s15000_ood_ep5_v1/checkpoints/smfa/last.pt; strict model/config checks and SHA256 recorded.
Each episode fixes corruption family. Initial severity uniform within base +/-10%; subsequent frames add Gaussian std0.02 random walk clipped to same bounds. Fresh per-frame operator RNG, matching current VDCS construction convention. First frame uses initial severity.
This follows ACO Table11 fixed-family Pi=I and AppendixA severity dynamics; input64 differs from original84. No claim of identical source random streams.
Base severities: rain/fog/snow0.6, motion_blur0.35, gaussian_noise0.5, low_light/jpeg0.7. Evaluation seeds400000+task_index*1000+episode; corruption_seed=seed+10000000.
Code /home/gpuadmin/CST/CORA/smfa-seed1-id; output /data1/CST/CORA/smfa-seed1-id/smfa_seed1_id7_single_ep10_v1.
Run supervisor.py using /data1/CST/CORA/aco-smfa-pilot/env/bin/python from code directory. Initially1 CPU worker, EGL GPU0. Automatically2 workers after markov45 complete.30-second poll, single-owner lock, source hashes, resumable full episodes. Failure stops only own children, recordsfailed; inspect before restart.
Local syntax, seven families bounded severity and paired deterministic outputs tested. Completion verifies700 unique full500-decision episodes and generates results.json/REPORT.md.
