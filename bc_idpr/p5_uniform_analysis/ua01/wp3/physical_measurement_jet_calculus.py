#!/usr/bin/env python3
"""Exact first/second jet calculus for the HS-whitened physical frame."""
from __future__ import annotations
import argparse
import json
import numpy as np


def herm(a: np.ndarray) -> np.ndarray:
    return 0.5 * (a + a.conj().T)


def opnorm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, ord=2))


def solve_positive_sylvester(h: np.ndarray, e: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh(herm(h))
    if float(vals.min()) <= 0.0:
        raise ValueError("positive Sylvester coefficient required")
    et = vecs.conj().T @ e @ vecs
    xt = et / (vals[:, None] + vals[None, :])
    return herm(vecs @ xt @ vecs.conj().T)


def snapshot(u: np.ndarray, psi: np.ndarray, weights: np.ndarray) -> np.ndarray:
    m = u.shape[0]
    gram = np.empty((m, m), dtype=complex)
    symbols = np.empty((psi.shape[0], m), dtype=complex)
    for i in range(m):
        for j in range(m):
            gram[i, j] = np.trace(u[i].conj().T @ u[j])
        symbols[:, i] = np.einsum("ai,ij,aj->a", psi.conj(), u[i], psi)
    vals, vecs = np.linalg.eigh(herm(gram))
    if float(vals.min()) <= 0.0:
        raise ValueError("Hilbert-Schmidt Gram rank wall")
    whitening = vecs @ np.diag(vals ** -0.5) @ vecs.conj().T
    return np.sqrt(weights)[:, None] * symbols @ whitening


def compute_jets(u, u1, u2, psi, psi1, psi2, weights, weights1=None, weights2=None):
    u = np.asarray(u, complex)
    u1 = np.asarray(u1, complex)
    u2 = np.asarray(u2, complex)
    psi = np.asarray(psi, complex)
    psi1 = np.asarray(psi1, complex)
    psi2 = np.asarray(psi2, complex)
    w = np.asarray(weights, float)
    w1 = np.zeros_like(w) if weights1 is None else np.asarray(weights1, float)
    w2 = np.zeros_like(w) if weights2 is None else np.asarray(weights2, float)
    if np.any(w <= 0.0):
        raise ValueError("strictly positive weights required")
    m = u.shape[0]
    n = psi.shape[0]
    symbols = np.empty((n, m), dtype=complex)
    symbols1 = np.empty((n, m), dtype=complex)
    symbols2 = np.empty((n, m), dtype=complex)
    gram = np.empty((m, m), dtype=complex)
    gram1 = np.empty((m, m), dtype=complex)
    gram2 = np.empty((m, m), dtype=complex)
    for i in range(m):
        ui, vi, zi = u[i], u1[i], u2[i]
        symbols[:, i] = np.einsum("ai,ij,aj->a", psi.conj(), ui, psi)
        symbols1[:, i] = (
            np.einsum("ai,ij,aj->a", psi1.conj(), ui, psi)
            + np.einsum("ai,ij,aj->a", psi.conj(), vi, psi)
            + np.einsum("ai,ij,aj->a", psi.conj(), ui, psi1)
        )
        symbols2[:, i] = (
            np.einsum("ai,ij,aj->a", psi2.conj(), ui, psi)
            + np.einsum("ai,ij,aj->a", psi.conj(), zi, psi)
            + np.einsum("ai,ij,aj->a", psi.conj(), ui, psi2)
            + 2.0 * np.einsum("ai,ij,aj->a", psi1.conj(), vi, psi)
            + 2.0 * np.einsum("ai,ij,aj->a", psi1.conj(), ui, psi1)
            + 2.0 * np.einsum("ai,ij,aj->a", psi.conj(), vi, psi1)
        )
        for j in range(m):
            uj, vj, zj = u[j], u1[j], u2[j]
            gram[i, j] = np.trace(ui.conj().T @ uj)
            gram1[i, j] = np.trace(vi.conj().T @ uj + ui.conj().T @ vj)
            gram2[i, j] = np.trace(zi.conj().T @ uj + 2.0 * vi.conj().T @ vj + ui.conj().T @ zj)
    gram, gram1, gram2 = herm(gram), herm(gram1), herm(gram2)
    root = np.sqrt(w)
    root1 = w1 / (2.0 * root)
    root2 = w2 / (2.0 * root) - w1**2 / (4.0 * root**3)
    measurement = root[:, None] * symbols
    measurement1 = root1[:, None] * symbols + root[:, None] * symbols1
    measurement2 = root2[:, None] * symbols + 2.0 * root1[:, None] * symbols1 + root[:, None] * symbols2
    vals, vecs = np.linalg.eigh(gram)
    gamma = float(vals.min())
    if gamma <= 0.0:
        raise ValueError("Hilbert-Schmidt Gram rank wall")
    h = herm(vecs @ np.diag(np.sqrt(vals)) @ vecs.conj().T)
    whitening = herm(vecs @ np.diag(vals ** -0.5) @ vecs.conj().T)
    h1 = solve_positive_sylvester(h, gram1)
    h2 = solve_positive_sylvester(h, gram2 - 2.0 * h1 @ h1)
    whitening1 = herm(-whitening @ h1 @ whitening)
    whitening2 = herm(2.0 * whitening @ h1 @ whitening @ h1 @ whitening - whitening @ h2 @ whitening)
    mhat = measurement @ whitening
    mhat1 = measurement1 @ whitening + measurement @ whitening1
    mhat2 = measurement2 @ whitening + 2.0 * measurement1 @ whitening1 + measurement @ whitening2
    singular = np.linalg.svd(mhat, compute_uv=False)
    sigma = float(singular[-1])
    l1, l2 = opnorm(mhat1), opnorm(mhat2)
    radius1 = sigma / l1 if l1 > 0.0 else None
    radius2 = (-l1 + np.sqrt(l1*l1 + 2.0*l2*sigma)) / l2 if l2 > 0.0 else radius1
    return {
        "sigma_min": sigma,
        "frame_alpha": sigma*sigma,
        "Mhat1_operator_norm": l1,
        "Mhat2_operator_norm": l2,
        "first_order_positive_radius_threshold": radius1,
        "second_order_positive_radius_threshold": radius2,
        "gamma_hs": gamma,
        "Mhat": mhat,
        "Mhat1": mhat1,
        "Mhat2": mhat2,
    }


def synthetic(theta: float):
    k = np.array([[0.,-1.,0.],[1.,0.,0.],[0.,0.,0.]])
    c, s = np.cos(theta), np.sin(theta)
    q = np.array([[c,-s,0.],[s,c,0.],[0.,0.,1.]])
    base = np.array([[[1.,.2,0.],[.2,-.3,.1],[0.,.1,-.7]],[[.1,.4,.2],[.4,-.2,0.],[.2,0.,.1]]])
    rot = np.asarray([q @ x @ q.T for x in base])
    rot1 = np.asarray([k @ x - x @ k for x in rot])
    rot2 = np.asarray([k @ x - x @ k for x in rot1])
    a = np.array([[1.+.1*theta,.2*np.sin(theta)],[.1*np.cos(theta),1.-.05*theta]])
    a1 = np.array([[.1,.2*np.cos(theta)],[-.1*np.sin(theta),-.05]])
    a2 = np.array([[0.,-.2*np.sin(theta)],[-.1*np.cos(theta),0.]])
    u = np.einsum("ji,jab->iab",a,rot)
    u1 = np.einsum("ji,jab->iab",a1,rot)+np.einsum("ji,jab->iab",a,rot1)
    u2 = np.einsum("ji,jab->iab",a2,rot)+2*np.einsum("ji,jab->iab",a1,rot1)+np.einsum("ji,jab->iab",a,rot2)
    raw=np.array([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.],[1.,1.,0.],[1.,0.,1.],[0.,1.,1.]])
    raw/=np.linalg.norm(raw,axis=1)[:,None]
    psi=raw@q.T; psi1=psi@k.T; psi2=psi@(k@k).T
    basew=np.array([.11,.13,.17,.19,.18,.22]); phase=np.linspace(0.,1.,6)
    w=basew*(1.+.08*np.sin(theta+phase)); w1=basew*.08*np.cos(theta+phase); w2=-basew*.08*np.sin(theta+phase)
    return u.astype(complex),u1.astype(complex),u2.astype(complex),psi.astype(complex),psi1.astype(complex),psi2.astype(complex),w,w1,w2


