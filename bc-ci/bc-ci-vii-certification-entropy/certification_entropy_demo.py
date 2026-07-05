#!/usr/bin/env python3
"""BC-CI VII certification entropy demo.

This script audits finite graph support multiplicity for robust reachability.
It is not thermodynamic entropy, not physical probability, not a path integral,
not dynamics, and not an empirical model. All path budgets, measures, and
macrostate recording rules are declared inputs.
"""
from __future__ import annotations
import argparse, json, math
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple, Any


def load_config(path: Path) -> Dict[str, Any]:
    cfg = json.loads(path.read_text(encoding="utf-8"))
    if int(cfg.get("path_budget", 0)) < 0:
        raise ValueError("path_budget must be nonnegative")
    if not cfg.get("nodes"):
        raise ValueError("nodes must be nonempty")
    for edge in cfg.get("edges", []):
        for key in ("id", "source", "target", "robust", "sections", "weight_fraction", "reset"):
            if key not in edge:
                raise ValueError(f"edge is missing {key}: {edge}")
        wf = float(edge["weight_fraction"])
        if not (0.0 <= wf <= 1.0):
            raise ValueError(f"weight_fraction must be in [0,1] for {edge['id']}")
    return cfg


def enumerate_paths(nodes: List[str], edges: List[Dict[str, Any]], source: str, target: str, budget: int, robust_only: bool=True) -> List[List[str]]:
    adj: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for e in edges:
        if robust_only and (not e["robust"] or e["reset"]):
            continue
        adj[e["source"]].append(e)
    paths: List[List[str]] = []
    def dfs(v: str, path: List[str], depth: int) -> None:
        if depth > budget:
            return
        if v == target:
            paths.append(path[:])
        if depth == budget:
            return
        for e in adj.get(v, []):
            path.append(e["target"])
            dfs(e["target"], path, depth + 1)
            path.pop()
    dfs(source, [source], 0)
    return paths


def edge_lookup(edges: List[Dict[str, Any]]) -> Dict[Tuple[str, str], List[Dict[str, Any]]]:
    out: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    for e in edges:
        out[(e["source"], e["target"])].append(e)
    return out


def path_signature(path: List[str]) -> str:
    return ">".join(path)


def path_edge_data(path: List[str], lookup: Dict[Tuple[str, str], List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    out=[]
    for a,b in zip(path, path[1:]):
        candidates=lookup.get((a,b), [])
        if not candidates:
            raise ValueError(f"missing edge {a}->{b}")
        out.append(candidates[0])
    return out


def path_weight_fraction(path: List[str], lookup: Dict[Tuple[str, str], List[Dict[str, Any]]]) -> float:
    # Conservative proxy: same policy must support all edges, estimated by minimum edge fraction.
    if len(path) <= 1:
        return 1.0
    return min(float(e["weight_fraction"]) for e in path_edge_data(path, lookup))


def path_sections(path: List[str], lookup: Dict[Tuple[str, str], List[Dict[str, Any]]]) -> Dict[str, Any]:
    if len(path) <= 1:
        return {"existential_count": 1, "uniform_sections": ["length_zero"]}
    edge_sections = [set(e["sections"]) for e in path_edge_data(path, lookup)]
    union = set().union(*edge_sections) if edge_sections else set()
    inter = set(edge_sections[0]) if edge_sections else set()
    for s in edge_sections[1:]:
        inter &= s
    return {"existential_count": len(union), "uniform_sections": sorted(inter)}


def assign_macrostate(path: List[str], macro_rules: Dict[str, List[str]]) -> str:
    sig = path_signature(path)
    for name, sigs in macro_rules.items():
        if sig in sigs:
            return name
    if len(path) == 1:
        return "identity"
    return "other_robust_support"


def entropy(count: float) -> float | None:
    if count <= 0:
        return None
    return math.log(count)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/default_entropy.json")
    ap.add_argument("--out", default="data/certification_entropy_audit.json")
    args = ap.parse_args()
    here = Path(__file__).resolve().parent
    cfg_path = Path(args.config)
    if not cfg_path.is_absolute():
        cfg_path = here / cfg_path
    cfg = load_config(cfg_path)
    nodes = cfg["nodes"]
    edges = cfg["edges"]
    budget = int(cfg["path_budget"])
    lookup = edge_lookup(edges)

    reachability = {p: {} for p in nodes}
    path_rows = []
    macro_counts: Dict[str, int] = defaultdict(int)
    macro_weight_support: Dict[str, float] = defaultdict(float)
    macro_examples: Dict[str, List[str]] = defaultdict(list)

    for p in nodes:
        for q in nodes:
            paths = enumerate_paths(nodes, edges, p, q, budget, robust_only=True)
            reachability[p][q] = bool(paths)
            for path in paths:
                sig = path_signature(path)
                macro = assign_macrostate(path, cfg.get("macrostate_rules", {}))
                wf = path_weight_fraction(path, lookup)
                sec = path_sections(path, lookup)
                row = {
                    "source": p,
                    "target": q,
                    "path": sig,
                    "length": len(path)-1,
                    "macrostate": macro,
                    "weight_fraction_proxy": wf,
                    "section_support": sec,
                    "statuses": ["CERTIFICATION_ENTROPY_DEFINED"]
                }
                if sec["existential_count"] > 1:
                    row["statuses"].append("NONUNIQUE_REACHABILITY")
                if wf < 0.05:
                    row["statuses"].append("MEASURE_FRAGILE")
                path_rows.append(row)
                macro_counts[macro] += 1
                macro_weight_support[macro] += wf
                if len(macro_examples[macro]) < 5:
                    macro_examples[macro].append(sig)

    macro_rows = []
    max_count = max(macro_counts.values()) if macro_counts else 0
    for macro, count in sorted(macro_counts.items()):
        statuses = ["MACROSTATE_CERTIFIED", "CERTIFICATION_ENTROPY_DEFINED"]
        if count == max_count:
            statuses.append("ENTROPY_DOMINANT")
        if macro == "reset_contaminated":
            statuses.append("RESET_CONTAMINATED")
        macro_rows.append({
            "macrostate": macro,
            "support_count": count,
            "count_entropy": entropy(count),
            "weight_support_proxy_sum": round(macro_weight_support[macro], 6),
            "examples": macro_examples[macro],
            "statuses": statuses
        })

    if not cfg.get("measure_declared_before_selection", False):
        measure_status = "MEASURE_TUNING_ARTIFACT"
    else:
        measure_status = "MEASURE_DECLARED"

    out = {
        "note": "Certification entropy audit only: not thermodynamic entropy, not physical probability, not dynamics, not a path integral, and not an arrow of time.",
        "path_budget": budget,
        "measure_status": measure_status,
        "reachability_matrix": reachability,
        "path_support_table": path_rows,
        "macrostate_entropy_table": macro_rows,
        "status_protocol": [
            "CERTIFICATION_ENTROPY_DEFINED", "EMPTY_SUPPORT", "NONUNIQUE_REACHABILITY",
            "MACROSTATE_CERTIFIED", "ENTROPY_DOMINANT", "COARSE_GRAINING_GAIN",
            "MEASURE_FRAGILE", "MEASURE_TUNING_ARTIFACT", "RESET_CONTAMINATED",
            "INCONCLUSIVE_ENTROPY"
        ]
    }

    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = here / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
