#!/usr/bin/env python3
"""Run all curriculum enhancement validation gates."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = [
    "audit_empty_sections.py",
    "validate_week_schema.py",
    "validate_age_bands.py",
    "detect_copyright_risk.py",
]

def main() -> int:
    failed = False
    for s in SCRIPTS:
        p = Path(__file__).parent / s
        print(f"\n=== {s} ===")
        r = subprocess.run([sys.executable, str(p)], cwd=ROOT)
        if r.returncode != 0:
            failed = True
    # Also run repository validator
    print("\n=== Validate-KutumbaRepository.ps1 ===")
    r2 = subprocess.run(
        ["powershell", "-File", str(ROOT / "scripts" / "Validate-KutumbaRepository.ps1")],
        cwd=ROOT,
    )
    if r2.returncode != 0:
        failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
