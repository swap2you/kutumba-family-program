#!/usr/bin/env python3
"""Build local Cycle 1 Gamma upload bundle (script + manifest; ZIP optional)."""
from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
EXPORT_ROOT = REPO / "build-evidence" / "exports" / "Cycle-1-Gamma-Bundle"
MANIFEST = REPO / "build-evidence" / "V8-GAMMA-BUNDLE-MANIFEST.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if EXPORT_ROOT.exists():
        shutil.rmtree(EXPORT_ROOT)
    EXPORT_ROOT.mkdir(parents=True, exist_ok=True)
    bundle_index = []
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        code = d.name.split("-")[0].upper() + "-" + d.name.split("-")[1].upper()
        out = EXPORT_ROOT / code
        out.mkdir(parents=True, exist_ok=True)
        gamma = d / "gamma"
        for name in [
            "GAMMA-PARENT-DECK-PROMPT.md",
            "GAMMA-LALA-LALI-DECK-PROMPT.md",
            "GAMMA-KISORA-KISORI-DECK-PROMPT.md",
            "GAMMA-ASSET-MAP.yaml",
            "GAMMA-POST-RENDER-QA.md",
        ]:
            src = gamma / name
            if src.exists():
                dest_name = name.replace("GAMMA-", "").replace("-DECK-PROMPT", "-prompt").lower()
                shutil.copy2(src, out / dest_name)
        assets_dir = out / "assets"
        assets_dir.mkdir(exist_ok=True)
        for png in (d / "visuals" / "png").glob("*.png"):
            shutil.copy2(png, assets_dir / png.name)
        for svg in (d / "visuals" / "rendered").glob("*.svg"):
            shutil.copy2(svg, assets_dir / svg.name)
        qa = out / "QA.md"
        qa.write_text(
            f"# {code} Gamma QA\n\n- Status: assets-complete-upload-required\n- Human doctrinal review: OPEN\n",
            encoding="utf-8",
        )
        bundle_index.append({"module": code, "path": str(out.relative_to(REPO)), "asset_count": len(list(assets_dir.glob("*")))})
    MANIFEST.write_text(
        json.dumps(
            {
                "generated": datetime.now(timezone.utc).isoformat(),
                "modules": bundle_index,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    zip_path = EXPORT_ROOT.parent / "Cycle-1-Gamma-Bundle.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in EXPORT_ROOT.rglob("*"):
            if f.is_file():
                zf.write(f, f.relative_to(EXPORT_ROOT.parent))
    print(f"Bundle: {EXPORT_ROOT.relative_to(REPO)} ({len(bundle_index)} modules)")
    print(f"ZIP (local export): {zip_path.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
