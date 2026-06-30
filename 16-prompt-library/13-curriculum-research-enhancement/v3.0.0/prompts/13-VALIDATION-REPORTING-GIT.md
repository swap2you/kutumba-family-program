# Prompt 13 — Semantic Validation, Reporting, Git, and Handoff

## Objective

Replace file-existence validation with curriculum-quality validation while preserving human review gates.

## Required utilities

Create maintainable scripts under `scripts/curriculum/`:

1. `audit_empty_sections.py`
2. `validate_week_schema.py`
3. `validate_source_registry.py`
4. `validate_claim_register.py`
5. `check_external_links.py`
6. `validate_age_bands.py`
7. `validate_visual_assets.py`
8. `validate_gamma_briefs.py`
9. `detect_copyright_risk.py`
10. `detect_unverified_claims.py`
11. `measure_live_session_load.py`
12. `build_week_quality_dashboard.py`
13. `build_cycle_coverage_report.py`
14. `generate_curriculum_status.py`

Use the simplest local runtime already available. Do not build a platform.

## Semantic failures

Validation must fail when:

- mandatory file is empty or nearly empty;
- table has header but no row;
- placeholder remains;
- source registry lacks direct primary links;
- claim lacks a supporting source;
- purported quotation cannot be traced;
- full purport or long copyrighted passage appears;
- Lāla–Lālī or Kiśora–Kiśorī lesson is absent;
- old three-band model remains in an active derivative;
- materials or assessment are empty;
- no newcomer adaptation;
- no Gamma prompt;
- no visual plan;
- no rights status;
- review status says complete while review file says pending;
- live delivery exceeds the defined session budget without a split plan.

## Quality score

Create a score per module:

- source authority — 20
- doctrinal traceability — 20
- adult learning — 10
- Lāla–Lālī — 10
- Kiśora–Kiśorī — 10
- practical application — 10
- visual/presentation readiness — 8
- safety/accessibility — 7
- rights/attribution — 5

Automated score is evidence, not spiritual approval.

## Required reports

Create:

- `build-evidence/FIRST-SIX-MONTH-CONTENT-AUDIT.md`
- `build-evidence/WEEK-QUALITY-DASHBOARD.md`
- `build-evidence/SOURCE-AND-CITATION-AUDIT.md`
- `build-evidence/VISUAL-AND-RIGHTS-AUDIT.md`
- `build-evidence/AGE-BAND-MIGRATION-REPORT.md`
- `build-evidence/CYCLE-PROJECT-AND-CELEBRATION-REPORT.md`
- `build-evidence/FINAL-CURRICULUM-ENHANCEMENT-REPORT.md`

## CURRENT-STATUS

Update with:

- module count audited;
- modules enhanced;
- gold-standard pilot verdict;
- cycle audit verdicts;
- empty section count;
- source-link count;
- claim count;
- Lāla–Lālī completion;
- Kiśora–Kiśorī completion;
- visual brief count;
- Gamma brief count;
- project count;
- open doctrinal reviews;
- open worship reviews;
- open safeguarding reviews;
- open rights reviews;
- current baseline and commits.

## Git

Before every phase commit:

- run targeted validation;
- inspect diff;
- confirm no secrets;
- confirm no long copyrighted text;
- confirm no unlicensed images;
- confirm status files are truthful.

Push to `origin/main` without force.

## Final handoff

Create:

`17-reviews-and-audits/CURRICULUM-ENHANCEMENT-INDEPENDENT-REVIEW-STARTUP.md`

The final output must state exactly what the external reviewer should inspect.
