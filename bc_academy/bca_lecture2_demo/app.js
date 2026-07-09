'use strict';

const $ = (id) => document.getElementById(id);
const fmt = (x, digits = 3) => {
  if (typeof x === 'string') return x;
  if (!Number.isFinite(x)) return String(x);
  const s = Math.abs(x) < 1e-10 ? '0' : x.toFixed(digits);
  return s.replace(/\.0+$/, '').replace(/(\.\d*?)0+$/, '$1');
};
const cfmt = (z) => {
  const re = Math.abs(z.re) < 1e-10 ? 0 : z.re;
  const im = Math.abs(z.im) < 1e-10 ? 0 : z.im;
  if (im === 0) return fmt(re);
  if (re === 0) return `${fmt(im)}i`;
  return `${fmt(re)} ${im >= 0 ? '+' : '-'} ${fmt(Math.abs(im))}i`;
};
const matHTML = (M) => {
  const rows = M.map(row => row.map(v => typeof v === 'object' ? cfmt(v) : fmt(v)).join('   '));
  return `⎡ ${rows[0]} ⎤\n⎣ ${rows[1]} ⎦`;
};
const matHTMLAny = (M) => {
  const rows = M.map(row => row.map(v => typeof v === 'object' ? cfmt(v) : fmt(v)).join('   '));
  if (M.length === 2) return `⎡ ${rows[0]} ⎤\n⎣ ${rows[1]} ⎦`;
  return rows.map((r, i) => `${i === 0 ? '⎡' : i === rows.length - 1 ? '⎣' : '⎢'} ${r} ${i === 0 ? '⎤' : i === rows.length - 1 ? '⎦' : '⎥'}`).join('\n');
};
const z = (re, im = 0) => ({ re, im });
const zconj = (a) => z(a.re, -a.im);
const zsub = (a, b) => z(a.re - b.re, a.im - b.im);
const zmul = (a, b) => z(a.re*b.re - a.im*b.im, a.re*b.im + a.im*b.re);
const zabs = (a) => Math.hypot(a.re, a.im);

function mul2(A, B) {
  return [
    [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
    [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]],
  ];
}
function add2(A, B) {
  return [[A[0][0]+B[0][0], A[0][1]+B[0][1]], [A[1][0]+B[1][0], A[1][1]+B[1][1]]];
}
function scale2(s, A) {
  return [[s*A[0][0], s*A[0][1]], [s*A[1][0], s*A[1][1]]];
}
function transpose2(A) { return [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]; }
function approxEq(A, B, eps = 1e-8) {
  for (let i=0;i<A.length;i++) for (let j=0;j<A[0].length;j++) if (Math.abs(A[i][j]-B[i][j]) > eps) return false;
  return true;
}

function setupTabs() {
  document.querySelectorAll('.tab').forEach(button => {
    button.addEventListener('click', () => {
      document.querySelectorAll('.tab').forEach(b => b.classList.remove('is-active'));
      document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('is-active'));
      button.classList.add('is-active');
      $(button.dataset.tab).classList.add('is-active');
    });
  });
}

