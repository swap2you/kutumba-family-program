# Prompt 06 — Enrich the Prabhupāda Media and Lecture Library

## Goal

Turn the public source map into a useful metadata-first Prabhupāda lecture, conversation, walk, letter, audio, image and video discovery library.

## Existing library

Preserve and extend:

`14-research-source-register/media-library/`

## Catalogs

Strengthen:

- `PRABHUPADA-LECTURE-CATALOG.yaml`
- `VIDEO-CATALOG.yaml`
- `KATHA-AUDIO-CATALOG.yaml`
- `BHAJANA-AND-KIRTANA-CATALOG.yaml`
- `MEDIA-RIGHTS-REGISTER.yaml`
- `TOPIC-TO-MEDIA-MAP.md`

Add, when useful:

- `PRABHUPADA-LETTERS-CATALOG.yaml`
- `MORNING-WALKS-AND-CONVERSATIONS-CATALOG.yaml`
- `PRABHUPADA-IMAGE-REFERENCE-CATALOG.yaml`

## Entry requirements

- stable source URL;
- title;
- date;
- place;
- type;
- speaker;
- duration when known;
- exact relevant timestamp or paragraph;
- module/topic;
- teaching purpose;
- transcript availability;
- canonical source;
- mirror links;
- rights status;
- review status;
- last verified.

## Source order

1. VedaBase / Bhaktivedanta Archives
2. PrabhupadaVani / Vanisource / Vanipedia
3. official channels
4. discovery mirrors

## Restrictions

- metadata and links only by default;
- no bulk AV downloads;
- no unverified automatic transcription;
- no anonymous quote cards;
- no approval of unknown speakers;
- no duplicate media entries for mirrors.

## Module integration

Update every module `audio-video/MEDIA-INDEX.yaml` with actual relevant entries or an honest `no-reviewed-entry-yet` status.

Do not count Gamma prompts as media entries.

## Report

Create:

`build-evidence/MEDIA-ENRICHMENT-REPORT.md`
