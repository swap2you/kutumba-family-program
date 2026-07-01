# V7 Source Count Reconciliation

Generated: 2026-06-29

## Summary

| Metric | Value |
|---|---|
| authoritative_source_map_url_count | 77 |
| catalog_entry_count | 78 |
| catalog_entries_not_directly_from_source_map | 1 |
| normalized_duplicate_count | 1 |
| reconciliation_missing_urls | 0 |

## Explanation

- **77 authoritative URLs** come from the canonical source map and original DOCX inventory (`reconcile_source_map_urls.py`).
- **78 catalog entries** include one consolidated alias entry after removing a Gita Press `srsltid` duplicate (V6 fix retained).
- Active `CURRENT-STATUS.md` reports both metrics separately to avoid contradiction with historical `SOURCE-MAP-URL-RECONCILIATION.md` (77/77 at generation time).

## Supersession

`build-evidence/SOURCE-MAP-URL-RECONCILIATION.md` — historical snapshot; see this report for active dual-metric reporting.
