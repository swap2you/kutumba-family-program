# Prompt 10 — Independent Source and Curriculum Audit

## Mode

Read-only audit first. Do not trust generated summaries.

## Verify independently

### Repository and provenance

- actual HEAD;
- source original copied;
- hashes match;
- Downloads originals untouched;
- manifest/inventory counts agree;
- canonical source-map extraction exists.

### Catalog

- every supplied URL is represented or intentionally excluded;
- tiering is correct;
- mirrors are deduplicated;
- rights status is not invented;
- tracking query strings removed;
- unresolved items queued.

### Curriculum

Sample every module and deeply inspect at least:

- C1-W1
- C1-W2
- C1-W3
- C2-W1
- C2-W3
- C2-W5
- C3-W1
- C3-W2
- C3-W3
- C3-W4
- C3-W6

Check:

- source relevance;
- claim traceability;
- kathā accuracy;
- child differentiation;
- newcomer adaptation;
- Gamma completeness;
- media metadata;
- rights boundaries;
- truncation;
- generic template residue;
- status honesty.

### Validators

Confirm validators do more than count lines or IDs.

Run:

```powershell
python scripts/curriculum/run_curriculum_validation.py
powershell -File scripts/Validate-KutumbaRepository.ps1
```

Also run all source-catalog validation scripts.

## Verdicts

Produce:

`17-reviews-and-audits/INDEPENDENT-SOURCE-AND-CURRICULUM-AUDIT.md`

Use finding IDs, severity, evidence, affected files, required action and owner.

Do not modify canonical content during the audit. Remediation findings must be handled in a separate commit after the report.
