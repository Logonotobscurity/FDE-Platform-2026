# ADR-001 v3 — Evidence-native CCM

## Status
Accepted (2026-09-01)

## Context
Continuous control monitoring for African operating environments needs deterministic-first evaluation, typed evidence, and a path to governance + regional packs without baking in cloud-vendor assumptions.

## Decision
1. **Evidence is the source of truth.** Adapters return typed Evidence only; no judgments in collection.
2. **Deterministic rules first.** LLM/agent assistance is policy-gated and recorded as `decision_basis`.
3. **Contracts over frameworks.** Pydantic v2 schemas for Evidence, Evaluation, Drift, Exception. PyYAML control pack.
4. **Skip on content hash.** Avoid re-eval when evidence unchanged.
5. **Governance plane Phase 2.** Exceptions, dual control, TTL, owner.
6. **Regional packs as data.** NG/KE adapters are YAML packs, not hard-coded.
7. **Phased OSCAL / events.** Machine-readable assessment later; event-driven collection optional.

## Consequences
- Replayable sample packs.
- Hard budgets in AgentBridge companion.
- Clear separation: collection purity vs evaluation rules.

## Alternatives considered
- Full LangGraph dependency (kept optional).
- Immediate OSCAL (deferred).
- Agent-first judgments (rejected; deterministic-first).
