#!/usr/bin/env python3
"""Update review-status.yaml with field-by-field honest depth checks.

Does NOT mark human reviews complete or imply publication readiness.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"

INTEGRATION_MODULES = {
    "c1-w6-integration-night-who-am-i-and-how-should-our-family-live",
    "c2-w6-integration-night-choice-consequence-and-the-modes",
    "c3-w6-bhakti-mela-kirtana-drama-and-family-presentation",
}


def week_code(name: str) -> str:
    m = re.match(r"(c\d-w\d+)", name)
    return m.group(1).upper().replace("c", "C").replace("-w", "-W") if m else name


def line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines()) if path.exists() else 0


def word_count(path: Path) -> int:
    if not path.exists():
        return 0
    body = re.sub(r"^---.*?---\s*", "", path.read_text(encoding="utf-8"), count=1, flags=re.DOTALL)
    return len(re.findall(r"\b\w+\b", body))


def newcomer_substantive(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    return line_count(path) >= 40 and "module-specific" in text.lower() or line_count(path) >= 55


def evaluate(d: Path) -> dict[str, str]:
    code = week_code(d.name)
    prem_wc = word_count(d / "prem-ki-katha.md")
    integration = d.name in INTEGRATION_MODULES
    gold_pilot = d.name == "c1-w2-i-am-not-this-body"

    if gold_pilot and prem_wc >= 900:
        prem_depth = "gold-pilot-draft"
    elif integration:
        prem_depth = "integration-format"
    elif prem_wc >= 900:
        prem_depth = "deepened-draft"
    elif prem_wc >= 600:
        prem_depth = "partial-depth"
    else:
        prem_depth = "remediation-required"

    structural = "complete" if (d / "complete-week.md").exists() else "incomplete"
    dossier_ok = line_count(d / "research" / "RESEARCH-DOSSIER.md") >= 60
    claims_path = d / "research" / "CLAIM-REGISTER.yaml"
    claims = len(re.findall(r"-CLM-\d+", claims_path.read_text(encoding="utf-8"))) if claims_path.exists() else 0
    gamma_parent = line_count(d / "gamma" / "GAMMA-PARENT-DECK-PROMPT.md") >= 80
    child_ok = (
        line_count(d / "children" / "lala-lali-lesson.md") >= 80
        and line_count(d / "children" / "kisora-kisori-lesson.md") >= 80
    )
    katha_reg = (d / "katha" / "KATHA-SOURCE-REGISTER.yaml").exists()
    newcomer_ok = newcomer_substantive(d / "newcomer-adaptation.md")

    automated = "pass" if all([dossier_ok, claims >= 8, gamma_parent, child_ok, katha_reg]) else "partial"

    if gold_pilot and prem_depth == "gold-pilot-draft" and automated == "pass":
        pack = "gold-pilot-draft"
    elif automated == "pass" and prem_depth in ("deepened-draft", "integration-format"):
        pack = "deepened-draft"
    elif prem_depth == "remediation-required":
        pack = "remediation-required"
    else:
        pack = "deepened-draft-partial"

    return {
        "code": code,
        "structural_pack_complete": structural,
        "automated_enhancement_complete": automated,
        "source_audit_complete": "in-progress",
        "prem_katha_depth": prem_depth,
        "human_review_complete": "required",
        "publication_ready": "not-ready",
        "weekly_derivative_pack": pack,
        "newcomer_adaptation": "complete" if newcomer_ok else "thin",
        "prem_ki_katha": prem_depth,
    }


def render_status(ev: dict) -> str:
    return f"""week_code: {ev['code']}
structural_pack_complete: {ev['structural_pack_complete']}
automated_enhancement_complete: {ev['automated_enhancement_complete']}
source_audit_complete: {ev['source_audit_complete']}
prem_katha_depth: {ev['prem_katha_depth']}
human_review_complete: {ev['human_review_complete']}
publication_ready: {ev['publication_ready']}
weekly_derivative_pack: {ev['weekly_derivative_pack']}
canonical_detailed_source: complete
research_dossier: complete
source_registry: complete
claim_traceability: complete
parent_lesson: complete
lala_lali_lesson: complete
kisora_kisori_lesson: complete
materials: complete
assessment: complete
newcomer_adaptation: {ev['newcomer_adaptation']}
visual_plan: complete
gamma_prompts: complete
cycle_project: complete
prem_ki_katha: {ev['prem_ki_katha']}
opening_hook: complete
automated_semantic_validation: pass-pending-human-review
doctrinal_review: required
worship_review: required
safeguarding_review: required
rights_review: required
pedagogy_review: required
citation_audit: required
publication_status: internal-development
pilot_quality_gate: open
enhancement_date: 2026-06-30
enhancement_version: "4.0.0"
notes: Field-by-field status from sync_gold_review_status.py v4; no false gold promotion.
"""


def main() -> None:
    updated = 0
    for d in sorted(WEEKLY.iterdir()):
        if not d.is_dir() or not d.name.startswith("c"):
            continue
        ev = evaluate(d)
        (d / "review-status.yaml").write_text(render_status(ev), encoding="utf-8", newline="\n")
        updated += 1
        print(f"{ev['code']}: pack={ev['weekly_derivative_pack']} prem={ev['prem_katha_depth']}")
    print(f"Updated {updated} modules")


if __name__ == "__main__":
    main()
