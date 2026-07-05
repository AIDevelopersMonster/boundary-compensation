#!/usr/bin/env python3
"""BC-CI V weight robust selection demo.

This script samples an admissible weight simplex and audits candidate hidden sections
by exact scalarized minimization, epsilon-suboptimality, and minimax score.
It is a certification demo, not a physical simulation, not an action principle, and
not a statement about empirical dynamics, causality, or a physical arrow of time.
The admissible weight domain is a declared input and must not be retrofitted after selection.
"""
from __future__ import annotations
import argparse, json, math, random
from pathlib import Path
from typing import Dict, List, Tuple


def dot(a: List[float], b: List[float]) -> float:
    return sum(x*y for x, y in zip(a, b))


def dirichlet_simplex(n: int) -> List[float]:
    xs = [-math.log(max(random.random(), 1e-15)) for _ in range(n)]
    s = sum(xs)
    return [x/s for x in xs]


def pareto_dominated(cost, all_costs) -> bool:
    for other in all_costs:
        if all(o <= c + 1e-12 for o, c in zip(other, cost)) and any(o < c - 1e-12 for o, c in zip(other, cost)):
            return True
    return False


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/default_weight_simplex.json")
    ap.add_argument("--out", default="data/weight_chambers.json")
    ap.add_argument("--seed", type=int, default=20260705)
    args = ap.parse_args()
    random.seed(args.seed)

    here = Path(__file__).resolve().parent
    cfg_path = Path(args.config)
    if not cfg_path.is_absolute():
        cfg_path = here / cfg_path
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    candidates = cfg["candidates"]
    eps = float(cfg.get("epsilon", 0.03))
    samples = int(cfg.get("num_weight_samples", 20000))
    m = len(cfg["components"])

    exact_counts: Dict[str, int] = {c["id"]: 0 for c in candidates}
    eps_counts: Dict[str, int] = {c["id"]: 0 for c in candidates}
    minimax_scores: Dict[str, float] = {c["id"]: 0.0 for c in candidates}
    all_costs = [c["cost"] for c in candidates]

    # Random simplex sampling for exact and epsilon regions.
    for _ in range(samples):
        w = dirichlet_simplex(m)
        vals = [(c["id"], dot(w, c["cost"])) for c in candidates]
        min_val = min(v for _, v in vals)
        winners = [cid for cid, v in vals if abs(v - min_val) <= 1e-12]
        for cid in winners:
            exact_counts[cid] += 1 / len(winners)
        for cid, v in vals:
            if v <= min_val + eps:
                eps_counts[cid] += 1

    # Conservative minimax over simplex: for nonnegative costs and full simplex,
    # max_w w.cost = max_i cost_i. For restricted domains this script would need
    # explicit optimization; the default domain is the full simplex.
    for c in candidates:
        minimax_scores[c["id"]] = max(c["cost"])
    best_minimax = min(minimax_scores.values())

    rows = []
    for c in candidates:
        cid = c["id"]
        exact_frac = exact_counts[cid] / samples
        eps_frac = eps_counts[cid] / samples
        dominated = pareto_dominated(c["cost"], all_costs)
        status = []
        if dominated:
            status.append("DOMINATED")
        else:
            status.append("PARETO_STABLE")
        if exact_frac > 0.02:
            status.append("EXACT_WEIGHT_ROBUST")
            status.append("FACET_ROBUST")
        if eps_frac > 0.05:
            status.append("EPSILON_ROBUST")
        if abs(minimax_scores[cid] - best_minimax) <= 1e-12:
            status.append("MINIMAX_ROBUST")
        if not dominated and exact_frac <= 0.002 and eps_frac <= 0.01:
            status.append("WEIGHT_FRAGILE")
        if not dominated and exact_frac <= 0.0005 and eps_frac <= 0.001:
            status.append("TUNING_ARTIFACT")
        rows.append({
            "id": cid,
            "label": c["label"],
            "cost": c["cost"],
            "exact_fraction": round(exact_frac, 6),
            "epsilon_fraction": round(eps_frac, 6),
            "minimax_score": round(minimax_scores[cid], 6),
            "status": status,
        })

    out = {
        "note": "Certification audit only: not a physical trajectory, not an action principle, not empirical evidence, not causality, and not a physical arrow of time. Weight domain is declared before selection.",
        "epsilon": eps,
        "num_weight_samples": samples,
        "components": cfg["components"],
        "results": rows,
    }
    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = here / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
