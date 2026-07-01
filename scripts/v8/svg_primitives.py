"""KUTUMBA-original SVG building blocks for teaching visuals."""
from __future__ import annotations

import html
from typing import Sequence


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def svg_open(title: str, desc: str, w: int = 800, h: int = 520) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img">
  <title>{esc(title)}</title>
  <desc>{esc(desc)}</desc>
  <rect width="{w}" height="{h}" fill="#faf8f5"/>
'''


def svg_close(asset_id: str, source_note: str) -> str:
    return f'''<text x="400" y="498" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11" fill="#666">
    KUTUMBA-original · {esc(asset_id)} · {esc(source_note)} · human doctrinal review required
  </text>
</svg>'''


def title_block(title: str, y: int = 42) -> str:
    return (
        f'<text x="400" y="{y}" text-anchor="middle" '
        f'font-family="Segoe UI,sans-serif" font-size="20" font-weight="600">{esc(title)}</text>\n'
    )


def box(x: int, y: int, w: int, h: int, label: str, sub: str = "", fill: str = "#e8f0fe") -> str:
    lines = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#4a6fa5" stroke-width="2"/>',
        f'<text x="{x + w // 2}" y="{y + 28}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="13" font-weight="600">{esc(label)}</text>',
    ]
    if sub:
        lines.append(
            f'<text x="{x + w // 2}" y="{y + 48}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11" fill="#444">{esc(sub)}</text>'
        )
    return "\n".join(lines) + "\n"


def arrow(x1: int, y1: int, x2: int, y2: int) -> str:
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#4a6fa5" stroke-width="2" marker-end="url(#arrowhead)"/>\n'
    )


def defs_arrowhead() -> str:
    return """<defs>
  <marker id="arrowhead" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
    <polygon points="0 0, 8 3, 0 6" fill="#4a6fa5"/>
  </marker>
</defs>
"""


def label_text(x: int, y: int, text: str, size: int = 12, anchor: str = "start", weight: str = "normal") -> str:
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Segoe UI,sans-serif" '
        f'font-size="{size}" font-weight="{weight}" fill="#333">{esc(text)}</text>\n'
    )


def concept_diagram(
    asset_id: str,
    title: str,
    desc: str,
    nodes: Sequence[tuple[str, str]],
    edges: Sequence[tuple[int, int]],
    conclusion: str,
    source: str,
) -> str:
    body = [defs_arrowhead(), title_block(title)]
    positions = [(80, 120), (320, 120), (560, 120), (200, 260), (440, 260)]
    for i, (label, sub) in enumerate(nodes):
        if i >= len(positions):
            break
        x, y = positions[i]
        body.append(box(x, y, 160, 70, label, sub))
    for a, b in edges:
        if a < len(positions) and b < len(positions):
            ax, ay = positions[a]
            bx, by = positions[b]
            body.append(arrow(ax + 80, ay + 70, bx + 80, by))
    body.append(box(250, 360, 300, 60, conclusion, "", "#fff3e0"))
    body.append(label_text(60, 440, f"Source: {source}", 11))
    return svg_open(title, desc) + "".join(body) + svg_close(asset_id, source)


def process_flow(
    asset_id: str,
    title: str,
    desc: str,
    steps: Sequence[str],
    source: str,
) -> str:
    body = [defs_arrowhead(), title_block(title)]
    x = 40
    for i, step in enumerate(steps):
        body.append(box(x, 100, 100, 55, f"Step {i + 1}", step[:28]))
        if i < len(steps) - 1:
            body.append(arrow(x + 100, 127, x + 130, 127))
        x += 130
    body.append(box(300, 220, 200, 50, "Outcome", steps[-1][:40] if steps else "", "#e8f5e9"))
    body.append(label_text(60, 300, f"Source: {source}", 11))
    return svg_open(title, desc) + "".join(body) + svg_close(asset_id, source)


def storyboard(
    asset_id: str,
    title: str,
    desc: str,
    panels: Sequence[tuple[str, str, str]],
    source: str,
) -> str:
    body = [title_block(title)]
    xs = [40, 220, 400, 580]
    for i, (seq, caption, src) in enumerate(panels[:4]):
        x = xs[i]
        body.append(f'<rect x="{x}" y="80" width="160" height="200" rx="6" fill="#fff" stroke="#888" stroke-width="1.5"/>')
        body.append(label_text(x + 80, 105, seq, 14, "middle", "600"))
        body.append(label_text(x + 12, 140, caption[:22], 11))
        body.append(label_text(x + 12, 160, caption[22:44] if len(caption) > 22 else "", 11))
        body.append(label_text(x + 12, 250, src[:20], 9, weight="normal"))
        if i < 3:
            body.append(f'<polygon points="{x + 168},{170} {x + 178},{175} {x + 168},{180}" fill="#888"/>')
    body.append(label_text(60, 320, f"Sequence source: {source}", 11))
    return svg_open(title, desc) + "".join(body) + svg_close(asset_id, source)


def analogy_diagram(
    asset_id: str,
    title: str,
    desc: str,
    left_title: str,
    left_items: Sequence[str],
    right_title: str,
    right_items: Sequence[str],
    teaches: str,
    limits: str,
    source: str,
) -> str:
    body = [title_block(title)]
    body.append(box(60, 80, 300, 180, left_title, ""))
    body.append(box(440, 80, 300, 180, right_title, ""))
    y = 120
    for item in left_items[:4]:
        body.append(label_text(80, y, f"• {item}", 11))
        y += 22
    y = 120
    for item in right_items[:4]:
        body.append(label_text(460, y, f"• {item}", 11))
        y += 22
    body.append(box(60, 290, 320, 50, "Teaches", teaches[:45], "#e8f5e9"))
    body.append(box(420, 290, 320, 50, "Does NOT teach", limits[:45], "#ffebee"))
    body.append(label_text(60, 380, f"Source: {source}", 11))
    return svg_open(title, desc) + "".join(body) + svg_close(asset_id, source)


def verse_card(
    asset_id: str,
    title: str,
    desc: str,
    reference: str,
    paraphrase: str,
    url: str,
    misconception: str,
    source: str,
) -> str:
    body = [title_block(title)]
    body.append(f'<rect x="100" y="70" width="600" height="8" fill="#e65100"/>')
    body.append(box(120, 88, 560, 60, reference, "KUTUMBA paraphrase — not full translation", "#fff8e1"))
    body.append(f'<rect x="120" y="155" width="560" height="80" rx="6" fill="#ffffff" stroke="#ccc"/>')
    body.append(label_text(140, 180, paraphrase, 13))
    body.append(box(120, 250, 260, 40, "Source link", "QR-ready URL", "#e3f2fd"))
    body.append(label_text(140, 275, url[:38], 10))
    body.append(box(420, 250, 260, 40, "Catalog key", source[:24], "#f3e5f5"))
    body.append(box(120, 310, 560, 50, "Misconception boundary", misconception[:55], "#ffebee"))
    body.append(f'<line x1="120" y1="380" x2="680" y2="380" stroke="#4a6fa5" stroke-width="1"/>')
    return svg_open(title, desc) + "".join(body) + svg_close(asset_id, source)


def practice_card(
    asset_id: str,
    title: str,
    desc: str,
    trigger: str,
    steps: Sequence[str],
    minimum: str,
    safety: str,
    source: str,
) -> str:
    body = [title_block(title)]
    body.append(box(80, 80, 640, 45, "Trigger", trigger[:60], "#e3f2fd"))
    y = 150
    for i, step in enumerate(steps[:3]):
        body.append(box(80, y, 640, 40, f"Step {i + 1}", step[:55]))
        y += 55
    body.append(box(80, y + 10, 300, 45, "Minimum version", minimum[:35], "#f3e5f5"))
    body.append(box(420, y + 10, 300, 45, "Opt-out / safety", safety[:35], "#ffebee"))
    body.append(label_text(80, 420, f"Source: {source}", 11))
    return svg_open(title, desc) + "".join(body) + svg_close(asset_id, source)


def comparison_chart(
    asset_id: str,
    title: str,
    desc: str,
    items: Sequence[str],
    source: str,
    center_label: str = "",
) -> str:
    body = [title_block(title)]
    if center_label:
        body.append(f'<circle cx="400" cy="250" r="70" fill="#e8f0fe" stroke="#4a6fa5" stroke-width="2"/>')
        body.append(label_text(400, 255, center_label, 12, "middle", "600"))
    angles = [0, 60, 120, 180, 240, 300]
    for i, item in enumerate(items[:6]):
        import math

        rad = math.radians(angles[i % 6] - 90)
        cx = int(400 + 150 * math.cos(rad))
        cy = int(250 + 150 * math.sin(rad))
        body.append(box(cx - 70, cy - 25, 140, 50, item[:18], item[18:36] if len(item) > 18 else ""))
        body.append(arrow(400, 250, cx, cy))
    body.append(label_text(60, 470, f"Source: {source}", 11))
    return svg_open(title, desc, 800, 520) + defs_arrowhead() + "".join(body) + svg_close(asset_id, source)
