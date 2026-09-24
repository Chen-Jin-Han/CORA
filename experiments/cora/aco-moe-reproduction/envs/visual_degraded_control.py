"""
Visual Degraded Control Suite (VDCS) for AWARE Framework
=========================================================

Environment wrapper that applies visual degradations to DeepMind Control Suite.
Compatible with both standard DMC and Distracting Control Suite (DCS).

Usage:
    # Single degradation
    env = VisualDegradedControl(
        name='walker_walk',
        degradation_type='rain',
        intensity=0.7
    )

    # Multiple degradations
    env = VisualDegradedControl(
        name='walker_walk',
        degradation_configs=[
            {'name': 'rain', 'intensity': 0.5},
            {'name': 'fog', 'intensity': 0.3}
        ],
        composition_mode='sequential'
    )

    # Use with existing DCS environment
    env = VisualDegradedControl(
        name='walker_walk',
        base_env='dcs',  # Use DCS instead of standard DMC
        difficulty='hard',
        degradation_type='motion_blur'
    )
"""

import gym
import numpy as np
from typing import Optional, List, Dict, Any, Union

try:
    from envs.visual_degradations import (
        get_degradation,
        create_composite_degradation,
        CompositeDegradation,
        VisualDegradation
    )
except ImportError:
    from visual_degradations import (
        get_degradation,
        create_composite_degradation,
        CompositeDegradation,
        VisualDegradation
    )


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


