# Gap Record — Digital Repository and Publishing (Workstream 9)

| Field | Value |
|---|---|
| Workstream | 9 — Repository, Drive, Website and Digital Library |
| Status | **SOURCE NOT YET SUPPLIED** |
| Production owner | Digital Lead |
| Required reviewers | Digital Lead, Governance Lead, Research Lead (rights) |
| Production prompt | `16-prompt-library/09-digital-publishing/produce-digital-repository-operating-model.md` |

## Required sections (when source is supplied)

1. Repository purpose and scope boundary (documentation vs. application)
2. Folder taxonomy and naming conventions
3. Access tiers (public curriculum vs. private operational records)
4. Version control relationship with this Git repository
5. Website / Drive / library publication workflow
6. Rights review before publishing third-party or BBT material
7. Retention and deletion rules for private records
8. Incident response for accidental publication

## Known decisions from Master Operating Model

- KUTUMBA is a formation program, not a technology product — digital tooling serves documentation and distribution
- Private participant records must not live in the public Git repository
- Śrīla Prabhupāda’s books and BBT material require separate rights handling
- Temple alignment and governance oversight apply to anything presented as official

## Source dependencies

| Dependency | Status |
|---|---|
| Dedicated Workstream 9 operating manual in KUTUMBA SANGA | **Not supplied** |
| Master Operating Model (`00-foundation/MASTER-OPERATING-MODEL.md`) | Available — contextual only |
| Governance Charter | Available |
| Current public Git repository structure | Available |

## Acceptance criteria

- Canonical Markdown operating model with `source_id` and hash provenance
- No fabricated website/API/database implementation in this pass
- Rights and privacy sections consistent with `SECURITY-PRIVACY.md` and `RIGHTS-AND-USE.md`
- Review queue entries closed only after Digital Lead and Governance sign-off

## Document-output expectations

- `09-digital-repository-publishing/DIGITAL-REPOSITORY-OPERATING-MODEL.md` (future)
- Publication manifest template linkage in `16-prompt-library/09-digital-publishing/`
- Updated `SOURCE-MANIFEST.yaml` entry when source is ingested

## Next exact action

1. Obtain or author the Workstream 9 source document outside this repository
2. Ingest via `scripts/ingest-sources.py` and normalize per Prompt 04
3. Run `produce-digital-repository-operating-model.md` prompt under human supervision

**Do not mark this workstream complete until a real source document is supplied and normalized.**
