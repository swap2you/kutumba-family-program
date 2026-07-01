#!/usr/bin/env python3
"""Generate module contact sheets for Cycle 1 visuals."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
GALLERY = REPO / "build-evidence" / "visual-contact-sheets"


def main() -> int:
    GALLERY.mkdir(parents=True, exist_ok=True)
    index_lines = ["# Cycle 1 Visual Contact Sheets\n", "| Module | Sheet |\n", "|---|---|\n"]
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c1-w"):
            continue
        manifest_path = d / "visuals" / "VISUAL-ASSET-MANIFEST.yaml"
        if not manifest_path.exists():
            continue
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        module_id = manifest.get("module_id", d.name)
        lines = [f"# {module_id} Visual Contact Sheet\n", "| Asset ID | Class | PNG | Source register | Rights | Review |\n", "|---|---|---|---|---|---|\n"]
        for asset in manifest.get("assets", []):
            aid = asset["asset_id"]
            png_rel = f"../../{d.relative_to(REPO).as_posix()}/visuals/png/{aid}.png"
            lines.append(
                f"| `{aid}` | {asset.get('asset_class','')} | ![{aid}]({png_rel}) | module register | "
                f"{asset.get('rights_status','')} | {asset.get('doctrinal_review','')} |\n"
            )
        sheet = GALLERY / f"{module_id}-CONTACT-SHEET.md"
        sheet.write_text("".join(lines), encoding="utf-8")
        index_lines.append(f"| {module_id} | [{module_id}]({sheet.name}) |\n")
    (GALLERY / "INDEX.md").write_text("".join(index_lines), encoding="utf-8")
    print(f"Contact sheets -> {GALLERY.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