class VisualDegradedControl:
    """
    Wrapper for applying visual degradations to DMC environments.

    This wrapper can work with:
    1. Standard DeepMind Control Suite (DMC)
    2. Distracting Control Suite (DCS)
    3. Any environment that outputs 'pixels' or 'image' observations
    """

    metadata = {}

    def __init__(
        self,
        name: str,
        action_repeat: int = 1,
        size: tuple = (64, 64),
        camera: Optional[int] = None,
        seed: int = 0,
        # Visual degradation parameters
        degradation_type: Optional[str] = None,
        degradation_preset: Optional[str] = None,  # NEW: preset support
        degradation_configs: Optional[List[Dict[str, Any]]] = None,
        intensity: float = 1.0,
        composition_mode: str = 'sequential',
        composition_probability: float = 1.0,
        intensity_jitter: float = 0.1,
        markov_stay_prob: float = 0.95,
        # Base environment type
        base_env: str = 'dmc',  # 'dmc' or 'dcs'
        # DCS-specific parameters (if base_env='dcs')
        difficulty: str = 'easy',
        dynamic: bool = True,
        background_dataset_path: Optional[str] = None,
        distraction_types: Optional[List[str]] = None,
        **kwargs
    ):
        """
        Initialize Visual Degraded Control environment.

        Args:
            name: Task name in format "domain_task" (e.g., "walker_walk")
            action_repeat: Number of times to repeat each action
            size: Rendering size (height, width)
            camera: Camera ID for rendering (None for default)
            seed: Random seed

            degradation_type: Single degradation type name (e.g., 'rain', 'fog')
            degradation_preset: Preset configuration name (e.g., 'weather_mix')
            degradation_configs: List of degradation configs for composition
            intensity: Degradation intensity (0.0 to 1.0)
            composition_mode: How to combine multiple degradations ('sequential', 'random', 'markov_temporal')
            composition_probability: Probability of applying each degradation in sequential mode
            intensity_jitter: Intensity jitter (relative) for markov_temporal mode
            markov_stay_prob: Stay probability for markov_temporal mode

            base_env: Base environment type ('dmc' or 'dcs')
            difficulty: DCS difficulty level (if base_env='dcs')
            dynamic: Use dynamic distractions (if base_env='dcs')
            background_dataset_path: Path to DAVIS dataset (if base_env='dcs')
            distraction_types: Types of distractions (if base_env='dcs')
        """
        self._name = name
        self._action_repeat = action_repeat
        self._size = size
        self._seed = seed
        self.reward_range = [-np.inf, np.inf]

        # Parse domain and task
        domain, task = name.split("_", 1)
        if domain == "cup":
            domain = "ball_in_cup"

        if camera is None:
            camera = dict(quadruped=2).get(domain, 0)
        self._camera = camera

        # Initialize base environment
        self._base_env_type = base_env.lower()
        if self._base_env_type == 'dcs':
            self._init_dcs_env(
                domain, task, seed, size, camera,
                difficulty, dynamic, background_dataset_path, distraction_types
            )
        else:  # standard DMC
            self._init_dmc_env(domain, task, seed)

        # Initialize degradation (with preset support)
        self._degradation = self._create_degradation(
            degradation_type, degradation_preset, degradation_configs, intensity,
            composition_mode, composition_probability, intensity_jitter, markov_stay_prob, seed
        )

    def _init_dmc_env(self, domain: str, task: str, seed: int):
        """Initialize standard DMC environment"""
        from dm_control import suite as dm_suite

        self._env = dm_suite.load(
            domain,
            task,
            task_kwargs={"random": seed},
        )
        print(f"[VDCS] Loaded standard DMC: {domain}_{task}")

    def _init_dcs_env(
        self,
        domain: str,
        task: str,
        seed: int,
        size: tuple,
        camera: int,
        difficulty: str,
        dynamic: bool,
        background_dataset_path: Optional[str],
        distraction_types: Optional[List[str]]
    ):
        """Initialize DCS environment"""
        try:
            try:
                from distracting_control import suite
            except ImportError:
                import sys
                from distracting_control import suite

            # Map difficulty to intensity
            intensity_map = {'easy': 0.8, 'medium': 1.0, 'hard': 1.0}
            intensity = intensity_map.get(difficulty, 0.8)

            self._env = suite.load(
                domain_name=domain,
                task_name=task,
                intensity=intensity,
                dynamic=dynamic,
                background_dataset_path=background_dataset_path,
                task_kwargs={'random': seed},
                visualize_reward=False,
                pixels_only=False,
                distraction_types=distraction_types,
            )

            print(f"[VDCS] Loaded DCS: {domain}_{task} (difficulty={difficulty}, dynamic={dynamic})")

        except ImportError as e:
            print(f"[VDCS] DCS not available, falling back to standard DMC")
            print(f"[VDCS] Error: {e}")
            self._init_dmc_env(domain, task, seed)

    def _create_degradation(
        self,
        degradation_type: Optional[str],
        degradation_preset: Optional[str],
        degradation_configs: Optional[List[Dict[str, Any]]],
        intensity: float,
        composition_mode: str,
        composition_probability: float,
        intensity_jitter: float,
        markov_stay_prob: float,
        seed: int
    ) -> Optional[Union[VisualDegradation, CompositeDegradation, MarkovTemporalDegradation]]:
        """Create degradation object from configuration"""

        def _build_composite(configs: List[Dict[str, Any]]):
            if composition_mode == 'markov_temporal':
                return MarkovTemporalDegradation(
                    configs,
                    intensity_jitter=float(intensity_jitter),
                    markov_stay_prob=float(markov_stay_prob),
                    seed=seed,
                )
            return create_composite_degradation(
                configs,
                mode=composition_mode,
                probability=composition_probability,
                seed=seed,
            )

        # Case 1: No degradation
        if degradation_type is None and degradation_preset is None and degradation_configs is None:
            print("[VDCS] No visual degradation applied")
            return None

        # Case 2: Using preset
        if degradation_preset is not None:
            # Define presets
            presets = {
                # Single degradations (pass through)
                'rain': {'degradation_type': 'rain'},
                'fog': {'degradation_type': 'fog'},
                'snow': {'degradation_type': 'snow'},
                'motion_blur': {'degradation_type': 'motion_blur'},
                'defocus_blur': {'degradation_type': 'defocus_blur'},
                'gaussian_noise': {'degradation_type': 'gaussian_noise'},
                'low_light': {'degradation_type': 'low_light'},

                # Composite presets
                'weather_mix': {
                    'degradation_configs': [
                        {'name': 'rain', 'intensity': intensity * 0.6},
                        {'name': 'fog', 'intensity': intensity * 0.4},
                    ]
                },
                'sensor_mix': {
                    'degradation_configs': [
                        {'name': 'motion_blur', 'intensity': intensity * 0.7},
                        {'name': 'gaussian_noise', 'intensity': intensity * 0.5},
                    ]
                },
                'extreme_mix': {
                    'degradation_configs': [
                        {'name': 'rain', 'intensity': intensity * 0.5},
                        {'name': 'fog', 'intensity': intensity * 0.3},
                        {'name': 'motion_blur', 'intensity': intensity * 0.6},
                        {'name': 'gaussian_noise', 'intensity': intensity * 0.4},
                    ]
                },
            }

            if degradation_preset not in presets:
                print(f"[VDCS] Warning: Unknown preset '{degradation_preset}', no degradation applied")
                return None

            preset_config = presets[degradation_preset]

            # If it's a single degradation preset
            if 'degradation_type' in preset_config:
                deg = get_degradation(preset_config['degradation_type'], intensity=intensity, seed=seed)
                print(f"[VDCS] Applied preset '{degradation_preset}': {preset_config['degradation_type']} (intensity={intensity})")
                return deg

            # If it's a composite preset
            elif 'degradation_configs' in preset_config:
                deg = _build_composite(preset_config['degradation_configs'])
                deg_names = [cfg['name'] for cfg in preset_config['degradation_configs']]
                print(f"[VDCS] Applied preset '{degradation_preset}': {deg_names} (mode={composition_mode})")
                return deg

        # Case 3: Single degradation
        if degradation_type is not None:
            deg = get_degradation(degradation_type, intensity=intensity, seed=seed)
            print(f"[VDCS] Applied degradation: {degradation_type} (intensity={intensity})")
            return deg

        # Case 4: Multiple degradations
        if degradation_configs is not None:
            deg = _build_composite(degradation_configs)
            deg_names = [cfg['name'] for cfg in degradation_configs]
            print(f"[VDCS] Applied composite degradation: {deg_names} (mode={composition_mode})")
            return deg

        return None

    @property
    def observation_space(self):
        """Return observation space compatible with DreamerV3"""
        spaces = {}
        for key, value in self._env.observation_spec().items():
            if len(value.shape) == 0:
                shape = (1,)
            else:
                shape = value.shape
            spaces[key] = gym.spaces.Box(-np.inf, np.inf, shape, dtype=np.float32)
        spaces["image"] = gym.spaces.Box(0, 255, self._size + (3,), dtype=np.uint8)
        return gym.spaces.Dict(spaces)

    @property
    def action_space(self):
        """Return action space"""
        spec = self._env.action_spec()
        return gym.spaces.Box(spec.minimum, spec.maximum, dtype=np.float32)

    def step(self, action):
        """Execute action and return observation with degradation applied"""
        assert np.isfinite(action).all(), action
        reward = 0
        for _ in range(self._action_repeat):
            time_step = self._env.step(action)
            reward += time_step.reward or 0
            if time_step.last():
                break

        obs = dict(time_step.observation)

        # Get image observation
        image = self._get_image_observation(obs)

        # Apply visual degradation if configured
        if self._degradation is not None:
            image = self._degradation.apply(image)

        obs["image"] = image

        # Process other observations
        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}

        obs["is_terminal"] = False if time_step.first() else time_step.discount == 0
        obs["is_first"] = time_step.first()
        done = time_step.last()
        info = {"discount": np.array(time_step.discount, np.float32)}
        return obs, reward, done, info

    def reset(self):
        """Reset environment and return initial observation with degradation"""
        time_step = self._env.reset()
        obs = dict(time_step.observation)

        # Get image observation
        image = self._get_image_observation(obs)

        # Apply visual degradation if configured
        if self._degradation is not None:
            if hasattr(self._degradation, "reset_episode"):
                self._degradation.reset_episode()
            image = self._degradation.apply(image)

        obs["image"] = image

        # Process other observations
        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}

        obs["is_terminal"] = False if time_step.first() else time_step.discount == 0
        obs["is_first"] = time_step.first()
        return obs

    def _get_image_observation(self, obs: dict) -> np.ndarray:
        """
        Extract and process image from observation.

        Handles different sources:
        1. 'pixels' key from DCS or pixel wrapper
        2. Direct rendering from physics
        """
        # Try to get from 'pixels' key (DCS or pixel wrapper)
        if 'pixels' in obs:
            pixels = obs.pop('pixels')
            # Resize if necessary
            if pixels.shape[:2] != self._size:
                import cv2
                pixels = cv2.resize(
                    pixels,
                    (self._size[1], self._size[0]),
                    interpolation=cv2.INTER_AREA
                )
            return pixels
        else:
            # Render directly from physics
            return self._env.physics.render(*self._size, camera_id=self._camera)

    def render(self, mode='rgb_array', height=None, width=None):
        """Render environment"""
        if height is None:
            height = self._size[0]
        if width is None:
            width = self._size[1]

        image = self._env.physics.render(height, width, camera_id=self._camera)

        # Apply degradation to rendered image
        if self._degradation is not None:
            image = self._degradation.apply(image)

        if mode == 'rgb_array':
            return image
        elif mode == 'human':
            # Display using cv2 or matplotlib
            try:
                import cv2
                cv2.imshow('Visual Degraded Control', image[:, :, ::-1])
                cv2.waitKey(1)
            except ImportError:
                print("OpenCV not available for human rendering")
            return image
        else:
            raise ValueError(f"Unsupported render mode: {mode}")

    def close(self):
        """Close environment"""
        if hasattr(self._env, 'close'):
            self._env.close()


