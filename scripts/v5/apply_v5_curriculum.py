#!/usr/bin/env python3
"""Apply V5 curriculum depth: source briefs, newcomer adaptations, prem-ki-katha, katha registers.

Usage:
  python scripts/v5/apply_v5_curriculum.py              # apply from module_curriculum_data.yaml
  python scripts/v5/apply_v5_curriculum.py --write-yaml   # regenerate module_curriculum_data.yaml only
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
DATA_PATH = Path(__file__).parent / "module_curriculum_data.yaml"
MODULES_ROOT = REPO / "11-weekly-program-library" / "first-six-months"
LECTURE_CATALOG = REPO / "14-research-source-register" / "media-library" / "PRABHUPADA-LECTURE-CATALOG.yaml"
TODAY = date.today().isoformat()

LOCKED_KATHA_SLUG = "c1-w2-i-am-not-this-body"
SKIP_NEWCOMER_IDS = {"C1-W2"}
INTEGRATION_IDS = {"C1-W6", "C2-W6", "C3-W6"}
KATHA_MIN_WORDS = 900
KATHA_MAX_WORDS = 1500
INTEGRATION_KATHA_MIN = 600
INTEGRATION_KATHA_MAX = 850

NEWCOMER_SECTIONS = [
    "minimum_concept",
    "terms_define",
    "terms_defer",
    "reduced_source_load",
    "parent_participation",
    "lala_lali_placement",
    "kisora_kisori_placement",
    "lab_adaptation",
    "home_practice_minimum",
    "sensitive_topic_caution",
    "host_family_action",
    "setu_bridge",
    "follow_up_path",
]


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def find_module_dir(slug: str) -> Path | None:
    for d in MODULES_ROOT.iterdir():
        if d.is_dir() and d.name == slug:
            return d
    parts = slug.split("-")[:2]
    prefix = "-".join(parts)
    for d in MODULES_ROOT.iterdir():
        if d.is_dir() and d.name.startswith(prefix):
            return d
    return None


def load_lecture_catalog() -> dict[str, dict]:
    if not LECTURE_CATALOG.exists():
        return {}
    data = yaml.safe_load(LECTURE_CATALOG.read_text(encoding="utf-8"))
    out: dict[str, dict] = {}
    for entry in data.get("entries", []):
        out[entry["media_id"]] = entry
    return out


def newcomer_is_substantive(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    if "KUTUMBA Setu" in text and word_count(text) >= 180:
        return True
    return all(s.replace("_", " ") in text.lower() or s.replace("_", "-") in text.lower() for s in NEWCOMER_SECTIONS[:6])


def render_source_brief(mod: dict) -> str:
    se = mod["source_expansion"]
    books = "\n".join(
        f"| {b['ref']} | [{b['url']}]({b['url']}) | {b['use']} |"
        for b in se["controlling_books"]
    )
    lectures = se.get("lectures") or []
    if lectures:
        lec_lines = "\n".join(
            f"| {l.get('media_id', '—')} | {l['date']} | {l['place']} | {l['title']} | "
            f"[VedaBase]({l['url']}) | {l.get('topic', '')} | {l.get('segment', 'full lecture')} |"
            for l in lectures
        )
        lec_table = f"""| Media ID | Date | Place | Title | URL | Topic | Segment |
| --- | --- | --- | --- | --- | --- | --- |
{lec_lines}"""
    else:
        lec_table = "_No catalogued lecture entry yet — research ticket KUT-RES-LECTURE-{mod['module_id']}_001._"

    katha_rows = "\n".join(
        f"| {k['ref']} | [{k['url']}]({k['url']}) | {k['use']} |"
        for k in se.get("katha_sources", [])
    )
    edu = "\n".join(f"- [{e['label']}]({e['url']}) — {e.get('use', 'pedagogy reference')}" for e in se.get("education", [])) or "- _No relevant official resource selected — KUTUMBA original adaptation required._"
    child = "\n".join(f"- {c}" for c in se.get("child_resources", [])) or "- ISKCON Education books-for-kids index — metadata only; KUTUMBA adaptation required"
    media = "\n".join(f"- [{m['label']}]({m['url']}) — {m.get('use', 'media candidate')}" for m in se.get("media", [])) or "- See module `MEDIA-INDEX.yaml` — no reviewed download committed"
    supp = "\n".join(f"- {s}" for s in se.get("supplementary", [])) or "- None directly required for this module"
    excl = "\n".join(f"- {e}" for e in se.get("excluded", [])) or "- None stated"
    claims = "\n".join(
        f"| {c['claim']} | {c['source_ref']} | [{c['url']}]({c['url']}) | {c['module_use']} |"
        for c in se.get("claim_mapping", [])
    )
    tier_a = "\n".join(f"- [{u}]({u})" for u in se.get("tier_a_urls", []))

    return f"""# Source Expansion Brief — {mod['module_id']}

