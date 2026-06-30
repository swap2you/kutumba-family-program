# Prompt 03 — Source Authority, Copyright, and Claim Control

## Objective

Create a bona fide source system without turning the public repository into an unauthorized copy of copyrighted books or media.

## Controlling source hierarchy

### Tier 1 — Primary controlling sources

1. Śrīla Prabhupāda’s published books in the Bhaktivedanta VedaBase.
2. Śrīla Prabhupāda’s verified lectures, conversations, letters, and morning walks in VedaBase/Bhaktivedanta Archives.
3. Current official ISKCON/GBC standards where institutional procedure, safeguarding, worship, branding, or public representation is involved.

### Tier 2 — User-approved disciplic guidance

1. Verified lectures and teachings of **Śrī Śrīmad Rādhā Govinda Dās Goswāmī Mahārāj**, using exact media metadata or user-supplied source IDs.
2. Other speakers only after their exact identity and approved source channel are entered in `approved-speakers.yaml`.
3. Never infer the identity of “Bhajji Maharaj” or any partially named teacher.

### Tier 3 — Recognized Gauḍīya texts and ācāryas

Use only through reviewed editions and with clear attribution:

- Six Gosvāmī works;
- Bhakti-rasāmṛta-sindhu;
- Upadeśāmṛta;
- works of Śrīla Bhaktivinoda Ṭhākura;
- works of Śrīla Bhaktisiddhānta Sarasvatī Ṭhākura;
- Caitanya-bhāgavata;
- related recognized Gauḍīya granthas.

Where Śrīla Prabhupāda has already presented the work as *Nectar of Devotion* or *Nectar of Instruction*, his presentation remains the normal KUTUMBA teaching source.

### Tier 4 — Itihāsa, Purāṇa, Upaniṣad, and devotional narrative

May include, with reviewed editions:

- Rāmāyaṇa;
- Mahābhārata;
- relevant Purāṇas;
- Upaniṣads;
- Rāmacaritamānasa as supplementary devotional literature.

These may enrich stories and applications, but they do not override the Tier 1 source conclusion.

Interpret the spoken reference to “Quran” in the source request as **Purāṇa** because it appears in a list of Vedic categories. Do not add Qur’anic comparative-religion material unless the Program Director separately authorizes it.

### Tier 5 — Educational and contemporary sources

Use reputable research for:

- pedagogy;
- developmental appropriateness;
- family communication;
- visual learning;
- memory and practice design;
- safeguarding;
- accessibility.

These sources may improve method, not establish siddhānta.

Forums and social media may identify common questions, but never serve as doctrinal evidence.

## Claim register

For every nontrivial doctrinal statement, create a claim entry:

- claim ID;
- exact KUTUMBA statement;
- claim type;
- primary source;
- direct link;
- source context;
- original KUTUMBA summary;
- audience;
- risk of misunderstanding;
- review requirement;
- reviewer;
- status.

Distinguish:

- `scripture-text`;
- `srila-prabhupada-explanation`;
- `kutumba-summary`;
- `analogy`;
- `pedagogical-application`;
- `contemporary-case`;
- `unresolved`.

## Copyright rules

The official VedaBase states that its content is used with permission and that BBT and Bhaktivedanta Archives rights are reserved.

Therefore:

- do not copy full purports into Git;
- do not copy entire translations, synonym blocks, or chapters at scale;
- store the VedaBase reference and stable link;
- use a short excerpt only when essential;
- create an original KUTUMBA summary;
- label the summary as a summary, not a quotation;
- record page/verse/lecture metadata;
- obtain written permission before broader reproduction.

Sanskrit verse text may be stored only after exact verification and rights review of the chosen transliteration or edition. Do not assume a formatted transliteration is rights-free merely because the underlying ancient verse is public domain.

## Image rules

Do not download BBT paintings or devotional images from Google search.

For each image candidate record:

- creator;
- source;
- URL;
- rights holder;
- licence;
- permission status;
- allowed use;
- attribution;
- local-copy status.

Until rights are confirmed, use:

- an external link;
- a placeholder;
- an original diagram;
- an original icon-free conceptual illustration.

## Required files

Create:

- `14-research-source-register/SOURCE-AUTHORITY-POLICY.md`
- `14-research-source-register/approved-speakers.yaml`
- `14-research-source-register/source-allowlist.yaml`
- `15-templates/CLAIM-REGISTER-SCHEMA.yaml`
- `15-templates/WEEK-SOURCE-REGISTRY-SCHEMA.yaml`
- `build-evidence/SOURCE-AND-CITATION-AUDIT.md`
