"""Detect clipped generator artifacts in curriculum markdown."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SCAN_ROOTS = [REPO / "11-weekly-program-library" / "first-six-months"]

# Short word fragment + exactly three dots at end of line (generator clip)
CLIP_RE = re.compile(r"\b([a-z]{4,8})\.\.\.\s*$")
SLICE_MARKER = re.compile(r"\[:\d+\]")
ALLOWLIST = re.compile(r"\[TRUNCATION-ALLOWED\]")


def scan_file(path: Path) -> list[str]:
    issues = []
    try:
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
    except OSError:
        return issues
    if ALLOWLIST.search(text):
        return issues
    for i, line in enumerate(lines, 1):
        if "vedabase.io/.../" in line or ("http" in line and "/.../" in line):
            continue
        if SLICE_MARKER.search(line):
            issues.append(f"{path.relative_to(REPO)}:{i}: generator-slice-marker")
        m = CLIP_RE.search(line)
        if m and m.group(1).lower() not in ("etc", "viz", "https"):
            issues.append(f"{path.relative_to(REPO)}:{i}: clipped: ...{line.strip()[-45:]}")
    return issues


def main() -> int:
    all_issues: list[str] = []
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            all_issues.extend(scan_file(path))
    if all_issues:
        for issue in all_issues[:50]:
            sys.stdout.buffer.write((f"FAIL: {issue}\n").encode("utf-8", errors="replace"))
        print(f"Total truncation artifacts: {len(all_issues)}")
        return 1
    print("PASS: no truncation artifacts detected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
