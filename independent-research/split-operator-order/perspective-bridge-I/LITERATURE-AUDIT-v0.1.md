# Targeted Literature Audit for the Cheshire-Cat Perspective

**Author:** Malachevsky, A.A. / Малачевский А.А.  
**ORCID:** 0009-0008-6009-3196  
**Date:** 2026-09-06  
**Status:** `TARGETED_AUDIT_COMPLETE / PRIORITY_CLAIMS_RESTRICTED`

## Scope

This audit covers the five literature interfaces that could overlap with the bridge article's intended research programme:

1. multiplicative domains versus noiseless/decoherence-free structures;
2. noncommutative carré du champ and quantum Markov geometry;
3. quantum/channel holonomy and geometric phases;
4. Lindbladian/Liouvillian learning and tomography;
5. process tensors, memory kernels, and non-Markovian characterization.

The audit is targeted, not exhaustive. It is sufficient for claim-boundary control, but not for universal priority language.

---

## 1. Multiplicative domain versus noiseless/decoherence-free algebras

### Established literature

The multiplicative domain of a CP/UCP map is already a mature operator-algebraic object. In quantum information it is explicitly connected to quantum error correction.

- M.-D. Choi, N. Johnston, D. W. Kribs, **The multiplicative domain in quantum error correction**, Journal of Physics A 42 (2009), 245303. DOI: `10.1088/1751-8113/42/24/245303`.
  - For unital quantum channels, the multiplicative domain captures unitarily correctable codes.
- N. Johnston, D. W. Kribs, **Generalized Multiplicative Domains and Quantum Error Correction**, Proc. Amer. Math. Soc. 139 (2011), 627–639. DOI: `10.1090/S0002-9939-2010-10556-7`.
  - Generalized multiplicative domains extend the representation-theoretic description to broader correctable-code/noiseless-subsystem structures.
- M.-D. Choi, D. W. Kribs, **Method to Find Quantum Noiseless Subsystems**, Phys. Rev. Lett. 96 (2006), 050501. DOI: `10.1103/PhysRevLett.96.050501`.
  - Develops noise-commutant/noiseless-subsystem structure for arbitrary operations.
- D. A. Lidar, **Review of Decoherence-Free Subspaces, Noiseless Subsystems, and Dynamical Decoupling** (2014), DOI: `10.1002/9781118742631.ch11`.
  - Reviews DFS/noiseless subsystem theory.
- D. Amato, P. Facchi, A. Konderak, **Decoherence-free algebras in quantum dynamics**, Letters in Mathematical Physics 116, 64 (2026). DOI: `10.1007/s11005-026-02095-3`.
  - Introduces a Choi-Effros decoherence-free algebra for asymptotic finite-dimensional dynamics and relates it to attractor spaces.
- V. V. Albert, **Asymptotics of quantum channels: conserved quantities, an adiabatic limit, and matrix product states**, Quantum 3, 151 (2019). DOI: `10.22331/q-2019-06-06-151`.
  - Studies fixed/rotating points, conserved quantities, and asymptotic channel structure.

### Audit conclusion

The bridge article **must not claim** that multiplicative-domain structure, noiseless subsystems, protected algebras, or their qualitative relation are new.

The potentially new research direction is narrower:

> use a transport-restricted defect scale `mu_Phi(S)` and loop observables to quantify how far a selected transport algebra lies from defect-free/multiplicative behaviour, then ask for model-dependent bounds connecting this to protected/noiseless dynamics.

This must remain a conjectural quantitative bridge, not a rediscovery of noiseless-subsystem theory.

Publication-safe wording:

> “The multiplicative domain and noiseless/correctable operator structures are established. Our proposed question is whether transport-restricted multiplicativity defects admit quantitative operational bounds on selected protected sectors.”

---

## 2. Carré du champ and quantum Markov geometry

### Established literature

The Leibniz-defect structure of quantum Markov generators belongs to a substantial noncommutative Dirichlet-form/carré-du-champ literature.

- M. Wirth, H. Zhang, **Complete Gradient Estimates of Quantum Markov Semigroups**, Commun. Math. Phys. 387 (2021), 761–791. DOI: `10.1007/s00220-021-04199-4`.
- M. Wirth, H. Zhang, **Curvature-Dimension Conditions for Symmetric Quantum Markov Semigroups**, Ann. Henri Poincaré 24 (2023), 717–750. DOI: `10.1007/s00023-022-01220-x`.
  - Develops noncommutative curvature-dimension conditions for symmetric quantum Markov semigroups.
- M. Vernooij, M. Wirth, **Derivations and KMS-Symmetric Quantum Markov Semigroups**, Commun. Math. Phys. 403 (2023), 381–416. DOI: `10.1007/s00220-023-04795-6`.
  - Represents generators via derivations into Hilbert bimodules in a symmetric setting.

### Audit conclusion

