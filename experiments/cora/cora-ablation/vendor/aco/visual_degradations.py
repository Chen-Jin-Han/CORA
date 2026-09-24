"""
Visual Degradation Transforms for AWARE Framework
==================================================

Pluggable visual degradation module that supports:
1. Weather effects (rain, fog, snow)
2. Sensor degradations (noise, blur, compression)
3. Lighting conditions (low-light, contrast)
4. Compositional degradations (multiple combined)

Inspired by:
- DrQ/RAD data augmentations
- SVEA strong augmentations
- ImageNet-C corruptions
- Real-world robotic vision challenges
"""

import numpy as np
import cv2
from typing import Optional, List, Dict, Any, Callable
import random


# ============================================================================
# Base Degradation Class
# ============================================================================

class VisualDegradation:
    """Base class for all visual degradations"""

    def __init__(self, intensity: float = 1.0, seed: Optional[int] = None):
        """
        Args:
            intensity: Degradation strength (0.0 to 1.0)
            seed: Random seed for reproducibility
        """
        self.intensity = np.clip(intensity, 0.0, 1.0)
        self.rng = np.random.RandomState(seed)

    def apply(self, image: np.ndarray) -> np.ndarray:
        """
        Apply degradation to image.

        Args:
            image: RGB image (H, W, 3) with values in [0, 255]

        Returns:
            Degraded image (H, W, 3) with values in [0, 255]
        """
        raise NotImplementedError

    def __call__(self, image: np.ndarray) -> np.ndarray:
        return self.apply(image)


# ============================================================================
# Weather Degradations
# ============================================================================

class RainDegradation(VisualDegradation):
    """Add rain streaks to image"""

    def __init__(self, intensity: float = 1.0, seed: Optional[int] = None,
                 length_range: tuple = (3, 10), thickness: int = 1,
                 angle_variance: float = 10.0):
        super().__init__(intensity, seed)
        self.length_range = length_range
        self.thickness = thickness
        self.angle_variance = angle_variance

    def apply(self, image: np.ndarray) -> np.ndarray:
        """Add rain streaks with alpha blending for semi-transparency"""
        img = image.copy().astype(np.float32)
        h, w = img.shape[:2]

        # Create rain layer
        rain_layer = np.zeros((h, w), dtype=np.uint8)

        # Number of rain drops based on intensity
        num_drops = int(self.intensity * 500)

        # Rain angle (mostly vertical with some variance)
        base_angle = 80  # degrees from horizontal

        for _ in range(num_drops):
            # Random drop position
            x = self.rng.randint(0, w)
            y = self.rng.randint(0, h)

            # Random length within range (scaled down for 64x64)
            length = self.rng.randint(*self.length_range)

            # Angle with variance
            angle = base_angle + self.rng.uniform(-self.angle_variance, self.angle_variance)
            angle_rad = np.deg2rad(angle)

            # End point
            x_end = int(x + length * np.cos(angle_rad))
            y_end = int(y + length * np.sin(angle_rad))

            # Draw rain streak on separate layer
            cv2.line(rain_layer, (x, y), (x_end, y_end), 255, self.thickness)

        # Blur rain layer slightly
        rain_layer = cv2.GaussianBlur(rain_layer, (3, 3), 0)

        # Convert to 3 channels for color images
        if len(image.shape) == 3:
            rain_layer_3d = cv2.cvtColor(rain_layer, cv2.COLOR_GRAY2BGR).astype(np.float32)
            rain_normalized = rain_layer_3d / 255.0
            # Alpha blend with semi-transparency (0.3 = 30% rain, 70% original)
            result = img * (1 - rain_normalized * 0.3) + rain_normalized * 255 * 0.3
        else:
            rain_normalized = rain_layer.astype(np.float32) / 255.0
            result = img * (1 - rain_normalized * 0.3) + rain_normalized * 255 * 0.3

        return np.clip(result, 0, 255).astype(np.uint8)


class FogDegradation(VisualDegradation):
    """Add fog/haze effect to image"""

    def __init__(self, intensity: float = 1.0, seed: Optional[int] = None):
        super().__init__(intensity, seed)

    def apply(self, image: np.ndarray) -> np.ndarray:
        """Apply atmospheric scattering fog effect"""
        img = image.copy().astype(np.float32)
        h, w = img.shape[:2]

        # Fog color (grayish white)
        fog_color = np.array([200, 200, 200], dtype=np.float32)

        # Create depth-based fog map (simulate distance)
        # Simple gradient: more fog at top (far) less at bottom (near)
        y_coords = np.arange(h)[:, np.newaxis]
        fog_density = (y_coords / h) ** 0.5  # Square root for smooth falloff
        fog_density = fog_density[:, :, np.newaxis]

        # Apply fog using alpha blending
        alpha = self.intensity * fog_density * 0.7  # Scale to max 0.7
        fogged = img * (1 - alpha) + fog_color * alpha

        return np.clip(fogged, 0, 255).astype(np.uint8)


