# Prompt 02 — Ingest and Normalize the Source Map

## Goal

Preserve the new source document, assign provenance, extract a canonical Markdown representation, and update the source manifest without creating duplicate clutter.

## Source discovery

Search this exact directory:

`C:\Users\swap2\Downloads\Personal\0. KUTUMBA SANGA`

Expected authoritative file:

`Public Source Map for Prabhupada and Related Sanatana Content.docx`

There may also be same-basename PDF or Markdown exports.

## Rules for companions

- DOCX is the authoritative source original.
- A PDF companion may be preserved as a visual/reference companion when present.
- Do not copy a downloaded Markdown export as a second canonical document.
- Compare any Markdown export to the DOCX extraction. Record it as a derivative or duplicate.
- Never alter or delete the Downloads originals.

## Repository destination

Create, only if absent:

`00-source-materials/01-current-kutumba-originals/9. KUTUMBA Digital Repository and Source Library/`

Copy the authoritative DOCX there.

Copy the PDF companion only when it exists and is a genuine same-source export.

## Provenance

- Calculate binary-safe SHA-256 for every copied artifact.
- Allocate the next sequential `KUT-SRC-####` IDs by reading `SOURCE-MANIFEST.yaml`; do not assume the next number.
- Use a shared `source_group_id` for DOCX/PDF companions.
- Update:
  - `00-source-materials/SOURCE-MANIFEST.yaml`
  - `00-source-materials/SOURCE-INVENTORY.md`
  - source-ingestion evidence
- Mark:
  - privacy class: `public-curriculum-development`
  - rights status: `kutumba-authored-research-compilation`
  - third-party contents: `links-and-summaries-only`
  - required reviews: `rights-review`, `research-review`

## Canonical extraction

Create:

`09-digital-repository-publishing/PUBLIC-SOURCE-MAP-FOR-PRABHUPADA-AND-SANATANA-CONTENT.md`

Requirements:

- frontmatter with `source_id`, `source_hash`, `source_group_id`, extraction date, version, status;
- preserve headings and exact URLs;
- remove ChatGPT tracking query strings such as `utm_source=chatgpt.com` and unrelated search tokens;
- preserve source labels and selection cautions;
- do not strengthen claims beyond the source document;
- distinguish claims requiring current verification;
- add a prominent statement that public access is not permission to redistribute.

## Workstream 9 gap

Update `09-digital-repository-publishing/GAP-RECORD.md` honestly:

- Public source-map component: supplied and normalized.
- Full Digital Repository Operating Manual: still separate unless already backed by a dedicated source.
- Do not falsely mark the entire Workstream 9 complete solely because the source map exists.

## Utilities

Create reusable utilities under `scripts/sources/` for:

- DOCX text/URL extraction;
- binary SHA-256;
- URL cleanup;
- manifest update;
- source-group comparison.

Do not introduce application dependencies. Prefer Python standard library plus already-installed `python-docx`/YAML libraries when available.

## Report

Create:

`build-evidence/SOURCE-MAP-INGESTION-REPORT.md`
