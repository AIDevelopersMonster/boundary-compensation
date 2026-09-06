# Choosing the Road: From Contextual Flatness to Measurable Context Loss in Open Quantum Systems

## The Cheshire Cat at the Crossroads: A Mathematical-Physics Perspective between Article I, Article II, and the Planned Article III

**Malachevsky, A.A.**  
ORCID: 0009-0008-6009-3196  
Version: v0.2  
Date: 2026-09-06  
Status: `POST-AUDIT REVIEW DRAFT / PERSPECTIVE + RESEARCH PROGRAMME`

---

## Abstract

This paper deliberately contains two distinct epistemic layers. The first consists of rigorous mathematical results proved in Article I and Article II, together with several direct consequences of their formulas. The second consists of explicitly labelled research conjectures and programme goals. The speculative layer is not presented as established physics and does not identify the loop defects considered here with spacetime curvature or physical gauge curvature.

Article I constructed an operator-order framework in which full contextual transport is exactly flat while context reduction can produce a nonzero loop defect. Article II transferred this mechanism into the standard language of UCP reductions in open quantum systems. Its central object is the multiplicativity defect

\[
\Delta_\Phi(X,Y)=\Phi(XY)-\Phi(X)\Phi(Y),
\]

and, for uniformly continuous GKSL dynamics, the Leibniz defect

\[
\Gamma_{\mathcal L}(X,Y)
=\mathcal L(XY)-\mathcal L(X)Y-X\mathcal L(Y)
=\sum_\alpha [V_\alpha^*,X][Y,V_\alpha].
\]

For a flat underlying loop, Article II gave an exact decomposition of the reduced loop defect into local multiplicativity losses and proved the sharp first-order Coxeter theorem

\[
L_d^{\mathrm{Cox}}
=\left\lfloor\frac{d^2}{2}\right\rfloor,
\qquad d\ge3,
\]

within an explicitly declared finite-dimensional matrix-valued first-order measurement model.

A targeted literature audit substantially narrows the admissible interpretation. Multiplicative domains, noiseless/decoherence-free structures, noncommutative carré du champ, quantum-channel holonomy, Lindbladian learning, and process tensors are established subjects. Our programme is therefore not to reinvent those frameworks, but to ask a more specific compatibility question: can transport-restricted multiplicativity loss be converted into a stably measurable loop signal, connected quantitatively to protected sectors or multitime memory inside existing frameworks, and only after further structural work be organized into a genuine effective geometry?

The long-range goal is intentionally written as a question rather than a result:

\[
\boxed{
\text{context loss}
\longrightarrow
\text{stable loop observables}
\longrightarrow
\text{environmental information}
\longrightarrow
\text{effective geometry?}
}
\]

---

## 1. Why choose a road before knowing where it ends?

A mathematical programme can generate correct theorems for a long time without making clear which physical question the apparatus is meant to address. That danger is real here. Article I can be read as a paper on operator order and permutation geometry. Article II can be read as a paper on UCP maps, GKSL generators, and finite-dimensional tomography. Both readings are correct, but both conceal the shared motivation.

The motivation is this:

> if a complete description preserves context and remains flat, while a physically natural reduction destroys multiplicativity and produces a loop defect, can that loss of structure be made stably measurable?

The Alice/Cheshire-Cat image is used here as a methodological device, not as an argument. If no destination is named, every mathematical road is equally admissible. Once a target is stated, future problems can be judged by whether they move the programme toward it.

---

## 2. Article I: contextual flatness as the reference structure

Article I, *Split-Interval Representation of Quantum Operator Order: Descent Obstructions, Order Ultrametrics, and Pair-Reduced Holonomy* [1], keeps operator-order information until it can be safely forgotten. In its contextual transport construction, a closed loop telescopes:

\[
T_m\cdots T_1=I.
\]

This exact identity is the programme's reference notion of flatness. Pair reduction in Article I may break that exact flatness and generate a nonzero reduced loop defect.

One distinction must remain explicit. Pair reduction in Article I is not the same operation as CP/UCP reduction in Article II. The relation is conceptual rather than literal: Article I shows that loss of contextual information can destroy exact flatness, whereas Article II studies a physically standard class of nonmultiplicative reductions in which an analogous question becomes operator-algebraic.

---

## 3. Article II: a reduced loop as a sum of local multiplicativity losses

Let \(\Phi\) be UCP, let

