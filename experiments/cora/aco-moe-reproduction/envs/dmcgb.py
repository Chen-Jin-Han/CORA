import os
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple, Union

import gym
import numpy as np


_DMCGB_MODES = {
    "train",
    # Geometric (camera) distributions
    "rotate_easy",
    "rotate_hard",
    "shift_easy",
    "shift_hard",
    "rotate_shift_easy",
    "rotate_shift_hard",
    # Photometric distributions
    "color_easy",
    "color_hard",
    "video_easy",
    "video_hard",
    "color_video_easy",
    "color_video_hard",
}


def _resolve_davis_frames_root(path: str) -> str:
    """
    Accepts common DAVIS roots:
      - .../DAVIS
      - .../DAVIS/JPEGImages
      - .../DAVIS/JPEGImages/480p
    Returns the resolved .../JPEGImages/480p path.
    """
    path = os.fsdecode(os.fspath(path))
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        raise FileNotFoundError(f"DAVIS path does not exist: {path}")

    def looks_like_frames_root(cand: str) -> bool:
        if not os.path.isdir(cand):
            return False
        try:
            entries = [e for e in os.scandir(cand) if e.is_dir()]
        except OSError:
            return False
        if not entries:
            return False
        # Check a small sample of video folders for image frames.
        for entry in entries[:10]:
            try:
                for f in os.scandir(entry.path):
                    if f.is_file() and f.name.lower().endswith((".jpg", ".jpeg", ".png")):
                        return True
            except OSError:
                continue
        return False

    # Prefer the actual frames directory (contains many <video_name>/xxxx.jpg).
    direct_480p = os.path.join(path, "JPEGImages", "480p")
    if path.endswith(os.path.join("JPEGImages", "480p")):
        if looks_like_frames_root(path):
            return path
    if path.endswith("JPEGImages"):
        cand = os.path.join(path, "480p")
        if looks_like_frames_root(cand):
            return cand
    if looks_like_frames_root(direct_480p):
        return direct_480p

    cand_480p = os.path.join(path, "480p")
    if looks_like_frames_root(cand_480p):
        return cand_480p
    if looks_like_frames_root(path):
        return path

    raise FileNotFoundError(
        f"Could not locate DAVIS frame folders under {path}. Expected something like "
        "`.../DAVIS/JPEGImages/480p/<video_name>/00000.jpg`."
    )


def _list_video_dirs(frames_root: str, split: Union[str, Sequence[str]]) -> List[str]:
    frames_root = os.fsdecode(os.fspath(frames_root))
    frames_root = _resolve_davis_frames_root(frames_root)
    existing = set(os.fsdecode(x) for x in os.listdir(frames_root))

    if isinstance(split, (list, tuple)):
        names = list(split)
    else:
        split = split.lower()
        if split in ("train", "training"):
            names = _DAVIS17_TRAINING_VIDEOS
        elif split in ("val", "valid", "validation"):
            names = _DAVIS17_VALIDATION_VIDEOS
        elif split in ("all", "*", "any"):
            names = sorted([d for d in existing if os.path.isdir(os.path.join(frames_root, d))])
        else:
            raise ValueError(f"Unsupported DAVIS split: {split!r} (use 'train'/'val'/'all' or a list)")

    video_dirs = [os.path.join(frames_root, str(name)) for name in names if str(name) in existing]
    if not video_dirs:
        raise FileNotFoundError(
            f"No DAVIS videos found under {frames_root} for split={split!r}. "
            "Check that DAVIS-2017 480p frames are present."
        )
    return video_dirs


def _rotation_matrix_yaw_pitch_roll(yaw: float, pitch: float, roll: float) -> np.ndarray:
    """Yaw(Z), pitch(Y), roll(X). Angles are in degrees."""
    yaw = np.radians(yaw)
    pitch = np.radians(pitch)
    roll = np.radians(roll)
    r_yaw = np.array(
        [[np.cos(yaw), -np.sin(yaw), 0], [np.sin(yaw), np.cos(yaw), 0], [0, 0, 1]],
        dtype=np.float64,
    )
    r_pitch = np.array(
        [[np.cos(pitch), 0, np.sin(pitch)], [0, 1, 0], [-np.sin(pitch), 0, np.cos(pitch)]],
        dtype=np.float64,
    )
    r_roll = np.array(
        [[1, 0, 0], [0, np.cos(roll), -np.sin(roll)], [0, np.sin(roll), np.cos(roll)]],
        dtype=np.float64,
    )
    return (r_yaw @ r_pitch @ r_roll).astype(np.float32)


