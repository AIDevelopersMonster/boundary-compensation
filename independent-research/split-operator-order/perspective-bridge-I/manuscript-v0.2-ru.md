# Выбирая дорогу: от контекстуальной плоскостности к измеримой потере контекста в открытых квантовых системах

## «Чеширский кот у развилки» как физико-математическая перспектива между Article I, Article II и будущей Article III

**Малачевский А.А.**  
ORCID: 0009-0008-6009-3196  
Версия: v0.2  
Дата: 2026-09-06  
Статус: `POST-AUDIT REVIEW DRAFT / PERSPECTIVE + RESEARCH PROGRAMME`

---

## Аннотация

Эта статья сознательно содержит два различающихся эпистемических слоя. Первый слой состоит из строгих математических результатов, уже доказанных в Article I и Article II, а также нескольких непосредственных следствий их формул. Второй слой состоит из явно обозначенных исследовательских гипотез и целей. Спекулятивная часть не объявляется установленной физикой и не отождествляет рассматриваемые петлевые дефекты с пространственно-временной или gauge-кривизной.

Article I построила операторно-порядковую конструкцию, в которой полный контекстуальный транспорт точно плосок, тогда как редукция контекста может порождать ненулевой петлевой дефект. Article II перенесла этот механизм в стандартный язык UCP-редукций открытых квантовых систем. Центральным объектом стал дефект мультипликативности

\[
\Delta_\Phi(X,Y)=\Phi(XY)-\Phi(X)\Phi(Y),
\]

а для равномерно непрерывной GKSL-динамики — лейбницев дефект

\[
\Gamma_{\mathcal L}(X,Y)
=\mathcal L(XY)-\mathcal L(X)Y-X\mathcal L(Y)
=\sum_\alpha [V_\alpha^*,X][Y,V_\alpha].
\]

Для плоской исходной петли Article II дала точное разложение редуцированного loop defect по локальным потерям мультипликативности и доказала sharp first-order Coxeter tomography theorem

\[
L_d^{\mathrm{Cox}}=\left\lfloor\frac{d^2}{2}\right\rfloor,
\qquad d\ge3,
\]

в специально объявленной конечномерной matrix-valued first-order measurement model.

После targeted literature audit граница программы уточняется. Multiplicative domains, noiseless/decoherence-free structures, noncommutative carré du champ, quantum-channel holonomy, Lindbladian learning и process tensors являются уже развитыми направлениями. Поэтому наша задача формулируется уже не как изобретение этих структур, а как вопрос совместимости и нового интерфейса: можно ли превратить transport-restricted multiplicativity loss в устойчиво измеримый loop signal, связать его с protected sectors и multitime memory внутри существующих формализмов и, только при выполнении дополнительных структурных требований, получить genuine effective geometry?

Главная дальняя цель записывается как вопрос, а не как вывод:

\[
\boxed{
\text{context loss}
\;\longrightarrow\;
\text{stable loop observables}
\;\longrightarrow\;
\text{environmental information}
\;\longrightarrow\;
\text{effective geometry?}
}
\]

---

## 1. Зачем выбирать дорогу заранее

Математическая программа может долго производить корректные теоремы, не отвечая на вопрос, ради какого физического результата строится её аппарат. В нашем случае эта опасность особенно велика. Article I можно прочитать как исследование операторного порядка и геометрии перестановок. Article II — как работу по UCP-отображениям, GKSL-генераторам и конечномерной томографии. Оба чтения корректны, но оба скрывают общий мотив.

Этот мотив можно сформулировать так:

> если полное описание сохраняет контекст и остаётся плоским, а физически естественная редукция разрушает мультипликативность и создаёт петлевой дефект, можно ли сделать эту потерю структуры устойчиво измеримой?

Образ Алисы и Чеширского кота здесь используется не как доказательство и не как литературная декорация, а как методологическая схема. Если не указать даже приблизительное направление, любая дорога одинаково допустима. Если цель названа, дальнейшие математические задачи можно оценивать по тому, приближают ли они нас к ней.

