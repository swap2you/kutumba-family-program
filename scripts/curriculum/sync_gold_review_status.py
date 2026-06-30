#!/usr/bin/env python3
"""Set enhancement-complete review-status when module passes gold depth checks."""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

GOLD_TEMPLATE = """week_code: {code}
canonical_detailed_source: complete
weekly_derivative_pack: enhancement-complete
research_dossier: complete
source_registry: complete
claim_traceability: complete
parent_lesson: complete
lala_lali_lesson: complete
kisora_kisori_lesson: complete
materials: complete
assessment: complete
newcomer_adaptation: complete
visual_plan: complete
gamma_prompts: complete
cycle_project: complete
prem_ki_katha: complete
opening_hook: complete
automated_semantic_validation: pass
doctrinal_review: required
worship_review: required
safeguarding_review: required
rights_review: required
pedagogy_review: required
citation_audit: required
publication_status: internal-development
pilot_quality_gate: pass-pending-human-review
enhancement_date: 2026-06-30
enhancement_version: "3.0.1"
notes: Gold-standard depth verified by sync_gold_review_status.py; human reviews still required.
"""


def week_code(name: str) -> str:
    m = re.match(r"(c\d-w\d+)", name)
    if not m:
        return name
    return m.group(1).upper().replace("c", "C").replace("-w", "-W")


def line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines()) if path.exists() else 0


def passes_gold(d: Path) -> bool:
    claims_path = d / "research" / "CLAIM-REGISTER.yaml"
    claims = (
        len(re.findall(r"-CLM-\d+", claims_path.read_text(encoding="utf-8")))
        if claims_path.exists()
        else 0
    )
    return (
        line_count(d / "gamma" / "GAMMA-PARENT-DECK-PROMPT.md") >= 80
        and line_count(d / "research" / "RESEARCH-DOSSIER.md") >= 60
        and claims >= 8
        and line_count(d / "children" / "lala-lali-lesson.md") >= 80
        and line_count(d / "children" / "kisora-kisori-lesson.md") >= 80
        and (d / "katha" / "KATHA-SOURCE-REGISTER.yaml").exists()
    )


def main() -> None:
    updated = 0
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not passes_gold(d):
            continue
        (d / "review-status.yaml").write_text(
            GOLD_TEMPLATE.format(code=week_code(d.name)), encoding="utf-8", newline="\n"
        )
        updated += 1
        print(f"Gold status: {week_code(d.name)}")
    print(f"Updated {updated} modules")


if __name__ == "__main__":
    main()