class _CameraShiftWrapper:
    """Camera shift wrapper adapted from DMC-GB2 geometric distributions."""

    def __init__(self, env, mode: str, seed: int, camera_id: int):
        self._env = env
        self._mode = mode
        self._camera_id = int(camera_id)
        self._random = np.random.RandomState(seed)
        self._shift_in_effect = "shift" in mode

        self._curr_cam_shift = np.eye(3, dtype=np.float32)
        self._start_shift_ind = 0
        self._num_starting_shifts = 100
        self._all_cam_shifts: List[np.ndarray] = []

        if self._shift_in_effect:
            self._all_cam_shifts = self._sample_cam_shifts()
            self._random.shuffle(self._all_cam_shifts)

    def _sample_cam_shifts(self) -> List[np.ndarray]:
        domain = getattr(self._env, "_domain_name", None)
        if not domain:
            raise AttributeError("Wrapped env must expose `_domain_name` for DMC-GB shift modes.")

        cam_edges = {
            "walker": [10, -10, 10, -10],  # right, left, down, up
            "cheetah": [10, -10, 10, -10],
            "cartpole": [8, -8, 10, -10],
            "finger": [6, -6, 12, -6],
            "ball_in_cup": [6, -6, 12, -6],
        }
        if domain not in cam_edges:
            raise ValueError(f"DMC-GB shift mode not supported for domain: {domain}")

        max_roll, min_roll, max_pitch, min_pitch = cam_edges[domain]
        if "easy" in self._mode:
            max_roll /= 1.5
            min_roll /= 1.5
            max_pitch /= 1.5
            min_pitch /= 1.5

        corners = np.array(
            [[0, min_roll, min_pitch], [0, max_roll, min_pitch], [0, max_roll, max_pitch], [0, min_roll, max_pitch]],
            dtype=np.float32,
        )
        num_points_each = self._num_starting_shifts // 4
        positions = []
        for i in range(4):
            j = (i + 1) % 4
            diff = corners[j] - corners[i]
            scale = diff / num_points_each
            sampled = (np.arange(num_points_each, dtype=np.float32)[:, None] * scale) + corners[i]
            positions.append(sampled)
        positions = np.concatenate(positions, axis=0)

        shifts: List[np.ndarray] = []
        for yaw, pitch, roll in positions:
            shifts.append(_rotation_matrix_yaw_pitch_roll(float(yaw), float(pitch), float(roll)))
        while len(shifts) < self._num_starting_shifts:
            shifts.append(shifts[len(shifts) % max(1, len(shifts))])
        return shifts[: self._num_starting_shifts]

    def _apply_shift(self):
        cam_xmat = np.reshape(self._env.physics.data.cam_xmat[self._camera_id], (3, 3))
        self._env.physics.data.cam_xmat[self._camera_id] = (cam_xmat @ self._curr_cam_shift).flatten()

    def reset(self):
        time_step = self._env.reset()
        if self._shift_in_effect:
            self._curr_cam_shift = self._all_cam_shifts[self._start_shift_ind]
            self._start_shift_ind = (self._start_shift_ind + 1) % len(self._all_cam_shifts)
            self._apply_shift()
        return time_step

    def step(self, action):
        time_step = self._env.step(action)
        if self._shift_in_effect:
            self._apply_shift()
        return time_step

    def __getattr__(self, name):
        return getattr(self._env, name)