Наша цель намеренно сформулирована шире текущих теорем, но уже после литературного аудита достаточно узко, чтобы быть проверяемой.

---

## 2. Article I: точная контекстуальная плоскостность

Первая работа программы — *Split-Interval Representation of Quantum Operator Order: Descent Obstructions, Order Ultrametrics, and Pair-Reduced Holonomy* [1] — сохраняет операторный порядок до тех пор, пока его нельзя безопасно забыть. В соответствующей transport construction полный контекстуальный транспорт по замкнутой петле телескопирует:

\[
T_m\cdots T_1=I.
\]

Это исходный эталон плоскостности программы. Pair reduction из Article I может нарушить эту плоскостность и породить ненулевой reduced loop defect.

Здесь важно не смешивать две разные операции. Pair reduction из Article I и UCP/CP reduction из Article II не являются одной и той же редукцией. Связь между статьями концептуальная: первая показывает, что удаление контекстной информации способно разрушать точную плоскостность; вторая изучает физически стандартный класс немультипликативных редукций, где аналогичный вопрос становится операторно-алгебраическим.

---

## 3. Article II: редуцированная петля как сумма локальных потерь мультипликативности

Пусть \(\Phi\) — UCP-map и

\[
P_k=T_k\cdots T_1,
\qquad
P_m=I.
\]

Редуцированный loop product определим как

\[
H_\Phi=\Phi(T_m)\cdots\Phi(T_1).
\]

Article II [2] доказывает точное тождество

\[
\boxed{
H_\Phi-I
=-\sum_{k=2}^{m}
\Phi(T_m)\cdots\Phi(T_{k+1})
\Delta_\Phi(T_k,P_{k-1}).
}
\]

Это тождество — главный строгий мост между «потерей контекста» и наблюдаемым loop defect. Петлевой эффект не вводится как новая геометрическая сущность: он точно раскладывается на локальные нарушения мультипликативности.

### Proposition 3.1 — transport-restricted loop bound

Пусть \(S\) содержит все \(T_k\) и все префиксы \(P_k\), и определим

\[
\mu_\Phi(S)
=
\sup_{\substack{X,Y\in S\\ \|X\|,\|Y\|\le1}}
\|\Delta_\Phi(X,Y)\|.
\]

Тогда для унитарной \(m\)-петли

\[
\boxed{
\|H_\Phi-I\|\le (m-1)\mu_\Phi(S).
}
\]

**Доказательство.** UCP maps контрактны. Поэтому каждый левый prefactor в точном разложении имеет норму не больше единицы, а каждый локальный defect не превышает \(\mu_\Phi(S)\). После применения triangle inequality получаем утверждение. \(\square\)

Это простой, но принципиальный факт: loop signal количественно контролируется локальной немультипликативностью именно на выбранном transport family.

---

## 4. Multiplicative domain: не новая структура, а точная граница нашей петлевой чувствительности

Multiplicative domain CP/UCP maps — давно установившаяся операторно-алгебраическая конструкция. В quantum information она связана с correctable codes и noiseless structures [3,4]. Поэтому никакого приоритета на саму эту связь здесь не заявляется.

Для нашей программы важен другой факт.

### Proposition 4.1 — exact flatness on the multiplicative domain

Если C*-алгебра, порождённая transport operators петли, содержится в \(MD(\Phi)\), то

\[
H_\Phi=I.
\]

**Доказательство.** На multiplicative domain \(\Phi(XY)=\Phi(X)\Phi(Y)\) для всех релевантных произведений, поэтому каждый член exact defect decomposition равен нулю. \(\square\)

Таким образом, multiplicative domain является точной границей между секторами, которые выбранная редукция переносит без loop defect, и секторами, на которых defect может возникать.

Литературный аудит требует осторожности: noiseless subsystems, decoherence-free subspaces и соответствующие operator algebras имеют самостоятельную развитую теорию [5–7]. Поэтому наш открытый вопрос должен быть количественным:

