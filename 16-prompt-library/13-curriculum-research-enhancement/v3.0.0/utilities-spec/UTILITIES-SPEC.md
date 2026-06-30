# Curriculum Utility Specification

Cursor must build these as small scripts, not as an application.

## `audit_empty_sections.py`

Detect:

- heading with no body;
- table header with no data row;
- placeholder tokens;
- files below meaningful content threshold;
- `complete` status conflicting with content.

## `validate_week_schema.py`

Validate all required files and directories.

## `validate_source_registry.py`

Validate:

- source tier;
- stable link;
- teaching function;
- context check;
- rights status;
- review status.

## `validate_claim_register.py`

Ensure every doctrinal claim has at least one primary source.

## `check_external_links.py`

Check status and redirects. Do not scrape or archive copyrighted content.

## `detect_copyright_risk.py`

Flag:

- long copied purport-like blocks;
- repeated VedaBase text;
- unlicensed image binaries;
- files named as full books;
- BBT/third-party content without rights metadata.

## `measure_live_session_load.py`

Estimate delivery time from activity durations and text load. Flag overflow.

## `build_week_quality_dashboard.py`

Produce a compact 18-row quality dashboard.

## `validate_gamma_briefs.py`

Verify:

- audience;
- actual content;
- card count;
- source notes;
- image-rights status;
- speaker notes;
- no invented quotation.

## `validate_visual_assets.py`

Verify Mermaid syntax, alt text, rights register, file size, and orphaned assets.
