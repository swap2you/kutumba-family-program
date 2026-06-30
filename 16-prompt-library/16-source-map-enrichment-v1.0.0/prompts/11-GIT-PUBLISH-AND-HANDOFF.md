# Prompt 11 — Git Publish and Handoff

## Preconditions

- all prior prompts executed;
- independent audit complete;
- critical findings remediated or explicitly open;
- working tree reviewed;
- no secrets;
- no private participant data;
- no unauthorized third-party content;
- repository remains public.

## Required final validation

```powershell
git status --short
git diff --check
python scripts/curriculum/run_curriculum_validation.py
powershell -File scripts/Validate-KutumbaRepository.ps1
```

Run source-catalog validation and URL-status generation.

## Commit plan

Use logical commits such as:

```text
docs: ingest public Prabhupada and Sanatana source map
docs: add governed public source catalogs
chore: add source link rights and provenance validation
docs: map public sources to first six-month curriculum
docs: enrich Prabhupada media and lecture metadata
docs: add official education and Bhakti-vriksha resource maps
docs: add supplementary source boundary controls
fix: complete source-informed curriculum quality remediation
docs: record independent source and curriculum audit
docs: finalize source enrichment handoff
```

Do not force-push.

Push to `origin/main`.

## Final handoff

Report:

- final HEAD;
- commits pushed;
- source artifacts ingested;
- source counts by authority tier;
- URLs verified/redirected/unresolved;
- rights classifications;
- module coverage;
- media entries;
- education-resource entries;
- supplementary entries;
- v4 corrections;
- validation results;
- warnings;
- human-review gates;
- publication readiness;
- exact files to return for ChatGPT validation.

Required files for external validation:

- `CURRENT-STATUS.md`
- `00-source-materials/SOURCE-MANIFEST.yaml`
- `09-digital-repository-publishing/PUBLIC-SOURCE-MAP-FOR-PRABHUPADA-AND-SANATANA-CONTENT.md`
- `build-evidence/FINAL-SOURCE-ENRICHMENT-REPORT.md`
- `build-evidence/PUBLIC-SOURCE-CATALOG-REPORT.md`
- `build-evidence/SOURCE-LINK-AND-RIGHTS-AUDIT.md`
- `build-evidence/MODULE-SOURCE-COVERAGE-REPORT.md`
- `build-evidence/V4-QUALITY-REMEDIATION-REPORT.md`
- `17-reviews-and-audits/INDEPENDENT-SOURCE-AND-CURRICULUM-AUDIT.md`

Do not issue unconditional publication GO.