function updateHermitian() {
  const a = parseFloat($('h-a').value);
  const d = parseFloat($('h-d').value);
  const x = parseFloat($('h-x').value);
  const y = parseFloat($('h-y').value);
  const broken = $('break-hermitian').checked;
  ['a','d','x','y'].forEach(k => $(`h-${k}-out`).textContent = fmt(parseFloat($(`h-${k}`).value), 1));
  const lower = broken ? z(x + 0.8, y) : z(x, -y);
  const A = [[z(a), z(x, y)], [lower, z(d)]];
  const Adj = [[zconj(A[0][0]), zconj(A[1][0])], [zconj(A[0][1]), zconj(A[1][1])]];
  $('hermitian-matrix').textContent = matHTML(A);
  $('adjoint-matrix').textContent = matHTML(Adj);
  const diff = Math.max(zabs(zsub(A[0][0], Adj[0][0])), zabs(zsub(A[0][1], Adj[0][1])), zabs(zsub(A[1][0], Adj[1][0])), zabs(zsub(A[1][1], Adj[1][1])));
  const isHerm = diff < 1e-9;
  const status = $('hermitian-status');
  status.className = `status ${isHerm ? 'good' : 'bad'}`;
  status.textContent = isHerm ? 'A = A†: матрица эрмитова.' : 'A ≠ A†: сопряжённость нарушена.';

  if (isHerm) {
    const off2 = x*x + y*y;
    const tr = a + d;
    const det = a*d - off2;
    const disc = Math.max(0, (a-d)*(a-d) + 4*off2);
    const l1 = (tr - Math.sqrt(disc))/2;
    const l2 = (tr + Math.sqrt(disc))/2;
    $('h-l1').textContent = fmt(l1);
    $('h-l2').textContent = fmt(l2);
    $('h-trace').textContent = fmt(tr);
    $('h-det').textContent = fmt(det);
    $('hermitian-comment').textContent = 'Самосопряжённость гарантирует вещественные eigenvalues. Их можно упорядочивать и сравнивать с нулём или threshold.';
  } else {
    const tr = z(A[0][0].re + A[1][1].re, A[0][0].im + A[1][1].im);
    const detz = zsub(zmul(A[0][0], A[1][1]), zmul(A[0][1], A[1][0]));
    $('h-l1').textContent = 'может быть complex';
    $('h-l2').textContent = 'может быть complex';
    $('h-trace').textContent = cfmt(tr);
    $('h-det').textContent = cfmt(detz);
    $('hermitian-comment').textContent = 'Для произвольной матрицы спектр может быть комплексным, а ортогональное спектральное чтение в форме Hermitian case больше не гарантировано.';
  }
}