\[
P_k=T_k\cdots T_1,
\qquad
P_m=I,
\]

and define

\[
H_\Phi=\Phi(T_m)\cdots\Phi(T_1).
\]

Article II [2] proves

\[
\boxed{
H_\Phi-I
=-\sum_{k=2}^{m}
\Phi(T_m)\cdots\Phi(T_{k+1})
\Delta_\Phi(T_k,P_{k-1}).
}
\]

Thus the loop defect is not introduced as a new geometric primitive. It is exactly decomposed into transported local failures of multiplicativity.

### Proposition 3.1 — transport-restricted loop bound

Let \(S\) contain all \(T_k\) and all prefixes \(P_k\), and define

\[
\mu_\Phi(S)
=
\sup_{\substack{X,Y\in S\\ \|X\|,\|Y\|\le1}}
\|\Delta_\Phi(X,Y)\|.
\]

Then for a unitary \(m\)-edge flat loop,

\[
\boxed{
\|H_\Phi-I\|
\le(m-1)\mu_\Phi(S).
}
\]

**Proof.** UCP maps are contractive. Hence every left prefactor in the exact loop decomposition has norm at most one, while each local defect has norm at most \(\mu_\Phi(S)\). The triangle inequality gives the result. \(\square\)

This direct estimate is the first quantitative bridge between local context loss and a loop-scale response.

---

## 4. Multiplicative domains: not a new structure, but an exact boundary for loop sensitivity

The multiplicative domain of a CP/UCP map is a standard operator-algebraic object. Its role in quantum error correction and correctable/noiseless structures is well established [7–10]. No novelty claim is made for that connection.

For the present programme, the relevant consequence is exact.

### Proposition 4.1 — flatness on the multiplicative domain

If the C*-algebra generated by the loop transports is contained in \(MD(\Phi)\), then

\[
H_\Phi=I.
\]

**Proof.** On the multiplicative domain, \(\Phi(XY)=\Phi(X)\Phi(Y)\) for every relevant product, so every term in the exact defect decomposition vanishes. \(\square\)

The multiplicative domain therefore gives an exact algebraic boundary between transport sectors that remain defect-free and sectors in which reduction can create a loop defect.

The open question is quantitative rather than qualitative:

> can the transport-restricted quantity \(\mu_\Phi(S)\) control, under explicit physical hypotheses, the distance of a selected transport algebra from a protected or noiseless regime?

This is **Research Question A**, not a proved equivalence.

---

## 5. Stinespring dilation: where the product information is lost

For a Stinespring representation

\[
\Phi(X)=V^*\pi(X)V,
\qquad P=VV^*,
\]

Article II gives

\[
\boxed{
\Delta_\Phi(X,Y)
=V^*\pi(X)(I-P)\pi(Y)V.
}
\]

The formula localizes the multiplicativity loss: between the two lifted factors lies a component that propagates through the complement of the compressed subspace.

A physically cautious interpretation is possible. A subsystem reduction can fail to retain the full operator context present in the dilated description. What does **not** follow is that \(I-P\) is itself curvature, entropy production, or a universal measure of decoherence.

---

## 6. GKSL and carré du champ: what is established, and what remains open here

For a bounded GKSL generator

\[
\mathcal L(X)
=i[H,X]
+
\sum_\alpha
\left(
V_\alpha^*XV_\alpha
-\frac12\{V_\alpha^*V_\alpha,X\}
\right),
\]

its Leibniz defect is

\[
\boxed{
\Gamma_{\mathcal L}(X,Y)
=
\sum_\alpha [V_\alpha^*,X][Y,V_\alpha].
}
\]

This sits close to the established noncommutative carré-du-champ and Dirichlet-form literature. Quantum Markov gradient estimates, curvature-dimension conditions, and derivation representations have been developed independently [11–13]. Hence \(\Gamma_{\mathcal L}\) must not be sold as a newly discovered quantum curvature.

What is specific to this programme is the coupling of such generator-level defects to a contextual loop construction.

### Proposition 6.1 — dissipative invisibility on the common noise commutant

Let

\[
\mathcal N_V
=
\{X:[X,V_\alpha]=[X,V_\alpha^*]=0\ \forall\alpha\}.
\]

Then for \(X,Y\in\mathcal N_V\),

\[
\Gamma_{\mathcal L}(X,Y)=0.
\]

