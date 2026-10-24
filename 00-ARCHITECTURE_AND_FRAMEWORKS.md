# FDE Platform — Architecture & Frameworks

**Date:** 2026-09-01  
**Positioning:** Evidence-native, deterministic-first continuous control monitoring with policy-gated agent assistance for African operating environments.

---

## 1. System map

| Folder / product | Role | Primary frameworks |
|------------------|------|--------------------|
| **01-ArchAudit** | Continuous Control Monitor (CCM) | Pydantic v2, PyYAML, pytest; LangGraph-shaped pipeline (optional `langgraph`) |
| **02-AgentBridge** | Multi-agent bridge + budgets + local context | Pydantic v2, trajectory eval harness; MCP-shaped tools |
| **03-GigPilot** | FDE engagement kit (discovery → handoff) | Markdown playbooks, `check_pack.py` |
| **00-Docs** | Strategy, ADR, narrative, architecture memos | DOCX + Markdown |

---

## 2. Runtime architecture (ArchAudit CCM)

```
Intake → Collection → Evaluation → Governance → Drift → Reporting
```

**Graph nodes (implemented):**

```
ingest_run → collect → maybe_skip → evaluate → drift → report
```

(`govern_check` reserved for Phase 2.)

| Layer | Responsibility |
|-------|----------------|
| Intake | `run_id`, control pack version, projected budget |
| Collection | Adapters return typed evidence only (no judgments) |
| Skip | Hash match → skip expensive re-eval |
| Evaluation | Deterministic rules first; `decision_basis` recorded |
| Drift | Materiality: none / informational / material / urgent |
| Reporting | `summary.md`, `evidence_index.json`, `metrics.json`, … |

**Canonical metrics:** Control Coverage % · Time-to-Evidence  

**Control families (v1):** Access · Change · Logging  

---

## 3. Frameworks & libraries

| Layer | Choice | Why |
|-------|--------|-----|
| Language | Python 3.11+ | Shared across CCM + bridge |
| Schemas | **Pydantic v2** | Strict Evidence / Evaluation / Drift contracts |
| Config | **PyYAML** | `controls.yaml` control pack |
| Tests | **pytest** | Rules + vertical-slice path |
| Orchestration | LangGraph-shaped (optional package) | StateGraph when installed; sync `run_pipeline` default |
| Tool protocol | MCP-shaped envelopes | `{ok, data, error_code, latency_ms, content_hash}` |
| Evidence store | Local FS (+ optional hash integrity) | Replayable sample packs |
| AgentBridge budgets | Hard stop in-process | `BudgetGuardian` pattern |
| Eval | Golden YAML trajectories | Deterministic harness, no network |

---

## 4. Design analogues (not dependencies)

| Reference | Borrow |
|-----------|--------|
| **Auditree** | Evidence lifecycle, fetcher/check purity |
| **Cloud Custodian** | Policy-as-code, event-driven (future), dry-run |
| **Prowler** | Control catalog discipline, reporting surface |
| **OSCAL / Trestle** | Machine-readable assessment direction |
| **OPA Gatekeeper** | Policy template vs instance, central gate |
| **africa-payments-mcp / civic-agent-kit** | Regional adapters as packs |
| **fde-guide / FDEOps** | Engagement stages for GigPilot |

---

## 5. Folder layout on Drive

```
FDE-Platform-2026/
  00-Docs/                          # Strategy, ADR, architecture DOCX, this file
  01-ArchAudit/                     # CCM source + samples + tests
  02-AgentBridge/                   # Bridge + evals + profiles
  03-GigPilot/                      # Playbook templates + examples
```

---

## 6. How to run (local)

```bash
# ArchAudit
cd 01-ArchAudit && pip install -r requirements.txt && make test && make run-sample

# AgentBridge
cd 02-AgentBridge && pip install -r requirements.txt && make eval

# GigPilot
python 03-GigPilot/scripts/check_pack.py
```

---

## 7. ADR trail

- `ADR-001` v2 — Accepted (narrow CCM, deterministic-first)  
- `ADR-001` **v3** — Evidence-native contracts, governance plane, regional packs, phased OSCAL/events  

See `01-ArchAudit/docs/adr/` and `00-Docs/` for full memos.
