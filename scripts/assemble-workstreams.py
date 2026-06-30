#!/usr/bin/env python3
"""Generate workstream scaffolding, legacy analysis, and prompt library skeleton."""

from datetime import datetime, timezone
from pathlib import Path
import shutil

REPO_ROOT = Path(r"C:\Development\Workspace\DevotionalRepo\kutumba-family-program")
PROMPT_SRC = REPO_ROOT / "KUTUMBA_CURSOR_PROMPT_LIBRARY_v2" / "KUTUMBA_CURSOR_PROMPT_LIBRARY_v2"


def w(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def workstream_gaps():
  w(REPO_ROOT / "09-digital-repository-publishing" / "README.md", """# Digital Repository, Drive, Website and Digital Library

## Status: SOURCE NOT YET SUPPLIED

No dedicated operating document was found in the KUTUMBA SANGA source folder.

## Established decisions (from Master Operating Model)

Digital repository and publishing capabilities are referenced as Workstream 9. Specific procedures, drive structure, website boundaries, and publication manifest rules are not yet supplied as a completed document.

## Expected deliverables

- Digital repository operating manual
- Drive/folder taxonomy aligned to workstreams
- Website and public-facing boundary policy
- Publication manifest and export controls
- Copyright and derivative-use workflow

## Gap record

See `09-digital-repository-publishing/GAP-RECORD.md` and production prompt `16-prompt-library/09-digital-publishing/produce-digital-repository-operating-model.md`.
""")

  w(REPO_ROOT / "09-digital-repository-publishing" / "GAP-RECORD.md", """# Gap Record — Digital Repository and Publishing

| Field | Value |
|---|---|
| Workstream | 9 — Repository, Drive, Website and Digital Library |
| Status | SOURCE NOT YET SUPPLIED |
| Reviewer | Digital Lead |
| Production prompt | `16-prompt-library/09-digital-publishing/produce-digital-repository-operating-model.md` |
""")

  w(REPO_ROOT / "10-kutumba-setu" / "README.md", """# KUTUMBA Setu

## Status: DRAFT REQUIRED

No dedicated KUTUMBA Setu source document was supplied in the KUTUMBA SANGA folder.

## Purpose

Bridge materials connecting families, facilitators, temple alignment, and onboarding.

## Gap record

See `10-kutumba-setu/GAP-RECORD.md`.
""")

  w(REPO_ROOT / "10-kutumba-setu" / "GAP-RECORD.md", """# Gap Record — KUTUMBA Setu

| Field | Value |
|---|---|
| Component | KUTUMBA Setu |
| Status | DRAFT REQUIRED |
| Reviewer | Setu Lead |
| Production prompt | `16-prompt-library/00-orchestration/produce-kutumba-setu-material.md` |
""")


def curriculum_architecture():
    arch = REPO_ROOT / "02-curriculum-architecture"
    w(arch / "CURRICULUM-MAP.md", """# Three-Year Curriculum Map

| Year | Theme | Focus |
|---|---|---|
| Year 1 | Sambandha | Family foundations and relationship with Kṛṣṇa |
| Year 2 | Abhidheya | Regulated practice and deepening sādhana |
| Year 3 | Śāstric readiness | Service, leadership, Bhakti Śāstrī readiness boundary |

Canonical source: `02-curriculum-architecture/THREE-YEAR-CURRICULUM-ARCHITECTURE.md`

## Annual structure

- 40 active weeks per year
- Cycle and off-week logic per three-year architecture document
- First six months: 18 active detailed sessions (Cycles 1–3) — **complete in source**
""")
    w(arch / "DOMAIN-MATRIX.md", "# Domain Matrix\n\nSee canonical `THREE-YEAR-CURRICULUM-ARCHITECTURE.md` for full domain matrix.\n")
    w(arch / "PREREQUISITE-MAP.md", "# Prerequisite Map\n\nSee canonical three-year architecture document.\n")
    w(arch / "SOURCE-COVERAGE-MAP.md", "# Source Coverage Map\n\nFirst six months: full detailed source supplied. Years 1–3 beyond month six: architecture only; detailed lessons not yet supplied.\n")
    w(arch / "LESSON-PRODUCTION-BACKLOG.md", """# Lesson Production Backlog

| Year | Cycle | Week | Status |
|---|---|---|---|
| Year 1 | Cycles 4+ | Future weeks | designed-architecture-only |
| Year 2 | All | — | designed-architecture-only |
| Year 3 | All | — | designed-architecture-only |
| First 6 months | C1–C3 | C1-W1 … C3-W6 | detailed-lesson-complete |

Do not generate shallow placeholder lessons for future years. Use `15-templates/DETAILED-WEEK-LESSON-TEMPLATE.md` when producing new weeks.
""")


def lesson_template():
    w(REPO_ROOT / "15-templates" / "DETAILED-WEEK-LESSON-TEMPLATE.md", """# Detailed Week Lesson Template

Required metadata: week_code, cycle, title, purpose, outcomes, key verse, review status.

## Required sections

1. Learning Outcomes
2. Primary Śrīla Prabhupāda Sources
3. Prem-kī-Kathā Script
4. Parent Lesson (40 minutes)
5. Children's Parallel Lesson (age 4–6, 7–9, 10–13)
6. Analogy and Practical Example
7. Questions: Discovery, Understanding, Application
8. Bhakti Laboratory
9. Family Home Practice
10. Slide Outline
11. Teacher Preparation
12. Required Materials
13. Assessment
14. Newcomer Adaptation
15. Risks and Sensitive Points
16. Printable Worksheet
17. This Week's Saṅkalpa

Quality standard: match `03-first-six-months/FIRST-SIX-MONTH-DETAILED-CURRICULUM.md` depth.
""")


def legacy_analysis():
    reg = REPO_ROOT / "14-research-source-register"
    w(reg / "LEGACY-BHAKTIVRIKSHA-CROSSWALK.md", """# Legacy Bhaktivriksha Crosswalk

**Status:** reference-only — no silent import

Indexed files: see `00-source-materials/03-external-reference-index/LEGACY-BHAKTIVRIKSHA-FILE-INDEX.csv` (1,595 files, BV Material subfolder excluded to prevent double-count).

## Classification summary

| Disposition | Notes |
|---|---|
| reference only | Default for all indexed legacy BV files |
| rights review required | Before any adoption or redistribution |
| doctrinal review required | Before sequence or content adaptation |
| worship review required | For any liturgical or ceremony content |
| safety review required | For children/youth modules |

## KUTUMBA authority

KUTUMBA governance, three-year architecture, first-six-month curriculum, child-safety model, and temple-alignment boundaries override legacy Bhaktivriksha structure.

No legacy module is canonical without formal adoption record citing source file ID, path, reason, modifications, and reviewer.
""")
    w(reg / "JAYAPATAKA-SWAMI-BV-MATERIAL-CROSSWALK.md", """# Jayapataka Swami BV Material Crosswalk

Indexed: 68 files in `JAYAPATAKA-SWAMI-BV-MATERIAL-INDEX.csv`.

**Default disposition:** reference only / rights review required.

Potential relevance: facilitator training patterns, BV operational checklists. Requires explicit adoption review before use in KUTUMBA.
""")
    w(reg / "GRANTH-TOPIC-CATALOG.md", """# Granth Topic Catalog

110 PDFs indexed in `GRANTH-PDF-CATALOG.csv`. Metadata only — not bulk-copied.

Use for research ticket creation. Prioritize Śrīla Prabhupāda's published books and authorized sources for canonical citations.
""")
    w(reg / "RESEARCH-BACKLOG.md", """# Research Backlog

| ID | Topic | Priority | Status |
|---|---|---|---|
| RB-001 | Map legacy BV lesson titles to KUTUMBA cycle domains | medium | not-started |
| RB-002 | Verify Granth PDF rights before any in-repo excerpt | high | not-started |
| RB-003 | Temple alignment check for worship content in Chat 7 manual | high | worship-review-required |
""")
    w(reg / "SOURCE-GAP-MAP.md", """# Source Gap Map

| Workstream | Supplied | Gap |
|---|---|---|
| Master Operating Model | yes | — |
| Governance | yes | — |
| Three-Year Architecture | yes | detailed future weeks |
| First Six Months | yes (18 sessions) | — |
| Children/Youth | yes | — |
| Parent Formation | yes | — |
| Prasāda Operations | yes | — |
| Kīrtana/Worship/Bhakti Labs | yes | worship review |
| Festivals/Calendar | yes | — |
| Digital Repository | **no** | operating manual required |
| KUTUMBA Setu | **no** | draft required |
""")
    w(REPO_ROOT / "17-reviews-and-audits" / "LEGACY-ADOPTION-REVIEW.md", """# Legacy Adoption Review

## Verdict

**No legacy content adopted in initial build.**

All legacy collections remain reference-only per `REFERENCE-RIGHTS-AND-USE-REVIEW.md`.

## Required before any adoption

- Source file ID and path citation
- Rights disposition
- Doctrinal / worship / safety reviewer sign-off
- Modification log vs. original
""")


PROMPT_DEFS = [
    ("00-orchestration/import-new-source-document.md", "Import a new KUTUMBA source document into the repository with manifest, hash, and canonical normalization."),
    ("00-orchestration/produce-kutumba-setu-material.md", "Produce KUTUMBA Setu bridge materials from governing decisions only — no fabrication of authority."),
    ("01-governance/produce-complete-operating-model.md", "Produce a complete workstream operating model matching KUTUMBA document depth."),
    ("02-curriculum-architecture/produce-six-week-cycle.md", "Produce a six-week cycle outline aligned to three-year architecture — architecture only unless detailed source supplied."),
    ("03-detailed-week-production/produce-detailed-weekly-lesson.md", "Produce one complete detailed weekly lesson matching first-six-month standard."),
    ("04-children-youth/generate-age-banded-child-adaptations.md", "Generate age-banded child adaptations (4–6, 7–9, 10–13) from parent lesson and sources."),
    ("05-parent-formation/produce-parent-formation-material.md", "Produce parent formation session material with citations and home practice."),
    ("06-prasadam-operations/produce-prasada-operations-material.md", "Produce prasāda and hospitality operations content from supplied models."),
    ("07-kirtana-worship/produce-bhakti-laboratory.md", "Produce bhakti laboratory content — worship review gate required."),
    ("08-festivals-yatras/produce-festival-yatra-pack.md", "Produce festival/yātrā pack — safety and temple alignment review required."),
    ("09-digital-publishing/produce-digital-repository-operating-model.md", "Produce digital repository operating model when authorized."),
    ("09-digital-publishing/update-publication-manifest.md", "Update publication manifest and export controls."),
    ("10-source-research/verify-citations.md", "Verify citations against authorized sources — never fabricate URLs."),
    ("11-quality-review/review-safeguarding-content.md", "Review children/youth content for safeguarding compliance."),
    ("11-quality-review/review-worship-content.md", "Review worship and liturgical content for temple authorization."),
    ("11-quality-review/generate-family-facing-derivative.md", "Generate family-facing derivative from canonical facilitator content."),
    ("11-quality-review/complete-independent-repository-audit.md", "Complete independent repository audit per Prompt 10."),
    ("12-remediation/remediate-audit-findings.md", "Remediate audit findings with evidence."),
    ("12-remediation/resume-interrupted-work.md", "Resume interrupted repository build from CURRENT-STATUS.md."),
]


def prompt_library():
    lib = REPO_ROOT / "16-prompt-library"
    w(lib / "README.md", f"""# KUTUMBA Internal Prompt Library

Version: 1.0.0 (initial build {datetime.now(timezone.utc).strftime('%Y-%m-%d')})

Reusable prompts for consistent content production without depending on a single chat session.

External bootstrap pack: `00-orchestration/external-bootstrap-pack/`
""")
    for rel, purpose in PROMPT_DEFS:
        w(lib / rel, f"""# {Path(rel).stem.replace('-', ' ').title()}

## Purpose

{purpose}

## Source inputs

- Relevant canonical documents in workstream folders
- `00-source-materials/SOURCE-MANIFEST.yaml`
- Governing decisions from Master Operating Model and Governance Charter

## Scope

As stated in purpose.

## Exclusions

- No invented citations or worship procedures
- No bulk copyrighted copying
- No private family data
- No shallow summaries replacing detailed operating models

## Required output files

Per task specification in `CURRENT-STATUS.md` and workstream README.

## Citation rules

Prioritize Śrīla Prabhupāda's published books and authorized ISKCON/temple standards. Never fabricate URLs.

## Copyright rules

Reference-only for legacy collections. Paraphrase; do not reproduce long copyrighted passages.

## Privacy rules

No private family records or secrets in Git.

## Review gates

- Doctrinal review when teachings are extended
- Worship review for liturgical content
- Safety review for children/youth content
- Rights review for third-party material

## Quality checklist

- [ ] Linked to source_id and source_hash
- [ ] Depth matches KUTUMBA baseline documents
- [ ] Review status recorded
- [ ] CURRENT-STATUS.md updated

## Validation

Run `scripts/Validate-KutumbaRepository.ps1` before commit.

## Git commit expectation

Concise message describing workstream and artifact produced.
""")

    # Copy external bootstrap pack
    ext_dest = lib / "00-orchestration" / "external-bootstrap-pack"
    if PROMPT_SRC.exists():
        if ext_dest.exists():
            shutil.rmtree(ext_dest)
        shutil.copytree(PROMPT_SRC, ext_dest)
    w(lib / "VERSION.md", f"""# Prompt Library Version Record

| Version | Date | Notes |
|---|---|---|
| 1.0.0 | {datetime.now(timezone.utc).strftime('%Y-%m-%d')} | Initial internal library from KUTUMBA Cursor Prompt Library v2 |
""")


def document_style_guide():
    w(REPO_ROOT / "15-templates" / "DOCUMENT-STYLE-GUIDE.md", """# KUTUMBA Document Style Guide

Derived from supplied operating documents (Master Operating Model, Governance Charter, First Six-Month Curriculum).

## Structure conventions

- Numbered top-level sections for operating models
- Document-control metadata in opening sections where present
- Tables for maps, roles, and curriculum grids
- Explicit cautions, boundaries, and review status language
- Age-banded headings for children's content (4–6, 7–9, 10–13)

## Visual baseline

Original DOCX files in `00-source-materials/01-current-kutumba-originals/` remain authoritative visual baselines.

Markdown is the canonical working source for search and Git review.

Automated DOCX regeneration: **later controlled capability** — not claimed in initial build.
""")


def content_coverage():
    w(REPO_ROOT / "build-evidence" / "CONTENT-COVERAGE-REPORT.md", """# Content Coverage Report

## Operating documents supplied and normalized

| Document | Canonical path | Status |
|---|---|---|
| Master Operating Model | `00-foundation/MASTER-OPERATING-MODEL.md` | normalized |
| Governance Charter | `01-governance/GOVERNANCE-CHARTER-AND-TEMPLE-RELATIONSHIP.md` | normalized |
| Three-Year Architecture | `02-curriculum-architecture/THREE-YEAR-CURRICULUM-ARCHITECTURE.md` | normalized |
| First Six-Month Curriculum | `03-first-six-months/FIRST-SIX-MONTH-DETAILED-CURRICULUM.md` | normalized |
| Children/Youth Model | `04-children-youth/CHILDREN-YOUTH-FORMATION-OPERATING-MODEL.md` | normalized |
| Parent Formation | `05-parent-formation/PARENT-FORMATION-AND-FAMILY-CARE-OPERATING-MODEL.md` | normalized |
| Prasāda Operations | `06-prasadam-operations/PRASADA-HOSPITALITY-WEEKLY-OPERATIONS-MANUAL.md` | normalized |
| Kīrtana/Worship/Bhakti Labs | `07-kirtana-worship-bhakti-labs/KIRTANA-WORSHIP-PRAYERS-BHAKTI-LABORATORIES-MANUAL.md` | normalized |
| Festivals/Calendar | `08-festivals-yatras-calendar/FESTIVALS-YATRAS-OUTDOOR-CALENDAR-FRAMEWORK.md` | normalized |
| Digital Repository | — | SOURCE NOT YET SUPPLIED |
| KUTUMBA Setu | — | DRAFT REQUIRED |

## Detailed weekly lessons

- First six months: **18 active sessions** (C1-W1 through C3-W6)
- Monolithic canonical preserved; weekly folders in `11-weekly-program-library/first-six-months/`
- Future three-year weeks: architecture only — production backlog, not fabricated
""")


def main():
    workstream_gaps()
    curriculum_architecture()
    lesson_template()
    document_style_guide()
    legacy_analysis()
    prompt_library()
    content_coverage()
    print("Assembly complete")


if __name__ == "__main__":
    main()