The identity

`Gamma_L(X,Y)=sum_alpha [V_alpha^*,X][Y,V_alpha]`

must be described as a GKSL Leibniz-defect/carré-du-champ-type formula, not a newly invented notion of quantum curvature.

The bridge article may ask whether **loop-integrated** or **transport-restricted** defect data induce a new geometry, but it must explicitly distinguish that goal from existing curvature-dimension, gradient estimate, noncommutative Wasserstein, and Dirichlet-form geometries.

Publication-safe research question:

> “Can the existing generator-level carré-du-champ structure be coupled to contextual loop transport to produce a distinct local-to-global holonomy structure?”

This is open in our programme and does not follow from existing curvature-dimension theory.

---

## 3. Quantum/channel holonomy

### Established literature

- D. Kult, J. Åberg, E. Sjöqvist, **Holonomy for Quantum Channels**, Phys. Rev. A 77 (2008), 012114. DOI: `10.1103/PhysRevA.77.012114`.
  - Defines holonomy for smoothly parametrized families of quantum channels using the Jamiołkowski representation, Uhlmann-type parallel transport, gauge structure, and an interferometric realization.

### Audit conclusion

This is the most important terminology collision.

Our Article-II object

`H_Phi=Phi(T_m)...Phi(T_1)`

is a product defect obtained by applying a fixed reduction edgewise to a flat operator-order loop. It is **not** the Kult–Åberg–Sjöqvist channel holonomy.

The bridge article may retain “reduced order holonomy” only with an explicit qualifier and boundary paragraph.

Forbidden wording:

- “we generalize quantum channel holonomy”;
- “our holonomy is the physical channel holonomy”;
- “the loop defect is already a gauge curvature”.

Allowed wording:

> “Our loop object is algebraically different from Uhlmann/Jamiołkowski channel holonomy. A future geometry would have to construct its own parallel-transport/covariance structure rather than borrow the terminology alone.”

This actually strengthens the geometry gate: if we want genuine geometry, we must earn it by constructing a connection/covariance framework.

---

## 4. Lindbladian/Liouvillian learning and tomography

### Established and recent literature

The operational learning landscape is already broad and fast-moving.

- T. Olsacher, T. Kraft, C. Kokail, B. Kraus, P. Zoller, **Hamiltonian and Liouvillian learning in weakly-dissipative quantum many-body systems**, Quantum Sci. Technol. 10 (2025), 015065. DOI: `10.1088/2058-9565/ad9ed5`.
  - Learns Hamiltonian/Liouvillian operator content from quench dynamics, with explicit shot-noise behaviour and ansatz dependence.
- S. Varona, M. Müller, A. Bermudez, **Lindblad-like quantum tomography for non-Markovian quantum dynamical maps**, npj Quantum Information 11, 96 (2025). DOI: `10.1038/s41534-025-01044-7`.
  - Time-local master-equation tomography allowing non-Markovian behaviour and negative rates.
- R. T. Birke et al., **Demonstrating and Benchmarking Classical Shadows for Lindblad Tomography**, arXiv:`2602.14694` (2026).
  - Experimental shadow-based Lindblad tomography on a superconducting transmon processor, reducing measurement configurations under locality assumptions.
- N. Romanov et al., **Learning Arbitrary Lindbladians with Quantum Error Correction**, arXiv:`2606.18188` (2026).
  - Ansatz-free sparse Lindbladian learning using quantum-error-correction primitives, with precision-scaling results.
- Z. Chen, Z. Yu, **Learning Arbitrary Lindbladians from Time Evolution**, arXiv:`2607.28610` (2026).
  - Efficient ancilla-free/control-free learning under dynamical-strength assumptions, with near-optimal experiment scaling up to logarithmic factors.
- C. Cheng, R. Bao, **Physically natural metric-measure Lindbladian ensembles and their learning hardness**, arXiv:`2601.01806` (2026).
  - Proves average-case learning-hardness results in statistical-query models for random Lindbladian ensembles.

### Audit conclusion

Article III cannot be marketed as “the first route to practical Lindblad tomography”. Existing work already addresses experiment counts, shot noise, shadows, sparse recovery, ansatz-free learning, and hardness.

Our distinct niche must be precise:

> conditioning and oversampling of a **specific loop-based first-order Coxeter measurement geometry**, starting from an exact algebraic minimal-face theorem.

Potential novelty is therefore in the geometry/design trade-off, not generic Lindbladian learning.

The strongest safe Article-III question is:

> Given an algebraically minimal Coxeter-loop measurement design, what redundancy is required to obtain a prescribed singular-value/conditioning threshold?

This is sufficiently distinct from existing learning algorithms provided the measurement model is defined explicitly.

---

## 5. Process tensors, memory kernels, and non-Markovian dynamics

### Established literature