# ============================================================================
# Convenience Functions
# ============================================================================

def make_degraded_env(
    name: str,
    degradation_preset: str = 'rain',
    intensity: float = 0.7,
    **kwargs
) -> VisualDegradedControl:
    """
    Convenience function to create degraded environment with preset.

    Args:
        name: Task name (e.g., 'walker_walk')
        degradation_preset: Preset name or single degradation type
        intensity: Degradation intensity
        **kwargs: Additional arguments for VisualDegradedControl

    Presets:
        - 'rain', 'fog', 'snow': Single weather degradation
        - 'motion_blur', 'defocus_blur': Single blur degradation
        - 'gaussian_noise', 'low_light': Single sensor degradation
        - 'weather_mix': Mix of rain, fog, snow
        - 'sensor_mix': Mix of blur and noise
        - 'extreme_mix': Combination of multiple degradations

    Returns:
        VisualDegradedControl environment
    """
    presets = {
        # Single degradations (pass through)
        'rain': {'degradation_type': 'rain'},
        'fog': {'degradation_type': 'fog'},
        'snow': {'degradation_type': 'snow'},
        'motion_blur': {'degradation_type': 'motion_blur'},
        'defocus_blur': {'degradation_type': 'defocus_blur'},
        'gaussian_noise': {'degradation_type': 'gaussian_noise'},
        'low_light': {'degradation_type': 'low_light'},

        # Composite presets
        'weather_mix': {
            'degradation_configs': [
                {'name': 'rain', 'intensity': intensity * 0.6},
                {'name': 'fog', 'intensity': intensity * 0.4},
            ],
            'composition_mode': 'sequential'
        },
        'sensor_mix': {
            'degradation_configs': [
                {'name': 'motion_blur', 'intensity': intensity * 0.7},
                {'name': 'gaussian_noise', 'intensity': intensity * 0.5},
            ],
            'composition_mode': 'sequential'
        },
        'extreme_mix': {
            'degradation_configs': [
                {'name': 'rain', 'intensity': intensity * 0.5},
                {'name': 'fog', 'intensity': intensity * 0.3},
                {'name': 'motion_blur', 'intensity': intensity * 0.6},
                {'name': 'gaussian_noise', 'intensity': intensity * 0.4},
            ],
            'composition_mode': 'sequential',
            'composition_probability': 0.7  # Don't apply all every time
        },
    }

    if degradation_preset not in presets:
        raise ValueError(
            f"Unknown preset '{degradation_preset}'. "
            f"Available: {', '.join(presets.keys())}"
        )

    preset_config = presets[degradation_preset].copy()

    # Add intensity if single degradation
    if 'degradation_type' in preset_config:
        preset_config['intensity'] = intensity

    # Merge with user kwargs (user kwargs take precedence)
    preset_config.update(kwargs)

    return VisualDegradedControl(name=name, **preset_config)


