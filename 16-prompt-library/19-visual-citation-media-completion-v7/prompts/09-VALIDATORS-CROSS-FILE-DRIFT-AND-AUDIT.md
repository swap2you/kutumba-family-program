# Prompt 09 — Validators, Cross-File Drift and Audit

## Objective

Replace validators that merely prove file presence with validators that detect the actual defects found in V6.

## Rename or split old validators

The old `validate_visual_assets.py` validates Mermaid viewer pairing only.

Rename/split into:

- `validate_mermaid_viewers.py`
- `validate_visual_asset_manifests.py`
- `validate_rendered_visual_assets.py`
- `validate_visual_rights.py`
- `validate_visual_alt_text.py`
- `validate_gamma_asset_references.py`

## New fact/citation validators

Create:

- `validate_canonical_fact_consistency.py`
- `detect_stale_fact_phrases.py`
- `validate_source_description_registry.py`
- `validate_claim_to_point_of_use_consistency.py`

Known failure phrases must include:

- `Bhāgavata as the ripened fruit of Vedic knowledge` when tied to SB 1.2.17;
- `birth in Vṛndāvana` in C3-W2 current files;
- charter statements sourced only to scripture;
- “approved” media without named reviewer.

## Visual validation

Fail when:

- a required Cycle 1 asset is missing;
- manifest points to a nonexistent file;
- rendered image is zero-byte or unreadable;
- SVG lacks a viewBox;
- PNG dimensions are below the declared requirement;
- asset has no alt text;
- source anchors are missing;
- rights status is absent or `rights-unclear-do-not-use` but the file is used;
- Gamma references a placeholder instead of an asset;
- visual text conflicts with canonical facts;
- stale/truncated text appears;
- asset is orphaned.

## Media validation

Fail when a selected media item lacks:

- exact URL;
- title;
- source;
- authority tier;
- rights posture;
- intended use;
- reviewer status.

Do not fail a deferred item merely because no media is selected.

## Gamma validation

Distinguish:

- scaffold;
- prompt-ready;
- render-ready;
- rendered-unreviewed;
- pilot-approved.

Only Cycle 1 should target render-ready in V7.

## Kathā validation

Apply Prompt 08 timing and quality standards. Do not call C1-W2 gold narrative pilot unless it meets them.

## Repository-wide scan

Scan current canonical files, not just dashboards. Exclude `99-archive` from active failures, but report archived occurrences separately.

## Validation runner

Wire all V7 validators into:

`python scripts/curriculum/run_curriculum_validation.py`

Group output:

- repository;
- provenance;
- fact/citation;
- curriculum;
- visual;
- media;
- Gamma;
- rights;
- human gates;
- publication readiness.

A PASS in automated categories must never convert open human gates to approved.

## Evidence

Create:

- `build-evidence/V7-VALIDATION-COVERAGE-REPORT.md`
- `build-evidence/V7-CROSS-FILE-DRIFT-REPORT.md`
- `build-evidence/V7-VISUAL-VALIDATION-REPORT.md`
- `build-evidence/V7-MEDIA-VALIDATION-REPORT.md`
- `build-evidence/V7-RIGHTS-VALIDATION-REPORT.md`.