| Field | Value |
|-------|-------|
| Module | {mod['title']} |
| Generated | {TODAY} |
| Source map | KUT-SRC-0013 |
| Human review | **OPEN** |

## 1. Controlling Prabhupāda book references

| Reference | VedaBase URL | Module use |
| --- | --- | --- |
{books}

## 2. Prabhupāda lecture / conversation / letter candidates

{lec_table}

## 3. Source-grounded kathā references

| Range | VedaBase URL | Kathā use |
| --- | --- | --- |
{katha_rows}

Align narrative claims with `katha/KATHA-SOURCE-REGISTER.yaml`. Paraphrase only in repository.

## 4. Official education / pedagogy resources

{edu}

## 5. Child-resource candidates

{child}

## 6. Media candidates

{media}

## 7. Supplementary Gauḍīya / Sanātana references

{supp}

## 8. Sources intentionally excluded

{excl}

## 9. Rights posture

- Default: **link-and-metadata-only**
- BBT material: permission workflow before republication
- No bulk transcript or purport storage in Git

## 10. Review required

| Review type | Status |
| --- | --- |
| Doctrinal | OPEN |
| Citation | OPEN |
| Pedagogy | OPEN |
| Rights | OPEN |

## Source-to-claim mapping

| Curriculum claim | Source ref | VedaBase / catalog URL | Module use |
| --- | --- | --- | --- |
{claims}

## Tier A entry points

{tier_a}

## Coverage scores (not publication approval)

| Dimension | Score |
| --- | --- |
| Primary text coverage | exact-linked |
| Prabhupāda spoken source coverage | {'catalog-linked' if lectures else 'candidate-identified'} |
| Katha coverage | human-review-required |
| Parent application coverage | draft-complete |
| Lala Lali coverage | draft-complete |
| Kisora Kisori coverage | draft-complete |
| Visual media coverage | metadata-only |
| Rights readiness | link-and-metadata-only |
| Human review readiness | open |
"""


def render_newcomer(mod: dict) -> str:
    nc = mod["newcomer"]
    define = "\n".join(f"- **{t['term']}** — {t['plain']}" for t in nc["terms_define"])
    defer = "\n".join(f"- {t}" for t in nc["terms_defer"])

    return f"""---
week_code: {mod['module_id']}
week_title: {mod['title']}
component: newcomer-adaptation.md
adaptation_version: v5.0.0
generated: {TODAY}
---

## Newcomer Adaptation

Apply KUTUMBA Setu principles: reduce Sanskrit load, explain terms once, offer opt-in participation, and never pressure personal disclosure.

### Minimum concept

{nc['minimum_concept']}

### Terms to define (once, plain English)

{define}

### Terms to defer (optional reading / later weeks)

{defer}

### Reduced source load

{nc['reduced_source_load']}

### Parent participation option

{nc['parent_participation']}

### Lāla–Lālī placement

{nc['lala_lali_placement']}

### Kiśora–Kiśorī placement

{nc['kisora_kisori_placement']}

### Laboratory adaptation

{nc['lab_adaptation']}

### Home practice minimum

{nc['home_practice_minimum']}

### Sensitive-topic caution

{nc['sensitive_topic_caution']}

### Host-family action

{nc['host_family_action']}

### KUTUMBA Setu bridge

{nc['setu_bridge']}

### Follow-up path

