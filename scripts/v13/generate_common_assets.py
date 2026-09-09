#!/usr/bin/env python3
"""Pillow PNG helpers for original, simple V13 line-art assets."""
from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parents[2]
CREAM, PLUM, SAFFRON, TEAL = "#FFF8E8", "#5B1933", "#E59B24", "#4F7C78"
SIZE = 384


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    names = ["segoeuib.ttf" if bold else "segoeui.ttf", "arialbd.ttf" if bold else "arial.ttf"]
    for name in names:
        path = Path(r"C:\Windows\Fonts") / name
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def canvas(size: tuple[int, int] = (SIZE, SIZE)):
    image = Image.new("RGB", size, CREAM)
    return image, ImageDraw.Draw(image)


def save(image: Image.Image, out_dir: Path, name: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / name
    image.save(path, "PNG", optimize=True)
    return path


def draw_icon_hear(out_dir: Path, name: str = "icon-hear.png") -> Path:
    im, d = canvas()
    d.arc((42, 42, 210, 260), 235, 115, fill=PLUM, width=13)
    d.arc((82, 82, 175, 220), 225, 110, fill=TEAL, width=10)
    d.line((130, 185, 130, 245, 105, 278), fill=PLUM, width=11)
    d.polygon([(205, 130), (286, 108), (350, 135), (350, 296), (286, 274), (205, 296)], outline=TEAL, width=10)
    d.line((286, 110, 286, 274), fill=SAFFRON, width=8)
    return save(im, out_dir, name)


def draw_icon_chant(out_dir: Path, name: str = "icon-chant.png") -> Path:
    im, d = canvas()
    beads = [(70 + i * 28, 230 + int(42 * math.sin(i / 2))) for i in range(10)]
    d.line(beads, fill=PLUM, width=7)
    for x, y in beads:
        d.ellipse((x - 10, y - 10, x + 10, y + 10), outline=SAFFRON, width=6)
    d.line((300, 65, 300, 205), fill=TEAL, width=10)
    d.line((300, 65, 355, 48, 355, 175), fill=TEAL, width=10)
    d.ellipse((266, 188, 307, 225), fill=TEAL)
    d.ellipse((321, 158, 362, 195), fill=TEAL)
    return save(im, out_dir, name)


def draw_icon_serve(out_dir: Path, name: str = "icon-serve.png") -> Path:
    im, d = canvas()
    d.arc((38, 92, 218, 315), 220, 350, fill=PLUM, width=16)
    d.arc((166, 92, 346, 315), 190, 320, fill=TEAL, width=16)
    d.line((62, 262, 142, 302, 197, 252), fill=PLUM, width=16)
    d.line((322, 262, 242, 302, 187, 252), fill=TEAL, width=16)
    d.ellipse((162, 96, 222, 156), outline=SAFFRON, width=10)
    return save(im, out_dir, name)


def draw_icon_respect(out_dir: Path, name: str = "icon-respect.png") -> Path:
    im, d = canvas()
    d.line((42, 170, 192, 55, 342, 170), fill=TEAL, width=13)
    d.rectangle((83, 164, 301, 326), outline=TEAL, width=11)
    d.polygon([(192, 280), (119, 207), (126, 166), (166, 153), (192, 181), (218, 153), (258, 166), (265, 207)], outline=PLUM)
    d.line((192, 280, 119, 207), fill=PLUM, width=10)
    d.line((192, 280, 265, 207), fill=PLUM, width=10)
    return save(im, out_dir, name)


def draw_card_outline(out_dir: Path, name: str = "card-outline.png", label: str = "") -> Path:
    im, d = canvas((420, 560))
    d.rounded_rectangle((24, 24, 396, 536), radius=28, outline=PLUM, width=10)
    d.line((70, 70, 350, 70), fill=SAFFRON, width=6)
    if label:
        b = d.textbbox((0, 0), label, font=font(28, True))
        d.text((210 - (b[2] - b[0]) / 2, 240), label, fill=PLUM, font=font(28, True))
    return save(im, out_dir, name)


def draw_path_timeline(
    out_dir: Path,
    labels: list[str],
    name: str = "path-timeline.png",
) -> Path:
    width = max(640, 120 * len(labels) + 80)
    im, d = canvas((width, 220))
    y = 110
    d.line((40, y, width - 40, y), fill=TEAL, width=8)
    for i, label in enumerate(labels):
        x = 60 + i * ((width - 120) / max(len(labels) - 1, 1))
        d.ellipse((x - 16, y - 16, x + 16, y + 16), fill=CREAM, outline=SAFFRON, width=6)
        b = d.textbbox((0, 0), label, font=font(16, True))
        d.text((x - (b[2] - b[0]) / 2, y + 28), label, fill=PLUM, font=font(16, True))
    return save(im, out_dir, name)


def draw_wheel(
    out_dir: Path,
    segments: list[str],
    name: str = "wheel.png",
    center_label: str = "",
) -> Path:
    im, d = canvas((640, 640))
    cx = cy = 320
    r = 240
    d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=TEAL, width=9)
    n = max(len(segments), 1)
    for i, label in enumerate(segments):
        angle = -90 + (360 * i / n)
        rad = math.radians(angle)
        x2 = cx + int(r * math.cos(rad))
        y2 = cy + int(r * math.sin(rad))
        d.line((cx, cy, x2, y2), fill=PLUM, width=5)
        mid = math.radians(angle + 180 / n)
        tx = cx + int((r * 0.62) * math.cos(mid))
        ty = cy + int((r * 0.62) * math.sin(mid))
        b = d.textbbox((0, 0), label, font=font(18, True))
        d.text((tx - (b[2] - b[0]) / 2, ty - (b[3] - b[1]) / 2), label, fill=PLUM, font=font(18, True))
    d.ellipse((cx - 70, cy - 70, cx + 70, cy + 70), fill=CREAM, outline=SAFFRON, width=8)
    if center_label:
        b = d.textbbox((0, 0), center_label, font=font(18, True))
        d.text((cx - (b[2] - b[0]) / 2, cy - (b[3] - b[1]) / 2), center_label, fill=PLUM, font=font(18, True))
    return save(im, out_dir, name)


