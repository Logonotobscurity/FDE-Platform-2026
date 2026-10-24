"""Validate GigPilot example packs have required files and no TODO/TBD."""
from __future__ import annotations

import sys
from pathlib import Path

REQUIRED = {
    "discovery.md",
    "architecture.md",
    "deploy.md",
    "metrics_table.md",
    "handoff.md",
}


def check(example_dir: Path) -> list[str]:
    errors = []
    for name in REQUIRED:
        p = example_dir / name
        if not p.exists():
            errors.append(f"missing {name} in {example_dir}")
            continue
        text = p.read_text(encoding="utf-8")
        if "TODO" in text or "TBD" in text:
            errors.append(f"{p} contains TODO/TBD")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parent.parent / "playbook" / "examples"
    all_errors = []
    for d in sorted(root.iterdir()):
        if d.is_dir():
            all_errors.extend(check(d))
    if all_errors:
        for e in all_errors:
            print(e)
        return 1
    print("all example packs OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
