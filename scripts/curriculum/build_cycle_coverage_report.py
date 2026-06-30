#!/usr/bin/env python3
"""Build cycle coverage report."""
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
EVIDENCE = REPO / "build-evidence"
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

def cycle_modules(c: int) -> list[Path]:
    return sorted([d for d in WEEKLY.iterdir() if d.is_dir() and d.name.startswith(f"c{c}-")])

def main() -> None:
    lines = ["# Cycle Coverage Report", "", f"Generated: 2026-06-30", ""]
    for c in (1, 2, 3):
        mods = cycle_modules(c)
        complete = sum(1 for m in mods if (m / "review-status.yaml").read_text(encoding="utf-8").find("enhancement-complete") >= 0)
        lines += [f"## Cycle {c}", "", f"- Modules: {len(mods)}", f"- enhancement-complete: {complete}", ""]
        for m in mods:
            code = m.name.split("-")[0].upper() + "-" + m.name.split("-")[1].upper()
            lines.append(f"- {code}: `{m.name}`")
        lines.append("")
    (EVIDENCE / "CYCLE-COVERAGE-REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Cycle coverage report written")

if __name__ == "__main__":
    main()
