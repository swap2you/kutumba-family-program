# Validation Coverage Report

Generated: 2026-06-30T21:03:38Z
HEAD: `acf3edbc6eef7d6a9b04e743e0437fafe96bbad1`

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

Structural: validate_week_schema.py, validate_age_bands.py, validate_visual_assets.py, validate_media_indexes.py
Semantic: validate_gamma_briefs.py, validate_prem_ki_katha.py, validate_review_status_honesty.py, detect_truncation_artifacts.py, measure_live_session_load.py
Source: validate_source_registry.py, validate_claim_register.py, detect_unverified_claims.py, detect_copyright_risk.py
Reporting: build_week_quality_dashboard.py, build_cycle_coverage_report.py, generate_curriculum_status.py

## Note

Warnings in repository validator (e.g. hash verify skips) are classified separately — not suppressed.
