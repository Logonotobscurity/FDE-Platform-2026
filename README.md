# FDE Platform 2026

Evidence-native, deterministic-first continuous control monitoring with policy-gated agent assistance for African operating environments.

## Components

- **01-ArchAudit-CCM**: Continuous Control Monitor
- **02-AgentBridge-Africa**: Multi-agent bridge with budgets and MCP-shaped adapters
- **03-GigPilot**: FDE engagement kit (discovery → handoff)

See [00-ARCHITECTURE_AND_FRAMEWORKS.md](00-ARCHITECTURE_AND_FRAMEWORKS.md) for full architecture.

## Quick start

```bash
# ArchAudit
cd 01-ArchAudit-CCM && pip install -r requirements.txt && make test && make run-sample

# AgentBridge
cd 02-AgentBridge-Africa && pip install -r requirements.txt && make eval

# GigPilot
python 03-GigPilot/scripts/check_pack.py
```
