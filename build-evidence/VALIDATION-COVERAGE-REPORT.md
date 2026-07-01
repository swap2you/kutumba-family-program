# Validation Coverage Report

Generated: 2026-07-01T01:29:14Z
HEAD: `d0243f2e472e936ac247e8ef4554316e073de731`

## Verdicts by category

| Category | Verdict |
|---|---|
| Structural validation | **PASS** |
| Semantic validation | **PASS** |
| Source validation | **PASS** |
| Source catalog validation | **PASS** |
| External link check | **PASS** |
| Rights validation | **PASS** (heuristic — human review required) |
| Repository validation | **PASS** |
| Human-review status | **OPEN** — not publication-ready |
| Publication readiness | **NO GO** — human gates open |

## Scripts executed

Structural: validate_week_schema.py, validate_age_bands.py, validate_visual_assets.py, validate_media_indexes.py, validate_internal_links.py
Semantic: validate_gamma_briefs.py, validate_prem_ki_katha.py, validate_review_status_honesty.py, detect_truncation_artifacts.py, measure_live_session_load.py, audit_katha_narrative_depth.py, validate_claim_source_support.py, validate_newcomer_glossary.py
Source: validate_source_registry.py, validate_claim_register.py, detect_unverified_claims.py, detect_copyright_risk.py
Reporting: build_week_quality_dashboard.py, build_cycle_coverage_report.py, generate_curriculum_status.py

## Note

Warnings in repository validator (e.g. hash verify skips) are classified separately — not suppressed.
