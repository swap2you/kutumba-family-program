# Confirmed V7 Findings Requiring Remediation

## F-001 — 42 “visual assets” are mostly text metadata cards

Generator:

`scripts/v7/build_c1_visuals.py`

Its `simple_diagram_svg()` writes:

- a title;
- one descriptive sentence;
- “Asset class”;
- “Source anchors: see module research pack”;
- rights text.

It does not create diagrams, nodes, arrows, storyboard panels, timelines, analogy illustrations or instructional graphics.

Examples:

- `c1-w1-storyboard-naimisharanya.svg`
- `c1-w2-concept-life-stages.svg`
- all 42 generated files share the same pattern.

Severity: CRITICAL for visual-completeness claims.

## F-002 — Theology expansion diagram is empty

`14-research-source-register/theology-visual-library/krishna-and-expansions/THEO-VIS-KRISHNA-EXP-001.svg`

contains only:

- title;
- footer reference note.

It has no Kṛṣṇa/Balarāma/catur-vyūha/Nārāyaṇa/puruṣa nodes or relationships.

Severity: CRITICAL.

## F-003 — V7 independent audit preceded actual visual production

Audit commit:

`58ed4e0 — docs: record V7 independent visual citation media audit`

Actual visual commit came later:

`3fbea42 — feat: Cycle 1 KUTUMBA-original SVG visual packs and architecture`

Gamma commit came later:

`f0f6aaf — docs: Cycle 1 Gamma render-ready packages`

Canonical fact registry came later:

`52cab55 — fix: add canonical fact registry`

The repository audit cannot be treated as a final-state independent audit.

Severity: HIGH.

## F-004 — Active citation drift remains

`C1-W1/research/SOURCE-EXPANSION-BRIEF.md` still maps:

“KUTUMBA is not a social club…” → SB 1.2.18

The claim register correctly uses `KUT-CHARTER`, but the point-of-use source-to-claim table does not.

Severity: HIGH.

## F-005 — Active C3-W2 geography drift remains in `.mmd`

`C3-W2/visuals/concept-map.mmd` still says:

“Kṛṣṇa's birth in Vṛndāvana”

The stale-phrase validator scans only `.md`, `.yaml`, `.yml`, so it misses `.mmd` and `.svg`.

Severity: HIGH.

## F-006 — Canonical fact registry keys do not resolve

Examples such as:

`PSC-VEDABASE-SB-1-2-17`

appear only in the canonical fact registry and are not proven to resolve to the module source matrices or public catalog.

Severity: HIGH.

## F-007 — Visual governance files are incomplete

`visual-asset-library/README.md` names `VISUAL-ASSET-CATALOG.yaml`, but the file is absent.

Per-module:

- `VISUAL-SOURCE-REGISTER.yaml` is absent;
- old `image-rights-register.yaml` may remain empty;
- manifests do not include source keys, dimensions, generation method or design review;
- no PNG derivatives/contact sheets are present.

Severity: HIGH.

## F-008 — Gamma is structurally packaged, not actually render-ready

`build_c1_gamma_packs.py`:

- marks every module `render-ready`;
- replaces only `[IMAGE: ...]` strings;
- does not verify every card has an exact asset;
- does not inspect whether an SVG is visually meaningful.

C1-W2 still contains instructions such as:

- “photo timeline placeholder”;
- “import from process-flow.mmd”;
- “Table from VISUAL-PLAN.md”;
- generic icon descriptions.

Severity: HIGH.

## F-009 — Media curation is incomplete

V7 execution ledger states:

`06 Media curation | partial backlog`

Expected reports such as `V7-MEDIA-CURATION-REPORT.md` and `V7-SOURCE-LIBRARY-UTILIZATION-REPORT.md` are absent.

Current media library remains:

- three sample Prabhupāda lectures;
- zero approved teachers;
- zero kathā audio;
- zero bhajana/kīrtana;
- zero video catalog entries.

Severity: MEDIUM/HIGH.

## F-010 — Validators are existence/count validators

`validate_visual_asset_manifests.py` checks:

- manifest exists;
- at least six assets;
- file exists;
- file size > 50;
- alt text present.

It does not inspect visual semantics.

`validate_gamma_asset_references.py` checks:

- files exist;
- map says `render-ready`.

It does not prove cards are render-ready.

Severity: HIGH.