> допускает ли transport-restricted величина \(\mu_\Phi(S)\) полезные bounds на близость выбранной transport algebra к защищённому/noiseless режиму при дополнительных физических предположениях?

Это **Research Question A**, а не уже доказанная идентификация.

---

## 5. Стайнспринг: строгая локализация потери произведения

Если

\[
\Phi(X)=V^*\pi(X)V,
\qquad P=VV^*,
\]

то Article II даёт

\[
\boxed{
\Delta_\Phi(X,Y)
=V^*\pi(X)(I-P)\pi(Y)V.
}
\]

Формула точно показывает, где возникает defect: между двумя lifted factors появляется компонента, проходящая через дополнение к compressed subspace.

Физически безопасная интерпретация такова: subsystem reduction может терять часть операторного контекста, присутствующего в dilated description. Но из этой формулы не следует, что \(I-P\) является физической кривизной, entropy production или универсальной мерой decoherence.

---

## 6. GKSL и carré du champ: что уже известно и что остаётся нашим вопросом

Для bounded GKSL generator

\[
\mathcal L(X)
=i[H,X]
+
\sum_\alpha
\left(
V_\alpha^*XV_\alpha
-\frac12\{V_\alpha^*V_\alpha,X\}
\right)
\]

лейбницев defect равен

\[
\boxed{
\Gamma_{\mathcal L}(X,Y)
=
\sum_\alpha [V_\alpha^*,X][Y,V_\alpha].
}
\]

Этот объект находится в непосредственной близости к established noncommutative carré-du-champ/Dirichlet-form literature. Gradient estimates, curvature-dimension conditions и derivation representations для quantum Markov semigroups уже развиваются независимо [8–10]. Поэтому \(\Gamma_{\mathcal L}\) нельзя подавать как впервые введённую quantum curvature.

Однако Article II связывает generator-level defect не просто с локальной energy form, а с конкретным contextual loop transport. Именно этот local-to-global интерфейс остаётся нашим предметом.

### Proposition 6.1 — dissipative invisibility on the common noise commutant

Положим

\[
\mathcal N_V
=
\{X:[X,V_\alpha]=[X,V_\alpha^*]=0\ \forall\alpha\}.
\]

Для \(X,Y\in\mathcal N_V\)

\[
\Gamma_{\mathcal L}(X,Y)=0.
\]

Если вся плоская transport loop и все её префиксы лежат в \(\mathcal N_V\), то

\[
H_t-I=O(t^2).
\]

То есть first-order loop probe слеп к сектору, полностью совместимому с noise operators.

### Proposition 6.2 — positive incompatibility certificate

Для любого \(A\)

\[
\boxed{
\Gamma_{\mathcal L}(A^*,A)
=
\sum_\alpha [A,V_\alpha]^*[A,V_\alpha]
\ge0.
}
\]

В фиксированном GKSL representation эта величина обращается в нуль тогда и только тогда, когда \([A,V_\alpha]=0\) для всех \(\alpha\).

Мы интерпретируем это только как algebraic certificate of dissipative incompatibility. Representation-independent operational meaning требует отдельной теории.

---

## 7. Малое время: от algebraic sensitivity к experimental sensitivity

Определим

\[
g_{\mathcal L}(S)
=
\sup_{\substack{X,Y\in S\\\|X\|,\|Y\|\le1}}
\|\Gamma_{\mathcal L}(X,Y)\|.
\]

Из first-order loop formula следует

### Proposition 7.1

\[
\boxed{
\|H_t-I\|
\le
 t(m-1)g_{\mathcal L}(S)+O(t^2).
}
\]

Эта оценка подчёркивает различие между двумя вопросами:

- **algebraic sensitivity:** существует ли ненулевой first-order signal;
- **experimental sensitivity:** можно ли этот signal устойчиво оценить из конечного noisy data set.

