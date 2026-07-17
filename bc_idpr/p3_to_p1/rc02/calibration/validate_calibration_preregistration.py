#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path

POLICY = "No statement from the Gemini advisory report is used as evidence."
EXPECTED_CAL = [[1,1,1,1],[1,1,2,2],[1,1,3,3],[1,1,5,5],[1,1,6,6],[1,2,4,5],[1,3,4,4],[1,3,6,6],[1,4,4,5],[1,5,6,6],[2,2,2,4],[2,3,3,6]]
EXPECTED_PILOT = [[1,2,3,4],[1,3,3,3],[1,3,4,6],[2,2,3,5]]
EXPECTED_CONFIRM = [[1,1,4,4],[1,2,2,3],[1,2,5,6],[1,3,3,5],[1,3,5,5],[1,4,5,6],[1,5,5,5],[2,2,4,6]]
EXPECTED_PAIRS = [[2,6.5],[3,8.5],[4,7.5],[5,9.5],[6,1.5],[7,3.5],[8,2.5],[9,5.5],[10,4.5]]

def fail(msg: str) -> None:
    raise SystemExit(f"RC02_CALIBRATION_PREREGISTRATION_INVALID: {msg}")

def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "CALIBRATION_PREREGISTRATION_v0.1.0.json")
    r = json.loads(path.read_text(encoding="utf-8"))
    if r.get("contract_id") != "BC-IDPR-P3-P1-RC02": fail("contract")
    if r.get("status") != "CALIBRATION_PREREGISTERED_EXECUTION_AUTHORIZED_CONFIRMATORY_SEALED": fail("status")
    s = r["stage_scope"]
    if s["calibration_families"] != EXPECTED_CAL: fail("calibration family drift")
    if s["pilot_families"] != EXPECTED_PILOT: fail("pilot family drift")
    if s["confirmatory_families"] != EXPECTED_CONFIRM: fail("confirmatory family drift")
    if len({tuple(x) for x in EXPECTED_CAL + EXPECTED_PILOT + EXPECTED_CONFIRM}) != 24: fail("split overlap")
    if s["calibration_ordered_carrier_count"] != 113: fail("carrier census")
    if s["pilot_data_allowed_in_mode_selection"] is not False: fail("pilot leakage")
    if s["confirmatory_access_authorized"] is not False: fail("confirmatory unsealed")
    a = r["frozen_analysis"]
    if a["integer_modes"] != list(range(2,11)): fail("mode drift")
    if a["frozen_pairs"] != EXPECTED_PAIRS: fail("pair drift")
    if a["mode_selection"] != "maximize primary mode_score; ties within 1e-12 choose the smallest integer mode": fail("selection rule")
    c = r["current_results"]
    if c != {"calibration_results_present":False,"confirmatory_results_present":False,"selected_mode":None,"outcome":None}: fail("premature results")
    if r.get("evidence_policy") != POLICY: fail("evidence policy")
    print("RC02_CALIBRATION_PREREGISTRATION_VALID")
    print("calibration_families=12 calibration_ordered_carriers=113 modes=9")
    print("pilot_used_for_selection=false confirmatory_access=false selected_mode=null")

if __name__ == "__main__":
    main()
