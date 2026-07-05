#!/usr/bin/env python3
"""BC-CI IV certification-cost selection demo.

This script generates deterministic finite-dimensional toy outputs for the
BC-CI IV companion package. It is not a physical simulation. The cost is not an
action, energy, entropy, or Lagrangian.
"""
from __future__ import annotations

import json
import math
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "configs" / "default_selection.json"
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"


def basis_candidates(max_norm: float):
    vals = [-1.0, -0.5, 0.0, 0.5, 1.0]
    out = []
    for x, y in product(vals, vals):
        if x * x + y * y <= max_norm * max_norm:
            out.append((x, y))
    return out


def leakage(vec):
    return vec[1] * vec[1]


def readout_penalty(vec, delta):
    return max(0.0, delta - abs(vec[0])) ** 2


def variation_penalty(section):
    total = 0.0
    for a, b in zip(section[:-1], section[1:]):
        total += (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
    return total


def balance_penalty(section):
    sx = sum(v[0] for v in section)
    sy = sum(v[1] for v in section)
    return sx * sx + sy * sy


def cost(section, cfg):
    delta = float(cfg["delta_read"])
    return (
        float(cfg["readout_weight"]) * sum(readout_penalty(v, delta) for v in section)
        + float(cfg["variation_weight"]) * variation_penalty(section)
        + float(cfg["leakage_weight"]) * sum(leakage(v) for v in section)
        + float(cfg["balance_weight"]) * balance_penalty(section)
    )


def generate(cfg):
    n = int(cfg.get("samples", 9))
    candidates = basis_candidates(float(cfg["max_norm"]))
    # A deliberately small structured family: three prototypes are tiled over the chain.
    prototypes = []
    for v in candidates:
        prototypes.append([v for _ in range(n)])
    # Add alternating and ramp-like sections.
    for amp in [0.5, 1.0]:
        prototypes.append([(amp if i < n // 2 else -amp, 0.0) for i in range(n)])
        prototypes.append([((i / (n - 1)) * 2 * amp - amp, 0.0) for i in range(n)])
        prototypes.append([(amp * math.sin(math.pi * i / (n - 1)), 0.0) for i in range(n)])
        prototypes.append([(amp * math.sin(math.pi * i / (n - 1)), 0.25 * math.cos(math.pi * i / (n - 1))) for i in range(n)])
    rows = []
    for idx, sec in enumerate(prototypes):
        rows.append({
            "id": idx,
            "cost": round(cost(sec, cfg), 6),
            "readout_penalty": round(sum(readout_penalty(v, cfg["delta_read"]) for v in sec), 6),
            "variation_penalty": round(variation_penalty(sec), 6),
            "leakage_penalty": round(sum(leakage(v) for v in sec), 6),
            "balance_penalty": round(balance_penalty(sec), 6),
            "section": [[round(a, 4), round(b, 4)] for a, b in sec],
        })
    rows.sort(key=lambda r: r["cost"])
    return {"config": cfg, "candidate_count": len(rows), "selected": rows[:5], "all_candidates": rows}


def write_svg(result):
    rows = result["all_candidates"][:25]
    W, H = 880, 360
    max_cost = max(r["cost"] for r in rows) or 1.0
    bars = []
    for i, r in enumerate(rows):
        x = 60 + i * 30
        h = 260 * r["cost"] / max_cost
        y = 310 - h
        color = "#2ca02c" if i == 0 else "#1f77b4"
        bars.append(f'<rect x="{x}" y="{y:.1f}" width="20" height="{h:.1f}" fill="{color}"/>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="100%" height="100%" fill="white"/>
  <text x="40" y="30" font-family="Arial" font-size="18">BC-CI IV certification-cost candidates</text>
  <line x1="50" y1="310" x2="835" y2="310" stroke="black"/>
  <line x1="50" y1="50" x2="50" y2="310" stroke="black"/>
  {''.join(bars)}
  <text x="60" y="340" font-family="Arial" font-size="13">green: selected minimum; blue: other admissible candidates</text>
</svg>\n'''
    (FIG_DIR / "cost_candidates.svg").write_text(svg, encoding="utf-8")


def main():
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    DATA_DIR.mkdir(exist_ok=True)
    FIG_DIR.mkdir(exist_ok=True)
    result = generate(cfg)
    (DATA_DIR / "cost_demo_output.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_svg(result)
    print(f"selected cost: {result['selected'][0]['cost']}")
    print(f"wrote {DATA_DIR / 'cost_demo_output.json'}")
    print(f"wrote {FIG_DIR / 'cost_candidates.svg'}")


if __name__ == "__main__":
    main()
