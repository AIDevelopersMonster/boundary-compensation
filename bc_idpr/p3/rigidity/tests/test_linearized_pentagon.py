#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

SPEC = importlib.util.spec_from_file_location("linearize_pentagon", SRC / "linearize_pentagon.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class LinearizedPentagonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = MODULE.build(
            ROOT / "data" / "ising_fusion_rules.json",
            ROOT / "data" / "ising_F_baseline.json",
        )

    def test_declared_dimensions(self) -> None:
        self.assertEqual(self.result["counts"]["n_variables"], 14)
        self.assertEqual(self.result["counts"]["n_raw_residual_rows"], 136)

    def test_exact_rank_consistency(self) -> None:
        ranks = self.result["rank"]
        self.assertEqual(ranks["raw"], ranks["nonzero"])
        self.assertEqual(ranks["raw"], ranks["projectively_reduced"])

    def test_rank_nullity(self) -> None:
        self.assertEqual(
            self.result["rank"]["raw"] + self.result["kernel"]["dimension"],
            self.result["counts"]["n_variables"],
        )

    def test_independent_directional_audit(self) -> None:
        self.assertTrue(self.result["independent_audit"]["verified"])


if __name__ == "__main__":
    unittest.main()
