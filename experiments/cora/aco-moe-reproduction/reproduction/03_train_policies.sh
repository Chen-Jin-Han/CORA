#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/common.sh"
gpu_guard
disk_guard

train_policy() {
  local task="$1" seed="$2" gpu="$3"
  local logdir="${LOG_ROOT}/policy/dmc_${task}/seed_${seed}"
  local stdout="${LOG_ROOT}/stdout/policy_${task}_seed${seed}.log"
  mkdir -p "${logdir}"
  if [[ "${SKIP_COMPLETED}" == "1" && -f "${logdir}/TRAINING_COMPLETE" && -f "${logdir}/latest.pt" ]]; then
    echo "[SKIP] completed policy=dmc_${task} seed=${seed}"
    return
  fi
  echo "[GPU ${gpu}] policy=dmc_${task} seed=${seed}"
  CUDA_VISIBLE_DEVICES="${gpu}" MUJOCO_GL="${MUJOCO_GL:-egl}" \
    python dreamer.py --configs paper_dmc_vision \
      --task "dmc_${task}" --seed "${seed}" --device cuda:0 \
      --logdir "${logdir}" --steps "${POLICY_STEPS}" \
      --eval_episode_num 0 --video_pred_log False \
      2>&1 | tee "${stdout}"
  require_file "${logdir}/latest.pt"
  printf 'task=dmc_%s\nseed=%s\nsteps=%s\ncompleted_utc=%s\n' \
    "${task}" "${seed}" "${POLICY_STEPS}" "$(date -u +%FT%TZ)" > "${logdir}/TRAINING_COMPLETE"
  if [[ "${PRUNE_REPLAY_AFTER_TRAIN}" == "1" ]]; then
    safe_prune_log_dir "${logdir}/train_eps"
    safe_prune_log_dir "${logdir}/eval_eps"
  fi
}

BATCH_PIDS=()
job=0
for seed in "${SEEDS[@]}"; do
  for task in "${POLICY_TASKS[@]}"; do
    gpu="${GPUS[$((job % ${#GPUS[@]}))]}"
    run_batch train_policy "${task}" "${seed}" "${gpu}"
    job=$((job + 1))
  done
done
finish_batch