def self_test():
    theta=.37
    data=synthetic(theta)
    result=compute_jets(*data)
    step=2e-4
    values=[snapshot(synthetic(theta+j*step)[0],synthetic(theta+j*step)[3],synthetic(theta+j*step)[6]) for j in (-2,-1,0,1,2)]
    fd1=(values[0]-8*values[1]+8*values[3]-values[4])/(12*step)
    fd2=(-values[4]+16*values[3]-30*values[2]+16*values[1]-values[0])/(12*step*step)
    e1=opnorm(fd1-result["Mhat1"]); e2=opnorm(fd2-result["Mhat2"])
    r1=e1/max(opnorm(result["Mhat1"]),1e-30); r2=e2/max(opnorm(result["Mhat2"]),1e-30)
    assert r1<2e-8 and r2<2e-6
    return {"status":"SELF_TEST_PASS","first_derivative_operator_error":e1,"first_derivative_relative_error":r1,"second_derivative_operator_error":e2,"second_derivative_relative_error":r2,"sigma_min":result["sigma_min"],"frame_alpha":result["frame_alpha"],"Mhat1_operator_norm":result["Mhat1_operator_norm"],"Mhat2_operator_norm":result["Mhat2_operator_norm"],"first_order_positive_radius_threshold":result["first_order_positive_radius_threshold"],"second_order_positive_radius_threshold":result["second_order_positive_radius_threshold"]}


def main():
    p=argparse.ArgumentParser(); p.add_argument("--self-test",action="store_true"); a=p.parse_args()
    if not a.self_test: p.error("use --self-test or import compute_jets")
    print(json.dumps(self_test(),indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
