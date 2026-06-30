# V5 Validation Report

Generated: 2026-06-30  
Baseline tag: `kutumba-source-architecture-baseline-v1.0.0` @ `fe84ed0`

## Automated suite (Phase 10)

| Gate | Result |
|---|---|
| `validate_source_manifest.py` | **PASS** — 14/14 entries, hashes match |
| `reconcile_source_map_urls.py` | **PASS** — 78 authoritative URLs, 0 missing |
| `validate_catalog_consistency.py` | **PASS** — 79 entries; tiers A=42, B=12, C=13, supplementary=12 |
| `validate_public_source_catalog.py` | **PASS** (heuristic) — 43 ok, 12 restricted, 24 queued |
| `run_curriculum_validation.py` | **PASS** — structural, semantic, source, catalog, links, repository |
| `Validate-KutumbaRepository.ps1` | **PASS** — 0 failures, 0 mojibake warnings |

## Module count

All curriculum validators now iterate `^c[1-3]-w[1-6]-` only → **18 modules** (not 21).

## Unicode internal links

PowerShell validator uses UTF-8 reads and NFC normalization — **0 mojibake warnings**.

## Scripture claims (C1)

`detect_unverified_claims.py` — **PASS**; C1 scripture keys bound to SOURCE-MATRIX; empty keys fail.

## Human gates

| Gate | Status |
|---|---|
| Doctrinal review | **OPEN** |
| Worship review | **OPEN** |
| Rights review | **OPEN** |
| Pedagogy review | **OPEN** |
| Publication readiness | **NO GO** |

## Publication readiness

**Not ready** — automated structural pass only; named human sign-off required per module.
