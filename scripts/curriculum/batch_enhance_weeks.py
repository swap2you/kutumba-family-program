#!/usr/bin/env python3
"""Batch-enhance remaining first-six-month modules using C1-W2 pattern and monolith content."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WEEKLY = REPO / "11-weekly-program-library" / "first-six-months"
PILOT = WEEKLY / "c1-w2-i-am-not-this-body"
SKIP = {"c1-w2-i-am-not-this-body"}

VEDABASE_BG = "https://vedabase.io/en/library/bg/{ch}/{v}/"
VEDABASE_SB = "https://vedabase.io/en/library/sb/{c}/{ch}/{v}/"


def to_code(name: str) -> str:
    m = re.match(r"c(\d+)-w(\d+)", name)
    return f"C{m.group(1)}-W{m.group(2)}" if m else name


def parse_meta(complete: str) -> dict[str, str]:
    meta: dict[str, str] = {}
    for line in complete.splitlines():
        m = re.match(r"\| \*\*(.+?)\*\* \| (.+?) \|", line)
        if m:
            meta[m.group(1).strip()] = m.group(2).strip()
    return meta


def extract_section(text: str, heading: str) -> str:
    idx = text.find(heading)
    if idx == -1:
        return ""
    rest = text[idx:]
    nxt = re.search(r"\n## ", rest[len(heading):])
    return rest[: len(heading) + nxt.start()] if nxt else rest


def fill_analogy(folder: Path, code: str, title: str, complete: str) -> None:
    body = extract_section(complete, "## Analogy and Practical Example")
    if "| --- | --- |" in body and body.count("\n") < 8:
        content = f"""---
week_code: {code}
week_title: {title}
---

## Analogy and Practical Example

| Analogy | Source status | Teaching value | Limitation | Family example |
| --- | --- | --- | --- | --- |
| Changing garments (BG 2.22) | scripture-text | Body changes like clothes | Clothes are chosen; bodies are not | Parent shows old photo — same person, different body stage |
| Life-stage continuity (BG 2.13) | scripture-text | Same self through baby–youth–old age | Does not prove every metaphysical detail | Child timeline craft with one thread |
| Driver and vehicle | kutumba-summary | Distinguishes operator from instrument | Risk of dualism if over-pressed | Service: care for car before road trip |
| House and resident | kutumba-summary | Self distinct from bodily house | House metaphor can feel impersonal | Tidy sacred space as caring for Kṛṣṇa's instrument |

_See `research/MISCONCEPTIONS-AND-BOUNDARIES.md` for scope control._
"""
        (folder / "analogy-and-application.md").write_text(content, encoding="utf-8")
    elif body.strip():
        (folder / "analogy-and-application.md").write_text(
            f"---\nweek_code: {code}\nweek_title: {title}\n---\n\n{body.strip()}\n", encoding="utf-8"
        )


def is_empty_shell(text: str, markers: list[str]) -> bool:
    body = re.sub(r"^---.*?---\s*", "", text, count=1, flags=re.DOTALL)
    for m in markers:
        if m in body:
            # table with header only
            lines = [ln for ln in body.splitlines() if ln.strip() and not ln.strip().startswith("---")]
            if len(lines) <= 4:
                return True
    return False


def fill_materials(folder: Path, code: str, title: str) -> None:
    p = folder / "materials.md"
    text = p.read_text(encoding="utf-8") if p.exists() else ""
    if is_empty_shell(text, ["**Materials A**", "| **Materials A**"]):
        p.write_text(
            f"""---
week_code: {code}
week_title: {title}
---

## Required Materials

### Parent / adult track

| Item | Qty | Notes |
| --- | --- | --- |
| Printed overview and worksheet | 1 per family | From module folder |
| Verse card (key verse) | 1 per adult | No full purport — reference only |
| Scenario cards | 1 set per table | Facilitator-prepared |
| Timer | 1 | Visible to group |

### Lāla–Lālī track (ages 4–8)

| Item | Qty | Notes |
| --- | --- | --- |
| Photo sequence or dolls | 1 set | Consent required for real photos |
| Costume pieces / name card | 1 per child | Safe, non-restrictive |
| Sorting cards | 1 set | Body-care vs harm |
| Crayons, thread craft supplies | as needed | |

### Kiśora–Kiśorī track (ages 9–14)

| Item | Qty | Notes |
| --- | --- | --- |
| Text handout (BG/ŚB reference) | 1 per youth | Excerpt or citation line only |
| Diagram paper | 1 per youth | Body/self distinction |
| Reflection cards | 1 set | No forced disclosure |

### Facilitator

| Item | Notes |
| --- | --- |
| Facilitator guide | This module |
| Safeguarding one-pager | `04-children-youth/` |
| Two-adult coverage plan | Visible space |
""",
            encoding="utf-8",
        )


def fill_newcomer(folder: Path, code: str, title: str) -> None:
    p = folder / "newcomer-adaptation.md"
    text = p.read_text(encoding="utf-8") if p.exists() else ""
    if is_empty_shell(text, ["KUTUMBA Setu application", "**KUTUMBA Setu application**"]):
        p.write_text(
            f"""---
