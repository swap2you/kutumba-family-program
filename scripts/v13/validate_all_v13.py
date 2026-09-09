#!/usr/bin/env python3
"""Run W1 immutable check plus validate_week for every registry entry that has exports."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
V13 = Path(__file__).resolve().parent
REGISTRY = V13 / "week_registry.yaml"
EXPORTS = REPO / "exports" / "final" / "v13"


def main() -> int:
    immutable = subprocess.run(
        [sys.executable, str(V13 / "check_w1_immutable.py")],
        cwd=REPO,
    )
    if immutable.returncode != 0:
        print("ABORT — W1 immutable check failed; skipping week validation")
        return immutable.returncode

    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    weeks = data["weeks"]
    validated = 0
    failed: list[str] = []
    skipped: list[str] = []
    for entry in weeks:
        export_dir = EXPORTS / Path(entry["export_subdir"])
        has_exports = export_dir.is_dir() and any(export_dir.glob("*.pdf"))
        if not has_exports:
            skipped.append(entry["id"])
            continue
        print(f"\n=== validate {entry['id']} ===")
        result = subprocess.run(
            [sys.executable, str(V13 / "validate_week.py"), "--week", entry["id"], "--skip-immutable"],
            cwd=REPO,
        )
        validated += 1
        if result.returncode != 0:
            failed.append(entry["id"])

    print("\n=== validate_all_v13 summary ===")
    print(f"Registry weeks: {len(weeks)}")
    print(f"Validated (exports present): {validated}")
    print(f"Skipped (no exports yet): {len(skipped)}")
    if skipped:
        print("Skipped: " + ", ".join(skipped))
    print(f"Failed: {len(failed)}")
    if failed:
        print("Failed weeks: " + ", ".join(failed))
        return 1
    print("PASS — immutable OK; all weeks with exports validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
