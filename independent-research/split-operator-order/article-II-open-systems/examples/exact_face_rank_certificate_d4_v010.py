#!/usr/bin/env python3
"""Reproducible exact finite-field certificate for the d=4 minimal design."""
import numpy as np
from finite_field_rank_common_v010 import P, mat, loop, measurement_block, rank_mod, traceless_hermitian_basis


def gates():
    d = 4
    x = mat(d, {(1,0):(1,0), (2,1):(1,0), (3,2):(1,0), (0,3):(1,0)})
    D = mat(d, {(0,0):(1,0), (1,1):(0,1), (2,2):(-1,0), (3,3):(0,-1)})
    r12 = mat(d, {(0,0):(3,0,5), (0,1):(4,0,5), (1,0):(-4,0,5), (1,1):(3,0,5), (2,2):(1,0), (3,3):(1,0)})
    r23 = mat(d, {(0,0):(1,0), (1,1):(3,0,5), (1,2):(4,0,5), (2,1):(-4,0,5), (2,2):(3,0,5), (3,3):(1,0)})
    return [x, D, r12, r23]


def main():
    u = gates(); fs = traceless_hermitian_basis(4)
    b01 = [0,1]*3; b12 = [1,2]*3
    specs = [
        ((0,1,2,3), b01),
        ((0,1,2,3), b12),
        ((0,1,3,2), b01),
        ((0,2,3,1), b01),
        ((1,0,2,3), b12),
        ((1,2,3,0), b01),
        ((2,0,1,3), b12),
        ((3,0,1,2), b12),
    ]
    blocks = [measurement_block(loop(u, perm, gens), fs) for perm, gens in specs]
    M = np.vstack(blocks)
    rank = rank_mod(M)
    print(f"prime={P} shape={M.shape[0]}x{M.shape[1]} rank={rank}")
    assert M.shape == (256, 225)
    assert rank == 225
    print("CERTIFIED_FULL_COLUMN_RANK_OVER_Q")


if __name__ == '__main__':
    main()
