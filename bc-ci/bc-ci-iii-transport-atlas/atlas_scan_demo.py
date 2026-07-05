#!/usr/bin/env python3
"""BC-CI III certified transport atlas toy scanner.

This script is not a physical simulation. It evaluates finite-dimensional
certification statuses for a declared three-chart parameter-base toy model.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "configs" / "default_atlas.json"
DATA = ROOT / "data"
FIG = ROOT / "figures"

STATUS_COLORS = {
    "GLUING_CERTIFIED": "#2ca02c",
    "OVERLAP_CERTIFIED": "#1f77b4",
    "RESET_EDGE": "#d62728",
    "TRIPLE_DEFECT": "#9467bd",
    "UNCERTIFIED": "#7f7f7f",
}


def projector_angle(chart: int, x: float, y: float, mode: str) -> float:
    base = math.atan2(y - 0.5, x - 0.5) / 4.0
    offset = [0.0, 0.08, -0.06][chart]
    if mode == "reset_edge" and chart == 1 and x > 0.47:
        offset += 0.9
    if mode == "triple_defect" and chart == 2 and 0.35 < x < 0.65 and 0.35 < y < 0.65:
        offset += 0.55
    return base + offset


def projector_distance(phi: float, psi: float) -> float:
    # Norm distance between rank-one line projectors in R^2.
    return abs(math.sin(phi - psi))


def classify_point(x: float, y: float, kappa: float, zeta: float, mode: str) -> str:
    phis = [projector_angle(i, x, y, mode) for i in range(3)]
    d01 = projector_distance(phis[0], phis[1])
    d12 = projector_distance(phis[1], phis[2])
    d02 = projector_distance(phis[0], phis[2])
    if max(d01, d12, d02) > kappa:
        return "RESET_EDGE"
    triple_defect = abs(d02 - min(1.0, d01 + d12))
    if triple_defect > zeta:
        return "TRIPLE_DEFECT"
    return "GLUING_CERTIFIED"


def run() -> dict:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    n = int(cfg["grid_size"])
    kappa = float(cfg["kappa"])
    zeta = float(cfg["zeta"])
    modes = ["clean", "reset_edge", "triple_defect"]
    results = []
    for mode in modes:
        counts = {}
        points = []
        for i in range(n):
            for j in range(n):
                x, y = i / (n - 1), j / (n - 1)
                status = classify_point(x, y, kappa, zeta, mode)
                counts[status] = counts.get(status, 0) + 1
                points.append({"x": round(x, 4), "y": round(y, 4), "status": status})
        results.append({"mode": mode, "kappa": kappa, "zeta": zeta, "status_counts": counts, "points": points})
    return {"scenario": cfg["scenario"], "results": results}


def write_svg(result: dict) -> None:
    for item in result["results"]:
        mode = item["mode"]
        pts = item["points"]
        cell = 10
        size = 41 * cell
        parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size+30}" viewBox="0 0 {size} {size+30}">', '<rect width="100%" height="100%" fill="white"/>', f'<text x="8" y="20" font-family="Arial" font-size="14">{mode}</text>']
        for p in pts:
            x = int(round(p["x"] * 40)) * cell
            y = int(round(p["y"] * 40)) * cell + 30
            color = STATUS_COLORS.get(p["status"], "#aaa")
            parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{color}"/>')
        parts.append('</svg>')
        (FIG / f"{mode}_atlas.svg").write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    DATA.mkdir(exist_ok=True)
    FIG.mkdir(exist_ok=True)
    result = run()
    (DATA / "atlas_scan_output.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_svg(result)
    print("Wrote data/atlas_scan_output.json and figures/*.svg")


if __name__ == "__main__":
    main()
