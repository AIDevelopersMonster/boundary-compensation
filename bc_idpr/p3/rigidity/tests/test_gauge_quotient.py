#!/usr/bin/env python3
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from build_gauge_tangent import build  # noqa: E402


class GaugeQuotientTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = build(
            ROOT / "data" / "ising_fusion_rules.json",
            ROOT / "data" / "ising_F_baseline.json",
        )

    def test_exact_complex_condition(self) -> None:
        self.assertTrue(self.result["complex_condition"]["verified"])
        self.assertEqual(self.result["complex_condition"]["nonzero_entries"], [])

    def test_image_equals_kernel(self) -> None:
        self.assertEqual(self.result["rank"]["kernel_DP_dimension"], 3)
        self.assertEqual(self.result["rank"]["DG"], 3)
        self.assertEqual(self.result["rank"]["quotient_dimension"], 0)
        self.assertTrue(self.result["image_kernel_equality"]["verified"])

    def test_full_symbolic_gauge_invariance(self) -> None:
        audit = self.result["full_symbolic_gauge_audit"]
        self.assertEqual(audit["n_scalar_residuals"], 136)
        self.assertTrue(audit["verified"])
        self.assertEqual(audit["failures"], [])

    def test_independent_first_order_audit(self) -> None:
        self.assertTrue(self.result["independent_first_order_audit"]["verified"])

    def test_every_kernel_vector_has_gauge_lift(self) -> None:
        audit = self.result["kernel_lift_audit"]
        self.assertTrue(audit["verified"])
        self.assertEqual(len(audit["canonical_lifts"]), 3)

    def test_final_status(self) -> None:
        self.assertEqual(
            self.result["status"], "LOCALLY_RIGID_IN_DECLARED_COMPLEX"
        )


if __name__ == "__main__":
    unittest.main()
