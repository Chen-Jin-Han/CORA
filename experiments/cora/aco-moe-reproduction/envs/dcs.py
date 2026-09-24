"""
Distracting Control Suite (DCS) environment wrapper for DreamerV3.

Based on "Distracting Control Suite: A Challenging Benchmark for
Reinforcement Learning from Pixels" (Stone et al., 2021)

GitHub: https://github.com/google-research/google-research/tree/master/distracting_control
"""

import gym
import numpy as np


class DistractingControl:
    """
    Wrapper for Distracting Control Suite environments.

    This adds visual distractions to DeepMind Control Suite tasks to create
    a more challenging benchmark for vision-based RL.
    """

    metadata = {}

    def __init__(
        self,
        name,
        action_repeat=1,
        size=(64, 64),
        camera=None,
        seed=0,
        difficulty='easy',
        dynamic=True,
        background_dataset_path=None,
        background_dataset_videos='train',
        distraction_types=None,
        intensity=None,
    ):
        """
        Initialize Distracting Control environment.

        Args:
            name: Task name in format "domain_task" (e.g., "walker_walk")
            action_repeat: Number of times to repeat each action
            size: Rendering size (height, width)
            camera: Camera ID for rendering (None for default)
            seed: Random seed
            difficulty: Distraction difficulty ('easy', 'medium', 'hard')
                       Maps to intensity: easy=0.3, medium=0.5, hard=1.0
            dynamic: Whether to use dynamic (True) or static (False) distractions
            background_dataset_path: Path to DAVIS dataset for background distractions
                                    (e.g., /path/to/DAVIS/JPEGImages/480p/)
            background_dataset_videos: Which videos to use ('train', 'val', or 'all')
            distraction_types: List of distraction types to apply. Options:
                              ['background', 'camera', 'color'].
                              If None, uses all distractions based on difficulty.
            intensity: Override difficulty with explicit intensity value (0.0-1.0)
        """
        domain, task = name.split("_", 1)
        if domain == "cup":  # Only domain with multiple words
            domain = "ball_in_cup"

        self._action_repeat = action_repeat
        self._size = size
        if camera is None:
            camera = dict(quadruped=2).get(domain, 0)
        self._camera = camera
        self.reward_range = [-np.inf, np.inf]

        # Try to import distracting_control suite
        try:
            # First try the packaged version from PyPI
            try:
                from distracting_control import suite
                self._use_packaged = True
            except ImportError:
                # Fall back to google-research version
                import sys
                import os
                # You may need to add the google-research repo to your path
                # sys.path.append('/path/to/google-research')
                from distracting_control import suite
                self._use_packaged = False

            # Map difficulty to intensity if not explicitly provided
            if intensity is None:
                intensity_map = {'easy': 0.8, 'medium': 1.0, 'hard': 1.0}
                intensity = intensity_map.get(difficulty, 0.8)

            # Prepare distraction configuration
            distraction_config = self._prepare_distraction_config(
                difficulty=difficulty,
                intensity=intensity,
                dynamic=dynamic,
                background_dataset_path=background_dataset_path,
                background_dataset_videos=background_dataset_videos,
                distraction_types=distraction_types,
            )

            # Load the environment with distractions
            # IMPORTANT: Set pixels_only=False to keep proprioceptive observations
            self._env = suite.load(
                domain_name=domain,
                task_name=task,
                intensity=intensity,  # Use intensity instead of difficulty
                dynamic=dynamic,
                background_dataset_path=background_dataset_path,
                background_dataset_videos=background_dataset_videos,
                task_kwargs={'random': seed},
                visualize_reward=False,
                pixels_only=False,  # Keep proprioceptive observations!
                distraction_types=distraction_config.get('distraction_types'),
                color_kwargs=distraction_config.get('color_kwargs'),
                camera_kwargs=distraction_config.get('camera_kwargs'),
            )

            print(f"[DCS] Loaded {name} with intensity={intensity}, dynamic={dynamic}")

            self._dcs_available = True

        except ImportError as e:
            print(f"[DCS] Warning: distracting_control not available, falling back to standard dm_control")
            print(f"[DCS] Install with: pip install distracting-control")
            print(f"[DCS] Or clone: https://github.com/google-research/google-research")
            print(f"[DCS] Error: {e}")

            # Fall back to standard dm_control
            from dm_control import suite as dm_suite
            self._env = dm_suite.load(
                domain,
                task,
                task_kwargs={"random": seed},
            )
            self._dcs_available = False

    def _prepare_distraction_config(
        self,
        difficulty,
        intensity,
        dynamic,
        background_dataset_path,
        background_dataset_videos,
        distraction_types
    ):
        """
        Prepare distraction configuration based on difficulty level.

        The suite supports three main types of distractions:
        1. Background: Natural video backgrounds from DAVIS dataset
        2. Camera: Random camera position changes
        3. Color: Random color perturbations
        """
        config = {}

        # Default distraction types based on difficulty
        if distraction_types is None:
            if difficulty == 'easy':
                distraction_types = ['color']
            elif difficulty == 'medium':
                distraction_types = ['color', 'camera']
            else:  # hard
                distraction_types = ['background', 'color', 'camera']

        # Set distraction_types explicitly
        config['distraction_types'] = distraction_types

        # Configure color distractions with stronger parameters
        if 'color' in distraction_types:
            # Scale color kwargs based on intensity
            # Higher intensity = more dramatic color changes
            config['color_kwargs'] = {
                'step_std': 0.05 * intensity,  # How much color changes per step
                'max_delta': 0.5 * intensity,  # Maximum color deviation from original
            }

        # Configure camera distractions
        if 'camera' in distraction_types:
            config['camera_kwargs'] = {
                'vertical_delta': 0.2 * intensity,
                'horizontal_delta': 0.2 * intensity,
            }

        # Note: background_dataset_path is passed directly to suite.load()
        # so we don't include it in config to avoid duplicate keyword argument

        return config

    @property
    def observation_space(self):
        """Return observation space compatible with DreamerV3."""
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
        """Return action space."""
        spec = self._env.action_spec()
        return gym.spaces.Box(spec.minimum, spec.maximum, dtype=np.float32)

    def step(self, action):
        """Execute action and return observation."""
        assert np.isfinite(action).all(), action
        reward = 0
        for _ in range(self._action_repeat):
            time_step = self._env.step(action)
            reward += time_step.reward or 0
            if time_step.last():
                break
        obs = dict(time_step.observation)

        # DCS uses 'pixels' key with distractions already applied
        # Extract and resize it to the desired size, then rename to 'image'
        if 'pixels' in obs:
            pixels = obs.pop('pixels')  # Remove 'pixels' from obs
            # Resize if necessary
            if pixels.shape[:2] != self._size:
                import cv2
                pixels = cv2.resize(
                    pixels,
                    (self._size[1], self._size[0]),  # cv2 uses (width, height)
                    interpolation=cv2.INTER_AREA
                )
            obs["image"] = pixels
        else:
            # Fallback: render directly from physics (no distractions)
            obs["image"] = self._render_from_physics()

        # Process other observations
        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}

        # There is no terminal state in DMC
        obs["is_terminal"] = False if time_step.first() else time_step.discount == 0
        obs["is_first"] = time_step.first()
        done = time_step.last()
        info = {"discount": np.array(time_step.discount, np.float32)}
        return obs, reward, done, info

    def reset(self):
        """Reset environment and return initial observation."""
        time_step = self._env.reset()
        obs = dict(time_step.observation)

        # DCS uses 'pixels' key with distractions already applied
        # Extract and resize it to the desired size, then rename to 'image'
        if 'pixels' in obs:
            pixels = obs.pop('pixels')  # Remove 'pixels' from obs
            # Resize if necessary
            if pixels.shape[:2] != self._size:
                import cv2
                pixels = cv2.resize(
                    pixels,
                    (self._size[1], self._size[0]),  # cv2 uses (width, height)
                    interpolation=cv2.INTER_AREA
                )
            obs["image"] = pixels
        else:
            # Fallback: render directly from physics (no distractions)
            obs["image"] = self._render_from_physics()

        # Process other observations
        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}

        obs["is_terminal"] = False if time_step.first() else time_step.discount == 0
        obs["is_first"] = time_step.first()
        return obs

    def _render_from_physics(self):
        """Render directly from physics (without distractions) - used as fallback."""
        return self._env.physics.render(*self._size, camera_id=self._camera)
