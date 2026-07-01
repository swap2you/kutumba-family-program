#!/usr/bin/env python3
"""Render PNG derivatives from Cycle 1 SVG teaching assets."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

RECT_RE = re.compile(
    r'<rect\s+x="([\d.]+)"\s+y="([\d.]+)"\s+width="([\d.]+)"\s+height="([\d.]+)"([^/>]*)/?>',
    re.I,
)
LINE_RE = re.compile(
    r'<line\s+x1="([\d.]+)"\s+y1="([\d.]+)"\s+x2="([\d.]+)"\s+y2="([\d.]+)"',
    re.I,
)
CIRCLE_RE = re.compile(
    r'<circle\s+cx="([\d.]+)"\s+cy="([\d.]+)"\s+r="([\d.]+)"',
    re.I,
)
VIEWBOX_RE = re.compile(r'viewBox="0\s+0\s+([\d.]+)\s+([\d.]+)"', re.I)
TITLE_RE = re.compile(r"<title>([^<]+)</title>", re.I)


def parse_color(attrs: str, default: str = "#e8f0fe") -> str:
    m = re.search(r'fill="([^"]+)"', attrs)
    if m and m.group(1) != "none":
        return m.group(1)
    return default


def svg_to_png_pil(svg_path: Path, png_path: Path) -> None:
    from PIL import Image, ImageDraw, ImageFont

    text = svg_path.read_text(encoding="utf-8")
    vb = VIEWBOX_RE.search(text)
    sw, sh = (800.0, 520.0)
    if vb:
        sw, sh = float(vb.group(1)), float(vb.group(2))
    out_w, out_h = int(sw), int(sh)
    img = Image.new("RGB", (out_w, out_h), "#faf8f5")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    for m in RECT_RE.finditer(text):
        x, y, w, h = map(float, m.groups()[:4])
        fill = parse_color(m.group(5) or "")
        outline = "#4a6fa5"
        if "stroke=" in (m.group(5) or ""):
            sm = re.search(r'stroke="([^"]+)"', m.group(5) or "")
            if sm:
                outline = sm.group(1)
        draw.rectangle([x, y, x + w, y + h], fill=fill, outline=outline, width=2)

    for m in LINE_RE.finditer(text):
        x1, y1, x2, y2 = map(float, m.groups())
        draw.line([x1, y1, x2, y2], fill="#4a6fa5", width=2)

    for m in CIRCLE_RE.finditer(text):
        cx, cy, r = map(float, m.groups())
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill="#e8f0fe", outline="#4a6fa5", width=2)

    title = TITLE_RE.search(text)
    if title:
        draw.text((20, out_h - 28), title.group(1)[:60], fill="#666666", font=font)

    png_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(png_path, format="PNG", optimize=True)


def render_svg_to_png(svg_path: Path, png_path: Path) -> None:
    """Pillow rasterizer — documented local renderer when Cairo/Inkscape unavailable."""
    svg_to_png_pil(svg_path, png_path)


def main() -> int:
    count = 0
    errors = []
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        rendered = d / "visuals" / "rendered"
        if not rendered.exists():
            continue
        png_dir = d / "visuals" / "png"
        for svg in sorted(rendered.glob("*.svg")):
            png = png_dir / f"{svg.stem}.png"
            try:
                render_svg_to_png(svg, png)
                if png.stat().st_size < 500:
                    raise RuntimeError("PNG too small")
                count += 1
            except Exception as exc:  # noqa: BLE001
                errors.append(f"{svg}: {exc}")
    theo_svg = REPO / "14-research-source-register" / "theology-visual-library" / "krishna-and-expansions" / "THEO-VIS-KRISHNA-EXP-001.svg"
    theo_png = theo_svg.with_suffix(".png")
    if theo_svg.exists():
        try:
            render_svg_to_png(theo_svg, theo_png)
            count += 1
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{theo_svg}: {exc}")
    print(f"Rendered {count} PNG files (Pillow SVG rasterizer)")
    if errors:
        for e in errors[:20]:
            print(f"FAIL: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
