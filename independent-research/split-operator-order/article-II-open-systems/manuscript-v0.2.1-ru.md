# Редукция контекста в открытых квантовых системах: дефекты мультипликативности, линдбладовская голономия порядка и точная томография Кокстера

**Малачевский А.А.**  
ORCID: 0009-0008-6009-3196  
Русская версия: v0.2.1, 6 сентября 2026 г.

## Аннотация

Исследуется поведение точно плоского контекстуального операторного транспорта после покомпонентной редукции унитальным вполне положительным (UCP) отображением. Основное препятствие связано не с неунитарностью как таковой, а с нарушением мультипликативности. Для UCP-отображения `Phi` используется стандартный дефект

`Delta_Phi(X,Y)=Phi(XY)-Phi(X)Phi(Y)`,

и доказывается точное разложение дефекта любой редуцированной плоской петли в сумму перенесённых дефектов мультипликативности. Для вложенных редукций получен точный закон композиции, а в представлении Стайнспринга тот же дефект имеет форму утечки в ортогональное дополнение к образу изометрии.

Для равномерно непрерывной UCP-полугруппы `Phi_t=e^{tL}` выводится точная формула Дюамеля. Для ограниченного генератора GKSL соответствующий дефект Лейбница равен

`Gamma_L(X,Y)=sum_alpha [V_alpha^*,X][Y,V_alpha]`.

Это даёт точное интегральное представление редуцированной петлевой голономии и аналитические формулы для кубитных каналов дефазировки, деполяризации и затухания амплитуды.

Далее рассматривается обратная задача. Данные замкнутых петель конечных каналов в общем случае не идентифицируют произвольный UCP-канал, тогда как полный инфинитезимальный дефект Лейбница определяет ограниченный конечномерный генератор с точностью до гамильтонова дифференцирования. Для `M_d(C)` размерность диссипативного фактор-пространства равна `(d^2-1)^2`. Доказывается точная формула

`L_d^Cox=floor(d^2/2)`, `d>=3`.

Теорема относится только к заявленной конечномерной матричнозначной first-order модели измерений на гранях Кокстера и не является универсальной нижней оценкой для произвольной квантовой процессной томографии или обучения линдбладианов.

## 1. Область применимости и границы утверждений

Пусть `A,B` — унитальные C*-алгебры, `Phi:A->B` — UCP-отображение, а унитарные контекстуальные переносы `T_1,...,T_m` удовлетворяют

`T_m ... T_1 = I`.

Редуцированный петлевой продукт определяется как

`H_Phi=Phi(T_m)...Phi(T_1)`.

Термин **редуцированная голономия порядка** означает только дефект произведения, возникающий при покомпонентной редукции точно плоской операторно-порядковой петли. Он не отождествляется с кривизной пространства-времени, физической калибровочной кривизной или голономией каналов в смысле параллельного переноса Ульмана/Ямиолковского.

## 2. Точное исчисление дефектов мультипликативности

Определим

`Delta_Phi(X,Y)=Phi(XY)-Phi(X)Phi(Y)`.

Пусть `P_k=T_k...T_1`. Тогда

`H_Phi-I = - sum_{k=2}^m Phi(T_m)...Phi(T_{k+1}) Delta_Phi(T_k,P_{k-1})`.

Для UCP-отображения из контрактности следует

`||H_Phi-I|| <= sum_{k=2}^m ||Delta_Phi(T_k,P_{k-1})||`.

Если алгебра, порождённая переносами, содержится в multiplicative domain `MD(Phi)`, все дефекты исчезают и `H_Phi=I`.

## 3. Вложенные редукции

Для композиции `Psi o Phi`

`Delta_{Psi o Phi}(X,Y) = Psi(Delta_Phi(X,Y)) + Delta_Psi(Phi(X),Phi(Y))`.

При цепочке редукций полный дефект раскладывается послойно. Это даёт точную локализацию потери мультипликативности, но не утверждает универсальной монотонности нормы дефекта или петлевой голономии при дальнейшей CP-редукции.

## 4. Обратный ход и утечка Стайнспринга

Для унитарного `U`

`D_R^Phi(U)=I-Phi(U)^*Phi(U)=Delta_Phi(U^*,U)>=0`,

`D_L^Phi(U)=I-Phi(U)Phi(U)^*=Delta_Phi(U,U^*)>=0`.

Одновременное обращение обоих дефектов в ноль эквивалентно принадлежности `U` multiplicative domain.

Если

`Phi(X)=V^* pi(X) V`, `P=VV^*`,

то

`Delta_Phi(X,Y)=V^* pi(X)(I-P)pi(Y)V`.

Таким образом, дефект мультипликативности в точности измеряет утечку через дополнение `I-P`.

