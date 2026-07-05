#!/usr/bin/env python3
"""BC-CI-VIII certified local distances demo.

Finite graph audit only. The outputs are certified distance diagnostics,
not spacetime geometry, not physical intervals, and not metric tensors.
"""
import json, math, heapq
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CFG = ROOT / "configs" / "default_distances.json"
OUT = ROOT / "data" / "certified_local_distances_audit.json"
FIG = ROOT / "figures"


def load():
    with CFG.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_graph(cfg, include_reset=False, robust_only=True):
    g = {n: [] for n in cfg["nodes"]}
    for e in cfg["edges"]:
        if robust_only and not e.get("robust", False):
            continue
        if not include_reset and e.get("reset", False):
            continue
        g[e["source"]].append(e)
    return g


def enumerate_paths(g, src, dst, budget):
    paths = []
    def rec(node, path, seen_depth):
        if len(path) > budget:
            return
        if node == dst:
            paths.append(list(path))
            return
        for e in g.get(node, []):
            # path budget prevents infinite cycle counting
            rec(e["target"], path + [e], seen_depth + 1)
    rec(src, [], 0)
    return paths


def dijkstra(g, nodes, src):
    dist = {n: math.inf for n in nodes}
    dist[src] = 0.0
    pq = [(0.0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for e in g.get(u, []):
            v = e["target"]
            nd = d + float(e["cost"])
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


def widest_path(g, nodes, src):
    width = {n: 0.0 for n in nodes}
    width[src] = math.inf
    pq = [(-math.inf, src)]
    while pq:
        negw, u = heapq.heappop(pq)
        w = -negw
        if w < width[u]:
            continue
        for e in g.get(u, []):
            v = e["target"]
            cand = min(w, float(e["margin"]))
            if cand > width[v]:
                width[v] = cand
                heapq.heappush(pq, (-cand, v))
    return width


def support_fraction_for_paths(paths):
    if not paths:
        return 0.0
    # Declared toy aggregation: union proxy clipped to 1.0 from product failures.
    # This is not probability unless the protocol declares it as such.
    fail_prod = 1.0
    for path in paths:
        if not path:
            frac = 1.0
        else:
            frac = 1.0
            for e in path:
                frac *= float(e.get("support_fraction", 0.0))
        fail_prod *= (1.0 - frac)
    return min(1.0, max(0.0, 1.0 - fail_prod))


def graph_connected_through_reset(cfg, src, dst):
    g_all = build_graph(cfg, include_reset=True, robust_only=False)
    seen = set([src])
    stack = [src]
    while stack:
        u = stack.pop()
        if u == dst:
            return True
        for e in g_all.get(u, []):
            v = e["target"]
            if v not in seen:
                seen.add(v); stack.append(v)
    return False


def write_svg_graph(cfg):
    pos = {"A":(60,120), "B":(190,60), "C":(190,180), "D":(330,120), "E":(470,80), "F":(470,200)}
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="560" height="260" viewBox="0 0 560 260">']
    parts.append('<rect x="0" y="0" width="560" height="260" fill="white"/>')
    for e in cfg["edges"]:
        x1,y1 = pos[e["source"]]; x2,y2 = pos[e["target"]]
        dash = ' stroke-dasharray="6,4"' if e.get("reset") else ''
        stroke = '#999' if not e.get("robust") else '#111'
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="2" marker-end="url(#arrow)"{dash}/>')
        mx,my=(x1+x2)/2,(y1+y2)/2
        parts.append(f'<text x="{mx}" y="{my-5}" font-size="10" text-anchor="middle">c={e["cost"]}, m={e["margin"]}</text>')
    parts.append('<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#111"/></marker></defs>')
    for n,(x,y) in pos.items():
        parts.append(f'<circle cx="{x}" cy="{y}" r="18" fill="#f5f5f5" stroke="#111"/>')
        parts.append(f'<text x="{x}" y="{y+5}" font-size="14" text-anchor="middle">{n}</text>')
    parts.append('<text x="280" y="240" font-size="12" text-anchor="middle">Certified local distance graph (dashed edge is reset/non-robust)</text>')
    parts.append('</svg>')
    (FIG / "certified_distance_graph.svg").write_text("\n".join(parts), encoding="utf-8")


def write_svg_matrix(nodes, matrix):
    cell=44; left=70; top=40
    w=left+cell*(len(nodes)+1); h=top+cell*(len(nodes)+1)+30
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">']
    parts.append('<rect width="100%" height="100%" fill="white"/>')
    for i,n in enumerate(nodes):
        parts.append(f'<text x="{left+cell*(i+1)+cell/2}" y="25" font-size="12" text-anchor="middle">{n}</text>')
        parts.append(f'<text x="35" y="{top+cell*i+cell/2+5}" font-size="12" text-anchor="middle">{n}</text>')
    for r,a in enumerate(nodes):
        for c,b in enumerate(nodes):
            val=matrix[a][b]
            txt='inf' if val is None else (str(val) if isinstance(val,int) else f'{val:.1f}')
            shade = 240 if val is None else max(170, 245-int(20*(val if isinstance(val,(int,float)) else 0)))
            parts.append(f'<rect x="{left+cell*(c+1)}" y="{top+cell*r}" width="{cell}" height="{cell}" fill="rgb({shade},{shade},{shade})" stroke="#aaa"/>')
            parts.append(f'<text x="{left+cell*(c+1)+cell/2}" y="{top+cell*r+cell/2+5}" font-size="11" text-anchor="middle">{txt}</text>')
    parts.append(f'<text x="{w/2}" y="{h-10}" font-size="12" text-anchor="middle">Depth distance matrix; inf means unreachable under protocol</text>')
    parts.append('</svg>')
    (FIG / "distance_matrix.svg").write_text("\n".join(parts), encoding="utf-8")


def main():
    cfg = load()
    nodes = cfg["nodes"]
    budget = int(cfg["path_budget"])
    g = build_graph(cfg, include_reset=False, robust_only=True)
    depth = {a:{} for a in nodes}
    cost = {a:{} for a in nodes}
    bott = {a:{} for a in nodes}
    entropy_dist = {a:{} for a in nodes}
    status = []
    for a in nodes:
        costs = dijkstra(g, nodes, a)
        widths = widest_path(g, nodes, a)
        for b in nodes:
            paths = enumerate_paths(g, a, b, budget)
            depth[a][b] = min((len(p) for p in paths), default=None)
            cost[a][b] = None if math.isinf(costs[b]) else round(costs[b], 4)
            bott[a][b] = None if widths[b] == 0.0 else ("inf" if math.isinf(widths[b]) else round(widths[b], 4))
            frac = support_fraction_for_paths(paths)
            entropy_dist[a][b] = None if frac <= 0 else round(-math.log(frac), 4)
            if depth[a][b] is None:
                st = "RESET_BLOCKED" if graph_connected_through_reset(cfg, a, b) else "UNREACHABLE"
            elif bott[a][b] != "inf" and bott[a][b] is not None and bott[a][b] < cfg["margin_warning_threshold"]:
                st = "MARGIN_LOW"
            else:
                st = "CERTIFIED_DISTANCE"
            status.append({"source":a,"target":b,"status":st,"path_count_under_budget":len(paths)})
    report = {
        "nonclaim": "certified distance diagnostics, not spacetime geometry",
        "path_budget": budget,
        "depth_distance_matrix": depth,
        "cost_distance_matrix": cost,
        "bottleneck_margin_matrix": bott,
        "entropy_support_distance": entropy_dist,
        "status_table": status,
        "global_statuses": ["ENTROPY_DISTANCE_NONMETRIC", "METRIC_TENSOR_NONCLAIM"]
    }
    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    write_svg_graph(cfg)
    write_svg_matrix(nodes, depth)
    print(json.dumps({"wrote": str(OUT), "nodes": len(nodes), "statuses": len(status)}, indent=2))

if __name__ == "__main__":
    main()