{nc['follow_up_path']}
"""


def render_prem_katha(mod: dict) -> str:
    k = mod["katha"]
    integration = mod["module_id"] in INTEGRATION_IDS
    exception_note = ""
    if integration:
        exception_note = (
            f"word_count_target: {INTEGRATION_KATHA_MIN}-{INTEGRATION_KATHA_MAX}\n"
            f"integration_exception: documented — synthesis/showcase module; no new principal līlā\n"
        )

    links_table = "\n".join(
        f"| {row['label']} | [vedabase]({row['url']}) | {row['use']} |"
        for row in k["primary_sources"]
    )
    narrative = "\n\n".join(k["narrative_paragraphs"])
    personalities = "\n".join(f"- **{p['name']}** — {p['role']}" for p in k.get("personalities", []))
    lala = "\n".join(f"{i}. {line}" for i, line in enumerate(k["lala_cues"], 1))
    kisora = "\n".join(f"{i}. {line}" for i, line in enumerate(k["kisora_cues"], 1))
    cautions = "\n".join(f"- {c}" for c in k.get("cautions", []))
    visuals = "\n".join(
        f"| {i} | {v['visual']} | {v['source']} |"
        for i, v in enumerate(k.get("visual_beats", []), 1)
    )

    setting = k.get("setting", "_[Facilitator transition — quiet room, families seated together]_")
    heart = k.get("heart_reflection", 'Ask inwardly: "What one understanding from this katha should not leave me this week?"')
    transition = k.get(
        "lesson_transition",
        '"The katha opened the heart; the lesson trains precise understanding. Both serve Kṛṣṇa."',
    )

    return f"""---
week_code: {mod['module_id']}
week_title: {mod['title']}
component: prem-ki-katha.md
katha_type: {k.get('katha_type', 'source-grounded-devotional-narrative')}
{exception_note}---

# Prem-kī-Kathā — {k['title']}

## 1. Katha title

**{k['title']}** — {k.get('subtitle', 'source-grounded devotional narrative for family hearing')}

## 2. Module connection

{k['module_connection']}

**Scope boundary:** {k.get('scope_boundary', 'See parent-lesson.md for full doctrinal scope.')}

## 3. Primary source references

| Source | Link | Use in katha |
|---|---|---|
{links_table}

Full registry: [`katha/KATHA-SOURCE-REGISTER.yaml`](katha/KATHA-SOURCE-REGISTER.yaml)

## 4. Setting and devotional mood

{setting}

## 5. Main personalities

{personalities}

## 6. Source-grounded narrative

_[Source narrative / paraphrase — not invented dialogue]_

{narrative}

## 7. Turning point

{k['turning_point']}

## 8. Central teaching

{k['central_teaching']}

**Memory line:** {k['memory_line']}

## 9. Heart reflection

_[60 seconds silence]_

{heart}

Optional soft chant: one round of the mahā-mantra together.

## 10. Lāla–Lālī interaction cues

{lala}

## 11. Kiśora–Kiśorī reflection cues

{kisora}

## 12. Parent bridge

{k['parent_bridge']}

## 13. Transition to philosophy lesson

_{transition}_

→ Continue with [`parent-lesson.md`](parent-lesson.md) or age-track lessons.

## 14. Narration cautions

{cautions}
- Do **not** invent direct quotes in "Kṛṣṇa said…" form unless reading from authorized text
- Keep total narration within **12–15 minutes** plus interaction

## 15. Visual / storyboard plan

| Beat | Visual | Source |
|---|---|---|
{visuals}

## 16. Rights and quotation status

- No full purports or book chapters in repository
- Narrative is **paraphrase** from sources linked above
- No invented sacred dialogue presented as direct quotation

## 17. Human doctrinal review status

**Status:** `human-review-required` — see [`reviews/DOCTRINAL-REVIEW.md`](reviews/DOCTRINAL-REVIEW.md)

---

_Modern entry hook (not katha):_ [`opening-hook.md`](opening-hook.md)
"""


def render_katha_register(mod: dict) -> str:
    k = mod["katha"]
    links = "\n".join(
        f"  - label: {s['label']}\n    url: {s['url']}" for s in k["primary_sources"]
    )
    verses = "\n".join(f"  - {v}" for v in k.get("exact_verses", []))
    paraphrase = "\n".join(f"  - {p}" for p in k.get("paraphrased_portions", []))
    omitted = "\n".join(f"  - {o}" for o in k.get("omitted", []))
    cautions = "\n".join(f"  - {c}" for c in k.get("cautions", []))

    return f"""module_id: {mod['module_id']}
