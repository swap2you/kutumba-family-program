#!/usr/bin/env python3
"""Cross-check master VISUAL-ASSET-CATALOG against module manifests."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
CATALOG = REPO / "14-research-source-register" / "visual-asset-library" / "VISUAL-ASSET-CATALOG.yaml"


def main() -> int:
    if not CATALOG.exists():
        print(f"FAIL: missing {CATALOG.relative_to(REPO)}")
        return 1
    catalog = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    cat_ids = {a["asset_id"] for a in catalog.get("assets", [])}
    manifest_ids = set()
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        mpath = d / "visuals" / "VISUAL-ASSET-MANIFEST.yaml"
        if not mpath.exists():
            continue
        m = yaml.safe_load(mpath.read_text(encoding="utf-8"))
        manifest_ids.update(a["asset_id"] for a in m.get("assets", []))
    if cat_ids != manifest_ids:
        missing = manifest_ids - cat_ids
        extra = cat_ids - manifest_ids
        if missing:
            print(f"FAIL: catalog missing {missing}")
        if extra:
            print(f"FAIL: catalog extra {extra}")
        return 1
    print(f"PASS: catalog consistent ({len(cat_ids)} assets)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
