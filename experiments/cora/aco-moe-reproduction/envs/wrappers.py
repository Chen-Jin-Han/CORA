import datetime
import gym
import numpy as np
import uuid


class TimeLimit(gym.Wrapper):
    def __init__(self, env, duration):
        super().__init__(env)
        self._duration = duration
        self._step = None

    def step(self, action):
        assert self._step is not None, "Must reset environment."
        obs, reward, done, info = self.env.step(action)
        self._step += 1
        if self._step >= self._duration:
            done = True
            if "discount" not in info:
                info["discount"] = np.array(1.0).astype(np.float32)
            self._step = None
        return obs, reward, done, info

    def reset(self):
        self._step = 0
        return self.env.reset()


class NormalizeActions(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)
        self._mask = np.logical_and(
            np.isfinite(env.action_space.low), np.isfinite(env.action_space.high)
        )
        self._low = np.where(self._mask, env.action_space.low, -1)
        self._high = np.where(self._mask, env.action_space.high, 1)
        low = np.where(self._mask, -np.ones_like(self._low), self._low)
        high = np.where(self._mask, np.ones_like(self._low), self._high)
        self.action_space = gym.spaces.Box(low, high, dtype=np.float32)

    def step(self, action):
        original = (action + 1) / 2 * (self._high - self._low) + self._low
        original = np.where(self._mask, original, action)
        return self.env.step(original)


class OneHotAction(gym.Wrapper):
    def __init__(self, env):
        assert isinstance(env.action_space, gym.spaces.Discrete)
        super().__init__(env)
        self._random = np.random.RandomState()
        shape = (self.env.action_space.n,)
        space = gym.spaces.Box(low=0, high=1, shape=shape, dtype=np.float32)
        space.discrete = True
        self.action_space = space

    def step(self, action):
        index = np.argmax(action).astype(int)
        reference = np.zeros_like(action)
        reference[index] = 1
        if not np.allclose(reference, action):
            raise ValueError(f"Invalid one-hot action:\n{action}")
        return self.env.step(index)

    def reset(self):
        return self.env.reset()

    def _sample_action(self):
        actions = self.env.action_space.n
        index = self._random.randint(0, actions)
        reference = np.zeros(actions, dtype=np.float32)
        reference[index] = 1.0
        return reference


class RewardObs(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)
        spaces = self.env.observation_space.spaces
        if "obs_reward" not in spaces:
            spaces["obs_reward"] = gym.spaces.Box(
                -np.inf, np.inf, shape=(1,), dtype=np.float32
            )
        self.observation_space = gym.spaces.Dict(spaces)

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        if "obs_reward" not in obs:
            obs["obs_reward"] = np.array([reward], dtype=np.float32)
        return obs, reward, done, info

    def reset(self):
        obs = self.env.reset()
        if "obs_reward" not in obs:
            obs["obs_reward"] = np.array([0.0], dtype=np.float32)
        return obs


class SelectAction(gym.Wrapper):
    def __init__(self, env, key):
        super().__init__(env)
        self._key = key

    def step(self, action):
        return self.env.step(action[self._key])


