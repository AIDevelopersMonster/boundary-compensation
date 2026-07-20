#!/usr/bin/env python3
"""P2-OR02 physical U3/U4 pullback identification audit.

The frozen N15 spherical four-gon chart embeds every family into the SU(2)
character coordinates (a,b,c,d,x,y,z).  The first four coordinates are the
ordered boundary traces and are constant on a family.  This audit checks the
U3/U4 images on the complete 160x126 registered grid, but persists only dry
summary data.  No family support basis or raw physical grid is written.
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import json
import math
import os
import resource
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.spatial import cKDTree


FAMILIES = {"U3": (3, 6, 5, 4), "U4": (2, 5, 7, 4)}
NX, NY = 160, 126
EPS = 1.0e-6
ROUNDING_RESERVE = 1.0e-12


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def source_root() -> Path:
    for base in Path(__file__).resolve().parents:
        candidate = base / "p2_e02_streaming" / "n15_source"
        if candidate.is_dir():
            return base
    raise RuntimeError("Frozen N15 source tree not found")


def forbid_runtime_writes() -> None:
    def hook(event: str, args: tuple[object, ...]) -> None:
        if event == "open" and len(args) >= 2:
            mode = args[1]
            if isinstance(mode, str) and any(x in mode for x in ("w", "a", "+", "x")):
                raise PermissionError("RAM-only worker rejected a file write")
            if isinstance(mode, int) and mode & (
                os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND
            ):
                raise PermissionError("RAM-only worker rejected write flags")
    sys.addaudithook(hook)


def scrub(*arrays: np.ndarray) -> None:
    for array in arrays:
        if isinstance(array, np.ndarray) and array.flags.writeable:
            array[...] = 0
    gc.collect()


def qmul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.array([
        a[0] * b[0] - np.dot(a[1:], b[1:]),
        a[0] * b[1] + b[0] * a[1] + a[2] * b[3] - a[3] * b[2],
        a[0] * b[2] + b[0] * a[2] + a[3] * b[1] - a[1] * b[3],
        a[0] * b[3] + b[0] * a[3] + a[1] * b[2] - a[2] * b[1],
    ])


def qconj(a: np.ndarray) -> np.ndarray:
    return np.r_[a[0], -a[1:]]


def qtrace(a: np.ndarray) -> float:
    return float(2.0 * a[0])


def side_lengths(family: str) -> np.ndarray:
    return np.asarray([math.pi * q / 16.0 for q in FAMILIES[family]], dtype=float)


def boundary_trace_vector(family: str) -> np.ndarray:
    l1, l2, l3, l4 = side_lengths(family)
    # N9 convention: (a,b,c,d)=(tr m4,tr m3,tr m2,tr m1).
    return np.asarray([2*math.cos(l4), 2*math.cos(l3), 2*math.cos(l2), 2*math.cos(l1)])


@dataclass(frozen=True)
class Domain:
    xmin: float
    xmax: float
    ymin: float = EPS
    ymax: float = math.pi / 2.0 - EPS


def domain(family: str) -> Domain:
    l1, l2, l3, l4 = side_lengths(family)
    return Domain(
        max(abs(l1-l2), abs(l3-l4)) + EPS,
        min(l1+l2, l3+l4, math.pi-EPS) - EPS,
    )


def axes(family: str) -> tuple[np.ndarray, np.ndarray]:
    d = domain(family)
    gx, _ = leggauss(NX)
    gy, _ = leggauss(NY)
    x = 0.5*(d.xmax-d.xmin)*gx + 0.5*(d.xmax+d.xmin)
    y = 0.5*(d.ymax-d.ymin)*gy + 0.5*(d.ymax+d.ymin)
    return x, y


def vertices(family: str, theta: float, phi: float) -> np.ndarray:
    l1, l2, l3, l4 = side_lengths(family)
    ca = (math.cos(l2)-math.cos(l1)*math.cos(theta))/(math.sin(l1)*math.sin(theta))
    cb = (math.cos(l3)-math.cos(l4)*math.cos(theta))/(math.sin(l4)*math.sin(theta))
    alpha = math.acos(float(np.clip(ca, -1.0, 1.0)))
    beta = math.acos(float(np.clip(cb, -1.0, 1.0)))
    return np.asarray([
        [1.0, 0.0, 0.0, 0.0],
        [math.cos(l1), math.sin(l1)*math.cos(alpha), math.sin(l1)*math.sin(alpha), 0.0],
        [math.cos(theta), math.sin(theta), 0.0, 0.0],
        [math.cos(l4), math.sin(l4)*math.cos(beta),
         math.sin(l4)*math.sin(beta)*math.cos(phi),
         math.sin(l4)*math.sin(beta)*math.sin(phi)],
    ])


def character_embedding(family: str, theta: float, half_phi: float) -> np.ndarray:
    v = vertices(family, theta, 2.0*half_phi)
    v1, v2, v3, v4 = v
    m1 = qmul(v2, qconj(v1))
    m2 = qmul(v3, qconj(v2))
    m3 = qmul(v4, qconj(v3))
    m4 = qmul(v1, qconj(v4))
    aq, bq, cq, dq = m4, m3, m2, m1
    return np.asarray([
        qtrace(aq), qtrace(bq), qtrace(cq), qtrace(dq),
        qtrace(qmul(aq, bq)), qtrace(qmul(bq, cq)), qtrace(qmul(aq, cq)),
    ])


def build_grid(family: str) -> tuple[np.ndarray, dict[str, object]]:
    x, y = axes(family)
    out = np.empty((NX*NY, 7), dtype=float)
    k = 0
    for theta in x:
        for half_phi in y:
            out[k] = character_embedding(family, float(theta), float(half_phi))
            k += 1
    boundary = boundary_trace_vector(family)
    boundary_residual = float(np.max(np.abs(out[:, :4] - boundary)))
    ranges = [[float(np.min(out[:, q])), float(np.max(out[:, q]))] for q in range(4, 7)]
    summary = {
        "family": family,
        "labels": list(FAMILIES[family]),
        "domain": [domain(family).xmin, domain(family).xmax, EPS, math.pi/2.0-EPS],
        "grid": [NX, NY],
        "nodes": NX*NY,
        "ordered_boundary_traces": boundary.tolist(),
        "maximum_boundary_trace_residual": boundary_residual,
        "internal_character_ranges_xyz": ranges,
    }
    scrub(x, y, boundary)
    return out, summary


def audit() -> dict[str, object]:
    forbid_runtime_writes()
    root = source_root()
    n15 = root / "p2_e02_streaming/n15_source/BC-Spec-L1-P04-P-N15-v0.1.0-ru-package"
    config_path = n15 / "n15_sealed_config.json"
    chart_path = n15 / "support/n14_reference/support/n12_reference/support/support/n9_ordered_volume_audit.py"
    p5_path = root / "p2_e02_streaming/sources/BC-IDPR-P5-Uniform-Analysis-v0.1.0-preprint.pdf"
    u3, s3 = build_grid("U3")
    u4, s4 = build_grid("U4")
    b3, b4 = boundary_trace_vector("U3"), boundary_trace_vector("U4")
    delta = b3-b4
    boundary_distance = float(np.linalg.norm(delta))
    tree = cKDTree(u4)
    nearest, _ = tree.query(u3, k=1, workers=1)
    sampled_distance = float(np.min(nearest))
    separation_lower = boundary_distance - ROUNDING_RESERVE
    same_boundary_sector = bool(np.array_equal(np.sort(FAMILIES["U3"]), np.sort(FAMILIES["U4"])))
    separated = bool(separation_lower > 0.0 and sampled_distance >= separation_lower)
    result = {
        "document_id": "BC-IDPR-P2-OR02-v0.1.0",
        "title": "Cross-Family Physical Pullback Identification",
        "status": "P2_CERTIFICATE_RESET" if separated else "PHYSICAL_PULLBACK_WALL_CROSSED",
        "frozen_source_convention": {
            "embedding": "N9/N12/N15 ordered SU(2) character coordinates (a,b,c,d,x,y,z)",
            "side_length_rule": "ell_i = 2*pi*q_i/32 = pi*q_i/16",
            "boundary_order": ["tr(m4)", "tr(m3)", "tr(m2)", "tr(m1)"],
            "grid": [NX, NY],
            "source_sha256": {
                "n15_sealed_config": sha256_file(config_path),
                "n9_four_gon_chart": sha256_file(chart_path),
                "p5_typed_uniform_analysis": sha256_file(p5_path),
            },
        },
        "families": [s3, s4],
        "physical_overlap_test": {
            "boundary_trace_difference_u3_minus_u4": delta.tolist(),
            "boundary_trace_euclidean_distance": boundary_distance,
            "certified_separation_lower": separation_lower,
            "complete_grid_nearest_distance": sampled_distance,
            "boundary_label_multisets_equal": same_boundary_sector,
            "physical_images_disjoint": separated,
            "proof_class": "Exact sector separation: boundary traces are constant family invariants and cos is injective on the frozen side-length interval; the displayed decimal lower bound uses a 1e-12 arithmetic reserve.",
        },
        "pullback": {
            "exists": False if separated else None,
            "jacobian_orientation": "UNDEFINED_FOR_DISJOINT_PHYSICAL_IMAGES" if separated else "WALL_TEST_REQUIRED",
            "post_hoc_index_reversal_used": False,
        },
        "cross_gram": {
            "defined": False if separated else None,
            "reason": "No common physical carrier: U3 and U4 lie in distinct ordered-boundary character sectors." if separated else "Physical wall requires local resolution.",
            "same_index_proxy_rejected": separated,
        },
        "decision": {
            "p2_e02_physical_interpretation": "RESET" if separated else "BLOCKED_AT_WALL",
            "z2_obstruction_certified": False,
            "mobius_interpretation_certified": False,
            "next_object": "P2-RC01 Typed Global Carrier and Coefficient-Analysis Map Reconstruction" if separated else "P2-OR03 Physical Pullback Wall Resolution",
        },
        "resource_contract": {
            "full_family_basis_materialized": False,
            "raw_grid_persisted": False,
            "runtime_write_veto_active": True,
            "raw_arrays_scrubbed_before_exit": True,
            "peak_rss_kib": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        },
        "claim_boundary": "Positive separation certificate for the frozen finite N15 U3/U4 character images; no arbitrary-family, continuum, spacetime, or physical-topology claim.",
    }
    scrub(u3, u4, b3, b4, delta, nearest)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    result = audit()
    print(json.dumps(result, sort_keys=True, indent=None if args.compact else 2))


if __name__ == "__main__":
    main()
