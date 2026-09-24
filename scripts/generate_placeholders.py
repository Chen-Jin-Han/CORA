"""Create README image slots once; existing user images are never overwritten."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SLOTS = {
    "assets/figures/cora-method.png": ("CORA", "Method diagram", (1600, 650)),
    "assets/tables/cora-component-ablation.png": ("CORA", "Component ablation", (1600, 400)),
}


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for name in ("C:/Windows/Fonts/arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if Path(name).exists():
            return ImageFont.truetype(name, size)
    return ImageFont.load_default()


for relative, (title, subtitle, size) in SLOTS.items():
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        continue
    image = Image.new("RGB", size, "#f5f7fa")
    draw = ImageDraw.Draw(image)
    margin = 28
    draw.rectangle((margin, margin, size[0] - margin, size[1] - margin), outline="#b8c4d2", width=3)
    draw.text((72, size[1] // 2 - 62), title, fill="#213044", font=font(54))
    draw.text((72, size[1] // 2 + 9), f"PLACEHOLDER — {subtitle}", fill="#607187", font=font(32))
    draw.text((72, size[1] - 90), f"Replace this file: {relative}", fill="#607187", font=font(24))
    image.save(path, optimize=True)
    print(relative)
