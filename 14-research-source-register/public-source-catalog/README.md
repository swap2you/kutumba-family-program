# Public Source Catalog

Governed machine-readable catalogs derived from `KUT-SRC-0013` (2026-06-30).

## Authority tiers

| Tier | Role |
|------|------|
| A | Controlling or provenance-anchor sources |
| B | Structured secondary research layers |
| C | Convenience mirrors and media discovery |
| supplementary | Gauḍīya/Sanātana references — do not override Prabhupāda-first layer |

## Files

- `MASTER-SOURCE-CATALOG.yaml` — unified index (79 entries)
- Tier-split catalogs for research planning
- `SOURCE-ALIAS-AND-MIRROR-MAP.yaml` — canonical/mirror relationships
- `RIGHTS-AND-PERMISSIONS-REGISTER.yaml` — rights posture by entry
- `SOURCE-VERIFICATION-QUEUE.yaml` — unresolved verification items

## Regeneration

```powershell
python scripts/sources/normalize_source_map.py
python scripts/sources/build_public_source_catalog.py
python scripts/sources/verify_public_source_catalog.py
```

Human doctrinal, rights, and publication approval remain **OPEN**.