katha_title: "{k['title']}"
primary_book: {k.get('primary_book', 'See primary sources')}
chapter_reference: "{k.get('chapter_reference', '')}"
stable_links:
{links}
exact_verses_used:
{verses}
direct_quotations: []
paraphrased_portions:
{paraphrase}
facilitator_transitions:
  - Modern family pause before philosophy block
  - Bridge to home practice
omitted_complex_details:
{omitted}
audience_cautions:
{cautions}
doctrinal_reviewer: pending
rights_status: scripture-reference-links-only
approval_status: human-review-required
"""


def apply_module(mod: dict, stats: dict) -> None:
    slug = mod["slug"]
    mod_dir = find_module_dir(slug)
    if mod_dir is None:
        stats["warnings"].append(f"Module directory not found: {slug}")
        return

    research = mod_dir / "research"
    research.mkdir(parents=True, exist_ok=True)
    brief_path = research / "SOURCE-EXPANSION-BRIEF.md"
    brief_path.write_text(render_source_brief(mod), encoding="utf-8")
    stats["source_briefs"] += 1

    mid = mod["module_id"]
    newcomer_path = mod_dir / "newcomer-adaptation.md"
    if mid in SKIP_NEWCOMER_IDS and newcomer_is_substantive(newcomer_path):
        stats["newcomer_skipped"].append(mid)
    else:
        newcomer_path.write_text(render_newcomer(mod), encoding="utf-8")
        stats["newcomer"] += 1

    if slug == LOCKED_KATHA_SLUG:
        stats["katha_skipped"].append(mid)
    else:
        katha_path = mod_dir / "prem-ki-katha.md"
        katha_text = render_prem_katha(mod)
        katha_path.write_text(katha_text, encoding="utf-8")
        body = re.sub(r"^---.*?---\s*", "", katha_text, count=1, flags=re.DOTALL)
        wc = word_count(body)
        min_w = INTEGRATION_KATHA_MIN if mid in INTEGRATION_IDS else KATHA_MIN_WORDS
        if wc < min_w:
            stats["warnings"].append(f"{mid}: prem-ki-katha {wc} words (target {min_w}+)")
        stats["katha"] += 1

        katha_dir = mod_dir / "katha"
        katha_dir.mkdir(parents=True, exist_ok=True)
        (katha_dir / "KATHA-SOURCE-REGISTER.yaml").write_text(render_katha_register(mod), encoding="utf-8")
        stats["registers"] += 1


def load_or_build_data() -> dict:
    if DATA_PATH.exists():
        return yaml.safe_load(DATA_PATH.read_text(encoding="utf-8"))
    from module_data_builder import build_all_modules  # type: ignore

    return build_all_modules()


def write_yaml(data: dict) -> None:
    DATA_PATH.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if "--write-yaml" in argv:
        sys.path.insert(0, str(Path(__file__).parent))
        from module_data_builder import build_all_modules

        data = build_all_modules()
        write_yaml(data)
        print(f"Wrote {DATA_PATH} ({len(data.get('modules', []))} modules)")
        return 0

    if not DATA_PATH.exists():
        print("module_curriculum_data.yaml missing — run with --write-yaml first", file=sys.stderr)
        return 1

    data = yaml.safe_load(DATA_PATH.read_text(encoding="utf-8"))
    stats = {
        "source_briefs": 0,
        "newcomer": 0,
        "katha": 0,
        "registers": 0,
        "newcomer_skipped": [],
        "katha_skipped": [],
        "warnings": [],
    }
    for mod in data.get("modules", []):
        apply_module(mod, stats)

    print(f"V5 curriculum applied — {stats['source_briefs']} source briefs, "
          f"{stats['newcomer']} newcomer files ({len(stats['newcomer_skipped'])} skipped), "
          f"{stats['katha']} kathas ({len(stats['katha_skipped'])} locked), "
          f"{stats['registers']} katha registers")
    if stats["newcomer_skipped"]:
        print(f"  Newcomer preserved (gold pilot): {', '.join(stats['newcomer_skipped'])}")
    if stats["katha_skipped"]:
        print(f"  Katha preserved (gold pilot): {', '.join(stats['katha_skipped'])}")
    for w in stats["warnings"]:
        print(f"  WARN: {w}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
