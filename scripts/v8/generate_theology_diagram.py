#!/usr/bin/env python3
"""Generate source-mapped Krishna and Expansions theology diagram."""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT = REPO / "14-research-source-register" / "theology-visual-library" / "krishna-and-expansions" / "THEO-VIS-KRISHNA-EXP-001.svg"
PNG = OUT.parent / "THEO-VIS-KRISHNA-EXP-001.png"

SVG = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 620" role="img">
  <title>Kṛṣṇa and Expansions — synthesis reference</title>
  <desc>Source-mapped diagram: Kṛṣṇa, expansions, incarnations, living entities</desc>
  <defs>
    <marker id="ah" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#4a6fa5"/>
    </marker>
  </defs>
  <rect width="900" height="620" fill="#faf8f5"/>
  <text x="450" y="36" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="20" font-weight="600">Kṛṣṇa and Expansions (synthesis reference)</text>
  <rect x="360" y="70" width="180" height="70" rx="8" fill="#fff3e0" stroke="#e65100" stroke-width="2"/>
  <text x="450" y="100" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="14" font-weight="600">Śrī Kṛṣṇa</text>
  <text x="450" y="120" text-anchor="middle" font-size="11">Original Supreme Person</text>
  <rect x="80" y="200" width="160" height="60" rx="6" fill="#e8f0fe" stroke="#4a6fa5"/>
  <text x="160" y="225" text-anchor="middle" font-size="12" font-weight="600">Balarāma</text>
  <text x="160" y="245" text-anchor="middle" font-size="10">first expansion</text>
  <rect x="280" y="200" width="160" height="60" rx="6" fill="#e8f0fe" stroke="#4a6fa5"/>
  <text x="360" y="225" text-anchor="middle" font-size="12" font-weight="600">Paramātmā</text>
  <text x="360" y="245" text-anchor="middle" font-size="10">Supersoul in hearts</text>
  <rect x="480" y="200" width="160" height="60" rx="6" fill="#e8f0fe" stroke="#4a6fa5"/>
  <text x="560" y="225" text-anchor="middle" font-size="12" font-weight="600">Brahman</text>
  <text x="560" y="245" text-anchor="middle" font-size="10">impersonal effulgence</text>
  <rect x="680" y="200" width="160" height="60" rx="6" fill="#e8f0fe" stroke="#4a6fa5"/>
  <text x="760" y="225" text-anchor="middle" font-size="12" font-weight="600">Viṣṇu expansions</text>
  <text x="760" y="245" text-anchor="middle" font-size="10">primary incarnations</text>
  <line x1="450" y1="140" x2="160" y2="200" stroke="#4a6fa5" stroke-width="2" marker-end="url(#ah)"/>
  <line x1="450" y1="140" x2="360" y2="200" stroke="#4a6fa5" stroke-width="2" marker-end="url(#ah)"/>
  <line x1="450" y1="140" x2="560" y2="200" stroke="#4a6fa5" stroke-width="2" marker-end="url(#ah)"/>
  <line x1="450" y1="140" x2="760" y2="200" stroke="#4a6fa5" stroke-width="2" marker-end="url(#ah)"/>
  <rect x="120" y="320" width="660" height="120" rx="8" fill="#fff" stroke="#888"/>
  <text x="450" y="350" text-anchor="middle" font-size="13" font-weight="600">Living entities (jīvas)</text>
  <text x="450" y="375" text-anchor="middle" font-size="11">Eternal parts and parcels — qualitatively one, quantitatively different</text>
  <line x1="450" y1="260" x2="450" y2="320" stroke="#4a6fa5" stroke-width="2" marker-end="url(#ah)"/>
  <text x="60" y="480" font-family="Segoe UI,sans-serif" font-size="11">Source map:</text>
  <text x="60" y="500" font-size="10">CC Adi 2 · SB 1.3 (incarnations) · BG 10.42 (opulence sample) · BG 15.7 (jīva)</text>
  <text x="60" y="530" font-size="10">Rights: kutumba-original line diagram — no copyrighted deity art</text>
  <text x="450" y="600" text-anchor="middle" font-size="11" fill="#666">THEO-VIS-KRISHNA-EXP-001 · human doctrinal review required</text>
</svg>
'''


def main() -> int:
    OUT.write_text(SVG, encoding="utf-8")
    sys.path.insert(0, str(Path(__file__).parent))
    try:
        from render_png_derivatives import render_svg_to_png

        render_svg_to_png(OUT, PNG)
        print(f"Wrote {OUT.name} and {PNG.name}")
    except Exception as exc:  # noqa: BLE001
        print(f"SVG written; PNG skipped: {exc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
