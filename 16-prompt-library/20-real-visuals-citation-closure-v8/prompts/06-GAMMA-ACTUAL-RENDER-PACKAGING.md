# Prompt 06 — Gamma Actual Render Packaging

## Objective

Make Cycle 1 packages practically usable in Gamma after the visuals are real.

## Current defect

V7 asset maps point to local SVG filenames, but:

- many files are not meaningful visuals;
- not every card uses an exact asset;
- decks still contain phrases such as “photo timeline placeholder,” “Table from VISUAL-PLAN.md” or generic icon instructions;
- the validator trusts `render_status: render-ready`.

## Correct status model

- `structural-scaffold`
- `content-complete-assets-missing`
- `assets-complete-upload-required`
- `rendered-unreviewed`
- `post-render-reviewed`
- `approved-for-internal-pilot`

Do not use `render-ready` without qualification.

## Card-level asset mapping

For every Cycle 1 deck/card record:

- card number;
- audience;
- exact asset ID;
- exact SVG;
- exact PNG;
- decorative treatment if no doctrinal visual is needed;
- source citation;
- rights;
- speaker note;
- accessibility note.

Every factual/teaching card must have either:

- an exact approved local asset; or
- a deliberate text-only treatment.

No unspecified placeholder.

## Upload bundle

Create a local, reproducible export script:

`scripts/export/build_gamma_cycle1_bundle.py`

It must produce, outside tracked canonical content or in a governed export area:

```text
Cycle-1-Gamma-Bundle/
├── C1-W1/
│   ├── parent-prompt.md
│   ├── lala-lali-prompt.md
│   ├── kisora-kisori-prompt.md
│   ├── assets/
│   ├── asset-map.yaml
│   └── QA.md
...
```

Create a ZIP locally for user upload, but commit only the script, manifest and checksum unless the project policy explicitly allows the ZIP.

## Validator

Gamma validation must fail when:

- `placeholder` remains in active Cycle 1 visual instructions;
- a card’s asset does not exist;
- an asset is classified metadata-card-placeholder;
- a card lacks a speaker note;
- factual card lacks source;
- rights missing;
- asset map does not map all teaching cards.

## Evidence

`build-evidence/V8-GAMMA-PACKAGING-REPORT.md`

Do not claim a Gamma deck is rendered until an exported artifact is supplied.