# ============================================================================
# Example Usage
# ============================================================================

if __name__ == "__main__":
    import cv2

    print("=" * 70)
    print("Visual Degraded Control Suite - Example Usage")
    print("=" * 70)

    # Example 1: Single degradation
    print("\n[1] Single Degradation: Rain")
    env = VisualDegradedControl(
        name='walker_walk',
        degradation_type='rain',
        intensity=0.7,
        size=(64, 64)
    )

    obs = env.reset()
    print(f"Observation keys: {obs.keys()}")
    print(f"Image shape: {obs['image'].shape}")

    # Run a few steps
    for i in range(5):
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        print(f"Step {i+1}: reward={reward:.3f}, done={done}")

        # Visualize (optional)
        cv2.imshow('Rain Degradation', obs['image'][:, :, ::-1])
        cv2.waitKey(100)

    env.close()
    cv2.destroyAllWindows()

    # Example 2: Multiple degradations
    print("\n[2] Composite Degradation: Rain + Fog + Blur")
    env = VisualDegradedControl(
        name='walker_walk',
        degradation_configs=[
            {'name': 'rain', 'intensity': 0.5},
            {'name': 'fog', 'intensity': 0.3},
            {'name': 'motion_blur', 'intensity': 0.6}
        ],
        composition_mode='sequential',
        size=(64, 64)
    )

    obs = env.reset()
    for i in range(5):
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)

        cv2.imshow('Composite Degradation', obs['image'][:, :, ::-1])
        cv2.waitKey(100)

    env.close()
    cv2.destroyAllWindows()

    # Example 3: Using preset
    print("\n[3] Using Preset: Weather Mix")
    env = make_degraded_env(
        name='walker_walk',
        degradation_preset='weather_mix',
        intensity=0.7
    )

    obs = env.reset()
    for i in range(5):
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)

    env.close()

    print("\n" + "=" * 70)
    print("Examples completed!")
    print("=" * 70)
