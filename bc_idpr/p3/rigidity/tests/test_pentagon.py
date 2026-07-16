#!/usr/bin/env python3
from __future__ import annotations
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src" / "build_pentagon_residuals.py"
SPEC = importlib.util.spec_from_file_location("build_pentagon_residuals", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class PentagonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        fusion = MODULE.load(ROOT / "data" / "ising_fusion_rules.json")
        baseline = MODULE.load(ROOT / "data" / "ising_F_baseline.json")
        cls.result = MODULE.build(fusion, baseline)

    def test_baseline_pentagon(self) -> None:
        self.assertEqual(self.result["status"], "BASELINE_PENTAGON_VERIFIED")

    def test_no_nonzero_residuals(self) -> None:
        self.assertEqual(self.result["n_nonzero_residuals"], 0)
        self.assertEqual(self.result["failures"], [])

    def test_registry_is_complete_and_nonempty(self) -> None:
        self.assertEqual(self.result["n_instances"], 106)
        self.assertEqual(self.result["n_scalar_residuals"], 136)


if __name__ == "__main__":
    unittest.main()
