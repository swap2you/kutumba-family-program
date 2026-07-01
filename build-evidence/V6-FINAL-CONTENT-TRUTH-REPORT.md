# V6 Final Content Truth Report

Generated: 2026-06-29  
Prompt: `16-prompt-library/18-content-truth-cycle1-pilot-v6/MASTER-PROMPT.md`

## Executive summary

V6 corrected content-truth defects for **Cycle 1 pilot readiness** without a blind 18-module regeneration pass. Automated validators pass for narrative depth, semantic claim typing (Cycle 1), newcomer glossary structure, Gamma truncation, and three-deck Gamma structure.

**Verdict: GO WITH CONDITIONS for Cycle 1 internal pilot preparation only.**

> **Supersession (V7, 2026-06-29):** Kathā minute estimates, visual completeness, and Gamma readiness claims superseded by `build-evidence/V7-KATHA-RUNTIME-AND-DEPTH-REPORT.md` and `17-reviews-and-audits/V7-INDEPENDENT-VISUAL-CITATION-MEDIA-AUDIT.md`.

## Source catalog

| Metric | Value |
|---|---|
| Master catalog entries | 78 (after Gita Press tracking duplicate removal) |
| Source-map URL reconciliation | 78/78 |
| Tracking params stripped | `srsltid`, `gclsrc`, `msclkid`, others per `url_cleanup.py` |
| Harikatha `/audios/` | reclassified supplementary Gauḍīya audio |
| Spanish VedaBase | `languages: [es]` only |

## Cycle 1 kathā (narrative section 6 only)

| Module | Narrative words | Est. min | Meets |
|---|---:|---|---|
| C1-W1 | 893 | 6.6–7.8 | yes |
| C1-W2 | 263 (gold pilot) | reference | preserved |
| C1-W3 | 730 | 5.4–6.3 | yes |
| C1-W4 | 755 | 5.6–6.6 | yes |
| C1-W5 | 764 | 5.7–6.6 | yes |
| C1-W6 | 437 | 3.2–3.8 | yes (integration) |

## Semantic citations (Cycle 1)

Claim registers patched with `semantic_support` and governance/scripture separation. See `17-reviews-and-audits/V6-CYCLE-1-SEMANTIC-CITATION-AUDIT.md`.

## Glossary

C2-W3 `dehī` defect corrected. Validator passes 18-module structure scan.

## Gamma

Truncation artifacts removed. Three decks per module structurally validated. C3 Kiśora decks are scaffolds — not pilot-depth content.

## Pilot package

`13-facilitator-library/cycle-1-pilot/` — internal pack with blank forms and exit criteria.

## Scripts added

- `audit_katha_narrative_depth.py`
- `validate_claim_source_support.py`
- `validate_newcomer_glossary.py`
- `katha_narrative_utils.py`
- `scripts/v6/*` maintenance utilities
- `module_data_builder.py` archived (requires `KUTUMBA_ALLOW_V5_BATCH=1`)

## Evidence index

- `build-evidence/V6-CONTENT-TRUTH-BASELINE.md`
- `build-evidence/V6-CYCLE-1-KATHA-DEPTH-AUDIT.md`
- `build-evidence/V6-CLAIM-SOURCE-SUPPORT-REPORT.md`
- `build-evidence/V6-NEWCOMER-GLOSSARY-AUDIT.md`
- `build-evidence/V6-GAMMA-CONTENT-AUDIT.md`
- `build-evidence/V6-CYCLE-1-SESSION-COHERENCE-REPORT.md`
- `17-reviews-and-audits/V6-INDEPENDENT-PILOT-READINESS-AUDIT.md`
