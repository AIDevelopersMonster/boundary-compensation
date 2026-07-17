#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src" / "minimal_generic_q_envelope.py"
SPEC = importlib.util.spec_from_file_location("minimal_generic_q_envelope", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class MinimalGenericQEnvelopeTests(unittest.TestCase):
    def test_anchor_matches_ising_block(self) -> None:
        expected = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
        self.assertEqual(
            sp.simplify(MODULE.recoupling(sp.pi / 4) - expected),
            sp.zeros(2),
        )

    def test_recoupling_is_symbolically_orthogonal(self) -> None:
        theta = sp.symbols("theta", real=True)
        matrix = MODULE.recoupling(theta)
        self.assertEqual(sp.simplify(matrix.T * matrix - sp.eye(2)), sp.zeros(2))

    def test_exact_intrinsic_margin(self) -> None:
        certificate = MODULE.build_certificate()
        self.assertEqual(certificate["intrinsic_margin_squared"], "8")
        self.assertEqual(certificate["relative_margin_squared"], "1/7")

    def test_independent_invariant_audit(self) -> None:
        certificate = MODULE.build_certificate()
        audit = certificate["invariant_audit"]
        self.assertEqual(audit["value_at_anchor"], "0")
        self.assertEqual(audit["derivative_at_anchor"], "2")
        self.assertTrue(audit["verified"])

    def test_nuisance_gram_is_nondegenerate(self) -> None:
        certificate = MODULE.build_certificate()
        self.assertEqual(
            certificate["nuisance_gram"],
            [["4", "0", "0"], ["0", "8", "0"], ["0", "0", "32"]],
        )

    def test_status(self) -> None:
        self.assertEqual(
            MODULE.build_certificate()["status"],
            "INTRINSIC_DIRECTION_CERTIFIED",
        )


if __name__ == "__main__":
    unittest.main()
