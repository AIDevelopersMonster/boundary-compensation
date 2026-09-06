# Article III — Direct All-d Weyl Cohomological Gap

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `PROVED / FRESH ALL-D POLYNOMIAL GAP / NONRECURSIVE GENERALIZED-LOOP DESIGN`

## 0. Purpose

The recursive sharp Coxeter construction is now quantitatively polynomial at each individual parity-extension stage. What remains dangerous is accumulation: multiplying a factor `d^{-C}` through many dimensions can produce a superpolynomial global loss.

The mathematically cleaner alternative is to stop inheriting conditioning altogether and construct a **fresh dimension-d measurement system directly**.

`ALL-D-WEYL-LOOP-TOMOGRAPHY-v0.1.md` already proves exact identifiability from Weyl multiplication defects. This note upgrades that theorem from rank to stability. The key observation is that the Weyl defect equations are a finite-group 1-cocycle system with an explicit averaging contraction.

The result is an all-d, nonrecursive, inverse-polynomial lower singular-value bound. It bypasses the accumulation problem completely.

This note concerns the generalized exact flat-loop realization of the Weyl defects. A quantitatively controlled compilation into the adjacent-transposition Coxeter-only face family remains a separate next problem.

---

## 1. Hilbert normalization

Let

\[
G=\mathbb Z_d\times\mathbb Z_d,
\qquad q=|G|=d^2.
\]

Let `{W_g:g in G}` be the Weyl unitary basis, orthonormal for

\[
\langle X,Y\rangle_{2,d}=\frac1d\operatorname{Tr}(X^*Y).
\]

For a complex-linear unital map

\[
D:M_d(\mathbb C)\to M_d(\mathbb C),
\qquad D(I)=0,
\]

define

\[
A_g=W_g^*D(W_g).
\tag{1.1}
\]

Left multiplication by `W_g^*` is unitary in Hilbert-Schmidt norm, hence

\[
\boxed{
\|D\|_{\mathrm{sop}}^2
=\frac1q\sum_{g\in G}\|A_g\|_{2,d}^2.
}
\tag{1.2}
\]

Let

\[
\alpha_g(X)=W_g^*XW_g.
\]

Projective phases cancel, so `alpha` is a genuine unitary representation of `G`.

---

## 2. Generator defect operator

Let

\[
e_1=(1,0),
\qquad
e_2=(0,1).
\]

For `j=1,2` define

\[
\boxed{
E_j(g)
=A_{e_j+g}-\alpha_g(A_{e_j})-A_g.
}
\tag{2.1}
\]

By the Weyl cocycle identity from the previous all-d theorem,

\[
E_j(g)=B_D(e_j,g),
\]

where `B_D` is the normalized multiplication defect.

Use the normalized data norm

