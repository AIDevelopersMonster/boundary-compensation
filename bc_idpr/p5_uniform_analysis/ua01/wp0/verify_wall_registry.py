#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction

ETA_MIN = Fraction(3, 5)
ETA_MAX = Fraction(23, 20)
ANCHOR = Fraction(1, 1)
CRITICAL_INDICES = tuple(range(1, 11))


def nearest_wall_for_index(n: int) -> dict[str, object]:
    candidates = []
    for k in range(-2, 5):
        eta = Fraction(12 * k, n)
        if eta < ETA_MIN:
            distance = ETA_MIN - eta
        elif eta > ETA_MAX:
            distance = eta - ETA_MAX
        else:
            distance = Fraction(0, 1)
        candidates.append((distance, eta, k))
    distance, eta, k = min(candidates, key=lambda x: (x[0], abs(x[1] - ANCHOR)))
    return {
        "n": n,
        "k": k,
        "wall_eta_exact": str(eta),
        "wall_eta": float(eta),
        "distance_eta_exact": str(distance),
        "distance_eta": float(distance),
    }


def main() -> None:
    rows = [nearest_wall_for_index(n) for n in CRITICAL_INDICES]
    nearest = min(rows, key=lambda row: row["distance_eta"])
    assert nearest["n"] == 10
    assert nearest["wall_eta_exact"] == "6/5"
    assert nearest["distance_eta_exact"] == "1/20"

    theta_margin = math.pi / 240.0
    theta_min = math.pi * float(ETA_MIN) / 12.0
    theta_max = math.pi * float(ETA_MAX) / 12.0
    positivity = all(0.0 < n * theta_min and n * theta_max < math.pi for n in CRITICAL_INDICES)
    assert positivity

    result = {
        "schema_version": "1.0",
        "contract": "BC-IDPR-P5-UA01-WP0",
        "status": "Q_WALL_AND_REAL_BRANCH_CHAMBER_CERTIFIED",
        "coordinate": "eta = 12 theta / pi",
        "anchor_eta": 1.0,
        "target_protocol_chamber": {
            "eta_interval_exact": [str(ETA_MIN), str(ETA_MAX)],
            "eta_interval": [float(ETA_MIN), float(ETA_MAX)],
            "theta_interval": [theta_min, theta_max],
        },
        "critical_q_indices": list(CRITICAL_INDICES),
        "nearest_q_wall": nearest,
        "global_q_wall_margin": {
            "eta_exact": "1/20",
            "eta": 0.05,
            "theta_exact": "pi/240",
            "theta": theta_margin,
        },
        "nested_chambers": {
            "inherited_local_nonvanishing": {
                "eta_interval": [0.99, 1.01],
                "theta_radius_exact": "pi/1200",
                "source_status": "RIGOROUS_ARB_UNIFORM_CONDITIONING_CERTIFIED",
                "minimum_abs_omega_lower_bound": 0.16025264148217666,
            },
            "inherited_outer_q_safe": {
                "eta_interval": [0.9, 1.1],
                "theta_radius_exact": "pi/120",
                "source_status": "OUTER_Q_WALL_SAFE_DISK",
            },
            "full_rc02_protocol": {
                "eta_interval": [0.6, 1.15],
                "q_number_sign": "strictly positive for n=1,...,10",
                "branch_status": "real q-factorial and square-root branches fixed",
                "omega_nonvanishing_status": "OPEN_OUTSIDE_ETA_0.99_1.01",
            },
        },
        "per_index_nearest_walls": rows,
        "open_walls": [
            "residual-rank walls",
            "measurement-frame rank walls",
            "phase-gauge anchor zeros",
            "carrier angular-speed zeros outside the inherited local chamber",
            "operator-adapted basis conditioning walls",
        ],
        "evidence_rule": "RC02 outcomes are not used to select or alter the chambers.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
