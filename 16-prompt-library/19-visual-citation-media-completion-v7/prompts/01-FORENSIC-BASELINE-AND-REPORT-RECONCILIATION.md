# Prompt 01 — Forensic Baseline and Report Reconciliation

## Objective

Establish the actual V7 baseline and eliminate contradictions between active status reports, catalogs and generated evidence.

## Known inconsistency to verify

At the V7 preparation baseline:

- `CURRENT-STATUS.md` and V6 reports stated 78 source-map URLs / 78 catalogued.
- `build-evidence/SOURCE-MAP-URL-RECONCILIATION.md` stated 77 authoritative URLs / 77 catalogued.
- `MASTER-SOURCE-CATALOG.yaml` stated 78 catalog entries.

Do not force these numbers to match if they describe different things.

Use separate metrics:

1. `authoritative_source_map_url_count`
2. `catalog_entry_count`
3. `catalog_entries_not_directly_from_source_map`
4. `normalized_duplicate_count`
5. `verification_queue_count`

Explain any extra catalog entry by source ID and purpose.

## Work

1. Re-run:
   ```powershell
   python scripts/sources/reconcile_source_map_urls.py
   python scripts/sources/validate_catalog_consistency.py
   python scripts/sources/validate_public_source_catalog.py
   python scripts/sources/validate_source_manifest.py
   ```

2. Inspect:
   - canonical source map;
   - original DOCX-derived URL inventory;
   - master catalog;
   - all split catalogs;
   - verification queue;
   - public source directory;
   - active V5/V6 reports.

3. Create:
   - `build-evidence/V7-BASELINE-AUDIT.md`
   - `build-evidence/V7-SOURCE-COUNT-RECONCILIATION.md`
   - `build-evidence/V7-SOURCE-COUNT-RECONCILIATION.csv`

4. Correct active documents:
   - `CURRENT-STATUS.md`
   - `README.md`
   - `ROADMAP.md`
   - active validation coverage report
   - active public source directory summary

5. Historical reports:
   - do not rewrite historical values;
   - add a short supersession note with the exact later report path.

6. Normalize dates:
   - use ISO 8601 UTC in machine-generated evidence;
   - use one human-readable date convention in narrative documents;
   - distinguish document generation time from audited commit time.

## Exit criteria

- no active report contains an unexplained source-count contradiction;
- active reports cite actual current HEAD or clearly identify the audited predecessor commit;
- historical reports remain preserved;
- source originals remain 14/14;
- no source-map URL is lost.
