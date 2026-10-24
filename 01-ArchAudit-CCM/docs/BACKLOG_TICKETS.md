# BACKLOG — ArchAudit CCM (Phase 2+)

## Phase 2
- [ ] `govern_check` node: exceptions, dual control, TTL, owner
- [ ] Materiality thresholds from control pack (not hardcoded)
- [ ] Evidence hash chain / integrity verification on replay
- [ ] FastAPI `/runs` + auth stub
- [ ] CI: pytest + schema validation in GitHub Actions

## Phase 3
- [ ] Regional evidence packs (NG, KE) as YAML packs
- [ ] Event-driven collection (webhook / poll adapters)
- [ ] OSCAL export of assessment results
- [ ] Dashboard metrics (coverage, TTE)

## Done in v3 slice
- [x] Deterministic rules first
- [x] Typed Evidence / Evaluation / Drift
- [x] Skip on content hash
- [x] Sample audit pack output
