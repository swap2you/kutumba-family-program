# Source Authority Policy

## Purpose

Establish a bona fide source hierarchy for KUTUMBA curriculum enhancement without committing unauthorized reproduction of copyrighted books, purports, lectures, or artwork into the public Git repository.

## Repository posture

- Public repository: `swap2you/kutumba-family-program`
- KUTUMBA-authored summaries: CC BY-NC-SA 4.0
- Third-party scripture editions, BBT publications, and media: reference and link only unless separately permitted

## Controlling hierarchy

### Tier 1 — Primary controlling sources

1. Śrīla Prabhupāda's published books (Bhaktivedanta VedaBase)
2. Verified Śrīla Prabhupāda lectures, conversations, letters, morning walks (VedaBase / Bhaktivedanta Archives)
3. Current official ISKCON/GBC standards for worship, safeguarding, branding, and public representation

### Tier 2 — User-approved disciplic guidance

1. Verified teachings of Śrī Śrīmad Rādhā Govinda Dās Goswāmī Mahārāj (exact media metadata required)
2. Other speakers only when listed in `approved-speakers.yaml`

### Tier 3 — Recognized Gauḍīya texts

Six Gosvāmī works, Bhakti-rasāmṛta-sindhu, Upadeśāmṛta, Bhaktivinoda Ṭhākura, Bhaktisiddhānta Sarasvatī Ṭhākura, Caitanya-bhāgavata — with clear attribution; Prabhupāda's NOD/NOI presentations remain normal teaching sources.

### Tier 4 — Itihāsa, Purāṇa, Upaniṣad, devotional narrative

Supplementary only; do not override Tier 1 conclusions.

### Tier 5 — Educational and contemporary sources

Pedagogy, safeguarding, developmental psychology, visual learning — method only, not siddhānta.

## Copyright rules

- Do **not** copy full purports, synonym blocks, or chapters into Git
- Store: stable VedaBase link, verse/chapter reference, short verified excerpt when essential, original KUTUMBA summary labeled as summary
- Sanskrit transliteration: verify edition and rights before committing at scale
- Images: external link or placeholder until `rights-status: cleared`

## Claim control

Every nontrivial doctrinal statement in enhanced modules must appear in `research/CLAIM-REGISTER.yaml` with type, source, and review status.

## Human review gates

Doctrinal, worship, safeguarding, and rights reviews remain open until human sign-off recorded in `reviews/`.
