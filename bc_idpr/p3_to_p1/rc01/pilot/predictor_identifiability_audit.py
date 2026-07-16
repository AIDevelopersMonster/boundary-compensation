#!/usr/bin/env python3
"""Response-independent reachability audit for frozen RC01 predictors."""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

EVIDENCE_POLICY = "No statement from the Gemini advisory report is used as evidence."


def frozen_grid(spec: dict) -> np.ndarray:
    grid = float(spec["start"]) + float(spec["step"]) * np.arange(int(spec["count"]))
    if abs(float(grid[-1]) - float(spec["stop"])) > 5e-13:
        raise RuntimeError("frozen grid mismatch")
    return grid


def cubic_projector(eta: np.ndarray) -> np.ndarray:
    x = 2.0 * (eta - eta[0]) / (eta[-1] - eta[0]) - 1.0
    basis = np.column_stack([np.ones_like(x), x, x * x, x * x * x])
    q, _ = np.linalg.qr(basis, mode="reduced")
    return q


def residualize(vector: np.ndarray, q: np.ndarray) -> np.ndarray:
    return vector - q @ (q.conj().T @ vector)


def audit(preregistration: Path) -> dict:
    record = json.loads(preregistration.read_text(encoding="utf-8"))
    eta = frozen_grid(record["grids"]["phase"])
    theta = math.pi * eta / 12.0
    q = cubic_projector(eta)
    rows = []
    for n in record["phase_dictionary"]["integer_modes"]:
        integer = residualize(np.exp(1j * n * theta), q)
        control = residualize(np.exp(1j * (n + 0.5) * theta), q)
        integer /= np.linalg.norm(integer)
        control /= np.linalg.norm(control)
        overlap = float(abs(np.vdot(integer, control)))
        bound = float(math.sqrt(max(0.0, 1.0 - overlap * overlap)))
        rows.append({"mode": n, "absolute_overlap": overlap, "advantage_bound": bound})
    largest = max(row["advantage_bound"] for row in rows)
    threshold = float(record["primary_confirmatory_criteria"]["median_energy_advantage_min"])
    return {
        "contract_id": record["contract_id"],
        "status": "CONFIRMATORY_THRESHOLD_UNREACHABLE" if largest < threshold else "REACHABLE",
        "rows": rows,
        "largest_attainable_energy_advantage_bound": largest,
        "frozen_threshold": threshold,
        "threshold_reachable": largest >= threshold,
        "evidence_policy": EVIDENCE_POLICY,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("preregistration", type=Path)
    args = parser.parse_args()
    result = audit(args.preregistration)
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["threshold_reachable"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
