# Prompt 09 — Git Handoff

## Final validation

```powershell
git diff --check
git status --short

python scripts/sources/validate_source_manifest.py
python scripts/sources/reconcile_source_map_urls.py
python scripts/sources/validate_catalog_consistency.py

python scripts/curriculum/validate_canonical_fact_source_keys.py
python scripts/curriculum/validate_claim_point_of_use_consistency.py
python scripts/curriculum/detect_stale_fact_phrases.py

python scripts/curriculum/classify_visual_substance.py
python scripts/curriculum/validate_visual_substance.py
python scripts/curriculum/validate_visual_asset_manifests.py
python scripts/curriculum/validate_visual_rights.py
python scripts/curriculum/validate_visual_source_registers.py
python scripts/curriculum/validate_visual_alt_text.py
python scripts/curriculum/validate_visual_catalog_consistency.py

python scripts/curriculum/validate_gamma_briefs.py
python scripts/curriculum/validate_gamma_asset_references.py
python scripts/curriculum/validate_media_candidate_records.py
python scripts/curriculum/audit_katha_narrative_depth.py
python scripts/curriculum/validate_audit_commit_order.py
python scripts/curriculum/run_curriculum_validation.py

powershell -File scripts/Validate-KutumbaRepository.ps1
```

## Required end state

- 14/14 source originals;
- source count metrics remain reconciled;
- no active point-of-use fact drift;
- canonical fact source keys resolve;
- no active C3-W2 “birth in Vṛndāvana”;
- C1-W1 governance claim directly cites charter;
- 42 existing IDs either replaced by meaningful visuals or explicitly retired;
- real SVG + PNG assets;
- visual catalog exists;
- source/rights registers populated;
- theology diagram has actual nodes/edges;
- priority media curation complete;
- Gamma card-level maps complete;
- no placeholders;
- final audit commit occurs after production;
- clean tree;
- repository remains public;
- publication remains NO GO until human approval.

## Logical commits

Suggested:

1. `docs: record V8 forensic truth baseline`
2. `fix: close canonical fact and point-of-use citation drift`
3. `feat: replace Cycle 1 visual placeholders with real diagrams`
4. `feat: create source-mapped Krishna expansion diagram`
5. `docs: complete priority media curation`
6. `docs: package Cycle 1 Gamma upload bundles`
7. `chore: enforce visual substance citation media and audit validators`
8. `docs: record V8 independent final-state audit`
9. `docs: finalize V8 handoff`

Push to `origin/main`. Do not force-push.

## Final response

Return:

- starting and final HEAD;
- safety tag;
- commits;
- placeholder visuals before/after;
- actual visuals by class;
- PNG/SVG counts;
- theology diagram status;
- citation corrections;
- media records;
- Gamma packaging;
- validation results;
- independent audit commit ordering;
- open human gates;
- Workstream 9;
- Setu;
- publication verdict;
- working-tree status.