Article II решает первый вопрос в своей measurement model. Второй остаётся открытым.

---

## 8. Sharp Coxeter tomography и граница её смысла

В Article II dissipative quotient имеет действительную размерность

\[
N_d=(d^2-1)^2,
\]

а в declared matrix-valued first-order Coxeter-face model доказано

\[
\boxed{
L_d^{\mathrm{Cox}}
=
\left\lfloor\frac{d^2}{2}\right\rfloor,
\qquad d\ge3.
}
\]

Это sharp algebraic identifiability theorem. Оно не означает автоматически:

- statistical optimality;
- noise robustness;
- optimal sample complexity;
- full finite-time UCP-channel tomography;
- generic optimal Lindbladian learning.

Именно здесь targeted audit оказался особенно важен. Современная литература уже содержит quench-based Hamiltonian/Liouvillian learning, Lindblad-like tomography, classical-shadow approaches, ansatz-free and sparse Lindbladian learning и learning-hardness results [12–17].

Поэтому самостоятельная задача Article III должна быть сформулирована не как «новая Lindblad tomography вообще», а как **conditioning and redundancy theory for a specific loop-based Coxeter measurement geometry**.

---

## 9. Article III: Stable Coxeter Tomography

После фиксации нормировки измерительной матрицы \(M_{\mathcal D}\) естественно определить

\[
\sigma_*(\mathcal D)=\sigma_{\min}(M_{\mathcal D}),
\qquad
\kappa(\mathcal D)
=
\frac{\sigma_{\max}(M_{\mathcal D})}
{\sigma_{\min}(M_{\mathcal D})}.
\]

### Definition 9.1 — \(\varepsilon\)-robust design

Full-rank Coxeter design называется \(\varepsilon\)-robust, если

\[
\sigma_{\min}(M_{\mathcal D})\ge\varepsilon.
\]

### Research Problem B — minimal robust Coxeter design

Определить

\[
\boxed{
L_d^{\mathrm{rob}}(\varepsilon)
=
\min\bigl\{
|\mathcal D|:
\sigma_{\min}(M_{\mathcal D})\ge\varepsilon
\bigr\}
}
\]

для физически и математически оправданной нормировки и dimension-dependent threshold \(\varepsilon_d\).

Здесь возникают две принципиально разные возможности.

**Branch A — robust sharp designs.** Минимальные дизайны \(|\mathcal D|=\lfloor d^2/2\rfloor\) допускают polynomial conditioning.

**Branch B — redundancy barrier.** Algebraically minimal designs неизбежно плохо обусловлены, а устойчивость требует oversampling.

Обе ветви являются открытыми. Вторая, если она верна, создаст новую количественную границу между algebraic minimality и operational minimality.

---

## 10. Holonomy: обязательная терминологическая граница

Kult, Åberg и Sjöqvist построили channel holonomy для smooth families of quantum channels через Jamiołkowski representation и Uhlmann-type parallel transport [11]. Это established geometric construction.

Наш объект

\[
H_\Phi=\Phi(T_m)\cdots\Phi(T_1)
\]

имеет другое происхождение: фиксированная reduction применяется edgewise к исходно плоской operator-order loop. Поэтому *reduced order holonomy* нельзя отождествлять с channel holonomy [11].

Эта граница полезна. Она превращает слово «геометрия» из удобной метафоры в строгую future obligation: если мы хотим настоящую connection/holonomy theory, её надо построить.

---

## 11. Geometry gate

Мы предлагаем считать future reduced-context construction genuine geometry только после выполнения как минимум следующих требований:

1. заданы objects/configurations, между которыми осуществляется transport;
2. transport имеет ясный composition law;
3. существует local connection или локальный defect object;
4. loop object выводится из local structure;
5. существует covariance/gauge principle;
6. определены invariants, не сводящиеся к переименованию исходных channel data;
7. хотя бы одна нетривиальная величина имеет operational or representation-independent evaluation procedure.

