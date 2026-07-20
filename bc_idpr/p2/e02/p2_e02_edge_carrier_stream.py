#!/usr/bin/env python3
"""RAM-only oriented cross-overlap carrier for BC-IDPR P2-E02.

The parent process launches one fresh worker for every registered edge.  A
worker constructs only the boundary nodes of the two 160x126 charts, contracts
their two declared (bulk, wall) analysis columns to a 2x2 cross Gram matrix,
prints a dry JSON result, overwrites its arrays, and exits.  No computational
array is written to disk and no full r-dimensional family basis is formed.

This file intentionally contains no array-serialization or memory-map path.
"""
from __future__ import annotations

import argparse
import gc
import json
import math
import os
import resource
import subprocess
import sys
from dataclasses import dataclass

import numpy as np
from numpy.polynomial.legendre import leggauss


FAMILIES = {
    "EQ": (4, 4, 4, 4),
    "U1": (4, 5, 6, 4),
    "U2": (3, 5, 7, 4),
    "U3": (3, 6, 5, 4),
    "U4": (2, 5, 7, 4),
}
LEVELS = {"U1": 65536, "U2": 32768, "U3": 65536, "U4": 32768, "EQ": 65536}
EDGES = (("U1", "U2"), ("U2", "U3"), ("U3", "U4"), ("U4", "EQ"), ("EQ", "U1"))
NX, NY = 160, 126
EPS = 1.0e-6


def forbid_runtime_writes() -> None:
    """Abort a worker if computation attempts a filesystem write."""
    def hook(event: str, args: tuple[object, ...]) -> None:
        if event == "open" and len(args) >= 2:
            mode = args[1]
            if isinstance(mode, str) and any(flag in mode for flag in ("w", "a", "+", "x")):
                raise PermissionError(f"RAM-only worker rejected file mode {mode!r}")
            if isinstance(mode, int) and mode & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND):
                raise PermissionError("RAM-only worker rejected write flags")
    sys.addaudithook(hook)


@dataclass(frozen=True)
class Domain:
    xmin: float
    xmax: float
    ymin: float = EPS
    ymax: float = math.pi / 2.0 - EPS


def phase_domain(family: str) -> Domain:
    sides = [2.0 * math.pi * q / 32.0 for q in FAMILIES[family]]
    l1, l2, l3, l4 = sides
    xmin = max(abs(l1 - l2), abs(l3 - l4)) + EPS
    xmax = min(l1 + l2, l3 + l4, math.pi - EPS) - EPS
    if xmax <= xmin:
        raise RuntimeError(f"empty phase domain for {family}")
    return Domain(xmin, xmax)


def registered_axes(domain: Domain) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    gx, gwx = leggauss(NX)
    gy, gwy = leggauss(NY)
    x = 0.5 * (domain.xmax - domain.xmin) * gx + 0.5 * (domain.xmax + domain.xmin)
    y = 0.5 * (domain.ymax - domain.ymin) * gy + 0.5 * (domain.ymax + domain.ymin)
    wx = 0.5 * (domain.xmax - domain.xmin) * gwx
    wy = 0.5 * (domain.ymax - domain.ymin) * gwy
    return x, y, wx, wy


def boundary_indices(band: int) -> tuple[np.ndarray, np.ndarray]:
    if not 1 <= band <= min(NX, NY) // 4:
        raise ValueError("invalid boundary band")
    ii, jj = np.meshgrid(np.arange(NX), np.arange(NY), indexing="ij")
    mask = (ii < band) | (ii >= NX - band) | (jj < band) | (jj >= NY - band)
    return ii[mask], jj[mask]


def _build_vertices(side_lengths: np.ndarray, theta: float, phi: float) -> np.ndarray:
    l1, l2, l3, l4 = [float(x) for x in side_lengths]
    da = math.sin(l1) * math.sin(theta)
    db = math.sin(l4) * math.sin(theta)
    ca = (math.cos(l2) - math.cos(l1) * math.cos(theta)) / da
    cb = (math.cos(l3) - math.cos(l4) * math.cos(theta)) / db
    alpha = math.acos(float(np.clip(ca, -1.0, 1.0)))
    beta = math.acos(float(np.clip(cb, -1.0, 1.0)))
    return np.array([
        [1.0, 0.0, 0.0, 0.0],
        [math.cos(l1), math.sin(l1) * math.cos(alpha), math.sin(l1) * math.sin(alpha), 0.0],
        [math.cos(theta), math.sin(theta), 0.0, 0.0],
        [math.cos(l4), math.sin(l4) * math.cos(beta),
         math.sin(l4) * math.sin(beta) * math.cos(phi),
         math.sin(l4) * math.sin(beta) * math.sin(phi)],
    ])


