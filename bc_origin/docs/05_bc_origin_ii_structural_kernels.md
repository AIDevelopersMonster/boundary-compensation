# BC-Origin II: Structural Kernels and the Emergence of κ

## 0. Objective

BC-Origin I introduced a signed spectral interaction model with a free coupling parameter κ:

D_signed =
\begin{pmatrix}
d_1 + γ s & κ \\
κ & d_2 + γ s
\end{pmatrix},
\quad s = sgn(n_1 n_2)

In BC-Origin II we eliminate κ as a fitted parameter and derive it as a structural overlap functional of hidden winding modes.

---

## 1. Hidden space of modes

Let hidden generators be oriented circle modes:

u_n(φ) = e^{i n φ},  n ∈ Z\{0}

with Hilbert space:

H = L^2(S^1)

---

## 2. Structural kernel

We introduce a self-adjoint structural operator:

A = (1 - Δ_{S^1})^{-1}

Kernel:

K(φ,φ') = Σ_m∈Z e^{i m(φ-φ')} / (1 + m^2)

---

## 3. Derivation of κ

κ_ij := <u_{n_i}, A u_{n_j}>

with u_n(φ)=e^{i n φ}

⇒ κ_ij = 1 / (1 + (n_i - n_j)^2)

---

## 4. Structural meaning

κ_ij is not a free parameter.
It is a spectral decay function:

0 < κ_ij ≤ 1
κ_ij decreases with |n_i - n_j|

---

## 5. Revised operator

D_ij =
\begin{pmatrix}
d_i + γ s_ij & κ_ij \\
κ_ij & d_j + γ s_ij
\end{pmatrix}

s_ij = sgn(n_i n_j)

---

## 6. Emergent geometry

- coupling = spectral overlap
- geometry emerges from Fourier distance decay
- interaction graph is weighted on Z

---

## 7. Consequence

- no fitted κ
- no arbitrary coupling
- interaction is fully structural

---

## 8. Bridge to BC-Core

κ_ij ~ <u_i, A u_j>
→ bounded operator matrix elements

---

## 9. Next step

1. N-body extension
2. spectrum of full D
3. phase transitions in connectivity
4. horizon condition λ_- = 0 linked to kernel decay

---

## Status

BC-Origin II = structural kernel theory of coupling emergence
