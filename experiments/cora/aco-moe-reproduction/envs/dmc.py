import gym
import numpy as np


class DeepMindControl:
    metadata = {}

    def __init__(self, name, action_repeat=1, size=(64, 64), camera=None, seed=0):
        domain, task = name.split("_", 1)
        if domain == "cup":  # Only domain with multiple words.
            domain = "ball_in_cup"
        if isinstance(domain, str):
            from dm_control import suite

            try:
                self._env = suite.load(
                    domain,
                    task,
                    task_kwargs={"random": seed},
                )
            except AttributeError as exc:
                if "bvh_geomid" not in str(exc):
                    raise
                try:
                    import importlib.metadata as importlib_metadata

                    dm_control_version = importlib_metadata.version("dm-control")
                except Exception:
                    dm_control_version = "unknown"
                try:
                    import mujoco

                    mujoco_version = getattr(mujoco, "__version__", "unknown")
                except Exception:
                    mujoco_version = "unknown"
                raise RuntimeError(
                    "Incompatible `dm_control`/`mujoco` versions detected while loading a DMC task "
                    f"({domain}_{task}).\n"
                    f"Detected: dm-control=={dm_control_version}, mujoco=={mujoco_version}\n"
                    "Fix (recommended): `pip install -U 'mujoco==2.3.7'`\n"
                    "Alternative: pin MuJoCo to 2.x (e.g. `pip install -U 'mujoco<3'`)."
                ) from exc
        else:
            assert task is None
            self._env = domain()
        self._action_repeat = action_repeat
        self._size = tuple(size)
        if camera is None:
            camera = dict(quadruped=2).get(domain, 0)
        self._camera = camera
        self.reward_range = [-np.inf, np.inf]

    @property
    def observation_space(self):
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
        spec = self._env.action_spec()
        return gym.spaces.Box(spec.minimum, spec.maximum, dtype=np.float32)

    def step(self, action):
        assert np.isfinite(action).all(), action
        reward = 0
        for _ in range(self._action_repeat):
            time_step = self._env.step(action)
            reward += time_step.reward or 0
            if time_step.last():
                break
        obs = dict(time_step.observation)
        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}
        obs["image"] = self.render()
        # There is no terminal state in DMC
        obs["is_terminal"] = False if time_step.first() else time_step.discount == 0
        obs["is_first"] = time_step.first()
        done = time_step.last()
        info = {"discount": np.array(time_step.discount, np.float32)}
        return obs, reward, done, info

    def reset(self):
        time_step = self._env.reset()
        obs = dict(time_step.observation)
        obs = {key: [val] if len(val.shape) == 0 else val for key, val in obs.items()}
        obs["image"] = self.render()
        obs["is_terminal"] = False if time_step.first() else time_step.discount == 0
        obs["is_first"] = time_step.first()
        return obs

    def close(self):
        if not getattr(self, "_closed", False):
            self._env.physics.free()
            self._closed = True

    def render(self, *args, **kwargs):
        if kwargs.get("mode", "rgb_array") != "rgb_array":
            raise ValueError("Only render mode 'rgb_array' is supported.")
        return self._env.physics.render(*self._size, camera_id=self._camera)


# Backwards-compatible alias used by some scripts.
DMC = DeepMindControl

__all__ = ["DeepMindControl", "DMC"]