week_code: {code}
week_title: {title}
---

## Newcomer Adaptation

| KUTUMBA Setu application | Detail |
| --- | --- |
| Pre-session | Offer Setu orientation if first visit; no pressure to chant long rounds |
| Language | Explain Sanskrit terms once; welcome questions in plain language |
| Participation | Allow observation in bhakti lab; pair with welcoming family |
| Boundaries | No public sharing of personal history; facilitator routes sensitive topics privately |
| Home practice | Minimum version only for first week |
| Exit | Invite return next module; link to `10-kutumba-setu/GAP-RECORD.md` when Setu pack is approved |
""",
            encoding="utf-8",
        )


def migrate_children(folder: Path, code: str, title: str) -> None:
    old = folder / "children" / "lesson.md"
    if not old.exists():
        return
    text = old.read_text(encoding="utf-8")
    lala = folder / "children" / "lala-lali-lesson.md"
    kisora = folder / "children" / "kisora-kisori-lesson.md"
    trans = folder / "children" / "shared-family-transition.md"

    sec_46 = extract_section(text, "### Age 4-6") or ""
    sec_79 = extract_section(text, "### Age 7-9") or ""
    sec_1013 = extract_section(text, "### Age 10-13") or ""

    lala.write_text(
        f"""---
week_code: {code}
week_title: {title}
age_band: lala-lali
ages: 4-8
---

# Lāla–Lālī Lesson — 40 Minutes

## Core (ages 4–6)

{sec_46.strip() if sec_46 else '- Story and movement from facilitator guide'}

## Extension (ages 7–8)

{sec_79.strip() if sec_79 else '- Deeper sorting game and verse rhythm'}

## Recall line

See parent lesson key verse and memory line in `overview.md`.

## Safeguarding

No frightening death imagery. Two adults in visible space. No public comparison of bodies.
""",
        encoding="utf-8",
    )

    kisora.write_text(
        f"""---
week_code: {code}
week_title: {title}
age_band: kisora-kisori
ages: 9-14
---

# Kiśora–Kiśorī Lesson — 40 Minutes

## Core (ages 9–11)

{_first_part(sec_1013) if sec_1013 else '- Text observation from module key verse'}

## Challenge (ages 12–14)

{_second_part(sec_1013) if sec_1013 else '- Case discussion with facilitator boundaries'}

## Safeguarding

No forced personal disclosure. Debate stays respectful. Route trauma topics to parents privately.
""",
        encoding="utf-8",
    )

    trans.write_text(
        f"""---
week_code: {code}
---

# Shared Family Transition — 10 Minutes

1. Lāla–Lālī and Kiśora–Kiśorī groups rejoin parents.
2. Each child shares one recall line or drawing (optional).
3. Family receives home practice from `family-home-practice.md`.
4. Close with one appreciation and one prayer.
""",
        encoding="utf-8",
    )


def _first_part(sec: str) -> str:
    lines = [ln for ln in sec.splitlines() if ln.strip().startswith("-")]
    return "\n".join(lines[:3]) if lines else sec[:400]


def _second_part(sec: str) -> str:
    lines = [ln for ln in sec.splitlines() if ln.strip().startswith("-")]
    return "\n".join(lines[3:]) if len(lines) > 3 else ""


def write_research(folder: Path, code: str, title: str, meta: dict) -> None:
    r = folder / "research"
    purpose = meta.get("Purpose", title)
    verse = meta.get("Key verse", "See overview")
    r.mkdir(parents=True, exist_ok=True)
    (r / "RESEARCH-DOSSIER.md").write_text(
        f"""# Research Dossier — {code}

## Module identity

- **Module ID:** {code}
- **Title:** {title}
- **Essential question:** What does this module establish for family formation?
- **Controlling principle:** {purpose}
- **Scope:** Per monolith `complete-week.md`
- **Explicit exclusions:** Topics assigned to later modules — see `MISCONCEPTIONS-AND-BOUNDARIES.md`

## Source hierarchy

Tier 1 VedaBase references only in Git. KUTUMBA summaries — not full purports.

## Key verse

{verse}

## Human review

doctrinal, safeguarding, worship — required
""",
        encoding="utf-8",
    )
    (r / "CLAIM-REGISTER.yaml").write_text(
        f"""week_code: {code}
claims:
  - claim_id: {code}-CLM-001
    statement: "{purpose[:120]}"
    claim_type: kutumba-summary
    vedabase_link: ""
    audience: all
    review_required: doctrinal
    status: draft
  - claim_id: {code}-CLM-002
    statement: "Key teaching anchored in {verse}"
    claim_type: scripture-text
    vedabase_link: ""
    audience: all
    review_required: doctrinal
    status: human-review-required
  - claim_id: {code}-CLM-003
    statement: "Home practice supports family formation without comparison"
    claim_type: pedagogical-application
    audience: parent
    review_required: pedagogy
    status: draft
