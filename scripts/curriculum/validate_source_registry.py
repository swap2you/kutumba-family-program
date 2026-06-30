#!/usr/bin/env python3
"""Validate sources.yaml and research source matrices."""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

def week_code(name: str) -> str:
    import re
    m = re.match(r"(c\d-w\d+)", name)
    return m.group(1).upper().replace("c", "C").replace("-w", "-W") if m else name

def main() -> int:
    failures = []
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir():
            continue
        sy = d / "sources.yaml"
        if not sy.exists():
            failures.append(f"{d.name}: missing sources.yaml")
            continue
        t = sy.read_text(encoding="utf-8")
        sm = d / "research" / "SOURCE-MATRIX.md"
        has_matrix = sm.exists() and "vedabase" in sm.read_text(encoding="utf-8").lower()
        has_yaml = "vedabase" in t.lower() or "url:" in t or "tier" in t.lower()
        if not has_yaml and not has_matrix:
            failures.append(f"{week_code(d.name)}: missing tier-1 source links in sources.yaml or SOURCE-MATRIX")
        if sm.exists() and len(sm.read_text(encoding="utf-8").splitlines()) < 10:
            failures.append(f"{week_code(d.name)}: SOURCE-MATRIX too thin")
    if failures:
        for f in failures[:20]:
            print(f"FAIL: {f}")
        return 1
    print("PASS: source registry checks OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())