If every transport and every prefix in a fixed flat loop belongs to \(\mathcal N_V\), then

\[
H_t-I=O(t^2)
\qquad (t\to0).
\]

Thus the first-order loop coefficient is blind to a transport sector fully compatible with the chosen noise operators.

### Proposition 6.2 — positive incompatibility certificate

For every \(A\),

\[
\boxed{
\Gamma_{\mathcal L}(A^*,A)
=
\sum_\alpha [A,V_\alpha]^*[A,V_\alpha]
\ge0.
}
\]

In a fixed GKSL representation this vanishes exactly when \([A,V_\alpha]=0\) for all \(\alpha\).

The statement is used only as an algebraic certificate of dissipative incompatibility. Representation-independent operational meaning would require additional work.

---

## 7. Small-time scale: algebraic sensitivity versus experimental sensitivity

Define

\[
g_{\mathcal L}(S)
=
\sup_{\substack{X,Y\in S\\\|X\|,\|Y\|\le1}}
\|\Gamma_{\mathcal L}(X,Y)\|.
\]

For a fixed finite flat loop, Article II's first-order expansion gives

### Proposition 7.1

\[
\boxed{
\|H_t-I\|
\le
 t(m-1)g_{\mathcal L}(S)+O(t^2),
\qquad t\to0.
}
\]

No dimension-uniform remainder estimate is claimed here.

This separates two questions:

- **algebraic sensitivity:** is the first-order coefficient nonzero?;
- **experimental sensitivity:** can the coefficient be estimated stably from finite noisy data?

Article II addresses the first question inside its declared measurement model. The second motivates Article III.

---

## 8. Sharp Coxeter tomography and the limit of the claim

In Article II the dissipative quotient has real dimension

\[
N_d=(d^2-1)^2,
\]

and the declared finite-dimensional matrix-valued first-order Coxeter-face model satisfies

\[
\boxed{
L_d^{\mathrm{Cox}}
=
\left\lfloor\frac{d^2}{2}\right\rfloor,
\qquad d\ge3.
}
\]

This is a sharp algebraic identifiability theorem. It does not automatically imply statistical optimality, noise robustness, optimal sample complexity, full finite-time UCP-channel tomography, or generic optimal Lindbladian learning.

That distinction is essential because the current literature already contains Liouvillian-learning protocols, non-Markovian Lindblad-like tomography, classical-shadow approaches, sparse or ansatz-free learning proposals, and learning-hardness results [15–20]. The remaining niche is therefore specific:

> conditioning and redundancy for a loop-based Coxeter measurement geometry whose algebraic minimum is already known exactly.

---

## 9. Article III: Stable Coxeter Tomography

After fixing a physically and mathematically meaningful normalization for the measurement matrix \(M_{\mathcal D}\), define

\[
\sigma_*(\mathcal D)=\sigma_{\min}(M_{\mathcal D}),
\qquad
\kappa(\mathcal D)
=
\frac{\sigma_{\max}(M_{\mathcal D})}
{\sigma_{\min}(M_{\mathcal D})}.
\]

### Definition 9.1 — \(\varepsilon\)-robust Coxeter design

A full-rank design is \(\varepsilon\)-robust if

\[
\sigma_{\min}(M_{\mathcal D})\ge\varepsilon.
\]

### Research Problem B — minimal robust design

Determine

\[
\boxed{
L_d^{\mathrm{rob}}(\varepsilon)
=
\min\left\{
|\mathcal D|:
\sigma_{\min}(M_{\mathcal D})\ge\varepsilon
\right\}
}
\]

for a declared normalization and a natural dimension-dependent threshold \(\varepsilon_d\).

Two incompatible outcomes are possible.

**Branch A — robust sharp designs.** Designs with \(|\mathcal D|=\lfloor d^2/2\rfloor\) admit polynomially controlled condition numbers.

**Branch B — redundancy barrier.** Algebraically minimal designs are systematically ill-conditioned, and stability requires oversampling.

If Branch B holds, the programme acquires a new distinction between algebraic minimality and operational minimality.

---

## 10. Holonomy: the terminology boundary

Kult, Åberg, and Sjöqvist constructed a channel holonomy for smooth families of quantum channels using a Jamiołkowski representation and Uhlmann-type parallel transport [14]. That is an established geometric construction.

Our object

\[
H_\Phi=\Phi(T_m)\cdots\Phi(T_1)
\]