class _CameraRotateWrapper:
    """Camera rotation wrapper adapted from DMC-GB2 geometric distributions."""

    def __init__(self, env, mode: str, seed: int, camera_id: int):
        self._env = env
        self._mode = mode
        self._camera_id = int(camera_id)
        self._random = np.random.RandomState(seed)
        self._rotate_in_effect = "rotate" in mode

        self._start_rot_ind = 0
        self._num_starting_rots = 100
        self._curr_cam_rot = np.eye(3, dtype=np.float32)
        self._all_cam_rots: List[np.ndarray] = []

        if self._rotate_in_effect:
            self._all_cam_rots = self._sample_cam_rots()
            self._random.shuffle(self._all_cam_rots)

    def _sample_cam_rots(self) -> List[np.ndarray]:
        bounds = np.array([-180.0, 180.0], dtype=np.float32)
        if "easy" in self._mode:
            bounds /= 2.0
        min_angle, max_angle = float(bounds[0]), float(bounds[1])
        scale = (max_angle - min_angle) / float(self._num_starting_rots)
        angles = (np.arange(self._num_starting_rots, dtype=np.float32) * scale) + min_angle
        rots = [_rotation_matrix_yaw_pitch_roll(float(a), 0.0, 0.0) for a in angles]
        while len(rots) < self._num_starting_rots:
            rots.append(rots[len(rots) % max(1, len(rots))])
        return rots[: self._num_starting_rots]

    def _apply_rot(self):
        cam_xmat = np.reshape(self._env.physics.data.cam_xmat[self._camera_id], (3, 3))
        self._env.physics.data.cam_xmat[self._camera_id] = (cam_xmat @ self._curr_cam_rot).flatten()

    def reset(self):
        time_step = self._env.reset()
        if self._rotate_in_effect:
            self._curr_cam_rot = self._all_cam_rots[self._start_rot_ind]
            self._start_rot_ind = (self._start_rot_ind + 1) % len(self._all_cam_rots)
            self._apply_rot()
        return time_step

    def step(self, action):
        time_step = self._env.step(action)
        if self._rotate_in_effect:
            self._apply_rot()
        return time_step

    def __getattr__(self, name):
        return getattr(self._env, name)


class _ColorDistractionWrapper:
    """DCS-style color distractions (random walk in material RGB)."""

    def __init__(self, env, step_std: float, max_delta: float, seed: int):
        if step_std < 0:
            raise ValueError("`step_std` must be >= 0")
        if max_delta < 0:
            raise ValueError("`max_delta` must be >= 0")
        self._env = env
        self._step_std = float(step_std)
        self._max_delta = float(max_delta)
        self._random = np.random.RandomState(seed)

        self._current_rgb = None
        self._max_rgb = None
        self._min_rgb = None
        self._original_rgb = None
        self._frame_count = 0

    def reset(self):
        self._frame_count = 0
        time_step = self._env.reset()
        self._reset_color()
        return time_step

    def _reset_color(self):
        if self._original_rgb is None:
            self._original_rgb = np.copy(self._env.physics.model.mat_rgba)[:, :3]
            self._max_rgb = np.clip(self._original_rgb + self._max_delta, 0.0, 1.0)
            self._min_rgb = np.clip(self._original_rgb - self._max_delta, 0.0, 1.0)

        r = self._random.uniform(size=self._min_rgb.shape)
        self._current_rgb = self._min_rgb + r * (self._max_rgb - self._min_rgb)
        self._env.physics.model.mat_rgba[:, :3] = self._current_rgb

    def step(self, action):
        self._frame_count += 1
        time_step = self._env.step(action)
        if time_step.first():
            self._reset_color()
            return time_step

        if self._frame_count % 2 == 0:
            color_change = self._random.randn(*self._current_rgb.shape) * self._step_std
        else:
            color_change = 0
        new_color = self._current_rgb + color_change
        self._current_rgb = np.clip(new_color, a_min=self._min_rgb, a_max=self._max_rgb)
        self._env.physics.model.mat_rgba[:, :3] = self._current_rgb
        return time_step

    def __getattr__(self, name):
        return getattr(self._env, name)