### Conjecture C — effective geometry from nonmultiplicative reduction

Существует нетривиальный класс open-system reductions, для которого multiplicativity-defect calculus допускает расширение до структуры, удовлетворяющей geometry gate, а Article-II loop defect возникает как соответствующий reduced holonomy object или его first-order limit.

Это центральная спекулятивная гипотеза статьи. Она **не следует** из Article I–II.

---

## 12. Protected sectors: теперь только количественный вопрос

Noiseless subsystems, decoherence-free subspaces и protected operator algebras уже изучены в quantum error correction и asymptotic quantum dynamics [5–7]. Поэтому наша задача не состоит в их переоткрытии.

### Conjecture D — transport-restricted protection bound

Для некоторого физически естественного класса subsystem reductions существуют условия, при которых малость

\[
\mu_\Phi(S)
\]

контролирует deviation выбранной transport algebra от protected/noiseless behaviour.

Содержательная версия этой conjecture должна указать:

- класс channels/dynamics;
- норму и operational metric;
- направление неравенства;
- constants и dimension dependence;
- связь с known correctability criteria.

Без этих данных фраза «multiplicative defect measures decoherence» запрещена.

---

## 13. Cohomological route: только после построения настоящего комплекса

Article II доказывает composition law

\[
\Delta_{\Psi\circ\Phi}(X,Y)
=
\Psi(\Delta_\Phi(X,Y))
+
\Delta_\Psi(\Phi(X),\Phi(Y)).
\]

Она напоминает cocycle/chain-rule identity, но сходства формы недостаточно для cohomological claim.

### Research Question E

Можно ли построить category или bicategory of reductions, где \(\Delta\) становится настоящим cochain-like object и displayed composition law реализуется как functorial cocycle identity?

Для положительного ответа потребуются objects, morphisms, coefficient bimodules/functors, coboundary operator и nontrivial invariants. До этого «cohomological» остаётся направлением, а не результатом.

---

## 14. Non-Markovian road: не новая теория памяти, а интерфейс с process tensors

Process tensors уже дают operational framework для multitime non-Markovian processes [18], transfer tensors позволяют реконструировать memory-kernel master equations [19], а non-Markovian process tomography экспериментально развивается [20].

Поэтому мы не предлагаем «изобрести» multitime memory description.

### Research Question F

Можно ли вложить Article-II multiplicativity-defect composition law в process-tensor formalism так, чтобы получить useful memory-resolved local-to-global defect decomposition?

Если ответ положителен, это будет связью двух существующих аппаратов. Если отрицателен, будет установлена граница применимости нашей defect calculus.

---

## 15. Операционный барьер

Чтобы программа стала физической, matrix-valued loop defects должны перейти в доступные observables. Минимальная цепочка выглядит так:

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

Article II закрывает algebraic rank layer. Article III должна исследовать conditioning layer. Отдельный будущий этап должен связать это с states, POVMs, randomized measurements, classical shadows или ancilla-assisted protocols.

Современная literature по Lindbladian learning показывает, что sample complexity и measurement design нельзя заменять rank counting [12–17]. Поэтому operational claim не должен появляться раньше соответствующей теоремы.

---

## 16. Что будет считаться успехом и что — провалом

Программа должна быть фальсифицируемой.

Сильным успехом будет, например, доказательство хотя бы одного из следующих результатов:

- polynomially conditioned sharp или near-sharp Coxeter designs;
- quantitative redundancy law for prescribed conditioning;
- operational estimator с доказанной sample complexity для first-order loop coefficients;
- transport-restricted bound, связывающий defect с protected-sector behaviour;
- process-tensor representation of the nested defect law;
- genuine connection/covariance construction, проходящая geometry gate.

Напротив, физико-геометрическая ветвь должна считаться ограниченной или неудачной, если будет доказано, что:

