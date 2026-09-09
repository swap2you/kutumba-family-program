#!/usr/bin/env python3
"""Hash and freeze accepted C1-W1 files for V13 immutable baseline checks."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
W1 = REPO / "11-weekly-program-library/first-six-months/c1-w1-what-is-kutumba-and-why-are-we-here"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def collect() -> list[Path]:
    paths: list[Path] = [
        REPO / "V12_2-WEEK1-START-HERE.md",
        W1 / "complete-week.md",
        W1 / "teacher/MAIN-FACILITATOR-GUIDE-V12.md",
        W1 / "teacher/PARENT-GUIDE.md",
        W1 / "teacher/YOUNGER-TEACHER-GUIDE.md",
        W1 / "teacher/OLDER-TEACHER-GUIDE.md",
        W1 / "gamma/V12-GAMMA-MASTER-DECK-PROMPT.md",
    ]
    for folder in (
        "activities/v12_2-younger",
        "activities/v12_2-older",
        "activities/v12_2-parent",
        "visuals/v12_2_1",
    ):
        d = W1 / folder
        if d.is_dir():
            paths.extend(sorted(p for p in d.iterdir() if p.is_file()))
    exp = REPO / "exports/final/week1"
    if exp.is_dir():
        paths.extend(sorted(p for p in exp.iterdir() if p.is_file()))
    scripts = REPO / "scripts/v12_2_1"
    if scripts.is_dir():
        paths.extend(sorted(scripts.glob("*.py")))
    for name in (
        "V12_2_1-WEEK1-VISUAL-QA.md",
        "V12_2_1-WEEK1-OPERATOR-ACCEPTANCE.md",
        "V12_2_1-WEEK1-REMOTE-ACCEPTANCE.md",
        "V12_2_1-WEEK1-BASELINE-FAILURES.md",
    ):
        paths.append(REPO / "build-evidence" / name)
    return paths


def main() -> None:
    files = []
    for path in collect():
        rel = path.resolve().relative_to(REPO.resolve()).as_posix()
        if not path.is_file():
            files.append({"path": rel, "missing": True})
            continue
        data = path.read_bytes()
        files.append({"path": rel, "bytes": len(data), "sha256": sha256(path)})
    out = {
        "baseline_tag": "v12.2.1-week1-publishing-closed",
        "baseline_head": "408c9e9127fe87c976ac7b958f90d31cef370d33",
        "created": "2026-09-09",
        "protected_file_count": sum(1 for f in files if not f.get("missing")),
        "files": files,
    }
    dest = REPO / "build-evidence" / "V13-W1-IMMUTABLE-BASELINE.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {dest} files={out['protected_file_count']}")


if __name__ == "__main__":
    main()
