#!/usr/bin/env python3
"""Move short prem-ki-katha hooks to opening-hook.md (preserve provenance)."""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
SKIP_NEW_KATHA = {"c1-w2-i-am-not-this-body"}  # C1-W2 gets new authentic katha separately


def main() -> None:
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir():
            continue
        prem = d / "prem-ki-katha.md"
        hook = d / "opening-hook.md"
        if not prem.exists():
            continue
        if d.name in SKIP_NEW_KATHA and hook.exists():
            continue
        text = prem.read_text(encoding="utf-8")
        if hook.exists() and len(hook.read_text(encoding="utf-8")) > 200:
            continue
        body = re.sub(r"^---.*?---\s*", "", text, count=1, flags=re.DOTALL).strip()
        hook_content = text.split("---", 2)
        fm = hook_content[1] if text.startswith("---") and len(hook_content) > 2 else ""
        header = "---\n" + fm + "---\n\n" if fm else ""
        hook_md = header + f"""## Opening Hook (modern scenario)

_This is a contemporary entry point — not Prem-kī-Kathā. See `prem-ki-katha.md` for the devotional narrative._

{body}

**Provenance:** Migrated from legacy `prem-ki-katha.md` during post-audit remediation (v3.0.0).
"""
        hook.write_text(hook_md, encoding="utf-8", newline="\n")
        if d.name not in SKIP_NEW_KATHA:
            print(f"Migrated hook: {d.name}")


if __name__ == "__main__":
    main()