- F. A. Pollock, C. Rodríguez-Rosario, T. Frauenheim, M. Paternostro, K. Modi, **Non-Markovian quantum processes: Complete framework and efficient characterization**, Phys. Rev. A 97 (2018), 012127. DOI: `10.1103/PhysRevA.97.012127`.
  - Operational process-tensor framework for arbitrary multitime non-Markovian processes.
- F. A. Pollock, K. Modi, **Tomographically reconstructed master equations for any open quantum dynamics**, Quantum 2, 76 (2018). DOI: `10.22331/q-2018-07-11-76`.
  - Reconstructs memory-kernel master equations from dynamical maps via transfer tensors.
- G. A. L. White et al., **Non-Markovian Quantum Process Tomography**, PRX Quantum 3 (2022), 020344. DOI: `10.1103/PRXQuantum.3.020344`.
  - Experimental/process-tensor tomography of temporally correlated noise.
- **Process Tensor Approaches to Non-Markovian Quantum Dynamics**, Phys. Rev. X (2026), recent Perspective.
  - Reviews process-tensor methods and tensor-network approaches for non-Markovian open systems.

### Audit conclusion

The bridge article must not present process tensors, temporal quantum combs, or multitime memory characterization as an unexplored destination.

The open question is much narrower:

> Can the Article-II multiplicativity-defect composition law be lifted into the process-tensor framework in a way that yields a useful memory-resolved local-to-global defect decomposition?

That is a genuine compatibility/translation problem between two formalisms, not a proposal to invent non-Markovian process tomography.

Publication-safe wording:

> “Process tensors already provide an operational theory of multitime quantum memory. We ask whether our multiplicativity-defect calculus admits a nontrivial representation inside that framework.”

---

## 6. Revised claim map for the bridge article

### Green — safe theorem-level statements

- Article-I contextual flatness / pair-reduced defect results.
- Article-II exact multiplicativity-defect loop decomposition.
- Stinespring leakage identity.
- GKSL Leibniz-defect identity.
- transport-restricted loop bound `||H-I|| <= (m-1)mu`.
- vanishing first-order defect on the common noise commutant.
- positivity `Gamma_L(A^*,A)>=0`.
- sharp Coxeter face count in the declared first-order model.

### Yellow — allowed only as research questions/conjectures

- quantitative relation between transport-restricted multiplicativity defect and protected/noiseless behaviour;
- conditioning/oversampling law for Coxeter designs;
- loop-coupled carré-du-champ geometry distinct from existing curvature-dimension frameworks;
- cohomological/categorical realization of the composition law;
- embedding of multiplicativity-defect calculus into process tensors;
- effective geometry satisfying the programme's geometry gate.

### Red — do not claim

- discovery of multiplicative domains/noiseless algebras;
- first theory of open-system curvature;
- equivalence to established quantum channel holonomy;
- first practical/efficient Lindbladian tomography;
- invention of non-Markovian process tensors;
- spacetime/gauge curvature, entropy production, or universal decoherence measure.

---

## 7. Important positive result of the audit

The audit does **not** kill the bridge article. It sharpens it.

The strongest surviving research programme is now:

`contextual flatness`

`-> edgewise UCP multiplicativity loss`

`-> transport-restricted loop defect`

`-> robust loop-design geometry`

`-> possible embedding into established protected-sector / process-tensor / noncommutative-geometric frameworks`

`-> genuine effective geometry only if the geometry gate is met`.

This is narrower than the original speculative horizon but scientifically stronger because every interface is now anchored against an established literature.

## 8. Required edits before publication

1. Add Choi–Johnston–Kribs 2009 and Johnston–Kribs 2011 to the multiplicative-domain section.
2. Add Lidar 2014, Choi–Kribs 2006, Albert 2019, and Amato–Facchi–Konderak 2026 around protected/decoherence-free structures.
3. Add Wirth–Zhang 2021/2023 and Vernooij–Wirth 2023 around carré-du-champ/geometry.
4. Keep Kult–Åberg–Sjöqvist 2008 as the mandatory holonomy boundary citation.
5. Expand Article-III context with Olsacher et al. 2025, Birke et al. 2026, Romanov et al. 2026, Chen–Yu 2026, and at least one learning-hardness reference.
6. In the non-Markovian section cite Pollock et al. 2018, Pollock–Modi 2018, White et al. 2022, and the recent process-tensor Perspective.
7. Replace any wording suggesting an unexplored area with a narrower compatibility/quantitative question.

## 9. Audit verdict

**Bridge manuscript status after targeted literature audit:** `SCIENTIFIC_DIRECTION_VALID / CLAIMS_REQUIRE_NARROWING`.

The speculative article remains worth publishing, but its strongest value is not a claim to a new physical theory. Its value is a disciplined research map that connects two proved operator-order/UCP results to several established fields through sharply formulated compatibility, stability, and geometry-gate questions.

No broad priority claim is licensed.
