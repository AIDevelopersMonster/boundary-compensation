#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

EVIDENCE_POLICY = "No statement from the Gemini advisory report is used as evidence."
EXPECTED_COUNTS = {
    (1, 1, 4, 4): 6,
    (1, 2, 2, 3): 12,
    (1, 2, 5, 6): 24,
    (1, 3, 3, 5): 12,
    (1, 3, 5, 5): 12,
    (1, 4, 5, 6): 24,
    (1, 5, 5, 5): 4,
    (2, 2, 4, 6): 12,
}


def canonical_sha(value: object) -> str:
    payload = json.dumps(value, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("preregistration", type=Path)
    parser.add_argument("carriers", type=Path)
    args = parser.parse_args()

    record = json.loads(args.preregistration.read_text(encoding="utf-8"))
    supplement = json.loads(args.carriers.read_text(encoding="utf-8"))

    assert record["contract_id"] == "BC-IDPR-P3-P1-RC02"
    assert record["frozen_analysis"]["selected_integer_mode"] == 5
    assert record["frozen_analysis"]["selected_mode_mutable"] is False
    assert record["frozen_analysis"]["paired_control_frequency"] == 9.5
    assert record["scope"]["confirmatory_family_count"] == 8
    assert record["scope"]["confirmatory_ordered_carrier_count"] == 106

    families = {tuple(item) for item in record["scope"]["confirmatory_families"]}
    assert families == set(EXPECTED_COUNTS)

    selected = [
        carrier
        for carrier in supplement["ordered_carriers"]
        if tuple(sorted(carrier)) in families
    ]
    counts = {
        family: sum(tuple(sorted(carrier)) == family for carrier in selected)
        for family in sorted(families)
    }
    assert counts == EXPECTED_COUNTS
    assert len(selected) == 106
    assert canonical_sha(selected) == record["scope"]["ordered_carrier_list_canonical_sha256"]

    rule = record["primary_decision_rule"]
    assert rule["positive_family_count_min"] == 7
    assert rule["family_count"] == 8
    assert rule["median_family_energy_advantage_min"] == 0.02
    assert abs(rule["exact_one_sided_sign_p_max"] - 9 / 256) < 1e-15
    assert rule["directional_R1_min"] == 0.6
    assert rule["phase_class_axial_R2_min"] == 0.75

    assert record["execution_rules"]["confirmatory_results_present"] is False
    assert record["execution_rules"]["outcome"] is None
    assert record["evidence_policy"] == EVIDENCE_POLICY

    print("RC02_CONFIRMATORY_PREREGISTRATION_VALID")
    print("families=8 ordered_carriers=106 selected_mode=5 control=9.5")
    print("positive_min=7 median_min=0.02 sign_p_max=0.03515625 R1_min=0.60 R2_class_min=0.75")
    print("confirmatory_results_present=false outcome=null")


if __name__ == "__main__":
    main()