def _resolve_color_palette_root(path: Optional[str]) -> Optional[Path]:
    candidates: List[Path] = []
    if path:
        candidates.append(Path(os.path.expanduser(os.fsdecode(os.fspath(path)))))
    env_path = os.environ.get("DMCGB_COLOR_PALETTE", "") or os.environ.get("DMCGB_COLOR_DATA", "")
    if env_path:
        candidates.append(Path(os.path.expanduser(env_path)))
    candidates.append(Path.cwd() / "src" / "env" / "data")
    candidates.append(Path.cwd() / "data" / "dmcgb")

    for cand in candidates:
        if not cand:
            continue
        if (cand / "color_hard.pt").exists() and (cand / "color_easy.pt").exists():
            return cand
    return None


def _load_color_palette(mode: str, root: Optional[Path]) -> List[dict]:
    if root is None:
        raise FileNotFoundError(
            "Color palette root not found. Set --dmcgb_color_palette_root or env DMCGB_COLOR_PALETTE."
        )
    import torch

    path = root / f"{mode}.pt"
    if not path.exists():
        raise FileNotFoundError(f"Missing color palette: {path}")
    colors = torch.load(path, weights_only=False)
    if not isinstance(colors, (list, tuple)) or not colors:
        raise ValueError(f"Invalid color palette content: {path}")
    return list(colors)


def _get_model_and_assets_from_setting_kwargs(model_fname: str, setting_kwargs: dict):
    from dm_control.suite import common
    from dm_control.utils import io as resources
    import xmltodict

    suite_dir = os.path.dirname(os.path.dirname(common.__file__))
    filenames = [
        "./common/materials.xml",
        "./common/skybox.xml",
        "./common/visual.xml",
    ]
    assets = {fn: resources.GetResource(os.path.join(suite_dir, fn)) for fn in filenames}

    if not setting_kwargs:
        return common.read_model(model_fname), assets

    model = xmltodict.parse(common.read_model(model_fname))
    materials = xmltodict.parse(assets["./common/materials.xml"])
    skybox = xmltodict.parse(assets["./common/skybox.xml"])

    if "grid_rgb1" in setting_kwargs:
        rgb = setting_kwargs["grid_rgb1"]
        materials["mujoco"]["asset"]["texture"]["@rgb1"] = f"{rgb[0]} {rgb[1]} {rgb[2]}"
    if "grid_rgb2" in setting_kwargs:
        rgb = setting_kwargs["grid_rgb2"]
        materials["mujoco"]["asset"]["texture"]["@rgb2"] = f"{rgb[0]} {rgb[1]} {rgb[2]}"
    if "grid_markrgb" in setting_kwargs:
        rgb = setting_kwargs["grid_markrgb"]
        materials["mujoco"]["asset"]["texture"]["@markrgb"] = f"{rgb[0]} {rgb[1]} {rgb[2]}"
    if "grid_texrepeat" in setting_kwargs:
        rep = setting_kwargs["grid_texrepeat"]
        materials["mujoco"]["asset"]["material"][0]["@texrepeat"] = f"{rep[0]} {rep[1]}"

    if "self_rgb" in setting_kwargs:
        rgb = setting_kwargs["self_rgb"]
        materials["mujoco"]["asset"]["material"][1]["@rgba"] = f"{rgb[0]} {rgb[1]} {rgb[2]} 1"

    if "skybox_rgb" in setting_kwargs:
        rgb = setting_kwargs["skybox_rgb"]
        skybox["mujoco"]["asset"]["texture"]["@rgb1"] = f"{rgb[0]} {rgb[1]} {rgb[2]}"
    if "skybox_rgb2" in setting_kwargs:
        rgb = setting_kwargs["skybox_rgb2"]
        skybox["mujoco"]["asset"]["texture"]["@rgb2"] = f"{rgb[0]} {rgb[1]} {rgb[2]}"
    if "skybox_markrgb" in setting_kwargs:
        rgb = setting_kwargs["skybox_markrgb"]
        skybox["mujoco"]["asset"]["texture"]["@markrgb"] = f"{rgb[0]} {rgb[1]} {rgb[2]}"

    model_xml = xmltodict.unparse(model)
    assets["./common/materials.xml"] = xmltodict.unparse(materials).encode("utf-8")
    assets["./common/skybox.xml"] = xmltodict.unparse(skybox).encode("utf-8")
    return model_xml, assets


