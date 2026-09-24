"""Restricted NumPy checkpoint loading, metadata and strict structure checks."""
import hashlib
import pickle
from pathlib import Path
import numpy as np


class NumpyUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        allowed = {
            ('numpy.core.multiarray', '_reconstruct'): np.core.multiarray._reconstruct,
            ('numpy._core.multiarray', '_reconstruct'): np.core.multiarray._reconstruct,
            ('numpy', 'ndarray'): np.ndarray,
            ('numpy', 'dtype'): np.dtype,
            ('numpy.core.multiarray', 'scalar'): np.core.multiarray.scalar,
        }
        if (module, name) not in allowed:
            raise pickle.UnpicklingError(f'Unexpected global: {module}.{name}')
        return allowed[module, name]


def load_checkpoint(path):
    with open(path, 'rb') as f:
        data = NumpyUnpickler(f).load()
    assert isinstance(data, dict) and isinstance(data['params'], dict)
    for name, value in data['params'].items():
        assert isinstance(value, np.ndarray), (name, type(value))
        assert np.isfinite(value).all(), name
    return data


def digest(path):
    with open(path, 'rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def signature(params):
    return {k: {'shape': list(v.shape), 'dtype': str(v.dtype)}
            for k, v in sorted(params.items())}


def strict_check(expected, received):
    a, b = signature(expected), signature(received)
    mismatch = {k: {'model': a.get(k), 'checkpoint': b.get(k)}
                for k in a.keys() | b.keys() if a.get(k) != b.get(k)}
    if mismatch:
        raise ValueError(f'Checkpoint mismatch ({len(mismatch)}): {mismatch}')
    return {'strict_match': True, 'leaves': len(a),
            'scalars_including_optimizer': sum(v.size for v in received.values())}


def resolve(run):
    run = Path(run)
    latest = (run / 'ckpt/latest').read_text().strip()
    path = (run / 'ckpt' / latest / 'agent.pkl').resolve()
    assert path.is_relative_to(run.resolve()), 'Checkpoint escaped run directory'
    return path
