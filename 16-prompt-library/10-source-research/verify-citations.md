# Verify Citations

## Purpose

Verify citations against authorized sources — never fabricate URLs.

## Source inputs

- Relevant canonical documents in workstream folders
- `00-source-materials/SOURCE-MANIFEST.yaml`
- Governing decisions from Master Operating Model and Governance Charter

## Scope

As stated in purpose.

## Exclusions

- No invented citations or worship procedures
- No bulk copyrighted copying
- No private family data
- No shallow summaries replacing detailed operating models

## Required output files

Per task specification in `CURRENT-STATUS.md` and workstream README.

## Citation rules

Prioritize Śrīla Prabhupāda's published books and authorized ISKCON/temple standards. Never fabricate URLs.

## Copyright rules

Reference-only for legacy collections. Paraphrase; do not reproduce long copyrighted passages.

## Privacy rules

No private family records or secrets in Git.

## Review gates

- Doctrinal review when teachings are extended
- Worship review for liturgical content
- Safety review for children/youth content
- Rights review for third-party material

## Quality checklist

- [ ] Linked to source_id and source_hash
- [ ] Depth matches KUTUMBA baseline documents
- [ ] Review status recorded
- [ ] CURRENT-STATUS.md updated

## Validation

Run `scripts/Validate-KutumbaRepository.ps1` before commit.

## Git commit expectation

Concise message describing workstream and artifact produced.
