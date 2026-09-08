import itertools
import numpy as np
import scipy.linalg as la

TOL = 1e-8


def hermitian_basis(d):
    basis = [np.eye(d, dtype=complex) / np.sqrt(d)]
    for i in range(d):
        for j in range(i + 1, d):
            m = np.zeros((d, d), dtype=complex)
            m[i, j] = m[j, i] = 1 / np.sqrt(2)
            basis.append(m)
            m = np.zeros((d, d), dtype=complex)
            m[i, j] = -1j / np.sqrt(2)
            m[j, i] = 1j / np.sqrt(2)
            basis.append(m)
    for k in range(1, d):
        m = np.zeros((d, d), dtype=complex)
        for i in range(k):
            m[i, i] = 1
        m[k, k] = -k
        m /= np.sqrt(k * (k + 1))
        basis.append(m)
    return basis


def weyl(d, a, b):
    w = np.exp(2j * np.pi / d)
    x = np.zeros((d, d), dtype=complex)
    for j in range(d):
        x[(j + 1) % d, j] = 1
    z = np.diag([w ** j for j in range(d)])
    return np.linalg.matrix_power(x, a) @ np.linalg.matrix_power(z, b)


def fourier(d):
    w = np.exp(2j * np.pi / d)
    return np.array(
        [[w ** (j * k) / np.sqrt(d) for k in range(d)] for j in range(d)],
        dtype=complex,
    )


def phase_gate(d):
    w = np.exp(2j * np.pi / d)
    return np.diag([w ** (j * (j - 1) // 2) for j in range(d)])


def sidon_anchor(d):
    m = 2 * d + 1
    e = np.array([j + m * j * j for j in range(d)], dtype=float)
    eps = 1 / (48 * d ** 3)
    return np.diag(np.exp(1j * eps * e))


def square_transports(u, v):
    return [u, v, u.conj().T, u.conj().T @ v.conj().T @ u]


def face_matrix(d, u, v):
    basis = hermitian_basis(d)
    n = d * d
    ts = square_transports(u, v)
    coeff = [[np.trace(b.conj().T @ t) for b in basis] for t in ts]
    out = np.zeros((2 * n, (n - 1) * n), dtype=float)

    col = 0
    for inp in range(1, n):
        for out_idx in range(n):
            kappa = np.zeros((d, d), dtype=complex)
            for k in range(4):
                left = np.eye(d, dtype=complex)
                for j in range(3, k, -1):
                    left = left @ ts[j]
                right = np.eye(d, dtype=complex)
                for j in range(k - 1, -1, -1):
                    right = right @ ts[j]
                kappa += left @ (coeff[k][inp] * basis[out_idx]) @ right

            flat = kappa.reshape(-1)
            out[:n, col] = flat.real
            out[n:, col] = flat.imag
            col += 1

    return out


def orth_row_basis(a, tol=TOL):
    if a.shape[0] == 0:
        return np.zeros((0, a.shape[1]), dtype=float)
    _, s, vh = la.svd(a, full_matrices=False)
    r = int(np.sum(s > tol))
    return vh[:r, :]


def greedy(blocks, labels, count, tol=TOL):
    q = np.zeros((0, blocks[0].shape[1]), dtype=float)
    remaining = set(range(len(blocks)))
    chosen = []
    history = []

    for step in range(count):
        best = None
        for idx in sorted(remaining):
            b = blocks[idx]
            bp = b - (b @ q.T) @ q if q.shape[0] else b
            s = la.svdvals(bp)
            positive = s[s > tol]
            gain = int(positive.size)
            quality = float(positive[-1]) if gain else 0.0
            score = (gain, quality)
            if best is None or score > best[0]:
                best = (score, idx, bp)

        score, idx, bp = best
        qnew = orth_row_basis(bp, tol)
        if qnew.shape[0]:
            q = orth_row_basis(np.vstack([q, qnew]), tol)
        chosen.append(idx)
        remaining.remove(idx)
        history.append((step + 1, labels[idx], q.shape[0], score))

    return chosen, history


def analyze_family(d, anchor_names):
    anchors = {
        "F": fourier(d),
        "P": phase_gate(d),
        "Z": sidon_anchor(d),
    }
    nonzero = [
        (a, b)
        for a in range(d)
        for b in range(d)
        if (a, b) != (0, 0)
    ]

    blocks = []
    labels = []
    for name in anchor_names:
        u = anchors[name]
        for g in nonzero:
            blocks.append(face_matrix(d, u, weyl(d, *g)))
            labels.append((name, g))

    sharp = (d * d) // 2 if d % 2 == 0 else (d * d - 1) // 2
    chosen, history = greedy(blocks, labels, sharp)

    core = np.vstack([blocks[i] for i in chosen[:-1]])
    full = np.vstack([blocks[i] for i in chosen])
    core_s = la.svdvals(core)
    full_s = la.svdvals(full)
    core_rank = int(np.sum(core_s > TOL))
    target = (d * d - 1) ** 2
    full_rank = int(np.sum(full_s > TOL))

    print(f"d={d}, anchors={anchor_names}")
    print("selected:")
    for item in history:
        print("  ", item)
    print(f"core_rank={core_rank}")
    print(f"full_rank={full_rank}, target={target}")
    print(f"core_sigma_min_plus={core_s[core_rank - 1]:.16g}")
    print(f"full_sigma_target={full_s[target - 1]:.16g}")
    print(f"full_sigma_max={full_s[0]:.16g}")
    print()


if __name__ == "__main__":
    for d in (3, 4, 5):
        analyze_family(d, ("F", "P"))
    # The Sidon/Fourier pair is also useful in the even d=4 direct-core regime.
    analyze_family(4, ("F", "Z"))