class _ColorPaletteWrapper:
    """DMC-GB style color distractions (fixed palette per episode)."""

    def __init__(
        self,
        env,
        mode: str,
        seed: int,
        *,
        palette_root: Optional[str] = None,
        domain_name: Optional[str] = None,
    ):
        self._env = env
        self._mode = mode
        self._random = np.random.RandomState(seed)
        self._domain_name = domain_name or getattr(env, "_domain_name", None)
        if not self._domain_name:
            raise ValueError("Color palette wrapper requires a domain name.")
        root = _resolve_color_palette_root(palette_root)
        palette_mode = mode
        if "color" in mode and "hard" in mode:
            palette_mode = "color_hard"
        elif "color" in mode and "easy" in mode:
            palette_mode = "color_easy"
        self._colors = _load_color_palette(palette_mode, root)

    def reset(self):
        time_step = self._env.reset()
        self._apply_palette()
        return time_step

    def _apply_palette(self):
        setting_kwargs = self._colors[int(self._random.randint(len(self._colors)))]
        state = self._env.physics.get_state()
        # Preserve task-specific model tweaks (e.g., hidden targets, randomized sites).
        preserve_attrs = (
            "body_pos",
            "body_quat",
            "geom_pos",
            "geom_quat",
            "geom_size",
            "geom_rgba",
            "site_pos",
            "site_quat",
            "site_size",
            "site_rgba",
            "cam_pos",
            "cam_quat",
            "dof_damping",
        )
        preserved = {}
        try:
            model = self._env.physics.model
            for attr in preserve_attrs:
                try:
                    arr = getattr(model, attr)
                except Exception:
                    continue
                try:
                    preserved[attr] = np.array(arr, copy=True)
                except Exception:
                    continue
        except Exception:
            preserved = {}
        model_xml, assets = _get_model_and_assets_from_setting_kwargs(
            f"{self._domain_name}.xml", setting_kwargs
        )
        self._env.physics.reload_from_xml_string(model_xml, assets=assets)
        self._env.physics.set_state(state)
        if preserved:
            try:
                model = self._env.physics.model
                for attr, val in preserved.items():
                    try:
                        arr = getattr(model, attr)
                        if arr.shape == val.shape:
                            arr[:] = val
                    except Exception:
                        continue
            except Exception:
                pass
            try:
                self._env.physics.forward()
            except Exception:
                pass

    def __getattr__(self, name):
        return getattr(self._env, name)

@dataclass(frozen=True)
class _SkyboxTextureSpec:
    texture_index: int = 0


