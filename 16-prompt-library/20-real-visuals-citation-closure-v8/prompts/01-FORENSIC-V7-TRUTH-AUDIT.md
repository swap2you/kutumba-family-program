# Prompt 01 — Forensic V7 Truth Audit

## Objective

Establish what V7 actually produced before modifying files.

## Required analysis

### Commit order

Verify the ancestry/order of:

- `58ed4e0`
- `3fbea42`
- `f0f6aaf`
- `52cab55`

Document that the existing V7 audit was committed before the final asset/Gamma/fact-registry commits.

### Visual fingerprinting

Inspect all 42 SVGs.

Classify each:

- `metadata-card-placeholder`
- `simple-card`
- `real-concept-diagram`
- `real-process-flow`
- `real-storyboard`
- `real-reference-card`
- `real-practice-card`

A file is a placeholder when it contains only:

- background;
- title;
- description;
- metadata/footer;

without instructional graphic structure.

Create a fingerprint detector:

`scripts/curriculum/classify_visual_substance.py`

Record:

- SVG element counts;
- non-background rectangles;
- paths;
- lines;
- arrows/markers;
- circles/ellipses;
- polygons;
- groups;
- meaningful text count;
- unique labels;
- metadata-only phrases;
- classification.

### Required audit files

- `build-evidence/V8-V7-TRUTH-AUDIT.md`
- `build-evidence/V8-VISUAL-SUBSTANCE-BASELINE.csv`
- `build-evidence/V8-MISSING-DELIVERABLES.md`

### Status correction

Update active status to say:

- V7 architecture complete;
- V7 visual files present but visual substance remediation required;
- Gamma structural packaging exists but true render readiness pending;
- media curation incomplete;
- final-state independent audit pending.

Do not delete V7 reports.