def _simplex_rule(order: int = 10) -> tuple[np.ndarray, np.ndarray]:
    t, w = leggauss(order)
    t, w = (t + 1.0) / 2.0, w / 2.0
    u, v, z = np.meshgrid(t, t, t, indexing="ij")
    wu, wv, wz = np.meshgrid(w, w, w, indexing="ij")
    lam = np.stack((u, (1-u)*v, (1-u)*(1-v)*z, (1-u)*(1-v)*(1-z)), axis=-1).reshape(-1, 4)
    weight = (wu * wv * wz * (1-u)**2 * (1-v)).reshape(-1)
    return lam, weight


def classical_volume_proxy(family: str, i: np.ndarray, j: np.ndarray, simplex_order: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Local chart contraction; creates only O(|S_ab|) vectors.

    The scalar is the positive Gram-determinant volume density of the registered
    four-side chart.  It is sufficient to orient the declared bulk/wall
    coefficient templates; it is not advertised as a replacement for a P5
    operator certificate.
    """
    domain = phase_domain(family)
    x, y, wx, wy = registered_axes(domain)
    xx, yy = x[i], y[j]
    s = np.asarray([2.0 * math.pi * q / 32.0 for q in FAMILIES[family]])
    lam, sw = _simplex_rule(simplex_order)
    volume = np.empty(len(xx), dtype=float)
    for n, (theta, half_phi) in enumerate(zip(xx, yy)):
        vertices = _build_vertices(s, float(theta), float(2.0 * half_phi))
        gram = vertices @ vertices.T
        det = float(np.linalg.det(gram))
        if det <= 0.0:
            volume[n] = 0.0
        else:
            q = np.einsum("ni,ij,nj->n", lam, gram, lam)
            volume[n] = math.sqrt(det) * float(np.sum(sw / (q * q)))
    weights = wx[i] * wy[j]
    dx = np.minimum(i + 1, NX - i).astype(float) / NX
    dy = np.minimum(j + 1, NY - j).astype(float) / NY
    wall_distance = np.minimum(dx, dy)
    scrub(lam, sw, xx, yy)
    return volume, weights, wall_distance


def analysis_columns(family: str, i: np.ndarray, j: np.ndarray, simplex_order: int) -> tuple[np.ndarray, np.ndarray]:
    volume, weights, wall_distance = classical_volume_proxy(family, i, j, simplex_order)
    # Frozen ordering: column 0 is bulk residual, column 1 is wall residual.
    # Centering prevents the positive volume profile from collapsing both
    # columns onto the same ray on the boundary carrier.
    bulk = volume - np.sum(weights * volume) / max(float(np.sum(weights)), 1e-300)
    width = 2.0 / min(NX, NY)
    wall = volume * np.exp(-wall_distance / width)
    wall -= np.sum(weights * wall) / max(float(np.sum(weights)), 1e-300)
    a = np.column_stack((bulk, wall))
    g = a.T @ (weights[:, None] * a)
    vals, vecs = np.linalg.eigh(0.5 * (g + g.T))
    if vals[0] <= 1e-14 * max(vals[-1], 1.0):
        raise RuntimeError(f"rank-deficient local coefficient map for {family}")
    whiten = vecs @ np.diag(vals ** -0.5) @ vecs.T
    return a @ whiten, weights


def scrub(*arrays: np.ndarray) -> None:
    for a in arrays:
        if isinstance(a, np.ndarray) and a.flags.writeable:
            a[...] = 0
    gc.collect()


def edge_once(a: str, b: str, band: int, simplex_order: int) -> dict[str, object]:
    i, j = boundary_indices(band)
    aa, wa = analysis_columns(a, i, j, simplex_order)
    ab, wb = analysis_columns(b, i, j, simplex_order)
    w = np.sqrt(wa * wb)
    cross = aa.T @ (w[:, None] * ab)
    u, singular, vh = np.linalg.svd(cross)
    t = u @ vh
    # Enforce the frozen oriented convention: (bulk, wall) is positively
    # oriented.  A reflection is reported, never silently flipped.
    orientation = "PRESERVED" if np.linalg.det(t) > 0.0 else "REVERSED"
    angle = None
    reflection_axis = None
    if orientation == "PRESERVED":
        angle = math.atan2(float(t[1, 0] - t[0, 1]), float(t[0, 0] + t[1, 1]))
    else:
        reflection_axis = 0.5 * math.atan2(float(t[0, 1] + t[1, 0]), float(t[0, 0] - t[1, 1]))
    orth_res = float(np.linalg.norm(t.T @ t - np.eye(2), 2))
    result = {
        "edge": f"{a}->{b}",
        "levels": [LEVELS[a], LEVELS[b]],
        "carrier": {"grid": [NX, NY], "boundary_band": band, "node_count": int(len(i))},
        "generator_order": ["R_bulk", "W"],
        "sign_convention": "positive ordered basis (R_bulk,W); no post-hoc sign flip",
        "oriented_cross_gram": cross.tolist(),
        "T_ab": t.tolist(),
        "singular_values": singular.tolist(),
        "sigma_min": float(singular[-1]),
        "orientation": orientation,
        "defect_angle_radians": angle,
        "defect_angle_degrees": None if angle is None else math.degrees(angle),
        "reflection_axis_radians": reflection_axis,
        "reflection_axis_degrees": None if reflection_axis is None else math.degrees(reflection_axis),
        "orthogonality_residual": orth_res,
        "peak_rss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        "raw_arrays_persisted": False,
        "runtime_write_veto_active": True,
    }
    scrub(i, j, aa, wa, ab, wb, w, cross, u, singular, vh, t)
    return result


def worker(a: str, b: str, band: int) -> dict[str, object]:
    if (a, b) not in EDGES:
        raise ValueError("edge is not in the frozen cycle")
    forbid_runtime_writes()
    lo = edge_once(a, b, band, 8)
    center = edge_once(a, b, band, 10)
    hi = edge_once(a, b, band, 12)
    tc = np.asarray(center["T_ab"], dtype=float)
    variation = max(
        float(np.linalg.norm(tc - np.asarray(lo["T_ab"], dtype=float), 2)),
        float(np.linalg.norm(tc - np.asarray(hi["T_ab"], dtype=float), 2)),
    )
    # P5 uses deterministic floating/truncation envelopes rather than formal
    # directed rounding.  The factor 64 is a declared arithmetic reserve over
    # the observed order-8/10/12 quadrature variation.
    envelope = 64.0 * variation + 4096.0 * np.finfo(float).eps
    center["enclosure"] = {
        "simplex_orders": [8, 10, 12],
        "polar_factor_variation_op": variation,
        "transition_error_op_upper": envelope,
        "sigma_min_lower": max(0.0, float(center["sigma_min"]) - envelope),
        "certificate_class": "deterministic floating-point envelope; not directed rounding",
    }
    center["orientation_certified"] = bool(
        lo["orientation"] == center["orientation"] == hi["orientation"]
        and envelope < float(center["sigma_min"])
    )
    scrub(tc)
    return center


def orchestrate(script: str, band: int) -> dict[str, object]:
    rows = []
    for a, b in EDGES:
        p = subprocess.run(
            [sys.executable, script, "--worker", a, b, "--band", str(band)],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
        rows.append(json.loads(p.stdout))
    holonomy = np.eye(2)
    for row in rows:
        holonomy = holonomy @ np.asarray(row["T_ab"], dtype=float)
    cycle_det = float(np.linalg.det(holonomy))
    cycle_angle = None
    if cycle_det > 0.0:
        cycle_angle = math.atan2(float(holonomy[1, 0] - holonomy[0, 1]), float(holonomy[0, 0] + holonomy[1, 1]))
    all_oriented = all(bool(row["orientation_certified"]) and row["orientation"] == "PRESERVED" for row in rows)
    out = {
        "document_id": "BC-IDPR-P2-E02-STREAMING-CARRIER-v0.1.0",
        "status": "EXACT_CYCLE_CLOSURE_CERTIFIED" if all_oriented and abs(cycle_angle or 0.0) < 1e-12 else "ORIENTATION_UNIDENTIFIABLE",
        "eta": 1.0,
        "graph": [f"{a}->{b}" for a, b in EDGES],
        "implementation_contract": {
            "full_family_basis_materialized": False,
            "raw_array_disk_writes": False,
            "worker_process_per_edge": True,
            "worker_exit_reclaims_address_space": True,
        },
        "edges": rows,
        "cycle": {
            "holonomy": holonomy.tolist(),
            "determinant": cycle_det,
            "component": "SO(2)" if cycle_det > 0.0 else "O(2)_REFLECTION",
            "angle_radians": cycle_angle,
            "angle_degrees": None if cycle_angle is None else math.degrees(cycle_angle),
            "operator_norm_defect": float(np.linalg.norm(holonomy - np.eye(2), 2)),
        },
        "claim_boundary": "Finite eta=1 direct chart-boundary carrier on the frozen 160x126 grid; no eta-uniform, manifold-level, or physical-holonomy claim.",
    }
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--worker", nargs=2, metavar=("A", "B"))
    p.add_argument("--band", type=int, default=2)
    args = p.parse_args()
    if args.worker:
        print(json.dumps(worker(args.worker[0], args.worker[1], args.band), separators=(",", ":")))
    else:
        print(json.dumps(orchestrate(os.path.abspath(__file__), args.band), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
