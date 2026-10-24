"""Thin FastAPI surface for CCM runs (MVP).

Run: uvicorn apps.api.main:app --app-dir . --reload
(from archaudit/ with PYTHONPATH=.)
"""
from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException

from archaudit.pipeline import run_pipeline

app = FastAPI(title="ArchAudit CCM", version="0.3.0")


@app.get("/health")
def health() -> dict:
    return {"ok": True, "service": "archaudit-ccm"}


@app.post("/runs")
def create_run(body: dict) -> dict:
    control_pack = body.get("control_pack") or str(Path("policies/controls.yaml"))
    if not Path(control_pack).exists():
        raise HTTPException(400, f"control pack not found: {control_pack}")
    out = body.get("output_dir") or "samples/audit_pack"
    budget = int(body.get("budget_ms") or 30_000)
    try:
        state = run_pipeline(control_pack, out, budget_ms=budget)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(500, str(exc)) from exc
    return {
        "run_id": state.run_id,
        "metrics": state.metrics.model_dump(),
        "drift_count": len(state.drifts),
        "evaluation_count": len(state.evaluations),
        "exception_count": len(state.exceptions),
    }
