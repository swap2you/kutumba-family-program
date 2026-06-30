# Prompt 04 — Verify Provenance, Rights, and Links

## Goal

Verify source identity and availability without confusing availability with permission.

## Link verification

Create:

`scripts/sources/verify_public_source_catalog.py`

Requirements:

- read the machine-readable catalog;
- normalize URLs;
- use a respectful user agent;
- rate-limit requests;
- try HEAD, then a limited GET when HEAD is blocked;
- record redirects;
- distinguish 403/405 from missing;
- cache results;
- do not crawl beyond listed entry points;
- do not bypass access controls;
- do not download large files.

Write:

`build-evidence/SOURCE-LINK-AND-RIGHTS-AUDIT.md`

## Rights classifications

Use these classifications:

- `link-and-metadata-only`
- `short-excerpt-with-review`
- `kutumba-original-summary`
- `download-for-private-review-only`
- `permission-required-before-republication`
- `rights-unclear`
- `official-policy-reference`
- `public-domain-or-explicit-open-license` only when verified

## Special handling

### BBT / VedaBase / Krishna.com

- link and metadata by default;
- do not copy full purports, synonym blocks, chapters, paintings or audiobooks;
- route permissions questions through a rights-review record.

### Bhaktivedanta Archives

- provenance/archival metadata;
- no bulk media copying without permission.

### ISKCON Education and Congregation PDFs

- extract metadata, table of contents, pedagogical structure and original KUTUMBA observations;
- do not commit full third-party PDFs unless explicit permission or license is recorded.

### PureBhakti / Harikatha

- exact attribution;
- supplementary status;
- no automatic doctrinal promotion;
- link/metadata by default.

### Gita Press

- catalog-level metadata and exact edition identification;
- do not treat a Gita Press translation as interchangeable with Śrīla Prabhupāda's translation.

### YouTube

- channel/video metadata and timestamps;
- no video/audio download;
- no auto-generated transcript committed without rights and accuracy review.

## Verification queue

Every unresolved item must enter:

`14-research-source-register/public-source-catalog/SOURCE-VERIFICATION-QUEUE.yaml`

Do not silently discard unresolved sources.
