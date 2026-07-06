#!/usr/bin/env python3
"""Reference toy implementation for the BC-CI Engineering Guide.

This script is deliberately small and deterministic. It is not a numerical
library and it does not implement physical dynamics. It demonstrates how a
finite-dimensional BC-CI protocol can return status tables, reachability,
certification entropy, and distance diagnostics from declared finite data.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
import os
from collections import defaultdict, deque
from typing import Dict, Iterable, List, Tuple

import numpy as np

try:
    import matplotlib.pyplot as plt
except Exception:  # pragma: no cover
    plt = None

Node = str
EdgeKey = Tuple[Node, Node]


def simplex_grid(dim: int, level: int = 8) -> np.ndarray:
    """Deterministic grid on the normalized simplex."""
    rows: List[List[float]] = []

    def rec(prefix: List[int], remaining: int, k: int) -> None:
        if k == 1:
            rows.append(prefix + [remaining])
            return
        for v in range(remaining + 1):
            rec(prefix + [v], remaining - v, k - 1)

    rec([], level, dim)
    return np.array(rows, dtype=float) / float(level)


def pareto_status(costs: Dict[str, np.ndarray]) -> Dict[str, str]:
    """Return PARETO_STABLE or DOMINATED for each section."""
    status: Dict[str, str] = {}
    names = list(costs)
    for name in names:
        c = costs[name]
        dominated = False
        for other in names:
            if other == name:
                continue
            d = costs[other]
            if np.all(d <= c) and np.any(d < c):
                dominated = True
                break
        status[name] = "DOMINATED" if dominated else "PARETO_STABLE"
    return status


def epsilon_regions(costs: Dict[str, np.ndarray], eps: float, level: int = 8) -> Dict[str, float]:
    """Approximate epsilon-robust weight-region fractions by simplex grid."""
    dim = len(next(iter(costs.values())))
    grid = simplex_grid(dim, level=level)
    values = {name: grid @ c for name, c in costs.items()}
    min_values = np.min(np.column_stack([values[name] for name in costs]), axis=1)
    fractions: Dict[str, float] = {}
    for name in costs:
        ok = values[name] <= min_values + eps + 1e-12
        fractions[name] = float(np.mean(ok))
    return fractions


def section_audit(config: dict) -> Tuple[List[dict], List[str]]:
    eps = float(config["thresholds"]["epsilon_opt"])
    min_frac = float(config["thresholds"]["robust_region_min_fraction"])
    costs = {k: np.array(v["cost"], dtype=float) for k, v in config["candidate_sections"].items()}
    pstatus = pareto_status(costs)
    fractions = epsilon_regions(costs, eps, level=8)
    rows: List[dict] = []
    robust: List[str] = []
    for name, cost in costs.items():
        frac = fractions[name]
        if pstatus[name] == "DOMINATED":
            rstatus = "DOMINATED"
        elif frac >= min_frac:
            rstatus = "EPSILON_ROBUST"
            robust.append(name)
        else:
            rstatus = "WEIGHT_FRAGILE"
        rows.append({
            "section": name,
            "pareto_status": pstatus[name],
            "epsilon_region_fraction": f"{frac:.6f}",
            "robustness_status": rstatus,
            "cost_vector": "[" + ", ".join(f"{x:.3f}" for x in cost) + "]",
        })
    return rows, robust


def response_status(config: dict) -> List[dict]:
    tau = float(config["thresholds"]["tau"])
    eta = float(config["thresholds"]["eta"])
    rows: List[dict] = []
    for node, mat in config["response_matrices"].items():
        B = np.array(mat, dtype=float)
        eigs = np.linalg.eigvalsh(B)
        min_eig = float(np.min(eigs))
        margin = min_eig - tau - eta
        status = "CHANNEL_CERTIFIED" if margin >= 0.0 else "READOUT_BELOW_THRESHOLD"
        rows.append({
            "node": node,
            "min_eigenvalue": f"{min_eig:.6f}",
            "threshold_margin": f"{margin:.6f}",
            "status": status,
        })
    return rows


def edge_audit(config: dict, robust_sections: Iterable[str]) -> Tuple[List[dict], Dict[EdgeKey, dict]]:
    robust_set = set(robust_sections)
    rows: List[dict] = []
    e_rob: Dict[EdgeKey, dict] = {}
    for e in config["declared_edges"]:
        src, dst = e["source"], e["target"]
        cert_by = set(e.get("certified_by", []))
        if e.get("status") == "CERTIFICATE_RESET":
            status = "RESET_BLOCKED"
        elif cert_by & robust_set and float(e["margin"]) > 0:
            status = "ROBUST_EDGE_CERTIFIED"
            e_rob[(src, dst)] = dict(e)
        elif cert_by:
            status = "WEIGHT_FRAGILE_EDGE"
        else:
            status = "EDGE_UNCERTIFIED"
        rows.append({
            "source": src,
            "target": dst,
            "cost": e["cost"],
            "margin": e["margin"],
            "declared_status": e.get("status", "EDGE_DECLARED"),
            "certified_by": ";".join(sorted(cert_by)),
            "edge_audit_status": status,
        })
    return rows, e_rob


def reachability(nodes: List[Node], e_rob: Dict[EdgeKey, dict], max_depth: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    n = len(nodes)
    idx = {v: i for i, v in enumerate(nodes)}
    adj: Dict[Node, List[Tuple[Node, float, float]]] = defaultdict(list)
    for (u, v), e in e_rob.items():
        adj[u].append((v, float(e["cost"]), float(e["margin"])))

    R = np.eye(n, dtype=int)
    depth = np.full((n, n), np.inf)
    cost = np.full((n, n), np.inf)
    bottleneck = np.full((n, n), -np.inf)
    for i in range(n):
        depth[i, i] = 0
        cost[i, i] = 0.0
        bottleneck[i, i] = np.inf

    for src in nodes:
        # state: node, depth, cost, min_margin
        dq = deque([(src, 0, 0.0, np.inf)])
        while dq:
            u, d, csum, bmin = dq.popleft()
            if d >= max_depth:
                continue
            for v, ecost, emargin in adj[u]:
                nd, nc, nb = d + 1, csum + ecost, min(bmin, emargin)
                i, j = idx[src], idx[v]
                R[i, j] = 1
                if nd < depth[i, j]:
                    depth[i, j] = nd
                if nc < cost[i, j]:
                    cost[i, j] = nc
                if nb > bottleneck[i, j]:
                    bottleneck[i, j] = nb
                dq.append((v, nd, nc, nb))
    return R, depth, cost, bottleneck


def count_paths(nodes: List[Node], e_rob: Dict[EdgeKey, dict], max_depth: int) -> np.ndarray:
    n = len(nodes)
    idx = {v: i for i, v in enumerate(nodes)}
    adj = defaultdict(list)
    for u, v in e_rob:
        adj[u].append(v)
    counts = np.zeros((n, n), dtype=int)
    for src in nodes:
        stack = [(src, 0)]
        while stack:
            u, depth = stack.pop()
            counts[idx[src], idx[u]] += 1
            if depth >= max_depth:
                continue
            for v in adj[u]:
                stack.append((v, depth + 1))
    return counts


def write_csv(path: str, rows: List[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not rows:
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def write_matrix(path: str, nodes: List[str], mat: np.ndarray, fmt: str = "{}") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["node"] + nodes)
        for node, row in zip(nodes, mat):
            out = []
            for x in row:
                if isinstance(x, (float, np.floating)) and not np.isfinite(x):
                    out.append("INF" if x > 0 else "UNDEFINED")
                else:
                    out.append(fmt.format(x))
            w.writerow([node] + out)


def draw_figures(config: dict, e_rob: Dict[EdgeKey, dict], out_dir: str) -> None:
    if plt is None:
        return
    os.makedirs(out_dir, exist_ok=True)
    nodes = config["nodes"]
    coords = {"0": (0.0, 0.0), "1": (1.0, 0.0), "2": (1.0, 1.0), "3": (0.0, 1.0)}
    fig, ax = plt.subplots(figsize=(5, 4))
    for node in nodes:
        x, y = coords[node]
        ax.scatter([x], [y], s=300)
        ax.text(x, y, node, ha="center", va="center")
    for e in config["declared_edges"]:
        u, v = e["source"], e["target"]
        x1, y1 = coords[u]
        x2, y2 = coords[v]
        style = "-" if (u, v) in e_rob else "--"
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", linestyle=style))
        ax.text((x1+x2)/2, (y1+y2)/2, e.get("status", "EDGE"), fontsize=7)
    ax.set_axis_off()
    ax.set_title("Diagnostic graph: certified edges solid, reset/fragile dashed")
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, "diagnostic_graph.svg"))
    plt.close(fig)

    # Simple status-tree sketch
    fig, ax = plt.subplots(figsize=(7, 4))
    labels = [
        (0.1, 0.8, "ProtocolPackage"), (0.4, 0.8, "ResponseScan"), (0.7, 0.8, "SectionAudit"),
        (0.4, 0.5, "EdgeAudit"), (0.7, 0.5, "Reachability"), (0.7, 0.25, "Entropy/Distance"),
        (0.1, 0.25, "RESET / TUNING / NONCLAIM")]
    for x, y, label in labels:
        ax.text(x, y, label, ha="center", va="center", bbox=dict(boxstyle="round", fc="white"))
    arrows = [(0.18,0.8,0.32,0.8),(0.48,0.8,0.62,0.8),(0.7,0.72,0.42,0.58),(0.48,0.5,0.62,0.5),(0.7,0.42,0.7,0.33),(0.32,0.48,0.18,0.3)]
    for x1,y1,x2,y2 in arrows:
        ax.annotate("", xy=(x2,y2), xytext=(x1,y1), arrowprops=dict(arrowstyle="->"))
    ax.set_axis_off()
    ax.set_title("Status-returning audit flow")
    fig.tight_layout()
    fig.savefig(os.path.join(out_dir, "status_tree.svg"))
    plt.close(fig)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="configs/toy_protocol_config.json")
    p.add_argument("--out", default="outputs")
    p.add_argument("--figures", default="figures")
    args = p.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)
    nodes = config["nodes"]
    L = int(config["thresholds"]["path_budget_L"])

    response_rows = response_status(config)
    section_rows, robust_sections = section_audit(config)
    edge_rows, e_rob = edge_audit(config, robust_sections)
    R, depth, cost, bottleneck = reachability(nodes, e_rob, L)
    counts = count_paths(nodes, e_rob, L)
    entropy = np.full(counts.shape, np.nan, dtype=float)
    positive = counts > 0
    entropy[positive] = np.log(counts[positive])

    os.makedirs(args.out, exist_ok=True)
    write_csv(os.path.join(args.out, "response_status.csv"), response_rows)
    write_csv(os.path.join(args.out, "section_status.csv"), section_rows)
    write_csv(os.path.join(args.out, "edge_status.csv"), edge_rows)
    write_matrix(os.path.join(args.out, "reachability_matrix.csv"), nodes, R)
    write_matrix(os.path.join(args.out, "distance_depth.csv"), nodes, depth, "{:.0f}")
    write_matrix(os.path.join(args.out, "distance_cost.csv"), nodes, cost, "{:.3f}")
    write_matrix(os.path.join(args.out, "bottleneck_margin.csv"), nodes, bottleneck, "{:.3f}")
    write_matrix(os.path.join(args.out, "path_count_matrix.csv"), nodes, counts)
    write_matrix(os.path.join(args.out, "certification_entropy.csv"), nodes, entropy, "{:.6f}")
    draw_figures(config, e_rob, args.figures)

    summary = {
        "protocol_id": config["protocol_id"],
        "robust_sections": robust_sections,
        "robust_edges": [f"{u}->{v}" for u, v in e_rob],
        "status": "REFERENCE_RUN_COMPLETE",
        "claim_firewall": [
            "TRANSPORT_NONPHYSICAL",
            "CAUSALITY_NONCLAIM",
            "THERMODYNAMIC_ENTROPY_NONCLAIM",
            "METRIC_TENSOR_NONCLAIM",
        ],
    }
    with open(os.path.join(args.out, "run_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