\[
\boxed{
\|\mathcal B_dD\|_{\mathrm{gen}}^2
=\frac1{2q}
\sum_{j=1}^2\sum_{g\in G}\|E_j(g)\|_{2,d}^2.
}
\tag{2.2}

The kernel consists exactly of derivations. The goal is a quantitative distance-to-kernel inequality.

---

## 3. Full cocycle defect

For arbitrary `h,g in G`, put

\[
\boxed{
C_A(h,g)
=A_{h+g}-\alpha_g(A_h)-A_g.
}
\tag{3.1}

Thus `C_A(e_j,g)=E_j(g)`.

The full normalized norm is

\[
\|C_A\|_{\mathrm{full}}^2
=\frac1{q^2}
\sum_{h,g\in G}\|C_A(h,g)\|_{2,d}^2.
\tag{3.2}

---

## 4. Generator defects control the full defect

Choose for every

\[
h=(a,b),\qquad 0\le a,b\le d-1,
\]

the canonical word consisting of `a` copies of `e_1` followed by `b` copies of `e_2`. Its length satisfies

\[
\ell(h)=a+b\le2(d-1).
\]

If `h'=h+e_j`, direct substitution in (3.1) gives the exact recurrence

\[
\boxed{
C_A(h+e_j,g)
=C_A(h,g)
+E_j(h+g)-\alpha_g(E_j(h)).
}
\tag{4.1}

Starting from `C_A(0,g)=0`, every `C_A(h,g)` is therefore a sum of at most `ell(h)` terms, each of which is a difference of two generator-defect values up to a unitary `alpha_g` action.

Let

\[
M_E=\max_{j,x}\|E_j(x)\|_{2,d}.
\]

Then

\[
\|C_A(h,g)\|_{2,d}
\le2\ell(h)M_E
\le4(d-1)M_E.
\tag{4.2}

Moreover

\[
M_E^2
\le
\sum_{j,x}\|E_j(x)\|_{2,d}^2
=2q\|\mathcal B_dD\|_{\mathrm{gen}}^2.
\]

Since `sqrt(q)=d`, (4.2) yields the deliberately simple uniform estimate

\[
\boxed{
\|C_A\|_{\mathrm{full}}
\le4\sqrt2\,d^2
\|\mathcal B_dD\|_{\mathrm{gen}}.
}
\tag{4.3}

The exponent is not claimed optimal. Fourier analysis of the torus blocks should improve it.

---

## 5. Exact averaging contraction to a coboundary

Let

\[
\overline A=rac1q\sum_{h\in G}A_h,
\qquad
K=-\overline A.
\tag{5.1}

Average (3.1) over `h`. Translation invariance of `G` gives

\[
\frac1q\sum_h C_A(h,g)
=\overline A-\alpha_g(\overline A)-A_g.
\tag{5.2}

Hence

\[
\boxed{
A_g-(\alpha_g(K)-K)
=-\frac1q\sum_hC_A(h,g).
}
\tag{5.3}

By Jensen,

\[
\frac1q\sum_g
\|A_g-(\alpha_g(K)-K)\|_{2,d}^2
\le
\|C_A\|_{\mathrm{full}}^2.
\tag{5.4}

But the family

\[
A_g^{(K)}=\alpha_g(K)-K
\]

corresponds exactly to the inner derivation

\[
D_K(X)=[K,X],
\]

because

\[
W_gA_g^{(K)}=KW_g-W_gK.
\]

Therefore

\[
\boxed{
\operatorname{dist}_{\mathrm{sop}}(D,\operatorname{Der})
\le
\|C_A\|_{\mathrm{full}}.
}
\tag{5.5}

Combining with (4.3) gives the main quantitative cohomology estimate.

---

## 6. Quantitative Weyl cocycle theorem

### Theorem 6.1 — generator-defect lower gap

For every `d>=2` and every complex-linear unital map `D:M_d(C)->M_d(C)`,

\[
\boxed{
\operatorname{dist}_{\mathrm{sop}}(D,\operatorname{Der}(M_d))
\le
4\sqrt2\,d^2
\|\mathcal B_dD\|_{\mathrm{gen}}.
}
\tag{6.1}

Equivalently, on the quotient by derivations,

\[
\boxed{
\sigma_{\min}(\mathcal B_d)
\ge
\frac1{4\sqrt2\,d^2}.
}
\tag{6.2}

This is a fresh all-dimensional lower singular-value theorem; no recursive extension is used.

---

## 7. Return to the real Hamiltonian quotient

Assume now that `D` is *-preserving. For a complex inner derivation `ad_K`, define its *-preserving projection

\[
\Pi_*(\operatorname{ad}_K)(X)
=
\frac12\left(
[K,X]+[K,X^*]^*
\right).
\]

A direct calculation gives

\[
\Pi_*(\operatorname{ad}_K)
=
\operatorname{ad}_{(K-K^*)/2}.
\]

The generator `(K-K^*)/2` is skew-adjoint, so this is a Hamiltonian derivation.

Since `Pi_*` is an orthogonal/contraction projection in the normalized superoperator Hilbert norm and `D` is already *-preserving,

\[
\operatorname{dist}(D,\mathcal D_d)
\le
\operatorname{dist}(D,\operatorname{Der}).
\]

Hence the same lower bound (6.2) holds on the real dissipative quotient

\[
\mathcal Q_d=\mathcal G_d/\mathcal D_d.
\]

---

## 8. Polynomial upper singular bound

From

\[
E_j(g)
=A_{g+e_j}-A_g-\alpha_g(A_{e_j}),
\]

and `||x+y+z||^2<=3(||x||^2+||y||^2+||z||^2)`,

\[
\|\mathcal B_dD\|_{\mathrm{gen}}^2
\le
3(d^2+2)\|D\|_{\mathrm{sop}}^2.
\tag{8.1}

Thus, for `d>=2`,

\[
\boxed{
\|\mathcal B_d\|\le3d.
}
\tag{8.2}

Combining (6.2) and (8.2),

\[
\boxed{
\kappa(\mathcal B_d|_{\mathcal Q_d})
\le12\sqrt2\,d^3.
}
\tag{8.3}

Again, this is deliberately nonoptimal; the theorem-level point is polynomiality without inherited losses.

---

## 9. Closed-loop extraction remains polynomially stable

For `h=e_j`, let

\[
P=W_hW_g.
\]

As in `ALL-D-WEYL-LOOP-TOMOGRAPHY-v0.1.md`, define the backtracking coefficient

\[
R_D(P)=D(P^*)P+P^*D(P)
\]

and the multiplication-triangle coefficient

\[
K_D(h,g)
=
D(P^*)P
+P^*D(W_h)W_g
+P^*W_hD(W_g).
\]

Then

\[
\boxed{
B_D(h,g)=R_D(P)-K_D(h,g).
}
\tag{9.1}

Let the loop-data norm be

\[
\|\mathcal M_dD\|_{\mathrm{loop}}^2
=
\frac1{3q}
\left[
\sum_{p\in G}\|R_D(W_p)\|_{2,d}^2
+
\sum_{j=1}^2\sum_{g\in G}
\|K_D(e_j,g)\|_{2,d}^2
\right].
\tag{9.2}

For each `j`, the map `g -> e_j+g` is a bijection of `G`. Hence

\[
\sum_{j,g}\|R_D(W_{e_j+g})\|^2
=2\sum_p\|R_D(W_p)\|^2.
\]

Using (9.1),

\[
\sum_{j,g}\|B_D(e_j,g)\|^2
\le
4\left[
\sum_p\|R_D(W_p)\|^2
+
\sum_{j,g}\|K_D(e_j,g)\|^2
\right].
\]

Therefore

\[
\boxed{
\|\mathcal B_dD\|_{\mathrm{gen}}
\le\sqrt6\,\|\mathcal M_dD\|_{\mathrm{loop}}.
}
\tag{9.3}

Combining with Theorem 6.1 gives

\[
\boxed{
\sigma_{\min}(\mathcal M_d|_{\mathcal Q_d})
\ge
\frac1{8\sqrt3\,d^2}.
}
\tag{9.4}

Thus the closed-loop realization itself retains an inverse-polynomial gap.

---

## 10. Upper loop bound and condition number

The backtrack satisfies

\[
\sum_p\|R_D(W_p)\|^2
\le4q\|D\|_{\mathrm{sop}}^2.
\tag{10.1}

For the triangle coefficient, the three summands are unitary left/right translates of

\[
D(P^*),\quad D(W_{e_j}),\quad D(W_g).
\]

Summing the three-term Cauchy bound over `j,g` gives

\[
\sum_{j,g}\|K_D(e_j,g)\|^2
\le
(12q+6q^2)\|D\|_{\mathrm{sop}}^2.
\tag{10.2}

Hence

\[
\|\mathcal M_dD\|_{\mathrm{loop}}^2
\le
\frac{16+6d^2}{3}\|D\|_{\mathrm{sop}}^2,
\]

and in particular

\[
\boxed{
\|\mathcal M_d\|\le3d.
}
\tag{10.3}

Together with (9.4),

\[
\boxed{
\kappa(\mathcal M_d|_{\mathcal Q_d})
\le24\sqrt3\,d^3.
}
\tag{10.4}

---

## 11. Direct robust all-d theorem

### Theorem 11.1 — nonrecursive robust Weyl flat-loop tomography

For every `d>=2`, there exists a fresh dimension-`d` family of at most `3d^2-1` exact flat matrix-valued loop coefficients which identifies every bounded unital *-preserving generator on `M_d(C)` modulo Hamiltonian derivations and obeys

\[
\boxed{
A_d^{\mathrm{Weyl}}
\ge
\frac1{192\,d^4}
}
\tag{11.1}

under the loop normalization (9.2), since

\[
A_d=\sigma_{\min}^2
\ge
\frac1{(8\sqrt3\,d^2)^2}
=
\frac1{192d^4}.
\]

Moreover

\[
\boxed{
\kappa_d^{\mathrm{Weyl}}
\le24\sqrt3\,d^3.
}
\tag{11.2}

No stage-wise conditioning factors are multiplied. The design is rebuilt directly in each dimension from the finite Weyl group.

---

## 12. Why this changes the Article-III strategy

The previous global barrier was stated as

\[
\text{polynomial local stages}
\not\Rightarrow
\text{polynomial recursively inherited sharp design}.
\]

The Weyl cohomological theorem shows that this is a limitation of the **recursive sharp construction**, not a general stability obstruction of contextual flat-loop tomography.

We now have a theorem-level separation:

\[
\boxed{
\text{fresh }O(d^2)\text{ flat-loop tomography is polynomially stable},
}
\]

while

\[
\boxed{
\text{fresh sharp Coxeter polynomial stability remains open}.
}
\]

This is a substantially sharper research target than the earlier vague accumulation problem.

---

## 13. Next strict target: robust Coxeter compilation

`ALL-D-COXETER-OD2-v0.1.md` already compiles exact identifiability into adjacent-transposition braid/square faces, but its proof is qualitative because it uses dense conjugation anchors.

The next mathematically decisive question is:

\[
\boxed{
\text{Can the quantitative Weyl cocycle gap be compiled into }O(d^2)
\text{ genuine Coxeter faces with only polynomial loss?}
}
\]

A positive theorem would give a fresh, nonrecursive, all-d **robust Coxeter** design and would completely separate the robustness question from recursive parity accumulation.

Only after that should one return to the sharper constant `floor(d^2/2)` and ask whether the constant-factor redundancy can be removed without destroying the polynomial lower frame bound.

---

## 14. Claim firewall

This note proves:

- a quantitative finite-group cocycle stability theorem for the two Weyl generators;
- a direct all-d inverse-polynomial generalized flat-loop tomography gap;
- a polynomial condition-number upper bound;
- elimination of recursive accumulation as a necessary feature of robust flat-loop tomography.

It does **not** yet prove:

- the same quantitative bound for the `3d^2-1` Coxeter-only construction;
- a polynomial lower frame bound at the sharp Coxeter count `floor(d^2/2)`;
- optimal exponents;
- a necessity theorem for oversampling;
- statistical/sample-complexity optimality.