class SnowDegradation(VisualDegradation):
    """Add snow particles to image"""

    def __init__(self, intensity: float = 1.0, seed: Optional[int] = None,
                 flake_size_range: tuple = (1, 2)):
        super().__init__(intensity, seed)
        self.flake_size_range = flake_size_range

    def apply(self, image: np.ndarray) -> np.ndarray:
        """Add snow flakes with alpha blending for semi-transparency"""
        img = image.copy().astype(np.float32)
        h, w = img.shape[:2]

        # Create snow layer
        snow_layer = np.zeros((h, w), dtype=np.uint8)

        # Number of snow flakes based on intensity
        num_flakes = int(self.intensity * 1000)

        for _ in range(num_flakes):
            # Random position
            x = self.rng.randint(0, w)
            y = self.rng.randint(0, h)

            # Random size (scaled down for 64x64)
            size = self.rng.randint(*self.flake_size_range)

            # Random brightness
            brightness = self.rng.randint(200, 255)

            # Draw snow flake on separate layer
            cv2.circle(snow_layer, (x, y), size, brightness, -1)

        # Blur snow layer slightly for softer edges
        snow_layer = cv2.GaussianBlur(snow_layer, (3, 3), 0)

        # Convert to 3 channels for color images
        if len(image.shape) == 3:
            snow_layer_3d = cv2.cvtColor(snow_layer, cv2.COLOR_GRAY2BGR).astype(np.float32)
            snow_normalized = snow_layer_3d / 255.0
            # Alpha blend with semi-transparency (0.5 = 50% snow, 50% original)
            result = img * (1 - snow_normalized * 0.5) + snow_normalized * 255 * 0.5
        else:
            snow_normalized = snow_layer.astype(np.float32) / 255.0
            result = img * (1 - snow_normalized * 0.5) + snow_normalized * 255 * 0.5

        return np.clip(result, 0, 255).astype(np.uint8)


# ============================================================================
# Blur Degradations
# ============================================================================

