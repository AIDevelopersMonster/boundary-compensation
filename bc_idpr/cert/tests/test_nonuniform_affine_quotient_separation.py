import importlib.util
from pathlib import Path
import unittest


def load_module():
    path = Path(__file__).resolve().parents[1] / 'src' / 'nonuniform_affine_quotient_separation.py'
    spec = importlib.util.spec_from_file_location('cert03', path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class Cert03Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = load_module().build(129)

    def test_status(self):
        self.assertEqual(self.result['status'], 'NONUNIFORM_AFFINE_QUOTIENT_SEPARATION_CERTIFIED')

    def test_preregistration(self):
        self.assertEqual(self.result['preregistration_commit'], 'be415393641808a84759de04293ee5ae9e1a9e87')

    def test_negative_control(self):
        self.assertLessEqual(self.result['observable']['negative_control_max_abs_derivative'], 1e-12)

    def test_denominator(self):
        self.assertGreaterEqual(self.result['observable']['endpoint_denominator_abs'], 1e-4)

    def test_affine_invariance(self):
        self.assertLessEqual(self.result['affine_quotient']['invariance_residual'], 1e-12)

    def test_monotonicity_margin(self):
        self.assertGreater(self.result['monotonicity']['uncertainty_adjusted_margin'], 0)

    def test_adjacent_margin(self):
        self.assertGreater(self.result['grid_separation']['net_minimum_adjacent_margin'], 0)

    def test_full_range(self):
        self.assertAlmostEqual(self.result['grid_separation']['full_range'], 1.0, places=14)

    def test_gate_split(self):
        self.assertEqual(self.result['gates']['nonuniform_affine_quotient_differential_pilot'], 'OPEN')
        self.assertEqual(self.result['gates']['confirmatory_phase_law'], 'BLOCKED')


if __name__ == '__main__':
    unittest.main()
