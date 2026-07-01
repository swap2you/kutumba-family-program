#!/usr/bin/env python3
"""Validate Cycle 1 Gamma render-readiness files."""
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"


def main() -> int:
    failures = []
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        g = d / "gamma"
        for name in [
            "GAMMA-ASSET-MAP.yaml",
            "GAMMA-RENDER-CHECKLIST.md",
            "GAMMA-POST-RENDER-QA.md",
        ]:
            if not (g / name).exists():
                failures.append(f"{d.name}: missing gamma/{name}")
        am = g / "GAMMA-ASSET-MAP.yaml"
        if am.exists():
            data = yaml.safe_load(am.read_text(encoding="utf-8")) or {}
            if data.get("render_status") != "render-ready":
                failures.append(f"{d.name}: gamma not render-ready")
            for c in data.get("cards", []):
                fp = d / c.get("path", "")
                if c.get("path") and not fp.exists():
                    failures.append(f"{d.name}: gamma asset missing {c['path']}")
        master = g / "GAMMA-MASTER-DECK-BRIEF.md"
        if master.exists() and "[IMAGE:" in master.read_text(encoding="utf-8"):
            failures.append(f"{d.name}: master brief still has IMAGE placeholder")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return 1
    print("PASS: Cycle 1 Gamma render-readiness files OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