class MotionBlurDegradation(VisualDegradation):
    """Add motion blur effect"""

    def __init__(self, intensity: float = 1.0, seed: Optional[int] = None,
                 kernel_size_range: tuple = (5, 25)):
        super().__init__(intensity, seed)
        self.kernel_size_range = kernel_size_range

    def apply(self, image: np.ndarray) -> np.ndarray:
        """Apply directional motion blur"""
        img = image.copy()

        # Kernel size based on intensity
        kernel_size = int(self.kernel_size_range[0] +
                         self.intensity * (self.kernel_size_range[1] - self.kernel_size_range[0]))
        kernel_size = kernel_size if kernel_size % 2 == 1 else kernel_size + 1

        # Random angle for motion direction
        angle = self.rng.uniform(0, 360)

        # Create motion blur kernel
        kernel = np.zeros((kernel_size, kernel_size))
        kernel[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
        kernel = kernel / kernel_size

        # Rotate kernel to desired angle
        center = (kernel_size // 2, kernel_size // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        kernel = cv2.warpAffine(kernel, M, (kernel_size, kernel_size))

        # Apply kernel
        blurred = cv2.filter2D(img, -1, kernel)

        return blurred


class DefocusBlurDegradation(VisualDegradation):
    """Add defocus/out-of-focus blur"""

    def __init__(self, intensity: float = 1.0, seed: Optional[int] = None,
                 kernel_size_range: tuple = (3, 15)):
        super().__init__(intensity, seed)
        self.kernel_size_range = kernel_size_range

    def apply(self, image: np.ndarray) -> np.ndarray:
        """Apply Gaussian defocus blur"""
        img = image.copy()

        # Kernel size based on intensity
        kernel_size = int(self.kernel_size_range[0] +
                         self.intensity * (self.kernel_size_range[1] - self.kernel_size_range[0]))
        kernel_size = kernel_size if kernel_size % 2 == 1 else kernel_size + 1

        # Sigma proportional to kernel size
        sigma = kernel_size / 3.0

        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)

        return blurred


# ============================================================================
# Noise Degradations
# ============================================================================

class GaussianNoiseDegradation(VisualDegradation):
    """Add Gaussian noise to image"""

    def __init__(self, intensity: float = 1.0, seed: Optional[int] = None,
                 max_sigma: float = 25.0):
        super().__init__(intensity, seed)
        self.max_sigma = max_sigma

    def apply(self, image: np.ndarray) -> np.ndarray:
        """Add Gaussian noise"""
        img = image.copy().astype(np.float32)

        # Noise level based on intensity
        sigma = self.intensity * self.max_sigma

        # Generate Gaussian noise
        noise = self.rng.normal(0, sigma, img.shape)

        # Add noise to image
        noisy = img + noise

        return np.clip(noisy, 0, 255).astype(np.uint8)


class SaltPepperNoiseDegradation(VisualDegradation):
    """Add salt and pepper noise"""

    def __init__(self, intensity: float = 1.0, seed: Optional[int] = None,
                 max_amount: float = 0.05):
        super().__init__(intensity, seed)
        self.max_amount = max_amount

    def apply(self, image: np.ndarray) -> np.ndarray:
        """Add salt and pepper noise"""
        img = image.copy()
        h, w = img.shape[:2]

        # Amount of noise based on intensity
        amount = self.intensity * self.max_amount
        num_salt = int(amount * h * w)
        num_pepper = int(amount * h * w)

        # Salt (white pixels)
        coords = [self.rng.randint(0, i - 1, num_salt) for i in (h, w)]
        img[coords[0], coords[1], :] = 255

        # Pepper (black pixels)
        coords = [self.rng.randint(0, i - 1, num_pepper) for i in (h, w)]
        img[coords[0], coords[1], :] = 0

        return img


# ============================================================================
# Lighting Degradations
# ============================================================================

class LowLightDegradation(VisualDegradation):
    """Simulate low-light conditions"""

    def __init__(self, intensity: float = 1.0, seed: Optional[int] = None,
                 min_brightness: float = 0.2):
        super().__init__(intensity, seed)
        self.min_brightness = min_brightness

    def apply(self, image: np.ndarray) -> np.ndarray:
        """Reduce brightness and add noise"""
        img = image.copy().astype(np.float32)

        # Brightness reduction based on intensity
        brightness_factor = 1.0 - self.intensity * (1.0 - self.min_brightness)
        darkened = img * brightness_factor

        # Add some noise (cameras are noisier in low light)
        noise_sigma = self.intensity * 15.0
        noise = self.rng.normal(0, noise_sigma, img.shape)
        noisy_dark = darkened + noise

        return np.clip(noisy_dark, 0, 255).astype(np.uint8)


class ContrastDegradation(VisualDegradation):
    """Adjust image contrast"""

    def __init__(self, intensity: float = 1.0, seed: Optional[int] = None,
                 mode: str = 'reduce'):
        """
        Args:
            mode: 'reduce' or 'increase'
        """
        super().__init__(intensity, seed)
        self.mode = mode

    def apply(self, image: np.ndarray) -> np.ndarray:
        """Adjust contrast"""
        img = image.copy().astype(np.float32)

        # Calculate mean intensity
        mean = np.mean(img)

        # Contrast factor based on intensity
        if self.mode == 'reduce':
            factor = 1.0 - self.intensity * 0.7  # Reduce to 30% contrast
        else:  # increase
            factor = 1.0 + self.intensity * 1.0  # Increase to 200% contrast

        # Apply contrast adjustment
        adjusted = (img - mean) * factor + mean

        return np.clip(adjusted, 0, 255).astype(np.uint8)


class BrightnessDegradation(VisualDegradation):
    """Adjust image brightness"""

    def __init__(self, intensity: float = 1.0, seed: Optional[int] = None,
                 mode: str = 'darken'):
        """
        Args:
            mode: 'darken' or 'brighten'
        """
        super().__init__(intensity, seed)
        self.mode = mode

    def apply(self, image: np.ndarray) -> np.ndarray:
        """Adjust brightness"""
        img = image.copy().astype(np.float32)

        # Brightness offset based on intensity
        if self.mode == 'darken':
            offset = -self.intensity * 100  # Darken up to -100
        else:  # brighten
            offset = self.intensity * 100  # Brighten up to +100

        adjusted = img + offset

        return np.clip(adjusted, 0, 255).astype(np.uint8)


# ============================================================================
# Compression Degradations
# ============================================================================

class JPEGCompressionDegradation(VisualDegradation):
    """Add JPEG compression artifacts"""

    def __init__(self, intensity: float = 1.0, seed: Optional[int] = None,
                 quality_range: tuple = (10, 90)):
        super().__init__(intensity, seed)
        self.quality_range = quality_range

    def apply(self, image: np.ndarray) -> np.ndarray:
        """Apply JPEG compression"""
        # Quality inversely proportional to intensity
        quality = int(self.quality_range[1] -
                     self.intensity * (self.quality_range[1] - self.quality_range[0]))

        # Encode and decode as JPEG
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        _, encimg = cv2.imencode('.jpg', image, encode_param)
        compressed = cv2.imdecode(encimg, cv2.IMREAD_COLOR)

        return compressed


# ============================================================================
# Compositional Degradation (Multiple Combined)
# ============================================================================

class CompositeDegradation:
    """Apply multiple degradations in sequence or randomly"""

    def __init__(self, degradations: List[VisualDegradation],
                 mode: str = 'sequential',
                 probability: float = 1.0,
                 seed: Optional[int] = None):
        """
        Args:
            degradations: List of degradation objects to apply
            mode: 'sequential' (apply all in order) or 'random' (pick one randomly)
            probability: Probability of applying each degradation (for sequential mode)
            seed: Random seed
        """
        self.degradations = degradations
        self.mode = mode
        self.probability = probability
        self.rng = np.random.RandomState(seed)

    def apply(self, image: np.ndarray) -> np.ndarray:
        """Apply degradations"""
        img = image.copy()

        if self.mode == 'sequential':
            # Apply each degradation in sequence with probability
            for deg in self.degradations:
                if self.rng.random() < self.probability:
                    img = deg.apply(img)
        elif self.mode == 'random':
            # Pick one degradation randomly
            deg = self.rng.choice(self.degradations)
            img = deg.apply(img)
        else:
            raise ValueError(f"Unknown mode: {self.mode}")

        return img

    def __call__(self, image: np.ndarray) -> np.ndarray:
        return self.apply(image)


# ============================================================================
# Utility Functions
# ============================================================================

def get_degradation(name: str, intensity: float = 1.0,
                   seed: Optional[int] = None, **kwargs) -> VisualDegradation:
    """
    Factory function to create degradation by name.

    Args:
        name: Degradation type name
        intensity: Degradation strength (0.0 to 1.0)
        seed: Random seed
        **kwargs: Additional degradation-specific parameters

    Returns:
        VisualDegradation instance
    """
    degradation_map = {
        'rain': RainDegradation,
        'fog': FogDegradation,
        'snow': SnowDegradation,
        'motion_blur': MotionBlurDegradation,
        'defocus_blur': DefocusBlurDegradation,
        'gaussian_noise': GaussianNoiseDegradation,
        'salt_pepper_noise': SaltPepperNoiseDegradation,
        'low_light': LowLightDegradation,
        'contrast': ContrastDegradation,
        'brightness': BrightnessDegradation,
        'jpeg': JPEGCompressionDegradation,
    }

    if name not in degradation_map:
        available = ', '.join(degradation_map.keys())
        raise ValueError(f"Unknown degradation '{name}'. Available: {available}")

    return degradation_map[name](intensity=intensity, seed=seed, **kwargs)


def create_composite_degradation(
    degradation_configs: List[Dict[str, Any]],
    mode: str = 'sequential',
    probability: float = 1.0,
    seed: Optional[int] = None
) -> CompositeDegradation:
    """
    Create a composite degradation from configuration.

    Args:
        degradation_configs: List of degradation configs, each with:
            - 'name': degradation type
            - 'intensity': degradation strength
            - other kwargs specific to degradation
        mode: 'sequential' or 'random'
        probability: Probability of applying each degradation
        seed: Random seed

    Returns:
        CompositeDegradation instance

    Example:
        configs = [
            {'name': 'rain', 'intensity': 0.5},
            {'name': 'fog', 'intensity': 0.3},
            {'name': 'motion_blur', 'intensity': 0.7, 'kernel_size_range': (5, 15)}
        ]
        degradation = create_composite_degradation(configs, mode='sequential')
    """
    degradations = []
    for config in degradation_configs:
        name = config.pop('name')
        deg = get_degradation(name, seed=seed, **config)
        degradations.append(deg)
        config['name'] = name  # Restore for potential reuse

    return CompositeDegradation(degradations, mode=mode,
                               probability=probability, seed=seed)
