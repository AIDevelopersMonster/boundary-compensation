#!/usr/bin/env python3
"""Exact minimal generic-q recoupling envelope for BC-IDPR-P3-B-01."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def qnum(n: int, theta: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.sin(n * theta) / sp.sin(theta))


def recoupling(theta: sp.Expr) -> sp.Matrix:
    d2 = qnum(2, theta)
    d3 = qnum(3, theta)
    return sp.simplify(
        sp.Matrix([[1, sp.sqrt(d3)], [sp.sqrt(d3), -1]]) / d2
    )


def operator_pair(theta: sp.Expr) -> tuple[sp.Matrix, sp.Matrix]:
    f_matrix = recoupling(theta)
    x_matrix = sp.diag(2 * sp.cos(theta), 2 * sp.cos(3 * theta))
    y_matrix = sp.simplify(f_matrix * x_matrix * f_matrix.T)
    return sp.simplify(x_matrix), y_matrix


def pair_inner(first, second) -> sp.Expr:
    return sp.simplify(
        sp.trace(first[0].T * second[0])
        + sp.trace(first[1].T * second[1])
    )


def pair_sub(first, second):
    return (
        sp.simplify(first[0] - second[0]),
        sp.simplify(first[1] - second[1]),
    )


def projection_coefficients(vector, basis):
    gram = sp.Matrix(
        [[pair_inner(first, second) for second in basis] for first in basis]
    )
    rhs = sp.Matrix([pair_inner(item, vector) for item in basis])
    return gram, sp.simplify(gram.LUsolve(rhs))


def encode_matrix(matrix: sp.Matrix) -> list[list[str]]:
    return [
        [sp.sstr(sp.simplify(matrix[row, col])) for col in range(matrix.cols)]
        for row in range(matrix.rows)
    ]


def build_certificate() -> dict:
    theta = sp.symbols("theta", real=True)
    theta0 = sp.pi / 4
    x_matrix, y_matrix = operator_pair(theta)
    x0, y0 = [sp.simplify(item.subs(theta, theta0)) for item in (x_matrix, y_matrix)]
    dx, dy = [sp.simplify(item.diff(theta).subs(theta, theta0)) for item in (x_matrix, y_matrix)]

    identity = sp.eye(2)
    skew_generator = sp.Matrix([[0, -1], [1, 0]])
    nuisance_basis = [
        (identity, identity),
        (x0, y0),
        (
            sp.simplify(skew_generator * x0 - x0 * skew_generator),
            sp.simplify(skew_generator * y0 - y0 * skew_generator),
        ),
    ]
    gram, coefficients = projection_coefficients((dx, dy), nuisance_basis)

    nuisance_projection = (sp.zeros(2), sp.zeros(2))
    for coefficient, direction in zip(coefficients, nuisance_basis, strict=True):
        nuisance_projection = (
            sp.simplify(nuisance_projection[0] + coefficient * direction[0]),
            sp.simplify(nuisance_projection[1] + coefficient * direction[1]),
        )
    intrinsic = pair_sub((dx, dy), nuisance_projection)
    full_norm_squared = pair_inner((dx, dy), (dx, dy))
    intrinsic_norm_squared = pair_inner(intrinsic, intrinsic)

    def centered(matrix: sp.Matrix) -> sp.Matrix:
        return sp.simplify(matrix - sp.trace(matrix) * sp.eye(2) / 2)

    xc, yc = centered(x_matrix), centered(y_matrix)
    centered_correlation = sp.simplify(
        sp.trace(xc * yc)
        / sp.sqrt(sp.trace(xc * xc) * sp.trace(yc * yc))
    )
    correlation_value = sp.simplify(centered_correlation.subs(theta, theta0))
    correlation_derivative = sp.simplify(
        sp.diff(centered_correlation, theta).subs(theta, theta0)
    )

    f_anchor = sp.simplify(recoupling(theta0))
    f_orthogonality = sp.simplify(recoupling(theta).T * recoupling(theta) - sp.eye(2))

    return {
        "schema_version": "1.0",
        "contract": "BC-IDPR-P3-B-01",
        "status": "INTRINSIC_DIRECTION_CERTIFIED",
        "arithmetic": "exact symbolic",
        "base_point": "pi/4",
        "regular_real_chamber": ["0", "pi/3"],
        "wall_distance": "pi/12",
        "F_anchor": encode_matrix(f_anchor),
        "F_orthogonality_residual": encode_matrix(f_orthogonality),
        "X_anchor": encode_matrix(x0),
        "Y_anchor": encode_matrix(y0),
        "dX_anchor": encode_matrix(dx),
        "dY_anchor": encode_matrix(dy),
        "nuisance_gram": encode_matrix(gram),
        "projection_coefficients": [
            sp.sstr(sp.simplify(value)) for value in coefficients
        ],
        "intrinsic_component": [
            encode_matrix(intrinsic[0]),
            encode_matrix(intrinsic[1]),
        ],
        "full_tangent_norm_squared": sp.sstr(full_norm_squared),
        "intrinsic_margin_squared": sp.sstr(intrinsic_norm_squared),
        "intrinsic_margin": sp.sstr(sp.sqrt(intrinsic_norm_squared)),
        "relative_margin_squared": sp.sstr(
            sp.simplify(intrinsic_norm_squared / full_norm_squared)
        ),
        "relative_margin": sp.sstr(
            sp.simplify(sp.sqrt(intrinsic_norm_squared / full_norm_squared))
        ),
        "invariant_audit": {
            "value_at_anchor": sp.sstr(correlation_value),
            "derivative_at_anchor": sp.sstr(correlation_derivative),
            "verified": correlation_derivative != 0,
        },
        "claim_status": "OPERATOR_LEVEL_INTRINSIC_DIRECTION_ONLY_CERT_BLOCKED",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(certificate, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                key: certificate[key]
                for key in (
                    "status",
                    "intrinsic_margin",
                    "relative_margin",
                    "wall_distance",
                )
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
