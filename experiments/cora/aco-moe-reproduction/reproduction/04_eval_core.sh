#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/common.sh"
gpu_guard

# condition:config list:adapter variant:adapter apply mode
CONDITIONS=(
  "clean|paper_dmc_vision||"
  "markov_raw|paper_dmc_vision paper_vdcs_markov||"
  "markov_oracle|paper_dmc_vision paper_vdcs_markov paper_agent_oracle||"
  "markov_aco|paper_dmc_vision paper_vdcs_markov paper_aco|full|agent_only_rgb_hard"
  "markov_single|paper_dmc_vision paper_vdcs_markov paper_aco|single|agent_only_rgb_hard"
  "markov_mask_only|paper_dmc_vision paper_vdcs_markov paper_aco|mask_only|agent_only_rgb_hard"
  "markov_rgb_only|paper_dmc_vision paper_vdcs_markov paper_aco|rgb_only|agent_only_rgb_hard"
  "markov_without_repair|paper_dmc_vision paper_vdcs_markov paper_aco|full|agent_only_input_hard"
)

eval_one() {
  local condition="$1" configs="$2" variant="$3" apply="$4" task="$5" seed="$6" gpu="$7"
  local policy adapter logdir stdout
  policy="$(policy_checkpoint "${task}" "${seed}")"
  require_file "${policy}"
  logdir="${LOG_ROOT}/eval/core/${condition}/${task}/seed_${seed}"
  stdout="${LOG_ROOT}/stdout/eval_core_${condition}_${task}_seed${seed}.log"
  mkdir -p "${logdir}"
  if eval_completed "${logdir}"; then
    echo "[SKIP] completed eval=${condition} task=${task} seed=${seed}"
    return
  fi
  local extra=()
  if [[ -n "${variant}" ]]; then
    adapter="$(adapter_checkpoint "${variant}" 0)"
    require_file "${adapter}"
    extra+=(--dual_stream_unet_checkpoint "${adapter}" --dual_stream_unet_apply "${apply}")
  fi
  read -r -a config_array <<<"${configs}"
  echo "[GPU ${gpu}] eval=${condition} task=${task} seed=${seed}"
  CUDA_VISIBLE_DEVICES="${gpu}" MUJOCO_GL="${MUJOCO_GL:-egl}" \
    python dreamer.py --configs "${config_array[@]}" \
      --task "dmc_${task}" --seed "${seed}" --device cuda:0 \
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
for seed in "${SEEDS[@]}"; do
  for task in "${DATA_TASKS[@]}"; do
    for spec in "${CONDITIONS[@]}"; do
      IFS='|' read -r condition configs variant apply <<<"${spec}"
      gpu="${GPUS[$((job % ${#GPUS[@]}))]}"
      run_batch eval_one "${condition}" "${configs}" "${variant}" "${apply}" "${task}" "${seed}" "${gpu}"
      job=$((job + 1))
    done
  done
done
finish_batch
