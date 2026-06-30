# Prompt 03 — Build the Machine-Readable Public Source Catalog

## Goal

Convert the source map into a governed, machine-readable catalog suitable for research planning and module enrichment.

## Destination

Create:

```text
14-research-source-register/public-source-catalog/
├── README.md
├── MASTER-SOURCE-CATALOG.yaml
├── PRABHUPADA-PRIMARY-AND-ARCHIVAL.yaml
├── PRABHUPADA-STRUCTURED-SECONDARY.yaml
├── ISKCON-EDUCATION-AND-CONGREGATION.yaml
├── SUPPLEMENTARY-GAUDIYA-SANATANA.yaml
├── MEDIA-AND-YOUTUBE-DISCOVERY.yaml
├── RIGHTS-AND-PERMISSIONS-REGISTER.yaml
├── SOURCE-ALIAS-AND-MIRROR-MAP.yaml
└── SOURCE-VERIFICATION-QUEUE.yaml
```

## Authority model

Use this operational model.

### Tier A — Controlling or provenance-anchor sources

- Bhaktivedanta VedaBase
- Bhaktivedanta Archives
- BBT / BBT International / Krishna.com for publishing and rights
- official ISKCON/GBC/ministry sources for policy, education, worship, safeguarding and congregation programs

### Tier B — Structured secondary research layers

- PrabhupadaVani
- Vanisource
- Vaniquotes
- Vanipedia

These may assist discovery, topic clustering, transcript access and alternate links. Final doctrinal claims should normally anchor to Tier A where available.

### Tier C — Convenience, comparison and media discovery

- ISKCON Desire Tree
- PrabhupadaBooks.com
- YouTube channels
- other mirrors

Use metadata and discovery only unless separately approved.

### Supplementary Gauḍīya/Sanātana layer

- PureBhakti
- Harikatha
- Gita Press
- other exact user-approved sources

These are supplementary references. They do not automatically override or merge with the Prabhupāda-first controlling layer.

## Catalog entry fields

Every entry must include:

- `source_id`
- `source_name`
- `owner_or_publisher`
- `base_url`
- `exact_entry_url`
- `source_category`
- `authority_tier`
- `content_types`
- `languages`
- `primary_or_secondary`
- `canonical_for`
- `mirror_of`
- `discovery_only`
- `rights_posture`
- `allowed_repository_use`
- `prohibited_repository_use`
- `authentication_required`
- `robots_or_access_notes`
- `last_verified`
- `verification_method`
- `status`
- `notes`

## Dedupe

Multiple sites may host the same Prabhupāda lecture, letter or book.

Create a canonical/mirror relationship:

- one canonical provenance anchor;
- alternate access links;
- no duplicate claim identity;
- no duplicate media downloads.

## No invented statistics

Do not hard-code counts such as transcript totals, letter totals or media totals unless re-verified on the execution date and stored as time-stamped observations.

## Report

Create:

`build-evidence/PUBLIC-SOURCE-CATALOG-REPORT.md`