def draw_mat(
    out_dir: Path,
    label: str,
    name: str,
    color: str = TEAL,
    size: tuple[int, int] = (640, 320),
) -> Path:
    im, d = canvas(size)
    d.rounded_rectangle((25, 25, size[0] - 25, size[1] - 25), radius=35, outline=color, width=12)
    b = d.textbbox((0, 0), label, font=font(40, True))
    d.text(((size[0] - (b[2] - b[0])) / 2, (size[1] - (b[3] - b[1])) / 2), label, fill=color, font=font(40, True))
    return save(im, out_dir, name)


def write_common_set(out_dir: Path) -> list[Path]:
    """Write a reusable starter set of icons, outlines, path, wheel, and mats."""
    paths = [
        draw_icon_hear(out_dir),
        draw_icon_chant(out_dir),
        draw_icon_serve(out_dir),
        draw_icon_respect(out_dir),
        draw_card_outline(out_dir),
        draw_path_timeline(out_dir, ["Hear", "Choose", "Serve", "Review"]),
        draw_wheel(out_dir, ["Hear", "Chant", "Serve", "Respect"], center_label="Practice"),
        draw_mat(out_dir, "SAFE", "mat-safe.png", TEAL),
        draw_mat(out_dir, "NEEDS RESET", "mat-reset.png", PLUM),
    ]
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate simple V13 line-art PNGs into a visuals/v13 folder.")
    parser.add_argument(
        "--out",
        required=True,
        help="Output directory (absolute or repo-relative), typically .../visuals/v13",
    )
    parser.add_argument(
        "--set",
        choices=("common",),
        default="common",
        help="Asset set to generate",
    )
    args = parser.parse_args()
    out = Path(args.out)
    if not out.is_absolute():
        out = REPO / out
    paths = write_common_set(out) if args.set == "common" else []
    for path in paths:
        with Image.open(path) as im:
            print(f"{path.relative_to(REPO).as_posix()} {im.size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
