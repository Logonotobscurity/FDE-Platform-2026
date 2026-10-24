"""Bridge state and ContextProfile."""
from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class ContextProfile(BaseModel):
    locale: str = "en-NG"
    currency: str = "NGN"
    max_run_cost_usd: float = 0.50
    offline_ok: bool = False


class BridgeState(BaseModel):
    run_id: str
    status: Literal["running", "done", "budget_exceeded", "error"] = "running"
    stop_reason: str | None = None
    spent_usd: float = 0.0
    profile: ContextProfile = Field(default_factory=ContextProfile)
    messages: list[dict[str, Any]] = Field(default_factory=list)
    tool_calls: list[dict[str, Any]] = Field(default_factory=list)