- sharp и near-sharp loop designs неизбежно катастрофически ill-conditioned;
- loop observables нельзя устойчиво оценивать без ресурсов, сопоставимых с full process tomography;
- defect calculus не даёт representation-independent информации сверх стандартного channel/generator description;
- geometry gate невозможно выполнить без искусственного переобозначения известных структур;
- multitime extension разрушает нужную local-to-global composition structure.

---

## 17. Claim firewall после литературного аудита

### Доказано и разрешено утверждать

Article-I contextual flatness и pair-reduced defects; Article-II exact UCP loop decomposition, Stinespring identity, GKSL Leibniz defect, first-order identifiability statements и sharp Coxeter count в declared model; Propositions 3.1, 4.1, 6.1, 6.2 и 7.1 настоящей статьи как прямые следствия этих результатов.

### Разрешено только как conjecture/research target

Quantitative protected-sector bounds; robust-minimal Coxeter designs; loop-coupled carré-du-champ geometry; cohomological realization; process-tensor embedding; effective geometry satisfying the geometry gate.

### Не разрешено без новых теорем

«Новая теория quantum curvature»; equivalence с Uhlmann/Jamiołkowski channel holonomy; universal decoherence or entropy-production measure; first practical Lindblad tomography; discovery of process tensors; spacetime curvature or physical gauge field generated by context loss.

---

## 18. Чеширский кот после аудита

После литературного аудита метафора становится даже точнее. Мы теперь видим, что многие дороги уже построены другими исследовательскими программами: noiseless structures, carré du champ geometry, channel holonomy, process tensors, Lindbladian learning. Наша задача не состоит в том, чтобы дать этим дорогам новые названия.

Наш возможный маршрут проходит между ними:

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

и только затем, если появятся новые строгие мосты,

\[
\boxed{
\to
\text{protected/memory interfaces}
\to
\text{effective geometry?}
}
\]

То есть Cheshire-Cat question теперь не «какую физику мы уже открыли?», а «какая из следующих доказуемых дорог действительно приближает нас к заявленной физической цели?»

---

## 19. Заключение

Article I дала эталон exact contextual flatness. Article II показала, что при UCP reduction loss of multiplicativity создаёт точно разлагаемый reduced loop defect, а в GKSL limit first-order structure определяется dissipative incompatibility. Она также решила sharp algebraic first-order Coxeter tomography problem в заявленной конечномерной модели.

Targeted literature audit существенно сузил допустимую интерпретацию и тем самым усилил программу. Multiplicative domains, protected/noiseless algebras, carré-du-champ geometry, quantum-channel holonomy, Lindbladian learning и process tensors не являются свободной территорией. Поэтому наша дальнейшая задача не в их переименовании, а в построении новых quantitative interfaces.

Первый такой интерфейс — Article III: определить цену устойчивости поверх точной algebraic minimality

\[
L_d^{\mathrm{Cox}}=\left\lfloor\frac{d^2}{2}\right\rfloor.
\]

Дальний вопрос остаётся открытым:

\[
\boxed{
\text{может ли потеря операторного контекста при редукции}
\text{ стать устойчиво измеримой и действительно геометрически организованной?}
}
\]

Мы не знаем ответа. Но теперь достаточно точно знаем, какие дороги уже существуют, какие слова нельзя использовать без доказательства и какой следующий математический барьер следует атаковать.

---

## Литература

[1] Malachevsky, A.A. *Split-Interval Representation of Quantum Operator Order: Descent Obstructions, Order Ultrametrics, and Pair-Reduced Holonomy*. Zenodo. DOI: 10.5281/zenodo.22289201.

[2] Malachevsky, A.A. *Context Reduction in Open Quantum Systems: Multiplicativity Defects, Lindblad Order Holonomy, and Sharp Coxeter Tomography*. Zenodo. DOI: 10.5281/zenodo.22421827.

[3] Choi, M.-D.; Johnston, N.; Kribs, D.W. *The multiplicative domain in quantum error correction*. Journal of Physics A 42 (2009), 245303. DOI: 10.1088/1751-8113/42/24/245303.