has a different origin: a fixed reduction is applied edgewise to an operator-order loop that was flat before reduction. Therefore *reduced order holonomy* must not be identified with standard channel holonomy.

This difference is productive rather than inconvenient. It turns “geometry” into a future obligation: if this programme is to construct a genuine connection/holonomy theory, it must build the corresponding covariance and local-to-global structure explicitly.

---

## 11. The geometry gate

A future reduced-context construction will be called a **genuine geometric theory** in this programme only if it provides at least:

1. a space or category of contextual configurations;
2. transport maps between them;
3. a composition law;
4. a local connection or defect object;
5. a loop holonomy derived from that local structure;
6. a covariance or gauge principle;
7. nontrivial invariants not reducible to a relabelling of the original channel data;
8. an operational or representation-independent procedure for evaluating at least one nontrivial geometric quantity.

### Conjecture C — effective geometry from nonmultiplicative reduction

There exists a nontrivial class of open-system reductions for which the multiplicativity-defect calculus extends to a structure satisfying the geometry gate, with the Article-II loop defect appearing as the corresponding reduced holonomy object or as its first-order limit.

This is the central speculative conjecture of the paper. It is not implied by Articles I–II.

---

## 12. Protected sectors: a quantitative question only

Noiseless subsystems, decoherence-free subspaces, and protected operator algebras are established subjects [7–10]. The programme therefore does not claim to discover them.

### Conjecture D — transport-restricted protection bound

For a physically natural class of subsystem reductions, there exist assumptions under which small

\[
\mu_\Phi(S)
\]

controls the deviation of a selected transport algebra from protected/noiseless behavior.

A meaningful theorem must specify the channel/dynamical class, norm or operational metric, inequality direction, constants, dimension dependence, and relation to known correctability criteria.

Without such a theorem, the phrase “multiplicativity defect measures decoherence” is not allowed.

---

## 13. A cohomological route, but only after a real complex is built

Article II proves

\[
\Delta_{\Psi\circ\Phi}(X,Y)
=
\Psi(\Delta_\Phi(X,Y))
+
\Delta_\Psi(\Phi(X),\Phi(Y)).
\]

The formula resembles a cocycle or chain-rule identity, but formal resemblance is not enough.

### Research Question E

Can one construct a category or bicategory of reductions in which \(\Delta\) becomes a genuine cochain-like object and the composition law above becomes a functorial cocycle identity?

A positive answer must specify objects, morphisms, coefficient bimodules or functors, a coboundary operator, and nontrivial invariants. Until then, “cohomological” is only a research direction.

---

## 14. The non-Markovian road: an interface with process tensors, not a new memory theory

Process tensors already provide an operational description of multitime non-Markovian processes [21], transfer-tensor methods reconstruct memory-kernel master equations [22], and non-Markovian process tomography has been developed experimentally [23].

Accordingly, the programme does not propose a new theory of multitime quantum memory.

### Research Question F

Can the Article-II multiplicativity-defect composition law be represented inside the process-tensor formalism in a way that produces a useful memory-resolved local-to-global defect decomposition?

A positive result would build a bridge between two existing formalisms. A negative result would establish a boundary of the defect calculus.

---

## 15. The operational barrier

For the programme to become genuinely physical, matrix-valued loop defects must be converted into accessible observables. A minimal chain is

\[
\text{control/transport design}
\to
\text{state preparation}
\to
\text{open evolution}
\to
\text{POVM/readout}
\to
\text{estimator}
\to
\text{parameter reconstruction}.
\]

Article II closes the algebraic-rank layer. Article III should address the conditioning layer. A later paper would need to connect the resulting design theory to states, POVMs, randomized measurements, classical shadows, or ancilla-assisted protocols.

The modern Lindbladian-learning literature makes clear that rank counting cannot substitute for sample-complexity and measurement-design analysis [15–20].

---

## 16. Success and failure conditions

The programme is intended to be falsifiable.

Strong positive outcomes would include at least one of the following:

- polynomially conditioned sharp or near-sharp Coxeter designs;
- a quantitative redundancy law for prescribed conditioning;
- an operational estimator with proved sample complexity for first-order loop coefficients;
- a transport-restricted bound connecting multiplicativity defect to protected-sector behavior;
- a process-tensor representation of the nested defect law;
- a genuine connection/covariance construction passing the geometry gate.

