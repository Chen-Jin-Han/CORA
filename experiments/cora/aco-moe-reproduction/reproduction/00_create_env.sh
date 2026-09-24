#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
source reproduction/settings.sh

CONDA_ENV_PREFIX="${CONDA_ENV_PREFIX:-${LARGE_ROOT}/envs/aco_moe_repro}"
PYTHON_VERSION="${PYTHON_VERSION:-3.10}"
mkdir -p "${LARGE_ROOT}/envs" "${PIP_CACHE_DIR}" "${TORCH_HOME}" "${XDG_CACHE_HOME}"

if ! command -v conda >/dev/null 2>&1; then
  for conda_profile in \
    "${HOME}/anaconda3/etc/profile.d/conda.sh" \
    "${HOME}/miniconda3/etc/profile.d/conda.sh" \
    "/opt/conda/etc/profile.d/conda.sh"; do
    if [[ -f "${conda_profile}" ]]; then source "${conda_profile}"; break; fi
  done
fi
command -v conda >/dev/null 2>&1 || { echo "conda installation not found" >&2; exit 2; }

if [[ ! -x "${CONDA_ENV_PREFIX}/bin/python" ]]; then
  conda create -y --prefix "${CONDA_ENV_PREFIX}" "python=${PYTHON_VERSION}"
fi

eval "$(conda shell.bash hook)"
conda activate "${CONDA_ENV_PREFIX}"
python -m pip install --upgrade pip setuptools wheel
python -m pip install torch==2.5.1 --index-url https://download.pytorch.org/whl/cu121
python -m pip install -r reproduction/requirements-server.txt

echo "Environment ready. Activate with: conda activate ${CONDA_ENV_PREFIX}"
