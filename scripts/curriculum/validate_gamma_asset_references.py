#!/usr/bin/env python3
"""Validate Cycle 1 Gamma asset-complete packaging (V8)."""
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

ALLOWED_STATUS = {
    "assets-complete-upload-required",
    "rendered-unreviewed",
    "post-render-reviewed",
    "approved-for-internal-pilot",
    "structural-scaffold",
    "content-complete-assets-missing",
}
FORBIDDEN_IN_DECKS = [
    "photo timeline placeholder",
    "table from visual-plan",
    "[image: placeholder]",
    "generic icon instructions",
]
PLACEHOLDER_SVG_MARKERS = ["Asset class:", "Source anchors: see module research pack"]


def main() -> int:
    failures = []
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        g = d / "gamma"
        for name in ["GAMMA-ASSET-MAP.yaml", "GAMMA-RENDER-CHECKLIST.md", "GAMMA-POST-RENDER-QA.md"]:
            if not (g / name).exists():
                failures.append(f"{d.name}: missing gamma/{name}")
        am = g / "GAMMA-ASSET-MAP.yaml"
        if am.exists():
            data = yaml.safe_load(am.read_text(encoding="utf-8")) or {}
            status = data.get("render_status", "")
            if status == "render-ready":
                failures.append(f"{d.name}: deprecated render-ready status")
            if status not in ALLOWED_STATUS:
                failures.append(f"{d.name}: invalid render_status {status}")
            for c in data.get("cards", []):
                svg_rel = c.get("svg") or c.get("path", "")
                png_rel = c.get("png", "")
                fp = d / svg_rel if svg_rel else None
                if fp and not fp.exists():
                    failures.append(f"{d.name}: gamma asset missing {svg_rel}")
                if png_rel and not (d / png_rel).exists():
                    failures.append(f"{d.name}: gamma PNG missing {png_rel}")
                if not c.get("speaker_note"):
                    failures.append(f"{d.name}: card {c.get('card_number')} missing speaker note")
                if fp and fp.exists():
                    text = fp.read_text(encoding="utf-8", errors="ignore")
                    if any(m in text for m in PLACEHOLDER_SVG_MARKERS):
                        failures.append(f"{d.name}: placeholder SVG {svg_rel}")
        for deck in g.glob("GAMMA-*-DECK-PROMPT.md"):
            low = deck.read_text(encoding="utf-8", errors="ignore").lower()
            for pat in FORBIDDEN_IN_DECKS:
                if pat in low:
                    failures.append(f"{d.name}: {deck.name} contains '{pat}'")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PASS: Cycle 1 Gamma asset-complete packaging OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