[4] Johnston, N.; Kribs, D.W. *Generalized Multiplicative Domains and Quantum Error Correction*. Proc. Amer. Math. Soc. 139 (2011), 627–639. DOI: 10.1090/S0002-9939-2010-10556-7.

[5] Choi, M.-D.; Kribs, D.W. *Method to Find Quantum Noiseless Subsystems*. Phys. Rev. Lett. 96 (2006), 050501. DOI: 10.1103/PhysRevLett.96.050501.

[6] Lidar, D.A. *Review of Decoherence-Free Subspaces, Noiseless Subsystems, and Dynamical Decoupling*. 2014. DOI: 10.1002/9781118742631.ch11.

[7] Albert, V.V. *Asymptotics of quantum channels: conserved quantities, an adiabatic limit, and matrix product states*. Quantum 3 (2019), 151. DOI: 10.22331/q-2019-06-06-151.

[8] Wirth, M.; Zhang, H. *Complete Gradient Estimates of Quantum Markov Semigroups*. Commun. Math. Phys. 387 (2021), 761–791. DOI: 10.1007/s00220-021-04199-4.

[9] Wirth, M.; Zhang, H. *Curvature-Dimension Conditions for Symmetric Quantum Markov Semigroups*. Ann. Henri Poincaré 24 (2023), 717–750. DOI: 10.1007/s00023-022-01220-x.

[10] Vernooij, M.; Wirth, M. *Derivations and KMS-Symmetric Quantum Markov Semigroups*. Commun. Math. Phys. 403 (2023), 381–416. DOI: 10.1007/s00220-023-04795-6.

[11] Kult, D.; Åberg, J.; Sjöqvist, E. *Holonomy for Quantum Channels*. Phys. Rev. A 77 (2008), 012114. DOI: 10.1103/PhysRevA.77.012114.

[12] Olsacher, T.; Kraft, T.; Kokail, C.; Kraus, B.; Zoller, P. *Hamiltonian and Liouvillian learning in weakly-dissipative quantum many-body systems*. Quantum Sci. Technol. 10 (2025), 015065. DOI: 10.1088/2058-9565/ad9ed5.

[13] Varona, S.; Müller, M.; Bermudez, A. *Lindblad-like quantum tomography for non-Markovian quantum dynamical maps*. npj Quantum Information 11 (2025), 96. DOI: 10.1038/s41534-025-01044-7.

[14] Birke, R.T. et al. *Demonstrating and Benchmarking Classical Shadows for Lindblad Tomography*. arXiv:2602.14694 (2026).

[15] Romanov, N. et al. *Learning Arbitrary Lindbladians with Quantum Error Correction*. arXiv:2606.18188 (2026).

[16] Chen, Z.; Yu, Z. *Learning Arbitrary Lindbladians from Time Evolution*. arXiv:2607.28610 (2026).

[17] Cheng, C.; Bao, R. *Physically natural metric-measure Lindbladian ensembles and their learning hardness*. arXiv:2601.01806 (2026).

[18] Pollock, F.A.; Rodríguez-Rosario, C.; Frauenheim, T.; Paternostro, M.; Modi, K. *Non-Markovian quantum processes: Complete framework and efficient characterization*. Phys. Rev. A 97 (2018), 012127. DOI: 10.1103/PhysRevA.97.012127.

[19] Pollock, F.A.; Modi, K. *Tomographically reconstructed master equations for any open quantum dynamics*. Quantum 2 (2018), 76. DOI: 10.22331/q-2018-07-11-76.

[20] White, G.A.L. et al. *Non-Markovian Quantum Process Tomography*. PRX Quantum 3 (2022), 020344. DOI: 10.1103/PRXQuantum.3.020344.

---

## Publication note

Этот v0.2 является первой полностью переписанной post-audit русской версией. Следующие gates: bibliographic verification of all recent/preprint references, English parity manuscript, theorem/claim audit, затем LaTeX/PDF publication build and visual audit.