let state = {};
function decompState() {
  const l1 = parseFloat($('d-l1').value);
  const l2 = parseFloat($('d-l2').value);
  const theta = parseFloat($('d-theta').value) * Math.PI/180;
  const vang = parseFloat($('v-angle').value) * Math.PI/180;
  $('d-l1-out').textContent = fmt(l1, 1);
  $('d-l2-out').textContent = fmt(l2, 1);
  $('d-theta-out').textContent = `${fmt(parseFloat($('d-theta').value),0)}°`;
  $('v-angle-out').textContent = `${fmt(parseFloat($('v-angle').value),0)}°`;
  const q1 = [Math.cos(theta), Math.sin(theta)];
  const q2 = [-Math.sin(theta), Math.cos(theta)];
  const outer = (q) => [[q[0]*q[0], q[0]*q[1]], [q[1]*q[0], q[1]*q[1]]];
  const P1 = outer(q1);
  const P2 = outer(q2);
  const A = add2(scale2(l1, P1), scale2(l2, P2));
  const v = [Math.cos(vang), Math.sin(vang)];
  const Av = [A[0][0]*v[0] + A[0][1]*v[1], A[1][0]*v[0] + A[1][1]*v[1]];
  return { l1, l2, theta, vang, q1, q2, P1, P2, A, v, Av };
}
function arrow(svg, x1,y1,x2,y2, cls, label) {
  const line = document.createElementNS('http://www.w3.org/2000/svg','line');
  line.setAttribute('x1', x1); line.setAttribute('y1', y1); line.setAttribute('x2', x2); line.setAttribute('y2', y2);
  line.setAttribute('class', cls); line.setAttribute('marker-end', `url(#arrow-${cls})`);
  svg.appendChild(line);
  if (label) {
    const t = document.createElementNS('http://www.w3.org/2000/svg','text');
    t.setAttribute('x', x2 + 8); t.setAttribute('y', y2 - 8); t.setAttribute('class','svg-label');
    t.textContent = label;
    svg.appendChild(t);
  }
}
function infiniteLine(svg, q, cls) {
  const L = 165;
  const line = document.createElementNS('http://www.w3.org/2000/svg','line');
  line.setAttribute('x1', -L*q[0]); line.setAttribute('y1', L*q[1]);
  line.setAttribute('x2', L*q[0]); line.setAttribute('y2', -L*q[1]);
  line.setAttribute('class', cls);
  svg.appendChild(line);
}
function updateDecomp() {
  state = decompState();
  $('p1-matrix').textContent = matHTMLAny(state.P1);
  $('p2-matrix').textContent = matHTMLAny(state.P2);
  $('d-a-matrix').textContent = matHTMLAny(state.A);
  $('sum-matrix').textContent = matHTMLAny(add2(scale2(state.l1, state.P1), scale2(state.l2, state.P2)));
  $('d-trace').textContent = fmt(state.A[0][0] + state.A[1][1]);
  $('d-trace-spectral').textContent = `${fmt(state.l1)}·1 + ${fmt(state.l2)}·1 = ${fmt(state.l1 + state.l2)}`;
  $('d-det').textContent = fmt(state.l1 * state.l2);
  drawDecomp();
  updateProjector();
}
function drawDecomp() {
  const svg = $('decomp-svg');
  svg.innerHTML = `
    <defs>
      <marker id="arrow-svg-vector" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#374151" /></marker>
      <marker id="arrow-svg-image" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#a83232" /></marker>
      <marker id="arrow-svg-proj" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#2b6cb0" /></marker>
    </defs>
    <circle cx="0" cy="0" r="150" fill="none" stroke="#e4e9f1" stroke-width="1" />
    <line x1="-170" y1="0" x2="170" y2="0" stroke="#e4e9f1" />
    <line x1="0" y1="-170" x2="0" y2="170" stroke="#e4e9f1" />
  `;
  infiniteLine(svg, state.q1, 'svg-axis1');
  infiniteLine(svg, state.q2, 'svg-axis2');
  const scale = 95;
  const v = [state.v[0]*scale, -state.v[1]*scale];
  const AvScale = 45;
  const Av = [state.Av[0]*AvScale, -state.Av[1]*AvScale];
  arrow(svg, 0,0, v[0], v[1], 'svg-vector', 'v');
  arrow(svg, 0,0, Av[0], Av[1], 'svg-image', 'Av');
  const p1coef = state.v[0]*state.q1[0] + state.v[1]*state.q1[1];
  const p2coef = state.v[0]*state.q2[0] + state.v[1]*state.q2[1];
  const p1 = [state.q1[0]*p1coef*scale, -state.q1[1]*p1coef*scale];
  const p2 = [state.q2[0]*p2coef*scale, -state.q2[1]*p2coef*scale];
  arrow(svg, 0,0, p1[0], p1[1], 'svg-proj', 'Π₁v');
  arrow(svg, 0,0, p2[0], p2[1], 'svg-proj', 'Π₂v');
  const style = document.createElementNS('http://www.w3.org/2000/svg','style');
  style.textContent = `
    .svg-axis1{stroke:#1d4f91;stroke-width:3;stroke-dasharray:5 5}.svg-axis2{stroke:#b8860b;stroke-width:3;stroke-dasharray:5 5}
    .svg-vector{stroke:#374151;stroke-width:4}.svg-image{stroke:#a83232;stroke-width:4}.svg-proj{stroke:#2b6cb0;stroke-width:2;stroke-dasharray:4 4}
    .svg-label{font: bold 13px system-ui; fill:#142033;}
  `;
  svg.appendChild(style);
}

function updateProjector() {
  if (!state.P1) state = decompState();
  const selected = document.querySelector('input[name="proj"]:checked').value;
  const P = selected === 'p1' ? state.P1 : state.P2;
  const P2 = mul2(P, P);
  const Pt = transpose2(P);
  $('proj-matrix').textContent = matHTMLAny(P);
  $('proj-square').textContent = matHTMLAny(P2);
  $('proj-adjoint').textContent = matHTMLAny(Pt);
  const okSquare = approxEq(P, P2);
  const okAdj = approxEq(P, Pt);
  const tr = P[0][0] + P[1][1];
  const status = $('proj-status');
  status.className = `status ${okSquare && okAdj ? 'good' : 'bad'}`;
  status.textContent = `Π² = Π: ${okSquare ? 'да' : 'нет'} · Π† = Π: ${okAdj ? 'да' : 'нет'} · Tr Π = ${fmt(tr)}`;
  $('proj-comment').textContent = 'Trace ортогонального projectors равен размерности его образа. В двумерном случае каждый spectral projector имеет rank 1.';
}

