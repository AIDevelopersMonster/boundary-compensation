#!/usr/bin/env python3
"""P2-OR01 RAM-only gauge, carrier and pullback robustness audit.

This audit does not alter P2-E02.  It stress-tests the reported Z2 orientation
signal in fresh subprocesses and persists only dry 2x2 transition data.
"""
from __future__ import annotations

import argparse
import gc
import importlib.util
import itertools
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys

import numpy as np

ROOT = Path(__file__).resolve().parent
WORKSPACE = next(p for p in (ROOT.parent, ROOT.parent.parent)
                 if (p / "p2_e02_streaming" / "release").is_dir())
BASE_PATH = WORKSPACE / "p2_e02_streaming" / "release" / "p2_e02_edge_carrier_stream.py"
BASE_RESULTS = WORKSPACE / "p2_e02_streaming" / "release" / "P2_E02_RESULTS.json"
EDGES = (("U1", "U2"), ("U2", "U3"), ("U3", "U4"), ("U4", "EQ"), ("EQ", "U1"))
VERTICES = ("U1", "U2", "U3", "U4", "EQ")


def load_base():
    spec = importlib.util.spec_from_file_location("p2_e02_base", BASE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import P2-E02 worker")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def scrub(*arrays: np.ndarray) -> None:
    for a in arrays:
        if isinstance(a, np.ndarray) and a.flags.writeable:
            a[...] = 0
    gc.collect()


def analysis_variant(base, family: str, i: np.ndarray, j: np.ndarray, order: int,
                     wall_scale: float, flip_x: bool, flip_y: bool):
    ii = base.NX - 1 - i if flip_x else i.copy()
    jj = base.NY - 1 - j if flip_y else j.copy()
    volume, weights, wall_distance = base.classical_volume_proxy(family, ii, jj, order)
    mean_v = np.sum(weights * volume) / max(float(np.sum(weights)), 1e-300)
    bulk = volume - mean_v
    width = wall_scale * 2.0 / min(base.NX, base.NY)
    wall = volume * np.exp(-wall_distance / width)
    wall -= np.sum(weights * wall) / max(float(np.sum(weights)), 1e-300)
    a = np.column_stack((bulk, wall))
    gram = a.T @ (weights[:, None] * a)
    vals, vecs = np.linalg.eigh(0.5 * (gram + gram.T))
    if vals[0] <= 1e-14 * max(vals[-1], 1.0):
        raise RuntimeError("rank-deficient variant")
    white = vecs @ np.diag(vals ** -0.5) @ vecs.T
    out = a @ white
    scrub(ii, jj, volume, wall_distance, bulk, wall, a, gram, vals, vecs, white)
    return out, weights


def edge_variant(a: str, b: str, band: int, order: int, wall_scale: float,
                 a_flip_x: bool, a_flip_y: bool, b_flip_x: bool, b_flip_y: bool):
    base = load_base()
    base.forbid_runtime_writes()
    i, j = base.boundary_indices(band)
    aa, wa = analysis_variant(base, a, i, j, order, wall_scale, a_flip_x, a_flip_y)
    ab, wb = analysis_variant(base, b, i, j, order, wall_scale, b_flip_x, b_flip_y)
    w = np.sqrt(wa * wb)
    cross = aa.T @ (w[:, None] * ab)
    u, s, vh = np.linalg.svd(cross)
    t = u @ vh
    det = float(np.linalg.det(t))
    result = {
        "edge": f"{a}->{b}", "band": band, "simplex_order": order,
        "wall_scale": wall_scale,
        "pullback": {
            "a_flip_x": a_flip_x, "a_flip_y": a_flip_y,
            "b_flip_x": b_flip_x, "b_flip_y": b_flip_y,
        },
        "determinant": det,
        "cross_gram_determinant": float(np.linalg.det(cross)),
        "component": "SO(2)" if det > 0 else "O(2)_REFLECTION",
        "sigma_min": float(s[-1]), "T_ab": t.tolist(),
        "peak_rss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "raw_arrays_persisted": False,
    }
    scrub(i, j, aa, wa, ab, wb, w, cross, u, s, vh, t)
    return result


def run_worker(script: str, args: list[str]):
    p = subprocess.run([sys.executable, script, "--worker", *args, "sentinel"], check=True,
                       text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    return json.loads(p.stdout)


def d4_group():
    mats = []
    for swap in (False, True):
        p = np.array([[0., 1.], [1., 0.]]) if swap else np.eye(2)
        for sx, sy in itertools.product((-1., 1.), repeat=2):
            mats.append(np.diag([sx, sy]) @ p)
    return mats


def gauge_exhaustion(ts: dict[str, np.ndarray]):
    group = d4_group()
    signs = set()
    max_orth = 0.0
    count = 0
    for choice in itertools.product(range(len(group)), repeat=len(VERTICES)):
        gauges = {v: group[k] for v, k in zip(VERTICES, choice)}
        h = np.eye(2)
        for a, b in EDGES:
            tp = gauges[a].T @ ts[f"{a}->{b}"] @ gauges[b]
            h = h @ tp
            max_orth = max(max_orth, float(np.linalg.norm(tp.T @ tp - np.eye(2), 2)))
        signs.add(1 if np.linalg.det(h) > 0 else -1)
        count += 1
    return {"gauge_assignments": count, "cycle_determinant_signs": sorted(signs),
            "invariant": signs == {-1}, "max_orthogonality_residual": max_orth}


def orchestrate(script: str):
    stability = []
    for band in (2, 4, 8, 12, 16):
        for wall_scale in (0.5, 1.0, 2.0, 4.0):
            stability.append(run_worker(script, ["U3", "U4", str(band), "10", str(wall_scale), "0", "0", "0", "0"]))
    for order in (8, 10, 12):
        stability.append(run_worker(script, ["U3", "U4", "2", str(order), "1.0", "0", "0", "0", "0"]))

    # Locate the component wall for the widest tested carrier.  The sign of
    # det(K_ab) equals the component of its nonsingular polar factor.
    lo_scale, hi_scale = 2.0, 4.0
    lo_row = run_worker(script, ["U3", "U4", "16", "10", str(lo_scale), "0", "0", "0", "0"])
    hi_row = run_worker(script, ["U3", "U4", "16", "10", str(hi_scale), "0", "0", "0", "0"])
    if lo_row["cross_gram_determinant"] * hi_row["cross_gram_determinant"] >= 0:
        raise RuntimeError("orientation-wall bracket lost")
    for _ in range(18):
        mid_scale = 0.5 * (lo_scale + hi_scale)
        mid_row = run_worker(script, ["U3", "U4", "16", "10", str(mid_scale), "0", "0", "0", "0"])
        if lo_row["cross_gram_determinant"] * mid_row["cross_gram_determinant"] <= 0:
            hi_scale, hi_row = mid_scale, mid_row
        else:
            lo_scale, lo_row = mid_scale, mid_row
    wall_bracket = {
        "band": 16, "simplex_order": 10,
        "wall_scale_lower": lo_scale, "wall_scale_upper": hi_scale,
        "bracket_width": hi_scale - lo_scale,
        "lower_cross_gram_determinant": lo_row["cross_gram_determinant"],
        "upper_cross_gram_determinant": hi_row["cross_gram_determinant"],
        "lower_sigma_min": lo_row["sigma_min"],
        "upper_sigma_min": hi_row["sigma_min"],
    }

    global_pullbacks = []
    for fx, fy in ((0, 0), (1, 0), (0, 1), (1, 1)):
        rows = []
        h = np.eye(2)
        for a, b in EDGES:
            row = run_worker(script, [a, b, "2", "10", "1.0", str(fx), str(fy), str(fx), str(fy)])
            rows.append({"edge": row["edge"], "component": row["component"], "sigma_min": row["sigma_min"]})
            h = h @ np.asarray(row["T_ab"], float)
        global_pullbacks.append({"flip_x": bool(fx), "flip_y": bool(fy),
                                 "cycle_determinant": float(np.linalg.det(h)), "edges": rows})
        scrub(h)

    relative_pullbacks = []
    for fx, fy in ((1, 0), (0, 1), (1, 1)):
        relative_pullbacks.append(run_worker(script, ["U3", "U4", "2", "10", "1.0", "0", "0", str(fx), str(fy)]))

    base = json.loads(BASE_RESULTS.read_text())
    ts = {e["edge"]: np.asarray(e["T_ab"], float) for e in base["edges"]}
    gauge = gauge_exhaustion(ts)
    for t in ts.values(): scrub(t)

    stable_reflection = all(r["component"] == "O(2)_REFLECTION" for r in stability)
    well_conditioned = [r for r in stability if r["sigma_min"] >= 1.0e-2]
    well_conditioned_reflection = all(r["component"] == "O(2)_REFLECTION" for r in well_conditioned)
    component_walls = [r for r in stability if r["component"] != "O(2)_REFLECTION"]
    global_negative = all(r["cycle_determinant"] < 0 for r in global_pullbacks)
    relative_components = sorted({r["component"] for r in relative_pullbacks})
    return {
        "document_id": "BC-IDPR-P2-OR01-v0.1.0",
        "title": "U3/U4 Orientation and Gauge Robustness Audit",
        "status": "CONDITIONAL_Z2_SIGNAL__ORIENTATION_WALL_AND_PULLBACK_DEPENDENCE_FOUND",
        "tests": {
            "u3_u4_stability_cases": len(stability),
            "all_stability_cases_reflective": stable_reflection,
            "well_conditioned_threshold": 1.0e-2,
            "well_conditioned_case_count": len(well_conditioned),
            "all_well_conditioned_cases_reflective": well_conditioned_reflection,
            "orientation_component_wall_count": len(component_walls),
            "orientation_component_walls": component_walls,
            "orientation_wall_bracket": wall_bracket,
            "bands": [2, 4, 8, 12, 16],
            "wall_scales": [0.5, 1.0, 2.0, 4.0],
            "simplex_orders": [8, 10, 12],
            "global_pullback_cycle_negative": global_negative,
            "relative_pullback_components": relative_components,
            "gauge": gauge,
        },
        "stability": stability,
        "global_pullbacks": global_pullbacks,
        "relative_u3_u4_pullbacks": relative_pullbacks,
        "interpretation": {
            "supported": "The Z2 reflection survives every well-conditioned carrier-width, wall-scale and quadrature test, all global chart reversals, and all 32768 local D4 coefficient-gauge assignments.",
            "not_supported": "The component changes at a near-singular carrier wall and under relative x-oriented pullbacks; physical non-orientability therefore remains unproved until the physical cross-family pullback and genuine P5 residual matrix elements are identified.",
        },
        "raw_arrays_persisted": False,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--worker", nargs=10, metavar=("A", "B", "BAND", "ORDER", "WALL", "AFX", "AFY", "BFX", "BFY", "EXTRA"))
    # argparse requires a stable arity; orchestrator appends a harmless sentinel.
    args, unknown = p.parse_known_args()
    if args.worker:
        a, b, band, order, wall, afx, afy, bfx, bfy, _ = args.worker
        print(json.dumps(edge_variant(a, b, int(band), int(order), float(wall),
                                      bool(int(afx)), bool(int(afy)), bool(int(bfx)), bool(int(bfy))),
                         separators=(",", ":")))
    else:
        print(json.dumps(orchestrate(os.path.abspath(__file__)), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