## 5. Равномерно непрерывные UCP-полугруппы

Пусть `Phi_t=e^{tL}` — равномерно непрерывная унитальная CP-полугруппа с ограниченным генератором `L`. Определим

`Gamma_L(X,Y)=L(XY)-L(X)Y-XL(Y)`.

Тогда

`d/dt Delta_t(X,Y) = L(Delta_t(X,Y)) + Gamma_L(Phi_t(X),Phi_t(Y))`,

`Delta_0=0`,

и поэтому

`Delta_t(X,Y)=int_0^t Phi_{t-s}(Gamma_L(Phi_s(X),Phi_s(Y))) ds`.

Для генератора GKSL

`L(X)=i[H,X]+sum_alpha(V_alpha^* X V_alpha - 1/2{V_alpha^*V_alpha,X})`

получаем

`Gamma_L(X,Y)=sum_alpha [V_alpha^*,X][Y,V_alpha]`.

Гамильтонова часть исчезает, поскольку является дифференцированием. Кроме того,

`Gamma_L(A^*,A)=sum_alpha [A,V_alpha]^*[A,V_alpha]>=0`.

## 6. Точная линдбладовская голономия петли

Для плоской петли

`H_t-I = - sum_{k=2}^m Phi_t(T_m)...Phi_t(T_{k+1}) int_0^t Phi_{t-s}(Gamma_L(Phi_s(T_k),Phi_s(P_{k-1}))) ds`.

При `t->0`

`H_t-I = -t sum_{k=2}^m T_m...T_{k+1} Gamma_L(T_k,P_{k-1}) + O(t^2)`.

## 7. Точные кубитные примеры

Для выбранной adjacent-swap braid-loop получены точные формулы для дефазировки, деполяризации и затухания амплитуды.

Для дефазировки

`H_eta=[[eta^4, 1/2 eta^3(1-eta^2)],[-1/2 eta^3(1-eta^2),eta^4]]`,

а при `eta=e^{-gamma t}`

`||H_t-I||=sqrt(17) gamma t+O(t^2)`.

Для деполяризации

`||H_t^dep-I||=(sqrt(123)/2) gamma t+O(t^2)`.

Для amplitude damping

`||H_t^AD-I||=(1/2)sqrt(57+2sqrt(314)) gamma t+O(t^2)`.

Эти коэффициенты являются отпечатками выбранной петли, а не универсальными инвариантами каналов.

## 8. No-go на конечном времени и инфинитезимальная идентифицируемость

Существуют различные UCP-каналы, имеющие одинаковые closed-loop data на всех петлях выбранного класса. Поэтому универсальная finite-time channel identification из замкнутых петель невозможна без дополнительных данных.

Однако для bounded unital *-preserving generators полный `Gamma_L` идентифицирует генератор modulo derivations. Если

`Gamma_{L1}=Gamma_{L2}`,

то

`L1-L2=i[H_0,·]`.

## 9. Конечномерный фактор и критерий ранга

Вещественная размерность пространства unital *-preserving complex-linear maps `M_d(C)->M_d(C)` равна `d^2(d^2-1)`. Hamiltonian derivations имеют размерность `d^2-1`. Поэтому размерность фактор-пространства равна

`N_d=(d^2-1)^2`.

Для Coxeter-loop design `D` строится вещественно-линейное measurement map `M_D`. Универсальная first-order identifiability modulo Hamiltonian derivations эквивалентна

`rank M_D=(d^2-1)^2`.

Одна matrix-valued face содержит не более `2d^2` вещественных координат, поэтому

`L_d^Cox >= ceil((d^2-1)^2/(2d^2)) = floor(d^2/2)`.

Точные finite-field certificates достигают этой границы при `d=3,4,5`: ранги `64,225,576` при `4,8,12` гранях.

## 10. Ограничительный потолок и extension-ready designs

При scalar-one embedding `M_d -> M_{d+1}` структурный restriction quotient имеет размерность

`R_res(d)=(d^2-1)(d+1)^2+2`.

Для lower-bound-sized design

`rank M_d^up <= (d^2-1)(d+1)^2 + 2*1_{d even}`.

**Extension-ready minimal design** — это дизайн с точно `floor(d^2/2)` гранями, native rank `(d^2-1)^2` и embedded rank, равным указанному потолку.

## 11. Точная теорема: архитектура доказательства

Для нечётного `n>=3` положим

`L=(n^2-1)/2`.

В centered scalar-one coordinate первый ненулевой tangent coefficient имеет порядок `epsilon^2` и распадается на четыре сектора:

`delta_reg F(X,Y)=F(XY)-F(X)Y-XF(Y)`,

