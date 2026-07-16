import importlib.util, sys, unittest
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'src' / 'q_racah_operator_envelope.py'
SPEC = importlib.util.spec_from_file_location('q_racah_operator_envelope', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)

class QRacahEnvelopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 80
        cls.result = MODULE.build(9, 80, None)

    def test_status(self):
        self.assertEqual(self.result['status'], 'THREE_CHANNEL_CONTINUUM_NONTRIVIALITY_AND_GRID_MARGIN_CERTIFIED')

    def test_ising_convention_bridge(self):
        self.assertTrue(self.result['convention_bridge']['verified'])

    def test_anchor_margin_positive(self):
        self.assertGreater(mp.mpf(self.result['anchor_result']['intrinsic_margin']), 0)

    def test_grid_margin_positive(self):
        self.assertGreater(mp.mpf(self.result['grid_summary']['minimum_intrinsic_margin']), 0)

    def test_operator_dual_bound_positive(self):
        self.assertGreater(mp.mpf(self.result['grid_summary']['minimum_operator_norm_dual_lower_bound']), 0)

    def test_nuisance_gram_nondegenerate(self):
        self.assertGreater(mp.mpf(self.result['grid_summary']['minimum_nuisance_gram_eigenvalue']), 0)

    def test_continuum_invariant(self):
        self.assertTrue(self.result['continuum_invariant_certificate']['verified'])

    def test_derivative_crosscheck(self):
        self.assertTrue(self.result['anchor_result']['derivative_crosscheck']['verified'])

    def test_recoupling_orthogonality(self):
        self.assertLess(mp.mpf(self.result['grid_summary']['maximum_F_orthogonality_residual']), mp.mpf('1e-60'))

if __name__ == '__main__':
    unittest.main()