class _DAVISBackgroundWrapper:
    """Video background distraction using DAVIS frames via MuJoCo skybox texture updates."""

    def __init__(
        self,
        env,
        frames_root: str,
        videos: Union[str, Sequence[str]] = "train",
        num_videos: Optional[int] = None,
        dynamic: bool = True,
        seed: int = 0,
        video_alpha: float = 1.0,
        ground_plane_alpha: Optional[float] = None,
        update_every: int = 2,
        texture: _SkyboxTextureSpec = _SkyboxTextureSpec(),
    ):
        if not 0.0 <= video_alpha <= 1.0:
            raise ValueError("`video_alpha` must be in [0, 1]")
        if update_every <= 0:
            raise ValueError("`update_every` must be >= 1")

        self._env = env
        frames_root = os.fsdecode(os.fspath(frames_root))
        self._frames_root = frames_root
        self._videos = videos
        self._num_videos = num_videos
        self._dynamic = bool(dynamic)
        self._random = np.random.RandomState(seed)
        self._video_alpha = float(video_alpha)
        self._ground_plane_alpha = ground_plane_alpha
        self._update_every = int(update_every)
        self._texture_index = int(texture.texture_index)

        self._video_dirs: List[str] = []
        self._file_names: List[str] = []
        self._current_index = 0
        self._direction = 1
        self._frame_count = 0

        self._sky_height = None
        self._sky_width = None
        self._sky_size = None
        self._sky_address = None
        self._sky_texture_ref = None
        self._sky_nchannel = None
        self._tex_storage = None

        self._video_dirs = _list_video_dirs(frames_root, videos)
        if self._num_videos is not None and self._num_videos > 0:
            self._random.shuffle(self._video_dirs)
            self._video_dirs = self._video_dirs[: self._num_videos]

        try:
            from PIL import Image  # noqa: F401
        except Exception as exc:
            raise ImportError("Pillow is required for DAVIS background loading.") from exc

        from dm_control.mujoco.wrapper import mjbindings as _mjbindings  # noqa: F401

    def reset(self):
        self._frame_count = 0
        time_step = self._env.reset()
        self._reset_background_state()
        self._apply_current_frame()
        return time_step

    def _reset_background_state(self):
        if self._ground_plane_alpha is not None:
            self._env.physics.named.model.mat_rgba["grid", "a"] = self._ground_plane_alpha

        model = self._env.physics.model
        self._sky_width = int(model.tex_width[self._texture_index])
        self._sky_height = int(model.tex_height[self._texture_index])
        if hasattr(model, "tex_nchannel"):
            self._sky_nchannel = int(model.tex_nchannel[self._texture_index])
        else:
            self._sky_nchannel = 3
        self._sky_address = int(model.tex_adr[self._texture_index])

        # MuJoCo 3+ stores textures in `tex_data` (uint8); older versions use `tex_rgb`.
        if hasattr(model, "tex_data"):
            self._tex_storage = model.tex_data
        else:
            self._tex_storage = model.tex_rgb

        # Infer this texture's byte size from the address table for robustness across MuJoCo versions.
        if int(model.ntex) > self._texture_index + 1:
            next_adr = int(model.tex_adr[self._texture_index + 1])
            available = max(0, next_adr - self._sky_address)
        else:
            available = int(self._tex_storage.shape[0]) - self._sky_address

        expected = int(self._sky_width * self._sky_height * self._sky_nchannel)
        if expected <= 0 or expected > available:
            denom = int(self._sky_width * self._sky_nchannel)
            if denom > 0 and available % denom == 0:
                self._sky_height = int(available // denom)
                expected = int(self._sky_width * self._sky_height * self._sky_nchannel)

        self._sky_size = int(expected)

        start = self._sky_address
        end = self._sky_address + self._sky_size
        self._sky_texture_ref = self._tex_storage[start:end].copy()

        video_dir = os.fsdecode(os.fspath(self._random.choice(self._video_dirs)))
        file_names = []
        for name in os.listdir(video_dir):
            name = os.fsdecode(name)
            if name.lower().endswith((".jpg", ".jpeg", ".png")):
                file_names.append(os.path.join(video_dir, name))
        file_names = sorted(file_names)
        if not file_names:
            raise FileNotFoundError(f"No frames found under DAVIS video dir: {video_dir}")
        if not self._dynamic:
            file_names = [self._random.choice(file_names)]

        self._file_names = file_names
        self._current_index = int(self._random.choice(len(self._file_names)))
        self._direction = int(self._random.choice([-1, 1]))

    def _size_and_flatten(self, image: np.ndarray) -> np.ndarray:
        """
        Convert an RGB image into a flat texture buffer for the current skybox texture.

        - If the skybox texture is packed as 6 faces (height == width * 6), tile the resized square image.
        - Otherwise, resize directly to (sky_width, sky_height).
        - Handles nchannel != 3 by padding alpha/extra channels.
        """
        from PIL import Image

        if self._sky_width is None or self._sky_height is None or self._sky_nchannel is None:
            raise RuntimeError("Skybox texture metadata was not initialized")

        img = np.asarray(Image.fromarray(image).resize(size=(self._sky_width, self._sky_width)))
        if self._sky_height == self._sky_width * 6:
            img = np.tile(img, (6, 1, 1))
        elif img.shape[0] != self._sky_height:
            img = np.asarray(Image.fromarray(img).resize(size=(self._sky_width, self._sky_height)))

        if self._sky_nchannel == 3:
            tex = img
        elif self._sky_nchannel == 4:
            alpha = np.full((img.shape[0], img.shape[1], 1), 255, dtype=np.uint8)
            tex = np.concatenate([img, alpha], axis=2)
        elif self._sky_nchannel == 1:
            tex = np.asarray(Image.fromarray(img).convert("L"))[..., None]
        else:
            pad = np.full((img.shape[0], img.shape[1], self._sky_nchannel - 3), 255, dtype=np.uint8)
            tex = np.concatenate([img, pad], axis=2)

        flat = tex.ravel(order="K")
        if int(flat.shape[0]) != int(self._sky_size):
            raise RuntimeError(
                f"Prepared texture size mismatch: got={int(flat.shape[0])} expected={int(self._sky_size)} "
                f"(w={self._sky_width}, h={self._sky_height}, c={self._sky_nchannel})"
            )
        return flat

    def _blend(self, image_flat: np.ndarray) -> np.ndarray:
        if self._video_alpha == 1.0:
            return image_flat
        if self._video_alpha == 0.0:
            return self._sky_texture_ref
        return (
            self._video_alpha * image_flat.astype(np.float32)
            + (1.0 - self._video_alpha) * self._sky_texture_ref.astype(np.float32)
        ).astype(np.uint8)

    def _apply_current_frame(self):
        from PIL import Image
        from dm_control.mujoco.wrapper import mjbindings

        frame_path = self._file_names[self._current_index]
        img = np.asarray(Image.open(frame_path).convert("RGB"))
        img_flat = self._size_and_flatten(img)
        texture = self._blend(img_flat)

        start = self._sky_address
        end = self._sky_address + self._sky_size
        self._tex_storage[start:end] = texture
        with self._env.physics.contexts.gl.make_current() as ctx:
            ctx.call(
                mjbindings.mjlib.mjr_uploadTexture,
                self._env.physics.model.ptr,
                self._env.physics.contexts.mujoco.ptr,
                self._texture_index,
            )

    def step(self, action):
        self._frame_count += 1
        time_step = self._env.step(action)
        if time_step.first():
            self._reset_background_state()
            self._apply_current_frame()
            return time_step

        if self._dynamic and self._frame_count % self._update_every == 0:
            self._current_index += self._direction
            if self._current_index <= 0:
                self._current_index = 0
                self._direction = abs(self._direction)
            if self._current_index >= len(self._file_names):
                self._current_index = len(self._file_names) - 1
                self._direction = -abs(self._direction)
            self._apply_current_frame()
        return time_step

    def __getattr__(self, name):
        return getattr(self._env, name)


class DMCGBControl:
    metadata = {}

    def __init__(
        self,
        name: str,
        action_repeat: int = 1,
        size: Tuple[int, int] = (64, 64),
        camera: Optional[int] = None,
        seed: int = 0,
        mode: str = "train",
        background_dataset_path: Optional[str] = None,
        background_dataset_videos: Union[str, Sequence[str]] = "train",
        dynamic: bool = True,
        video_alpha: float = 1.0,
        video_update_every: int = 2,
        num_videos_easy: int = 10,
        num_videos_hard: int = 100,
        ground_plane_alpha: Optional[float] = None,
        color_mode: str = "random_walk",
        color_palette_root: Optional[str] = None,
    ):
        mode = str(mode).lower()
        if mode not in _DMCGB_MODES:
            raise ValueError(f"Unsupported dmcgb mode: {mode!r}. Supported: {sorted(_DMCGB_MODES)}")

        domain, task = name.split("_", 1)
        if domain == "cup":
            domain = "ball_in_cup"

        from dm_control import suite

        env = suite.load(domain, task, task_kwargs={"random": seed})
        env._domain_name = domain

        self._action_repeat = int(action_repeat)
        self._size = tuple(size)
        if camera is None:
            camera = dict(quadruped=2).get(domain, 0)
        self._camera = int(camera)
        self.reward_range = [-np.inf, np.inf]

        if mode != "train":
            use_palette = str(color_mode).lower() in ("palette", "dmcgb", "standard")

            # If using palette colors with video modes, apply color first to avoid
            # reloading physics after the video wrapper caches texture buffers.
            if "color" in mode and use_palette and "video" in mode:
                env = _ColorPaletteWrapper(
                    env,
                    mode=mode,
                    seed=seed,
                    palette_root=color_palette_root,
                    domain_name=domain,
                )

            if "video" in mode:
                if not background_dataset_path:
                    raise ValueError(
                        "DMC-GB video modes require `background_dataset_path` pointing to "
                        "a DAVIS root, e.g. /path/to/DAVIS or /path/to/DAVIS/JPEGImages/480p"
                    )
                num_videos = int(num_videos_easy if "easy" in mode else num_videos_hard)
                env = _DAVISBackgroundWrapper(
                    env,
                    frames_root=background_dataset_path,
                    videos=background_dataset_videos,
                    num_videos=num_videos,
                    dynamic=dynamic,
                    seed=seed,
                    video_alpha=video_alpha,
                    ground_plane_alpha=ground_plane_alpha,
                    update_every=video_update_every,
                )

            if "color" in mode:
                if use_palette:
                    # Palette-based DMC-GB colors (fixed per episode).
                    if not ("video" in mode):
                        env = _ColorPaletteWrapper(
                            env,
                            mode=mode,
                            seed=seed,
                            palette_root=color_palette_root,
                            domain_name=domain,
                        )
                else:
                    # DCS-like scaling: easy < hard.
                    step_std = 0.02 if "easy" in mode else 0.05
                    max_delta = 0.2 if "easy" in mode else 0.5
                    env = _ColorDistractionWrapper(env, step_std=step_std, max_delta=max_delta, seed=seed)

            if "shift" in mode:
                env = _CameraShiftWrapper(env, mode=mode, seed=seed, camera_id=self._camera)
            if "rotate" in mode:
                env = _CameraRotateWrapper(env, mode=mode, seed=seed, camera_id=self._camera)

        self._env = env

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

    def render(self, *args, **kwargs):
        if kwargs.get("mode", "rgb_array") != "rgb_array":
            raise ValueError("Only render mode 'rgb_array' is supported.")
        return self._env.physics.render(*self._size, camera_id=self._camera)


# Backwards-compatible alias.
DMCGB = DMCGBControl


# DAVIS splits (DAVIS 2017).
_DAVIS17_TRAINING_VIDEOS = [
    "bear",
    "bmx-bumps",
    "boat",
    "boxing-fisheye",
    "breakdance-flare",
    "bus",
    "car-turn",
    "cat-girl",
    "classic-car",
    "color-run",
    "crossing",
    "dance-jump",
    "dancing",
    "disc-jockey",
    "dog-agility",
    "dog-gooses",
    "dogs-scale",
    "drift-turn",
    "drone",
    "elephant",
    "flamingo",
    "hike",
    "hockey",
    "horsejump-low",
    "kid-football",
    "kite-walk",
    "koala",
    "lady-running",
    "lindy-hop",
    "longboard",
    "lucia",
    "mallard-fly",
    "mallard-water",
    "miami-surf",
    "motocross-bumps",
    "motorbike",
    "night-race",
    "paragliding",
    "planes-water",
    "rallye",
    "rhino",
    "rollerblade",
    "schoolgirls",
    "scooter-board",
    "scooter-gray",
    "sheep",
    "skate-park",
    "snowboard",
    "soccerball",
    "stroller",
    "stunt",
    "surf",
    "swing",
    "tennis",
    "tractor-sand",
    "train",
    "tuk-tuk",
    "upside-down",
    "varanus-cage",
    "walking",
]
_DAVIS17_VALIDATION_VIDEOS = [
    "bike-packing",
    "blackswan",
    "bmx-trees",
    "breakdance",
    "camel",
    "car-roundabout",
    "car-shadow",
    "cows",
    "dance-twirl",
    "dog",
    "dogs-jump",
    "drift-chicane",
    "drift-straight",
    "goat",
    "gold-fish",
    "horsejump-high",
    "india",
    "judo",
    "kite-surf",
    "lab-coat",
    "libby",
    "loading",
    "mbike-trick",
    "motocross-jump",
    "paragliding-launch",
    "parkour",
    "pigs",
    "scooter-black",
    "shooting",
    "soapbox",
]


__all__ = ["DMCGBControl", "DMCGB"]
