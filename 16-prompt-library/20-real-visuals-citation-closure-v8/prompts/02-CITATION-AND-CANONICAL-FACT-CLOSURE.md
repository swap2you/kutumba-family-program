# Prompt 02 — Citation and Canonical Fact Closure

## Objective

Make canonical facts, source keys and every active point of use agree.

## Source key normalization

Use existing source IDs from:

- module `SOURCE-MATRIX.md`;
- module claim registers;
- KUTUMBA source manifest;
- public source catalog.

Do not invent unresolved IDs such as `PSC-VEDABASE-SB-1-2-17` unless they are formally added to a governed registry and validated.

Preferred verse keys:

- `SB-1-2-17`
- `SB-1-2-18`
- `SB-1-2-19`
- `SB-1-1-1`
- `SB-1-1-4`
- module-consistent equivalents.

Create:

`scripts/curriculum/validate_canonical_fact_source_keys.py`

It must resolve every canonical fact source key to a governed source-matrix/catalog record.

## Mandatory corrections

1. C1-W1 source-to-claim table:
   - direct documentary source = `KUT-CHARTER`;
   - SB 1.2.18 may be theological support only.

2. C3-W2:
   - scan `.md`, `.mmd`, `.svg`, `.yaml`, `.yml`, `.json`, `.csv`, active `.py`, reader pages and data files;
   - remove active “birth in Vṛndāvana” drift;
   - preserve phrase only in prohibited-wording rules or historical audit evidence.

3. SB 1.2.17–1.2.19:
   - verify every active teaching description;
   - correct every point of use.

4. SB 1.1.1 versus 1.1.4+:
   - invocation and assembly/inquiry must remain distinct.

## Cross-file validator

Create:

`scripts/curriculum/validate_claim_point_of_use_consistency.py`

For every Cycle 1 module compare:

- claim register;
- source matrix;
- source-expansion brief;
- verse study;
- kathā source register;
- lesson prose;
- visual text;
- Gamma cards;
- media metadata.

## Drift scan extensions

Update stale-fact scanning to include:

- `.mmd`
- `.svg`
- `.html`
- `.txt`
- `.csv`
- `.json`
- active `.py`

Exclude historical archives from failure, but report archived occurrences.

## Evidence

- `build-evidence/V8-CITATION-CLOSURE-REPORT.md`
- `build-evidence/V8-POINT-OF-USE-DRIFT.csv`
- `17-reviews-and-audits/V8-CITATION-AUDIT.md`