class UUID(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)
        timestamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
        self.id = f"{timestamp}-{str(uuid.uuid4().hex)}"

    def reset(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
        self.id = f"{timestamp}-{str(uuid.uuid4().hex)}"
        return self.env.reset()


class AgentOnlyPixels(gym.Wrapper):
    def __init__(
        self,
        env,
        background_color=(0, 0, 0),
        agent_body=None,
        extra_sites=None,
        extra_geoms=None,
        keep_target_sites=True,
        keep_target_geoms=True,
        strict=False,
    ):
        super().__init__(env)
        bg = np.array(background_color, dtype=np.uint8).reshape((1, 1, 3))
        if bg.shape != (1, 1, 3):
            raise ValueError(f"background_color must be length-3, got {background_color!r}")
        self._bg = bg
        self._agent_body = agent_body
        self._extra_sites = extra_sites
        self._extra_geoms = extra_geoms
        self._keep_target_sites = bool(keep_target_sites)
        self._keep_target_geoms = bool(keep_target_geoms)
        self._strict = bool(strict)
        self._physics = None
        self._camera_id = 0
        self._keep_geom = None  # bool[ngeom]
        self._keep_site = None  # bool[nsite]
        self._geom_objtype = 5
        self._site_objtype = 6
        self._init_segmentation()

    def _init_segmentation(self):
        base = self.env
        for _ in range(100):
            inner = getattr(base, "env", None)
            if inner is None:
                break
            base = inner

        physics = None
        if hasattr(base, "physics"):
            physics = base.physics
        elif hasattr(base, "_env") and hasattr(base._env, "physics"):
            physics = base._env.physics

        if physics is None:
            if self._strict:
                raise RuntimeError(
                    "AgentOnlyPixels requires a dm_control-style env exposing `.physics` "
                    "or `._env.physics`."
                )
            return

        camera_id = getattr(base, "_camera", None)
        if camera_id is None:
            camera_id = getattr(base, "_camera_id", 0)
        self._physics = physics
        self._camera_id = int(camera_id)

        try:
            import mujoco  # type: ignore

            self._geom_objtype = int(mujoco.mjtObj.mjOBJ_GEOM)
            self._site_objtype = int(mujoco.mjtObj.mjOBJ_SITE)
        except Exception:
            self._geom_objtype = 5
            self._site_objtype = 6

        keep_bodies = self._resolve_agent_bodies(physics, self._agent_body)
        self._keep_geom, self._keep_site = self._compute_keep_masks(physics, keep_bodies)

    def _resolve_agent_bodies(self, physics, agent_body):
        if agent_body is None:
            return self._default_agent_bodies(physics)
        if isinstance(agent_body, str):
            if "," in agent_body:
                return [x.strip() for x in agent_body.split(",") if x.strip()]
            return [agent_body]
        if isinstance(agent_body, (list, tuple)):
            return [str(x) for x in agent_body if str(x)]
        return [str(agent_body)]

    def _default_agent_bodies(self, physics):
        model = physics.model
        # Finger domain: spinner is a separate subtree from proximal/distal.
        try:
            model.name2id("proximal", "body")
            model.name2id("spinner", "body")
            return ["proximal", "spinner"]
        except Exception:
            pass

        for cand in ("torso", "cart", "pole", "finger", "ball"):
            try:
                model.name2id(cand, "body")
                return [cand]
            except Exception:
                continue
        return ["torso"]

    def _compute_keep_masks(self, physics, agent_bodies):
        model = physics.model
        parents = np.asarray(getattr(model, "body_parentid", None), dtype=np.int32)
        nbody = int(getattr(model, "nbody"))

        root_ids = []
        for body_name in agent_bodies or []:
            try:
                root_ids.append(int(model.name2id(body_name, "body")))
            except Exception:
                if self._strict:
                    raise ValueError(f"Could not resolve agent body name: {body_name!r}")
                continue
        if not root_ids:
            return None, None

        in_subtree = np.zeros((nbody,), dtype=bool)
        for bid in range(nbody):
            cur = int(bid)
            while True:
                if cur in root_ids:
                    in_subtree[bid] = True
                    break
                nxt = int(parents[cur])
                if nxt == cur:
                    break
                cur = nxt

        geom_bodyid = np.asarray(getattr(model, "geom_bodyid", None), dtype=np.int32)
        ngeom = int(getattr(model, "ngeom"))
        keep_geom = np.zeros((ngeom,), dtype=bool)
        for gid in range(ngeom):
            keep_geom[gid] = bool(in_subtree[int(geom_bodyid[gid])])

        # Also keep extra geoms by name (e.g., target for reacher)
        extra_geom_names = []
        if isinstance(self._extra_geoms, str) and self._extra_geoms.strip():
            if "," in self._extra_geoms:
                extra_geom_names.extend([x.strip() for x in self._extra_geoms.split(",") if x.strip()])
            else:
                extra_geom_names.append(self._extra_geoms.strip())
        elif isinstance(self._extra_geoms, (list, tuple)):
            extra_geom_names.extend([str(x).strip() for x in self._extra_geoms if str(x).strip()])

        if self._keep_target_geoms:
            extra_geom_names.append("target")

        if extra_geom_names:
            for gid in range(ngeom):
                try:
                    name = model.id2name(int(gid), "geom")
                except Exception:
                    name = None
                if name and name in extra_geom_names:
                    keep_geom[gid] = True

        keep_site = None
        try:
            nsite = int(getattr(model, "nsite"))
            site_bodyid = np.asarray(getattr(model, "site_bodyid", None), dtype=np.int32)
            keep_site = np.zeros((nsite,), dtype=bool)
            for sid in range(nsite):
                keep_site[sid] = bool(in_subtree[int(site_bodyid[sid])])

            extras = []
            if isinstance(self._extra_sites, str) and self._extra_sites.strip():
                if "," in self._extra_sites:
                    extras.extend([x.strip() for x in self._extra_sites.split(",") if x.strip()])
                else:
                    extras.append(self._extra_sites.strip())
            elif isinstance(self._extra_sites, (list, tuple)):
                extras.extend([str(x).strip() for x in self._extra_sites if str(x).strip()])

            if self._keep_target_sites:
                extras.append("target")

            if extras:
                for sid in range(nsite):
                    try:
                        name = model.id2name(int(sid), "site")
                    except Exception:
                        name = None
                    if not name:
                        continue
                    if any(name == ex for ex in extras):
                        keep_site[sid] = True
        except Exception:
            keep_site = None

        return keep_geom, keep_site

    def _apply_mask(self, obs):
        if self._physics is None or "image" not in obs:
            return obs

        img = obs["image"]
        if not isinstance(img, np.ndarray) or img.ndim != 3 or img.shape[-1] != 3:
            return obs

        height, width = int(img.shape[0]), int(img.shape[1])
        try:
            seg = self._physics.render(
                height, width, camera_id=self._camera_id, segmentation=True
            )
        except Exception:
            if self._strict:
                raise
            return obs

        if self._keep_geom is None:
            if self._strict:
                raise RuntimeError("AgentOnlyPixels could not build keep-geom mask.")
            return obs

        objid = seg[..., 0].astype(int)
        objtype = seg[..., 1].astype(int) if seg.shape[-1] >= 2 else None
        mask = np.zeros((height, width), dtype=bool)
        if objtype is None:
            valid = (objid >= 0) & (objid < self._keep_geom.shape[0])
            mask[valid] = self._keep_geom[objid[valid]]
        else:
            valid_geom = (
                (objtype == self._geom_objtype)
                & (objid >= 0)
                & (objid < self._keep_geom.shape[0])
            )
            if np.any(valid_geom):
                mask[valid_geom] = self._keep_geom[objid[valid_geom]]

            if self._keep_site is not None:
                valid_site = (
                    (objtype == self._site_objtype)
                    & (objid >= 0)
                    & (objid < self._keep_site.shape[0])
                )
                if np.any(valid_site):
                    mask[valid_site] = self._keep_site[objid[valid_site]]

        out = np.broadcast_to(self._bg, img.shape).copy()
        out[mask] = img[mask]
        obs = dict(obs)
        obs["image"] = out.astype(np.uint8, copy=False)
        return obs

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        return self._apply_mask(obs), reward, done, info

    def reset(self):
        return self._apply_mask(self.env.reset())