`delta_L F(X,Y)=F(XY)-XF(Y)`,

`delta_R F(X,Y)=F(XY)-F(X)Y`,

`delta_0 F(X,Y)=F(XY)`.

Для simple-spectrum diagonal anchor `H` полное regular one-anchor kernel состоит из off-diagonal inner derivation и off-diagonal Schur multiplier. Cyclic-shift binder переводит Schur coefficients в path-additive форму

`c_rs=a_s+a_{s+1}+...+a_{r-1}`,

оставляя modulo diagonal derivations одну cycle-holonomy coordinate `q=sum_i a_i`.

Ровно `L` H-anchored faces реализуют полный anchor rowspace. Сжатый dependency operator `D_n` имеет размер `n(n-2)` и после cycle factorization становится triangular edge operator. Binder-compatible transversality доказывает одновременную ненулевость cycle pivot и всех diagonal coefficients `theta_e` внутри reverse-cycle-zero parameter space.

Однопараметрический путь `H+tS` не даёт native tilt: holonomy-line остаётся в `F(I)=0` для всех `t`. Поперечное возмущение `Y_* -> Y_*+sE_{r-1,r}` создаёт diagonal spikes `-tsq`; finite reconstruction argument показывает, что хотя бы один такой spike не уничтожается, и holonomy-line выходит из native hyperplane.

Отсюда:

**Теорема.** Для каждого нечётного `n>=3` существует extension-ready minimal Coxeter design с `(n^2-1)/2` гранями.

Для перехода odd-to-even все carrier/local witnesses строятся непосредственно в `SL_n(C)`, без некорректной post hoc scalar determinant normalization. Один carrier восстанавливает пять недостающих old restriction coordinates, а `d` local/binding faces разрешают relative quotient modulo exactly three-dimensional Hamiltonian gauge. Zariski density `SU(n)` в `SL_n(C)` возвращает конструкцию к genuine unitary Coxeter faces.

Следовательно, для нечётного `d>=3`

`ER_d -> ER_{d+1}`

с ровно `d+1` новыми faces.

## 12. Главная теорема

Для всякого `d>=3`

`L_d^Cox=floor(d^2/2)`.

Для нечётного `d` lower bound достигается all-odd ER theorem. Для чётного `d` применяется odd-to-even transfer из размерности `d-1`:

`((d-1)^2-1)/2 + d = d^2/2`.

### Граница d=2

Двухгранный дизайн не может быть extension-ready при scalar-one embedding `M_2 -> M_3`. Это не доказывает невозможность native two-face tomography в `d=2`; поэтому sharp theorem заявляется только для `d>=3`.

## 13. Воспроизводимость и прежние верхние оценки

Старые конструкции `L_d^Cox<=3d^2-1` и `L_d^Cox<=2d^2` остаются корректными constructive upper bounds, но больше не являются frontier.

Репозиторий содержит exact scripts и finite-field certificates, включая `d=5`:

`prime=1000033 shape=600x576 rank=576`

`CERTIFIED_FULL_COLUMN_RANK_OVER_Q`.

## 14. Связь с литературой и claim firewall

Stinespring dilation, Choi Schwarz inequality/multiplicative domain, GKSL/Lindblad generator representation, noncommutative carré du champ и общая Lindbladian/Liouvillian tomography являются независимой инфраструктурой.

Channel holonomy Kult-Åberg-Sjöqvist математически отличается от рассматриваемой здесь reduced order holonomy: там используется Jamiołkowski/Uhlmann-type parallel transport для гладких семейств каналов, здесь — product defect после edgewise reduction точно плоской операторно-порядковой петли.

Статья не утверждает:

- universal finite-time identification произвольных UCP channels;
- conditioning/sample-complexity/noise/SPAM bounds;
- universal monotonicity under further CP reductions;
- equality with entropy-production, recoverability или channel-capacity quantities;
- unbounded/infinite-dimensional GKSL extensions;
- полноценную non-Markovian process-tensor theory;
- physical spacetime/gauge curvature.

## Библиографическая граница

Основные инфраструктурные источники: Stinespring (1955), Choi (1974), Lindblad (1976), Gorini-Kossakowski-Sudarshan (1976), Rahaman (2017), Wirth-Zhang (2023), Kult-Åberg-Sjöqvist (2008), Olsacher et al. (2025), Varona-Müller-Bermudez (2025). Полная библиография и DOI сохранены в англоязычном publication source v0.2.1 и русской PDF-версии.

## Репозиторий

`AIDevelopersMonster/boundary-compensation`

Ветка: `research/split-operator-order-article-II-v0.1`.

Article-specific Zenodo DOI будет внесён только после фактического депозита; до этого DOI не назначается и не подставляется вручную.
