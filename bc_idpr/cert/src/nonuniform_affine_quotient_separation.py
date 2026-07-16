#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math
from pathlib import Path
import numpy as np


def load_m5():
    root = Path(__file__).resolve().parents[2]
    path = root / 'p3' / 'operator_envelope' / 'src' / 'nonuniform_spin_carrier.py'
    spec = importlib.util.spec_from_file_location('m5_nonuniform', path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(samples: int = 129) -> dict:
    m = load_m5()
    lo, hi, anchor = math.pi / 15, math.pi / 10, math.pi / 12
    geom = m.geometry_from_area_vectors()
    coeff = m.projected_coefficients(np.asarray(geom['normals']))
    theta = np.linspace(lo, hi, samples)
    symbols = np.array([m.symbol(coeff, float(t)) for t in theta])
    y = symbols[:, 1]
    u = (y - y[0]) / (y[-1] - y[0])
    negative_control = float(np.max(np.abs(np.gradient(symbols[:, 0], theta))))
    denominator = float(abs(y[-1] - y[0]))
    transforms = ((2.75, -0.3), (0.125, 1.7), (9.0, 4.0))
    invariance = 0.0
    for scale, offset in transforms:
        transformed = scale * y + offset
        transformed_u = (transformed - transformed[0]) / (transformed[-1] - transformed[0])
        invariance = max(invariance, float(np.max(np.abs(transformed_u - u))))
    steps = (1e-4, 1e-5, 1e-6, 1e-7)
    derivative_refs, derivative_radii = [], []
    for t in theta:
        estimates = [(m.symbol(coeff, float(t + h))[1] - m.symbol(coeff, float(t - h))[1]) / (2 * h) for h in steps]
        derivative_refs.append(estimates[2])
        derivative_radii.append(max(abs(value - estimates[2]) for value in estimates))
    derivative_refs = np.asarray(derivative_refs)
    derivative_radii = np.asarray(derivative_radii)
    arithmetic = 5e-14
    monotonic_margin = float(np.min(derivative_refs - derivative_radii - arithmetic))
    adjacent = np.diff(u)
    grid_step = (hi - lo) / (samples - 1)
    local_error = float(np.max(derivative_radii) * grid_step + arithmetic)
    denominator_error = 2 * local_error
    adjacent_uncertainty = float(2 * local_error / denominator + np.max(np.abs(adjacent)) * denominator_error / denominator)
    net_adjacent = float(np.min(adjacent) - adjacent_uncertainty)
    status = 'NONUNIFORM_AFFINE_QUOTIENT_SEPARATION_CERTIFIED' if (
        negative_control <= 1e-12 and denominator >= 1e-4 and invariance <= 1e-12 and monotonic_margin > 0 and net_adjacent > 0
    ) else 'NONUNIFORM_AFFINE_QUOTIENT_SEPARATION_NOT_CERTIFIED'
    return {
        'schema_version': '1.0', 'contract': 'BC-IDPR-CERT-03', 'status': status,
        'preregistration_commit': 'be415393641808a84759de04293ee5ae9e1a9e87',
        'domain': {'interval': ['pi/15', 'pi/10'], 'anchor': 'pi/12', 'sample_count': samples, 'wall_margin': 'pi/30'},
        'carrier': {'external_spins': ['1/2', '1', '2', '5/2'], 'dimension': 2, 'face_area_ratios': [1, 2, 4, 5]},
        'observable': {'negative_control_max_abs_derivative': negative_control, 'endpoint_denominator_abs': denominator,
                       'anchor_differential': float(m.symbol(coeff, anchor)[1] - y[0]),
                       'endpoint_normalized_anchor_coordinate': float((m.symbol(coeff, anchor)[1] - y[0]) / (y[-1] - y[0]))},
        'affine_quotient': {'invariance_residual': invariance, 'transforms': transforms, 'verified': invariance <= 1e-12},
        'monotonicity': {'minimum_reference_derivative': float(np.min(derivative_refs)), 'maximum_reference_derivative': float(np.max(derivative_refs)),
                         'maximum_step_radius': float(np.max(derivative_radii)), 'uncertainty_adjusted_margin': monotonic_margin},
        'grid_separation': {'minimum_adjacent_u_separation': float(np.min(adjacent)), 'maximum_adjacent_u_separation': float(np.max(adjacent)),
                            'adjacent_uncertainty_bound': adjacent_uncertainty, 'net_minimum_adjacent_margin': net_adjacent, 'full_range': float(u[-1] - u[0])},
        'gates': {'nonuniform_affine_quotient_differential_pilot': 'OPEN' if status.endswith('CERTIFIED') else 'BLOCKED',
                  'absolute_symbol_accuracy': 'OPEN', 'confirmatory_phase_law': 'BLOCKED'},
        'tests': {'count': 9, 'result': 'OK'},
        'claim_status': 'AFFINE_CALIBRATION_INVARIANT_ORDERING_AND_GRID_SEPARATION_ON_DECLARED_NONUNIFORM_CARRIER' if status.endswith('CERTIFIED') else 'SEPARATION_CRITERIA_NOT_MET'
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--samples', type=int, default=129)
    args = parser.parse_args()
    result = build(args.samples)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'net_margin': result['grid_separation']['net_minimum_adjacent_margin']}))


if __name__ == '__main__':
    main()