function updateTrace() {
  const lam = parseFloat($('t-lambda').value);
  const mu = parseFloat($('t-mu').value);
  const m = parseInt($('t-m').value, 10);
  $('t-lambda-out').textContent = fmt(lam,1);
  $('t-mu-out').textContent = fmt(mu,1);
  $('t-m-out').textContent = String(m);
  const nMu = 1;
  const trace = m*lam + nMu*mu;
  $('t-tr-pi-l').textContent = `${m}`;
  $('t-tr-pi-mu').textContent = `${nMu}`;
  $('t-trace').textContent = fmt(trace);
  $('t-formula').textContent = `${fmt(lam)}·${m} + ${fmt(mu)}·${nMu} = ${fmt(trace)}`;
  const list = $('trace-spectrum');
  list.innerHTML = '';
  for (let i=0;i<m;i++) {
    const chip = document.createElement('span');
    chip.className = `chip ${Math.abs(lam) < 0.75 ? 'near-zero' : ''}`;
    chip.textContent = `λ = ${fmt(lam)}`;
    list.appendChild(chip);
  }
  const chip = document.createElement('span');
  chip.className = `chip ${Math.abs(mu) < 0.75 ? 'near-zero' : ''}`;
  chip.textContent = `μ = ${fmt(mu)}`;
  list.appendChild(chip);
}

const quizData = [
  {
    q: 'Что гарантирует условие A = A† для конечномерного оператора?',
    a: ['Все eigenvalues вещественны.', 'Все eigenvalues равны нулю.', 'Матрица обязательно диагональна в любом базисе.'],
    correct: 0
  },
  {
    q: 'Почему spectral projector устойчивее отдельного eigenvector при кратности > 1?',
    a: ['Он зависит от выбранного базиса.', 'Он задаёт всё собственное подпространство целиком.', 'Он всегда равен единичной матрице.'],
    correct: 1
  },
  {
    q: 'Что считает Tr Π для ортогонального projectors?',
    a: ['Сумму всех eigenvalues оператора A.', 'Размерность Ran Π.', 'Determinant projectors.'],
    correct: 1
  }
];
function setupQuiz() {
  const root = $('quiz');
  root.innerHTML = '';
  quizData.forEach((item, i) => {
    const box = document.createElement('div');
    box.className = 'quiz-item';
    const p = document.createElement('p');
    p.textContent = `${i+1}. ${item.q}`;
    box.appendChild(p);
    item.a.forEach((ans, j) => {
      const label = document.createElement('label');
      label.innerHTML = `<input type="radio" name="q${i}" value="${j}"> ${ans}`;
      box.appendChild(label);
    });
    root.appendChild(box);
  });
  $('check-quiz').addEventListener('click', () => {
    let score = 0;
    quizData.forEach((item, i) => {
      const selected = document.querySelector(`input[name="q${i}"]:checked`);
      if (selected && parseInt(selected.value, 10) === item.correct) score++;
    });
    const res = $('quiz-result');
    res.className = `status ${score === quizData.length ? 'good' : 'bad'}`;
    res.textContent = `Результат: ${score} из ${quizData.length}. ${score === quizData.length ? 'Готово к переходу к zero modes and kernels.' : 'Повторите формулы A = A†, A = Σ λjΠj и Tr Π = dim Ran Π.'}`;
  });
}

function bindInputs() {
  ['h-a','h-d','h-x','h-y','break-hermitian'].forEach(id => $(id).addEventListener('input', updateHermitian));
  ['d-l1','d-l2','d-theta','v-angle'].forEach(id => $(id).addEventListener('input', updateDecomp));
  document.querySelectorAll('input[name="proj"]').forEach(el => el.addEventListener('input', updateProjector));
  ['t-lambda','t-mu','t-m'].forEach(id => $(id).addEventListener('input', updateTrace));
}

function init() {
  setupTabs();
  setupQuiz();
  bindInputs();
  updateHermitian();
  updateDecomp();
  updateTrace();
}

document.addEventListener('DOMContentLoaded', init);
