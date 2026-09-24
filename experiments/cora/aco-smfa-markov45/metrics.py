"""BasicSR-compatible uint8 RGB metrics, crop_border=0.
SSIM: Gaussian 11x11 sigma=1.5, valid window; Y: BT.601 studio range.
Adapted from vendored BasicSR metrics/psnr_ssim.py and utils/color_util.py.
"""
import cv2
import numpy as np


def y_channel(rgb):
    # BasicSR float32 RGB [0,1] -> YCbCr Y [0,1] -> [0,255].
    x = rgb.astype(np.float32) / 255.
    return ((np.dot(x, [65.481, 128.553, 24.966]) + 16.) / 255.).astype(np.float32) * 255.


def psnr(a, b):
    mse = np.mean((a.astype(np.float64) - b.astype(np.float64))**2)
    return float('inf') if mse == 0 else float(10*np.log10(255**2/mse))


def ssim(a, b):
    a, b = a.astype(np.float64), b.astype(np.float64)
    kernel = cv2.getGaussianKernel(11, 1.5)
    window = np.outer(kernel, kernel.T)
    filt = lambda x: cv2.filter2D(x, -1, window)[5:-5, 5:-5]
    ma, mb = filt(a), filt(b)
    va, vb, cov = filt(a*a)-ma*ma, filt(b*b)-mb*mb, filt(a*b)-ma*mb
    return float(np.mean(((2*ma*mb+6.5025)*(2*cov+58.5225)) /
                         ((ma*ma+mb*mb+6.5025)*(va+vb+58.5225))))


def measure(a, b):
    assert a.dtype == b.dtype == np.uint8 and a.shape == b.shape
    ay, by = y_channel(a), y_channel(b)
    return dict(psnr_y=psnr(ay, by), ssim_y=ssim(ay, by), psnr_rgb=psnr(a, b),
                ssim_rgb=float(np.mean([ssim(a[..., i], b[..., i]) for i in range(3)])))


def uint8(tensor):
    return ((tensor.detach().float().clamp(-1, 1).cpu().permute(0, 2, 3, 1).numpy()+1)*127.5).round().clip(0,255).astype(np.uint8)
