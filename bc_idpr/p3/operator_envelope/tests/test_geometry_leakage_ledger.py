import importlib.util
import sys
import unittest
from pathlib import Path

import mpmath as mp

P = Path(__file__).parents[1] / "src" / "geometry_leakage_ledger.py"
S = importlib.util.spec_from_file_location("m3", P)
m3 = importlib.util.module_from_spec(S)
sys.modules["m3"] = m3
assert S.loader is not None
S.loader.exec_module(m3)


class GeometryLeakageLedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 80
        cls.result = m3.build(samples=9, dps=80, config=None)

    def test_status(self):
        self.assertEqual(self.result["status"], "COMPLETE_EXTERNAL_GEOMETRY_AND_ZERO_LEAKAGE_CERTIFIED")

    def test_exact_external_geometry(self):
        checks = self.result["external_geometry"]["checks"]
        self.assertTrue(checks["all_edges_unit"])
        self.assertTrue(checks["all_faces_equilateral_area"])
        self.assertTrue(checks["closure_exact"])
        self.assertTrue(checks["normal_gram_exact"])
        self.assertEqual(checks["normal_gram_rank"], 3)
        self.assertTrue(checks["normal_gram_null_vector_ones"])
        self.assertTrue(checks["volume_exact"])
        self.assertTrue(checks["label_area_calibration_exact"])
        self.assertTrue(checks["noncoplanar_normals"])

    def test_external_leakage_is_zero(self):
        self.assertEqual(self.result["independent_path_certificate"]["forbidden_external_leakage_norm"], "0")
        self.assertTrue(all(x["derivative"] == "0" for x in self.result["external_leakage_ledger"]))

    def test_internal_response_nonzero(self):
        anchor = self.result["anchor_internal_response"]
        self.assertGreater(mp.mpf(anchor["internal_response_norm"]), 0)
        self.assertNotEqual(mp.mpf(anchor["spectral_shape_derivative"]), 0)
        self.assertNotEqual(mp.mpf(anchor["orientation_correlation_derivative"]), 0)

    def test_intrinsic_margin_persists(self):
        self.assertGreater(mp.mpf(self.result["grid_summary"]["minimum_intrinsic_margin"]), 0)
        self.assertGreater(mp.mpf(self.result["grid_summary"]["minimum_operator_norm_dual_lower_bound"]), 0)

    def test_q_racah_conditioning(self):
        self.assertLess(mp.mpf(self.result["grid_summary"]["maximum_orthogonality_residual"]), mp.mpf("1e-60"))
        self.assertGreater(mp.mpf(self.result["grid_summary"]["minimum_nuisance_gram_eigenvalue"]), 0)

    def test_semantic_bridge_remains_open(self):
        self.assertEqual(self.result["semantic_bridge"]["status"], "OPEN_OBLIGATION")
        self.assertEqual(self.result["claim_status"], "P3_B_M3_GEOMETRY_CONTROL_CLOSED_CERT_SEMANTIC_BRIDGE_OPEN")


if __name__ == "__main__":
    unittest.main()
