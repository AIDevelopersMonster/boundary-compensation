#!/usr/bin/env python3
"""Dependency-free structural validator for BC-IDPR-P3-P1-RC01.

No statement from the Gemini advisory report is used as evidence.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EVIDENCE = "No statement from the Gemini advisory report is used as evidence."


def load(name: str):
    with (ROOT / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def key(family):
    return ",".join(str(value) for value in family)


def digest(seed, family):
    payload = f"{seed}|{key(family)}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    prereg = load("PREREGISTRATION_v0.1.0.json")
    split = load("FROZEN_FAMILY_SPLIT.json")

    assert prereg["contract_id"] == "BC-IDPR-P3-P1-RC01"
    assert prereg["status"] == "PREREGISTRATION_FROZEN_AWAITING_PILOT"
    assert prereg["upstream"]["carrier_count"] == 283
    assert prereg["upstream"]["family_count"] == 24
    assert prereg["upstream"]["doi"] == "10.5281/zenodo.21401141"
    assert prereg["evidence_policy"] == EVIDENCE
    assert split["evidence_policy"] == EVIDENCE

    phase = prereg["grids"]["phase"]
    cert = prereg["grids"]["certified_local"]
    assert round((phase["stop"] - phase["start"]) / phase["step"]) + 1 == phase["count"]
    assert round((cert["stop"] - cert["start"]) / cert["step"]) + 1 == cert["count"]
    assert phase["stop"] < prereg["deformation"]["first_declared_positive_wall_eta"]
    assert math.isclose(
        prereg["deformation"]["first_declared_positive_wall_eta"] - phase["stop"],
        phase["upper_wall_margin"], rel_tol=0.0, abs_tol=1e-12
    )

    all_families = []
    for role in ("pilot", "calibration", "confirmatory"):
        families = split[role]
        assert len(families) == split["expected_counts"][role]
        for family in families:
            assert len(family) == 4
            assert family == sorted(family)
            all_families.append(tuple(family))
            prefix = split["hash_prefixes"][role][key(family)]
            assert digest(split["seed"], family).startswith(prefix)

    assert len(all_families) == 24
    assert len(set(all_families)) == 24
    assert prereg["phase_dictionary"]["integer_modes"] == list(range(2, 11))
    assert prereg["primary_confirmatory_criteria"]["confirmatory_family_count"] == 8
    assert prereg["primary_confirmatory_criteria"]["positive_family_count_min"] == 7
    assert math.isclose(
        prereg["primary_confirmatory_criteria"]["exact_one_sided_sign_p_max"],
        9 / 256, rel_tol=0.0, abs_tol=1e-12
    )

    print("RC01_PREREGISTRATION_STRUCTURE_VALID")
    print("families=24 pilot=4 calibration=12 confirmatory=8")
    print("phase_grid=1101 certified_grid=401 modes=9")
    print("confirmatory_results_present=false")


if __name__ == "__main__":
    main()
