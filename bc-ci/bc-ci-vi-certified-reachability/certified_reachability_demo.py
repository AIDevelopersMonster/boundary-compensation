#!/usr/bin/env python3
"""BC-CI VI certified reachability demo.

This script audits a finite directed diagnostic graph. It computes robustly
certified edges, certified reachability, strongly connected components, quotient
order, cycle labels, and a finite potential acyclicity check.

This is a certification demo, not physical spacetime, not physical causality,
not a light-cone model, not Hamiltonian dynamics, and not empirical evidence.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict, deque
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple

Edge = Tuple[str, str]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def classify_edge(edge: dict, section_status: Dict[str, Set[str]], accepted: Set[str]) -> str:
    if edge.get("atlas_status") == "RESET":
        return "CERTIFICATE_RESET"
    sections = edge.get("sections", [])
    if not sections:
        return "UNCERTIFIED_EDGE"
    if any(section_status.get(s, set()) & accepted for s in sections):
        return "ROBUST_EDGE"
    if any("TUNING_ARTIFACT" in section_status.get(s, set()) for s in sections):
        return "TUNED_EDGE"
    return "WEIGHT_FRAGILE_EDGE"


def adjacency(nodes: List[str], robust_edges: List[Edge]) -> Dict[str, List[str]]:
    adj = {n: [] for n in nodes}
    for u, v in robust_edges:
        adj[u].append(v)
    return adj


def reachability(nodes: List[str], adj: Dict[str, List[str]]) -> Dict[str, List[str]]:
    out = {}
    for start in nodes:
        seen = {start}
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj.get(u, []):
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        out[start] = sorted(seen)
    return out


def tarjan_scc(nodes: List[str], adj: Dict[str, List[str]]) -> List[List[str]]:
    index = 0
    stack: List[str] = []
    on_stack: Set[str] = set()
    indices: Dict[str, int] = {}
    low: Dict[str, int] = {}
    comps: List[List[str]] = []

    def strongconnect(v: str) -> None:
        nonlocal index
        indices[v] = index
        low[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)
        for w in adj.get(v, []):
            if w not in indices:
                strongconnect(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                comp.append(w)
                if w == v:
                    break
            comps.append(sorted(comp))

    for v in nodes:
        if v not in indices:
            strongconnect(v)
    return sorted(comps, key=lambda c: (len(c), c))


def quotient_edges(components: List[List[str]], robust_edges: List[Edge]) -> List[Tuple[int, int]]:
    comp_id = {}
    for i, comp in enumerate(components):
        for n in comp:
            comp_id[n] = i
    q_edges = set()
    for u, v in robust_edges:
        cu, cv = comp_id[u], comp_id[v]
        if cu != cv:
            q_edges.add((cu, cv))
    return sorted(q_edges)


def potential_report(edges: List[dict], edge_status: Dict[str, str], potentials: Dict[str, float]) -> dict:
    bad = []
    for e in edges:
        key = f"{e['from']}->{e['to']}"
        if edge_status.get(key) != "ROBUST_EDGE":
            continue
        u, v = e["from"], e["to"]
        if potentials[v] <= potentials[u]:
            bad.append({"edge": key, "phi_from": potentials[u], "phi_to": potentials[v]})
    return {
        "status": "ACYCLICITY_POTENTIAL_PASSED" if not bad else "POTENTIAL_NOT_MONOTONE",
        "violations": bad,
    }


def simple_cycle_labels(edges: List[dict], edge_status: Dict[str, str]) -> List[dict]:
    # Minimal audit for directed 3-cycles present in the declared graph.
    edge_map = {(e["from"], e["to"]): f"{e['from']}->{e['to']}" for e in edges}
    nodes = sorted({e["from"] for e in edges} | {e["to"] for e in edges})
    cycles = []
    seen = set()
    for a in nodes:
        for b in nodes:
            for c in nodes:
                if len({a, b, c}) != 3:
                    continue
                if (a, b) in edge_map and (b, c) in edge_map and (c, a) in edge_map:
                    canonical = tuple(sorted([a, b, c]))
                    oriented = (a, b, c)
                    if (canonical, frozenset([(a,b),(b,c),(c,a)])) in seen:
                        continue
                    seen.add((canonical, frozenset([(a,b),(b,c),(c,a)])))
                    keys = [edge_map[(a, b)], edge_map[(b, c)], edge_map[(c, a)]]
                    statuses = [edge_status[k] for k in keys]
                    if all(s == "ROBUST_EDGE" for s in statuses):
                        label = "CERTIFIED_CYCLE"
                    elif any(s == "CERTIFICATE_RESET" for s in statuses):
                        label = "RESET_CYCLE"
                    elif any(s == "TUNED_EDGE" for s in statuses):
                        label = "TUNED_LOOP"
                    elif any(s == "WEIGHT_FRAGILE_EDGE" for s in statuses):
                        label = "CYCLE_FRAGILE"
                    else:
                        label = "CYCLE_AMBIGUOUS"
                    cycles.append({"cycle": list(oriented), "edges": keys, "edge_statuses": statuses, "status": label})
    return cycles


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="configs/default_reachability.json")
    ap.add_argument("--out", default="data/reachability_audit.json")
    args = ap.parse_args()

    here = Path(__file__).resolve().parent
    cfg_path = Path(args.config)
    if not cfg_path.is_absolute():
        cfg_path = here / cfg_path
    cfg = load_json(cfg_path)

    nodes = [n["id"] for n in cfg["nodes"]]
    potentials = {n["id"]: float(n.get("potential", 0.0)) for n in cfg["nodes"]}
    accepted = set(cfg.get("accepted_section_statuses", []))
    section_status = {s["id"]: set(s.get("status", [])) for s in cfg["sections"]}

    edge_status: Dict[str, str] = {}
    robust_edges: List[Edge] = []
    for e in cfg["edges"]:
        key = f"{e['from']}->{e['to']}"
        st = classify_edge(e, section_status, accepted)
        edge_status[key] = st
        if st == "ROBUST_EDGE":
            robust_edges.append((e["from"], e["to"]))

    adj = adjacency(nodes, robust_edges)
    reach = reachability(nodes, adj)
    scc = tarjan_scc(nodes, adj)
    q_edges = quotient_edges(scc, robust_edges)
    cycles = simple_cycle_labels(cfg["edges"], edge_status)
    phi = potential_report(cfg["edges"], edge_status, potentials)

    edge_status_table = [
        {"edge": key, "status": value}
        for key, value in sorted(edge_status.items())
    ]
    reset_barrier_report = [
        row for row in edge_status_table if row["status"] == "CERTIFICATE_RESET"
    ]
    cycle_status_table = cycles
    tuned_loop_audit = [
        row for row in cycle_status_table if row.get("status") == "TUNED_LOOP"
    ]

    result = {
        "note": "Certification reachability audit only: not physical causality, not spacetime, not light cones, not dynamics, not empirical signal propagation.",
        "accepted_section_statuses": sorted(accepted),
        "edge_status_table": edge_status_table,
        "edge_status": edge_status,
        "robust_edges": [list(e) for e in robust_edges],
        "reachability_matrix": reach,
        "reachability": reach,
        "strongly_connected_components": scc,
        "quotient_order": [list(e) for e in q_edges],
        "quotient_component_edges": [list(e) for e in q_edges],
        "cycle_status_table": cycle_status_table,
        "cycle_audit": cycles,
        "reset_barrier_report": reset_barrier_report,
        "tuned_loop_audit": tuned_loop_audit,
        "potential_audit": phi,
    }

    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = here / out_path
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
