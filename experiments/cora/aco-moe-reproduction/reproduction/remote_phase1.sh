#!/usr/bin/env bash
# First server execution phase: validate the deployment, then run the full
# adapter training data/ablations and one formal control task on one GPU.
set -euo pipefail
cd "$(dirname "$0")/.."
source reproduction/settings.sh

mkdir -p "${LARGE_ROOT}/outputs/supervisor"
exec > >(tee -a "${LARGE_ROOT}/outputs/supervisor/phase1.log") 2>&1
echo "[$(date -u +%FT%TZ)] phase1 started on GPUs: ${GPUS[*]}"

bash reproduction/00_create_env.sh
for conda_profile in \
  "${HOME}/anaconda3/etc/profile.d/conda.sh" \
  "${HOME}/miniconda3/etc/profile.d/conda.sh" \
  "/opt/conda/etc/profile.d/conda.sh"; do
  if [[ -f "${conda_profile}" ]]; then source "${conda_profile}"; break; fi
done
conda activate "${LARGE_ROOT}/envs/aco_moe_repro"
bash reproduction/00_preflight.sh --require-idle

# Fast end-to-end validation in an isolated large-file directory.
if [[ ! -f "${LARGE_ROOT}/outputs/supervisor/SMOKE_COMPLETE" ]]; then
  LARGE_ROOT="${LARGE_ROOT}/smoke" \
  SEEDS="0" ADAPTER_SEEDS="0" GPUS="${GPUS[*]}" \
  DATA_TASKS_OVERRIDE="cartpole_swingup" \
  POLICY_TASKS_OVERRIDE="cartpole_swingup" \
  SAMPLES_PER_TASK=20 ACO_STEPS=2 ACO_MICRO_BATCH=2 ACO_GRAD_ACCUM=1 \
  POLICY_STEPS=200 EVAL_EPISODES=1 \
    bash reproduction/run_core_pipeline.sh
  date -u +%FT%TZ > "${LARGE_ROOT}/outputs/supervisor/SMOKE_COMPLETE"
fi

# Paper-oriented adapter data and four adapter ablations across all 8 tasks.
bash reproduction/01_generate_vdcs_data.sh
bash reproduction/02_train_adapters.sh

# First formal control result: cartpole_swingup, seed 0, all core conditions.
SEEDS="0" POLICY_TASKS_OVERRIDE="cartpole_swingup" \
  bash reproduction/03_train_policies.sh
SEEDS="0" DATA_TASKS_OVERRIDE="cartpole_swingup" \
  bash reproduction/04_eval_core.sh
bash reproduction/07_collect_results.sh

date -u +%FT%TZ > "${LARGE_ROOT}/outputs/supervisor/PHASE1_COMPLETE"
echo "[$(date -u +%FT%TZ)] phase1 completed"

# Continue through the remaining released-source experiment matrix while still
# using the same single GPU. Completed phase-1 jobs are skipped by markers.
if [[ "${CONTINUE_FULL:-1}" == "1" ]]; then
  echo "[$(date -u +%FT%TZ)] continuing full source-based matrix"
  bash reproduction/03_train_policies.sh
  bash reproduction/04_eval_core.sh
  bash reproduction/05_eval_static.sh
  bash reproduction/06_eval_dmcgb.sh
  bash reproduction/07_collect_results.sh
  date -u +%FT%TZ > "${LARGE_ROOT}/outputs/supervisor/FULL_RELEASED_MATRIX_COMPLETE"
  echo "[$(date -u +%FT%TZ)] full released-source matrix completed"
fi
