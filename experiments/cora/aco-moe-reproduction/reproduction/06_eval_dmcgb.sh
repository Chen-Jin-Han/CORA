#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/common.sh"
gpu_guard

eval_dmcgb() {
  local mode="$1" method="$2" task="$3" seed="$4" gpu="$5"
  local policy adapter logdir stdout profile
  policy="$(policy_checkpoint "${task}" "${seed}")"
  require_file "${policy}"
  profile="paper_dmcgb_${mode}"
  logdir="${LOG_ROOT}/eval/dmcgb/${mode}/${method}/${task}/seed_${seed}"
  stdout="${LOG_ROOT}/stdout/eval_dmcgb_${mode}_${method}_${task}_seed${seed}.log"
  mkdir -p "${logdir}"
  if eval_completed "${logdir}"; then
    echo "[SKIP] completed dmcgb=${mode} method=${method} task=${task} seed=${seed}"
    return
  fi
  local configs=(paper_dmc_vision "${profile}")
  local extra=()
  if [[ "${method}" == "aco" ]]; then
    configs+=(paper_aco)
    adapter="$(adapter_checkpoint full 0)"
    require_file "${adapter}"
    extra+=(--dual_stream_unet_checkpoint "${adapter}")
  fi
  if [[ "${mode}" == "video_hard" ]]; then
    [[ -n "${DAVIS_PATH}" ]] || { echo "DAVIS_PATH is required for video_hard" >&2; return 2; }
    extra+=(--dmcgb_background_path "${DAVIS_PATH}")
  fi
  echo "[GPU ${gpu}] dmcgb=${mode} method=${method} task=${task} seed=${seed}"
  CUDA_VISIBLE_DEVICES="${gpu}" MUJOCO_GL="${MUJOCO_GL:-egl}" \
    python dreamer.py --configs "${configs[@]}" \
      --task "dmcgb_${task}" --seed "${seed}" --device cuda:0 \
      --logdir "${logdir}" --policy_checkpoint "${policy}" \
      --eval_only True --eval_episode_num "${EVAL_EPISODES}" --compile False \
      "${extra[@]}" 2>&1 | tee "${stdout}"
  if [[ "${PRUNE_EVAL_EPISODES}" == "1" ]]; then
    safe_prune_log_dir "${logdir}/eval_eps"
    safe_prune_log_dir "${logdir}/train_eps"
  fi
}

BATCH_PIDS=()
job=0
MODES=(color_hard)
if [[ -n "${DAVIS_PATH}" ]]; then
  MODES+=(video_hard)
else
  echo "[WARN] DAVIS_PATH is empty; running color_hard only."
fi
for seed in "${SEEDS[@]}"; do
  for task in "${DMCGB_TASKS[@]}"; do
    for mode in "${MODES[@]}"; do
      for method in raw aco; do
        gpu="${GPUS[$((job % ${#GPUS[@]}))]}"
        run_batch eval_dmcgb "${mode}" "${method}" "${task}" "${seed}" "${gpu}"
        job=$((job + 1))
      done
    done
  done
done
finish_batch
