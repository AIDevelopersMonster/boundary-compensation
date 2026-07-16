from __future__ import annotations

import importlib.util
import pathlib
import unittest

import numpy as np

SOURCE = pathlib.Path(__file__).parents[1] / "src" / "nonuniform_spin_carrier.py"
SPEC = importlib.util.spec_from_file_location("m5", SOURCE)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(SOURCE)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TestNonuniformSpinCarrier(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = MODULE.build_certificate()

    def test_status(self) -> None:
        self.assertEqual(self.certificate["status"], "NONUNIFORM_SPIN_UNEQUAL_AREA_CARRIER_CERTIFIED")

    def test_carrier_dimension(self) -> None:
        self.assertEqual(self.certificate["carrier"]["dimension"], 2)

    def test_exact_area_pattern(self) -> None:
        self.assertTrue(np.allclose(self.certificate["geometry"]["face_areas"], [0.5, 1.0, 2.0, 2.5]))

    def test_area_vector_closure(self) -> None:
        self.assertLess(self.certificate["geometry"]["area_vector_closure_norm"], 1e-12)

    def test_vertex_reconstruction(self) -> None:
        self.assertLess(self.certificate["geometry"]["vertex_reconstruction_area_vector_residual"], 1e-12)

    def test_basis_orthonormality(self) -> None:
        self.assertLess(self.certificate["carrier"]["basis_gram_residual"], 1e-12)

    def test_q_recoupling_orthogonality(self) -> None:
        self.assertLess(self.certificate["q_response"]["maximum_F_orthogonality_residual"], 1e-12)

    def test_nonzero_q_response(self) -> None:
        self.assertGreater(self.certificate["q_response"]["anchor_derivative_norm"], 1e-3)


if __name__ == "__main__":
    unittest.main()
