#!/usr/bin/env python3
"""Build master VISUAL-ASSET-CATALOG and per-module VISUAL-SOURCE-REGISTER files."""
from __future__ import annotations

import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
CATALOG = REPO / "14-research-source-register" / "visual-asset-library" / "VISUAL-ASSET-CATALOG.yaml"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    entries = []
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        manifest_path = d / "visuals" / "VISUAL-ASSET-MANIFEST.yaml"
        if not manifest_path.exists():
            continue
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        module_id = manifest.get("module_id", "")
        register_assets = []
        for asset in manifest.get("assets", []):
            aid = asset["asset_id"]
            svg = d / "visuals" / "rendered" / f"{aid}.svg"
            png = d / "visuals" / "png" / f"{aid}.png"
            entry = {
                "asset_id": aid,
                "module_id": module_id,
                "module_path": d.relative_to(REPO).as_posix(),
                "asset_class": asset.get("asset_class"),
                "svg_path": asset.get("path"),
                "png_path": f"visuals/png/{aid}.png" if png.exists() else None,
                "rights_status": asset.get("rights_status", "kutumba-original"),
                "alt_text": asset.get("alt_text", ""),
                "doctrinal_review": asset.get("doctrinal_review", "human-review-required"),
                "substance_class": "kutumba-original-teaching-visual",
            }
            if svg.exists():
                entry["svg_sha256"] = sha256(svg)
                entry["svg_bytes"] = svg.stat().st_size
            if png.exists():
                entry["png_sha256"] = sha256(png)
                entry["png_bytes"] = png.stat().st_size
            entries.append(entry)
            register_assets.append(
                {
                    "asset_id": aid,
                    "source_keys": asset.get("source_keys", ["module-research-pack"]),
                    "rights_status": asset.get("rights_status", "kutumba-original"),
                    "review_status": "human-review-required",
                }
            )
        reg_path = d / "visuals" / "VISUAL-SOURCE-REGISTER.yaml"
        reg_path.write_text(
            yaml.safe_dump(
                {
                    "module_id": module_id,
                    "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                    "assets": register_assets,
                },
                sort_keys=False,
                allow_unicode=True,
            ),
            encoding="utf-8",
        )
    CATALOG.parent.mkdir(parents=True, exist_ok=True)
    CATALOG.write_text(
        yaml.safe_dump(
            {
                "catalog_version": "1.0.0",
                "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "total_assets": len(entries),
                "assets": entries,
            },
            sort_keys=False,
            allow_unicode=True,
        ),
        encoding="utf-8",
    )
    print(f"Catalog: {len(entries)} assets -> {CATALOG.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
