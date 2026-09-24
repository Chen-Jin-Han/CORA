from typing import List, Dict, Any, Optional
import numpy as np
from visual_degradations import get_degradation

class MarkovTemporalDegradation:
    """Markov temporal degradation sequence for VDCS."""

    def __init__(
        self,
        degradation_configs: List[Dict[str, Any]],
        *,
        intensity_jitter: float = 0.1,
        markov_stay_prob: float = 0.95,
        seed: Optional[int] = None,
    ):
        self.degradation_types = []
        self.intensity_by_type = {}
        for cfg in degradation_configs:
            name = cfg.get("name")
            if not name:
                continue
            if str(name) == "jpeg_compression":
                name = "jpeg"
            self.degradation_types.append(str(name))
            self.intensity_by_type[str(name)] = float(cfg.get("intensity", 0.6))

        if not self.degradation_types:
            raise ValueError("markov_temporal requires non-empty degradation_configs")

        self.intensity_jitter = float(intensity_jitter)
        self.markov_stay_prob = float(markov_stay_prob)
        self.rng = np.random.RandomState(seed)
        self.current_type = None
        self.current_intensity = None
        self._degradation = None
        self.reset_episode()

    def _intensity_bounds(self, deg_type: str):
        base = float(self.intensity_by_type.get(deg_type, 0.6))
        jitter = abs(self.intensity_jitter) * base
        low = max(0.1, base - jitter)
        high = min(1.0, base + jitter)
        return low, high

    def _sample_intensity(self, deg_type: str) -> float:
        low, high = self._intensity_bounds(deg_type)
        if high <= low:
            return float(low)
        return float(self.rng.uniform(low, high))

    def _clip_intensity(self, intensity: float, deg_type: str) -> float:
        low, high = self._intensity_bounds(deg_type)
        return float(np.clip(intensity, low, high))

    def _update_degradation(self, deg_type: str, intensity: float) -> None:
        seed = int(self.rng.randint(0, 2**31 - 1))
        self._degradation = get_degradation(
            deg_type, intensity=float(intensity), seed=seed
        )
        self.current_type = str(deg_type)
        self.current_intensity = float(intensity)

    def reset_episode(self) -> None:
        self.current_type = str(self.rng.choice(self.degradation_types))
        self.current_intensity = self._sample_intensity(self.current_type)
        self._update_degradation(self.current_type, self.current_intensity)

    def step(self) -> None:
        if self.rng.random() < self.markov_stay_prob:
            new_intensity = float(self.current_intensity) + float(
                self.rng.normal(0.0, 0.02)
            )
            new_intensity = self._clip_intensity(new_intensity, self.current_type)
            self.current_intensity = new_intensity
            if self._degradation is not None:
                self._degradation.intensity = float(new_intensity)
            return
        other = [t for t in self.degradation_types if t != self.current_type]
        if not other:
            return
        new_type = str(self.rng.choice(other))
        new_intensity = self._sample_intensity(new_type)
        self._update_degradation(new_type, new_intensity)

    def apply(self, image: np.ndarray) -> np.ndarray:
        if self._degradation is None:
            return image
        self.step()
        return self._degradation.apply(image)

    def __call__(self, image: np.ndarray) -> np.ndarray:
        return self.apply(image)


