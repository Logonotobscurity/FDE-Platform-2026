# Run State Diagram — ArchAudit CCM

```
[start]
   |
   v
ingest_run  -- run_id, control_pack, budget
   |
   v
collect     -- adapters → typed Evidence only
   |
   v
maybe_skip  -- content_hash match? → skip re-eval
   |
   v
evaluate    -- deterministic rules → Evaluation + decision_basis
   |
   v
drift       -- materiality none|informational|material|urgent
   |
   v
report      -- summary.md, evidence_index.json, metrics.json
   |
   v
[end]
```

`govern_check` reserved for Phase 2 (exceptions, dual control).
