# Prompt 07 — Validators and Contact Sheets

## Objective

Make automated PASS meaningful.

## Implement

### Visual substance

`scripts/curriculum/validate_visual_substance.py`

Fail user-facing Cycle 1 visuals when:

- fewer than required semantic graphic elements;
- only title/metadata text;
- no relationships for diagrams/flows;
- no panels for storyboards;
- boilerplate metadata dominates;
- source register absent;
- PNG derivative absent;
- SVG/PNG dimensions invalid.

### Visual rights and source

- `validate_visual_rights.py`
- `validate_visual_source_registers.py`
- `validate_visual_alt_text.py`
- `validate_visual_catalog_consistency.py`

### Fact drift

Extend stale-phrase scan to active:

- md, mmd, svg, yaml, yml, json, csv, txt, html, py.

Add allowlisted paths for canonical prohibited-wording records and historical reports.

### Gamma

Strengthen:

- `validate_gamma_briefs.py`
- `validate_gamma_asset_references.py`

Do not trust status fields; derive status from actual content.

### Media

Create:

`validate_media_candidate_records.py`

### Audit ordering

Create:

`validate_audit_commit_order.py`

It must verify that the final independent audit commit is descended from all V8 production commits.

## Contact sheets

Generate a visual gallery:

- module-by-module HTML/Markdown;
- thumbnail PNGs;
- asset ID;
- title;
- class;
- source;
- rights;
- review status.

A human must be able to open one page and inspect all Cycle 1 visuals.

## Runner

Wire V8 validators into the main runner with separate verdicts:

- structure;
- citations;
- visual substance;
- visual rights;
- media;
- Gamma packaging;
- kathā;
- human review;
- publication.

## Evidence

- `build-evidence/V8-VALIDATION-COVERAGE.md`
- `build-evidence/V8-VISUAL-SUBSTANCE-RESULTS.csv`
- `build-evidence/V8-VALIDATION-REPORT.md`