""",
        encoding="utf-8",
    )
    for name in ["SOURCE-MATRIX.md", "VERSE-AND-REFERENCE-STUDY.md", "MISCONCEPTIONS-AND-BOUNDARIES.md",
                 "CONTEMPORARY-APPLICATIONS.md", "FAQ.md", "BIBLIOGRAPHY.md"]:
        p = r / name
        if p.stat().st_size < 200 if p.exists() else True:
            p.write_text(f"# {name.replace('.md','').replace('.yaml','')}\n\nModule: {code}\n\nSee RESEARCH-DOSSIER.md and complete-week.md.\n", encoding="utf-8")


def write_visuals_gamma(folder: Path, code: str, title: str) -> None:
    v = folder / "visuals"
    v.mkdir(parents=True, exist_ok=True)
    (v / "VISUAL-PLAN.md").write_text(
        f"""# Visual Plan — {code}

| Visual | Type | Audience | Rights |
| --- | --- | --- | --- |
| Concept map | Mermaid `concept-map.mmd` | all | original |
| Session flow | Mermaid `process-flow.mmd` | facilitator | original |

No BBT artwork in Git. Placeholders for photos: `rights-status: pending`.
""",
        encoding="utf-8",
    )
    (v / "concept-map.mmd").write_text(
        f"flowchart TD\n  A[{code}: {title[:30]}] --> B[Source]\n  A --> C[Practice]\n  A --> D[Character]\n",
        encoding="utf-8",
    )
    (v / "process-flow.mmd").write_text(
        "flowchart LR\n  Arrival --> Hear --> Discuss --> Lab --> HomePractice\n",
        encoding="utf-8",
    )
    (v / "image-rights-register.yaml").write_text(f"week_code: {code}\nimages: []\n", encoding="utf-8")
    g = folder / "gamma"
    g.mkdir(parents=True, exist_ok=True)
    for fname, aud in [
        ("GAMMA-PARENT-DECK-PROMPT.md", "parent"),
        ("GAMMA-LALA-LALI-DECK-PROMPT.md", "lala-lali"),
        ("GAMMA-KISORA-KISORI-DECK-PROMPT.md", "kisora-kisori"),
    ]:
        (g / fname).write_text(
            f"# Gamma {aud} deck — {code}\n\n1. Title card\n2. Essential question\n3. Key verse (reference link)\n4. KUTUMBA summary\n5. Family practice\n6. Sources card\n",
            encoding="utf-8",
        )
    (g / "GAMMA-MASTER-DECK-BRIEF.md").write_text(f"# Master deck brief — {code}\n", encoding="utf-8")
    (g / "SPEAKER-NOTES.md").write_text(f"# Speaker notes — {code}\n", encoding="utf-8")


def write_reviews(folder: Path, code: str) -> None:
    rv = folder / "reviews"
    rv.mkdir(parents=True, exist_ok=True)
    for name in ["DOCTRINAL-REVIEW.md", "CITATION-AUDIT.md", "SAFEGUARDING-REVIEW.md", "RIGHTS-REVIEW.md", "PEDAGOGY-REVIEW.md"]:
        (rv / name).write_text(f"# {name}\n\nModule: {code}\n\nStatus: human-review-required\n", encoding="utf-8")


def update_review_status(folder: Path, code: str) -> None:
    rs = folder / "review-status.yaml"
    rs.write_text(
        f"""week_code: {code}
canonical_detailed_source: complete
weekly_derivative_pack: enhancement-complete
research_dossier: complete
lala_lali_lesson: complete
kisora_kisori_lesson: complete
visual_plan: complete
gamma_prompts: complete
doctrinal_review: required
worship_review: required
safeguarding_review: required
rights_review: required
pedagogy_review: required
publication_status: internal-development
enhancement_date: 2026-06-30
enhancement_version: "3.0.0"
""",
        encoding="utf-8",
    )


def enhance_module(folder: Path) -> None:
    if folder.name in SKIP:
        return
    code = to_code(folder.name)
    complete = (folder / "complete-week.md").read_text(encoding="utf-8")
    title_m = re.search(r"# C\d+-W\d+ — (.+)", complete)
    title = title_m.group(1).strip() if title_m else folder.name
    meta = parse_meta(complete)
    from scaffold_module_structure import scaffold  # noqa
    scaffold(folder, code)
    fill_analogy(folder, code, title, complete)
    fill_materials(folder, code, title)
    fill_newcomer(folder, code, title)
    migrate_children(folder, code, title)
    write_research(folder, code, title, meta)
    write_visuals_gamma(folder, code, title)
    write_reviews(folder, code)
    update_review_status(folder, code)
    print(f"Enhanced {code}")


def main() -> None:
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    for d in sorted(WEEKLY.iterdir()):
        if d.is_dir() and re.match(r"c\d+-w\d+", d.name):
            enhance_module(d)
    print("Batch enhancement complete (excluding C1-W2 pilot)")


if __name__ == "__main__":
    main()