Conversely, the physical/geometric branch should be regarded as limited or unsuccessful if one can prove that sharp and near-sharp loop designs are necessarily catastrophically ill-conditioned, that loop observables require resources comparable to full process tomography, that the defect calculus adds no representation-independent information beyond standard channel/generator descriptions, that the geometry gate can be met only by relabelling known structures, or that a multitime extension destroys the required local-to-global composition law.

---

## 17. Post-audit claim firewall

**Proved and allowed:** Article-I contextual flatness and pair-reduced defects; Article-II exact UCP loop decomposition, Stinespring identity, GKSL Leibniz defect, first-order identifiability statements, and sharp Coxeter count within the declared model; Propositions 3.1, 4.1, 6.1, 6.2, and 7.1 as direct consequences.

**Allowed only as conjecture or research target:** quantitative protected-sector bounds; robust-minimal Coxeter designs; loop-coupled carré-du-champ geometry; cohomological realization; process-tensor embedding; effective geometry satisfying the geometry gate.

**Not allowed without new theorems:** a new theory of quantum curvature; equivalence with Uhlmann/Jamiołkowski channel holonomy; a universal decoherence or entropy-production measure; the first practical Lindblad tomography; discovery of process tensors; spacetime curvature or physical gauge fields generated by context loss.

---

## 18. The Cheshire Cat after the audit

The literature audit makes the metaphor more precise. Several neighboring roads already exist: noiseless structures, carré-du-champ geometry, channel holonomy, process tensors, and Lindbladian learning. The programme should not rename those roads.

Its possible route instead runs through

\[
\boxed{
\text{contextual flatness}
\to
\text{edgewise UCP multiplicativity loss}
\to
\text{transport-restricted loop defect}
\to
\text{robust loop-design geometry}
}
\]

and only if new rigorous bridges are built,

\[
\boxed{
\to
\text{protected/memory interfaces}
\to
\text{effective geometry?}
}
\]

The Cheshire-Cat question is therefore no longer “what new physics have we already discovered?” but “which next theorem actually moves us toward the declared physical destination?”

---

## 19. Conclusion

Article I supplied the reference structure of exact contextual flatness. Article II showed that UCP reduction turns loss of multiplicativity into an exactly decomposable reduced loop defect and that, in the GKSL limit, first-order structure is governed by dissipative incompatibility. It also solved a sharp algebraic first-order Coxeter tomography problem in its declared finite-dimensional measurement model.

The targeted literature audit narrows the admissible interpretation and thereby strengthens the programme. Multiplicative domains, protected/noiseless algebras, carré-du-champ geometry, quantum-channel holonomy, Lindbladian learning, and process tensors are not empty territory. The task is not to rename them but to build genuinely new quantitative interfaces.

The first such interface is Article III: determine the price of stability above the exact algebraic minimum

\[
L_d^{\mathrm{Cox}}
=\left\lfloor\frac{d^2}{2}\right\rfloor.
\]

The distant question remains open:

\[
\boxed{
\text{can context loss under reduction become}
\text{ stably measurable and genuinely geometrically organized?}
}
\]

We do not know the answer. We now know much more precisely which roads already exist, which words require proof, and which mathematical barrier should be attacked next.

---

## References

[1] Malachevsky, A.A. *Split-Interval Representation of Quantum Operator Order: Descent Obstructions, Order Ultrametrics, and Pair-Reduced Holonomy*. Zenodo. DOI: 10.5281/zenodo.22289201.

[2] Malachevsky, A.A. *Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Holonomy, and Sharp Coxeter Tomography*. Zenodo. DOI: 10.5281/zenodo.22421827.

[3] Stinespring, W.F. *Positive Functions on C*-Algebras*. Proc. Amer. Math. Soc. 6 (1955), 211–216. DOI: 10.1090/S0002-9939-1955-0069403-4.

[4] Choi, M.-D. *Completely positive linear maps on complex matrices*. Linear Algebra Appl. 10 (1975), 285–290. DOI: 10.1016/0024-3795(75)90075-0.

[5] Gorini, V.; Kossakowski, A.; Sudarshan, E.C.G. *Completely positive dynamical semigroups of N-level systems*. J. Math. Phys. 17 (1976), 821–825. DOI: 10.1063/1.522979.

[6] Lindblad, G. *On the generators of quantum dynamical semigroups*. Commun. Math. Phys. 48 (1976). DOI: 10.1007/BF01608499.

