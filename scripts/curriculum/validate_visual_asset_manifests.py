#!/usr/bin/env python3
"""Validate Cycle 1 VISUAL-ASSET-MANIFEST.yaml and rendered files."""
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"


def main() -> int:
    failures = []
    ok = 0
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        manifest = d / "visuals" / "VISUAL-ASSET-MANIFEST.yaml"
        if not manifest.exists():
            failures.append(f"{d.name}: missing VISUAL-ASSET-MANIFEST.yaml")
            continue
        data = yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}
        assets = data.get("assets", [])
        if len(assets) < 6:
            failures.append(f"{d.name}: fewer than 6 manifest assets ({len(assets)})")
        for a in assets:
            rel = a.get("path", "")
            fp = d / rel.replace("/", "\\") if "\\" not in rel else d / rel
            fp = d / rel
            if not fp.exists():
                failures.append(f"{d.name}: missing {rel}")
            elif fp.stat().st_size < 50:
                failures.append(f"{d.name}: zero-byte or tiny {rel}")
            elif not a.get("alt_text"):
                failures.append(f"{d.name}: no alt_text for {a.get('asset_id')}")
            else:
                ok += 1
        alt = d / "visuals" / "ALT-TEXT.md"
        if not alt.exists():
            failures.append(f"{d.name}: missing ALT-TEXT.md")
    if failures:
        for f in failures[:40]:
            print(f"FAIL: {f}")
        return 1
    print(f"PASS: Cycle 1 visual manifests OK ({ok} assets)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