[7] Choi, M.-D.; Johnston, N.; Kribs, D.W. *The multiplicative domain in quantum error correction*. J. Phys. A 42 (2009), 245303. DOI: 10.1088/1751-8113/42/24/245303.

[8] Johnston, N.; Kribs, D.W. *Generalized Multiplicative Domains and Quantum Error Correction*. Proc. Amer. Math. Soc. 139 (2011), 627–639. DOI: 10.1090/S0002-9939-2010-10556-7.

[9] Choi, M.-D.; Kribs, D.W. *Method to Find Quantum Noiseless Subsystems*. Phys. Rev. Lett. 96 (2006), 050501. DOI: 10.1103/PhysRevLett.96.050501.

[10] Lidar, D.A. *Review of Decoherence-Free Subspaces, Noiseless Subsystems, and Dynamical Decoupling*. Advances in Chemical Physics 154 (2014), 295–354. DOI: 10.1002/9781118742631.ch11. See also Albert, V.V., *Asymptotics of quantum channels*, Quantum 3 (2019), 151, DOI: 10.22331/q-2019-06-06-151; and Amato, D.; Facchi, P.; Konderak, A., *Decoherence-free algebras in quantum dynamics*, Lett. Math. Phys. 116 (2026), 64, DOI: 10.1007/s11005-026-02095-3.

[11] Wirth, M.; Zhang, H. *Complete Gradient Estimates of Quantum Markov Semigroups*. Commun. Math. Phys. 387 (2021), 761–791. DOI: 10.1007/s00220-021-04199-4.

[12] Wirth, M.; Zhang, H. *Curvature-Dimension Conditions for Symmetric Quantum Markov Semigroups*. Ann. Henri Poincaré 24 (2023), 717–750. DOI: 10.1007/s00023-022-01220-x.

[13] Vernooij, M.; Wirth, M. *Derivations and KMS-Symmetric Quantum Markov Semigroups*. Commun. Math. Phys. 403 (2023), 381–416. DOI: 10.1007/s00220-023-04795-6.

[14] Kult, D.; Åberg, J.; Sjöqvist, E. *Holonomy for Quantum Channels*. Phys. Rev. A 77 (2008), 012114. DOI: 10.1103/PhysRevA.77.012114.

[15] Olsacher, T.; Kraft, T.; Kokail, C.; Kraus, B.; Zoller, P. *Hamiltonian and Liouvillian learning in weakly-dissipative quantum many-body systems*. Quantum Sci. Technol. 10 (2025), 015065. DOI: 10.1088/2058-9565/ad9ed5.

[16] Varona, S.; Müller, M.; Bermudez, A. *Lindblad-like quantum tomography for non-Markovian quantum dynamical maps*. npj Quantum Information 11 (2025), 96. DOI: 10.1038/s41534-025-01044-7.

[17] Birke, R.T. et al. *Demonstrating and Benchmarking Classical Shadows for Lindblad Tomography*. arXiv:2602.14694 (2026), preprint.

[18] Romanov, N. et al. *Learning Arbitrary Lindbladians with Quantum Error Correction*. arXiv:2606.18188 (2026), preprint.

[19] Chen, Z.; Yu, Z. *Learning Arbitrary Lindbladians from Time Evolution*. arXiv:2607.28610 (2026), preprint.

[20] Cheng, C.; Bao, R. *Physically natural metric-measure Lindbladian ensembles and their learning hardness*. arXiv:2601.01806 (2026), preprint.

[21] Pollock, F.A.; Rodríguez-Rosario, C.; Frauenheim, T.; Paternostro, M.; Modi, K. *Non-Markovian quantum processes: Complete framework and efficient characterization*. Phys. Rev. A 97 (2018), 012127. DOI: 10.1103/PhysRevA.97.012127.

[22] Pollock, F.A.; Modi, K. *Tomographically reconstructed master equations for any open quantum dynamics*. Quantum 2 (2018), 76. DOI: 10.22331/q-2018-07-11-76.

[23] White, G.A.L. et al. *Non-Markovian Quantum Process Tomography*. PRX Quantum 3 (2022), 020344. DOI: 10.1103/PRXQuantum.3.020344.

---

## Publication note

This v0.2 English manuscript is the post-audit parity version. Before release, bibliography numbering and metadata must be rechecked after LaTeX conversion, the article-specific licence must be fixed, and the final PDF must pass compilation and visual audit.
