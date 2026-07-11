
(function(){
  const navy = '#082c5f', blue = '#2f6fc1', sky = '#d9e7fb', gold = '#c89426', red = '#b83a3a', gray = '#8da0b8', grid = '#d9e2ef';
  function $(id){ return document.getElementById(id); }
  function fmt(x, digits=3){
    if (!isFinite(x)) return String(x);
    if (Math.abs(x) < 1e-10) x = 0;
    let s = Number(x).toFixed(digits);
    s = s.replace(/\.0+$/,'').replace(/(\.\d*?)0+$/,'$1');
    return s;
  }
  function matrix(a,b,c,d){ return {a:+a,b:+b,c:+c,d:+d}; }
  function mul(A,v){ return {x:A.a*v.x + A.b*v.y, y:A.c*v.x + A.d*v.y}; }
  function det(A){ return A.a*A.d - A.b*A.c; }
  function tr(A){ return A.a + A.d; }
  function eig2(A){
    const T = tr(A), D = det(A), disc = T*T - 4*D;
    if (disc >= -1e-10){
      const s = Math.sqrt(Math.max(0,disc));
      return {real:true, values:[(T-s)/2,(T+s)/2], trace:T, determinant:D, discriminant:disc};
    }
    const re = T/2, im = Math.sqrt(-disc)/2;
    return {real:false, values:[{re,im},{re,im:-im}], trace:T, determinant:D, discriminant:disc};
  }
  function eigText(E){
    if(E.real) return '{ ' + E.values.map(v=>fmt(v,3)).join(', ') + ' }';
    return '{ ' + E.values.map(z=>fmt(z.re,3)+(z.im>=0?'+':'')+fmt(z.im,3)+'i').join(', ') + ' }';
  }
  function setText(id, text){ const el=$(id); if(el) el.textContent = text; }
  function matText(A){ return '['+fmt(A.a,2)+'  '+fmt(A.b,2)+'; '+fmt(A.c,2)+'  '+fmt(A.d,2)+']'; }
  function syncNumberRange(prefix, cb){
    const range = $(prefix), num = $(prefix+'n');
    if(!range || !num) return;
    const update = (fromRange)=>{
      if(fromRange) num.value = range.value; else range.value = num.value;
      cb && cb();
    };
    range.addEventListener('input',()=>update(true));
    num.addEventListener('input',()=>update(false));
  }
  function bindRange(id, cb){ const el=$(id); if(el) el.addEventListener('input', cb); }
  function getMatrix(ids=['a','b','c','d']){ return matrix($(ids[0]).value,$(ids[1]).value,$(ids[2]).value,$(ids[3]).value); }
  function setupCanvas(canvas, logicalW=720, logicalH=480){
    const dpr = window.devicePixelRatio || 1;
    const rectW = canvas.clientWidth || logicalW;
    const scale = rectW / logicalW;
    canvas.width = Math.round(logicalW * dpr);
    canvas.height = Math.round(logicalH * dpr);
    canvas.style.height = Math.round(logicalH * scale) + 'px';
    const ctx = canvas.getContext('2d');
    ctx.setTransform(dpr,0,0,dpr,0,0);
    return {ctx,w:logicalW,h:logicalH};
  }
  function mapPoint(p, center, unit){ return {x:center.x + p.x*unit, y:center.y - p.y*unit}; }
  function arrow(ctx,p,q,color=navy,width=2, dashed=false){
    ctx.save(); ctx.strokeStyle=color; ctx.fillStyle=color; ctx.lineWidth=width; ctx.lineCap='round';
    if(dashed) ctx.setLineDash([8,6]);
    ctx.beginPath(); ctx.moveTo(p.x,p.y); ctx.lineTo(q.x,q.y); ctx.stroke();
    ctx.setLineDash([]);
    const ang=Math.atan2(q.y-p.y,q.x-p.x), head=10+width*1.5;
    ctx.beginPath(); ctx.moveTo(q.x,q.y);
    ctx.lineTo(q.x-head*Math.cos(ang-Math.PI/7), q.y-head*Math.sin(ang-Math.PI/7));
    ctx.lineTo(q.x-head*Math.cos(ang+Math.PI/7), q.y-head*Math.sin(ang+Math.PI/7));
    ctx.closePath(); ctx.fill(); ctx.restore();
  }
  function line(ctx,p,q,color=navy,width=1,dashed=false){
    ctx.save(); ctx.strokeStyle=color; ctx.lineWidth=width; if(dashed) ctx.setLineDash([6,5]);
    ctx.beginPath(); ctx.moveTo(p.x,p.y); ctx.lineTo(q.x,q.y); ctx.stroke(); ctx.restore();
  }
  function dot(ctx,p,r=5,color=gold){ ctx.save(); ctx.fillStyle=color; ctx.beginPath(); ctx.arc(p.x,p.y,r,0,Math.PI*2); ctx.fill(); ctx.restore(); }
  function label(ctx, text, p, color=navy, size=16, align='center'){
    ctx.save(); ctx.fillStyle=color; ctx.font=`${size}px Georgia, serif`; ctx.textAlign=align; ctx.textBaseline='middle'; ctx.fillText(text,p.x,p.y); ctx.restore();
  }
  function drawAxes(ctx, center, unit, opts={}){
    const w=opts.w||720,h=opts.h||480, lim=opts.lim||3;
    ctx.save(); ctx.strokeStyle=grid; ctx.lineWidth=1;
    for(let i=-lim;i<=lim;i++){
      const x=center.x+i*unit, y=center.y-i*unit;
      ctx.beginPath(); ctx.moveTo(x,22); ctx.lineTo(x,h-22); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(22,y); ctx.lineTo(w-22,y); ctx.stroke();
    }
    arrow(ctx,{x:30,y:center.y},{x:w-30,y:center.y},'#111',1.4,false);
    arrow(ctx,{x:center.x,y:h-30},{x:center.x,y:30},'#111',1.4,false);
    label(ctx,'x',{x:w-44,y:center.y+18},'#111',18);
    label(ctx,'y',{x:center.x+18,y:44},'#111',18);
    ctx.restore();
  }
  function drawOriginalGrid(ctx, center, unit, lim=2, color='#edf2fa'){
    for(let i=-lim;i<=lim;i++){
      line(ctx,mapPoint({x:-lim,y:i},center,unit),mapPoint({x:lim,y:i},center,unit),color,1);
      line(ctx,mapPoint({x:i,y:-lim},center,unit),mapPoint({x:i,y:lim},center,unit),color,1);
    }
  }
  function drawTransformedGrid(ctx,A,center,unit,lim=2, color=blue){
    ctx.save(); ctx.globalAlpha=.62;
    for(let i=-lim;i<=lim;i++){
      let prev=null;
      for(let t=-lim;t<=lim;t+=.08){
        const p = mul(A,{x:t,y:i}), q=mapPoint(p,center,unit);
        if(prev) line(ctx,prev,q,color,.9); prev=q;
      }
      prev=null;
      for(let t=-lim;t<=lim;t+=.08){
        const p = mul(A,{x:i,y:t}), q=mapPoint(p,center,unit);
        if(prev) line(ctx,prev,q,color,.9); prev=q;
      }
    }
    ctx.restore();
  }
  function drawVectorDemo(canvasId,A,v,opts={}){
    const canvas=$(canvasId); if(!canvas) return;
    const {ctx,w,h}=setupCanvas(canvas,720,460); ctx.clearRect(0,0,w,h);
    const center={x:w/2,y:h/2+12}, unit=opts.unit||58;
    drawOriginalGrid(ctx,center,unit,3);
    drawTransformedGrid(ctx,A,center,unit,2);
    drawAxes(ctx,center,unit,{w,h,lim:3});
    const p0=mapPoint({x:0,y:0},center,unit), pv=mapPoint(v,center,unit), Av=mul(A,v), pAv=mapPoint(Av,center,unit);
    arrow(ctx,p0,pv,navy,3,false); label(ctx,'u',{x:pv.x+14,y:pv.y-12},navy,18,'left');
    arrow(ctx,p0,pAv,gold,3,true); label(ctx,'Au',{x:pAv.x+12,y:pAv.y-10},gold,18,'left');
    dot(ctx,pv,4,navy); dot(ctx,pAv,4,gold);
  }
  function drawSpectrum(canvasId,E){
    const canvas=$(canvasId); if(!canvas) return;
    const {ctx,w,h}=setupCanvas(canvas,720,180); ctx.clearRect(0,0,w,h);
    if(E.real){
      const vals=E.values, min=Math.min(-3,...vals)-.5, max=Math.max(3,...vals)+.5;
      const y=h/2, x0=60, x1=w-60;
      arrow(ctx,{x:x0,y},{x:x1,y},navy,2,false);
      for(let t=Math.ceil(min);t<=Math.floor(max);t++){
        const x=x0+(t-min)/(max-min)*(x1-x0);
        line(ctx,{x,y:y-8},{x,y:y+8},navy,1);
        label(ctx,String(t),{x,y:y+24},'#334',13);
      }
      vals.forEach((v,i)=>{
        const x=x0+(v-min)/(max-min)*(x1-x0);
        dot(ctx,{x,y},8,gold); label(ctx,'λ'+(i+1)+' = '+fmt(v,3),{x,y:y-34},gold,17);
      });
      label(ctx,'real spectral line',{x:w/2,y:h-18},gray,13);
    }else{
      const center={x:w/2,y:h/2}, unit=55;
      drawAxes(ctx,center,unit,{w,h,lim:2});
      E.values.forEach((z,i)=>{
        const p=mapPoint({x:z.re,y:z.im},center,unit); dot(ctx,p,8,gold); label(ctx,'λ'+(i+1),{x:p.x+18,y:p.y-12},gold,16,'left');
      });
      label(ctx,'complex spectral plane',{x:w/2,y:h-18},gray,13);
    }
  }
  function drawEigenDirections(ctx,A,center,unit){
    const E=eig2(A); if(!E.real) return;
    E.values.forEach((lam,i)=>{
      let vx,vy;
      const m11=A.a-lam, m12=A.b, m21=A.c, m22=A.d-lam;
      if(Math.abs(m12)>Math.abs(m21)){ vx=1; vy= -m11/(m12 || 1); }
      else { vy=1; vx= -m22/(m21 || 1); }
      const n=Math.hypot(vx,vy)||1; vx/=n; vy/=n;
      const p1=mapPoint({x:-3*vx,y:-3*vy},center,unit), p2=mapPoint({x:3*vx,y:3*vy},center,unit);
      line(ctx,p1,p2,i?red:gold,2,true); label(ctx,'eigenline λ='+fmt(lam,2),{x:p2.x,y:p2.y-10},i?red:gold,13,'left');
    });
  }
  function inv2(S){ const D=det(S); return {a:S.d/D,b:-S.b/D,c:-S.c/D,d:S.a/D}; }
  function mmul(A,B){ return {a:A.a*B.a+A.b*B.c,b:A.a*B.b+A.b*B.d,c:A.c*B.a+A.d*B.c,d:A.c*B.b+A.d*B.d}; }

  window.BC = { $, fmt, matrix, mul, det, tr, eig2, eigText, setText, matText, syncNumberRange, bindRange, getMatrix, setupCanvas, drawAxes, drawOriginalGrid, drawTransformedGrid, drawVectorDemo, drawSpectrum, drawEigenDirections, mapPoint, arrow, line, dot, label, inv2, mmul };

  window.initMainDemo = function(){
    ['a','b','c','d','vx','vy'].forEach(id=>syncNumberRange(id,update));
    ['preset1','preset2','preset3','preset4'].forEach(id=>{ const el=$(id); if(el) el.addEventListener('click',()=>{
      const presets={preset1:[2,1,0,3,1,1], preset2:[1,1,0,1,1,1], preset3:[0.3,0,0,1,1,1], preset4:[0,-1,1,0,1,0]};
      const p=presets[id]; ['a','b','c','d','vx','vy'].forEach((k,i)=>{ $(k).value=p[i]; $(k+'n').value=p[i]; }); update();
    });});
    function update(){
      const A=getMatrix(), v={x:+$('vx').value,y:+$('vy').value}, Av=mul(A,v), E=eig2(A);
      drawVectorDemo('mainCanvas',A,v,{unit:52}); drawSpectrum('spectrumCanvas',E);
      setText('matrixVal', matText(A)); setText('vectorVal','u = ('+fmt(v.x,2)+', '+fmt(v.y,2)+')');
      setText('imageVal','Au = ('+fmt(Av.x,2)+', '+fmt(Av.y,2)+')');
      setText('traceDetVal','tr = '+fmt(tr(A),2)+', det = '+fmt(det(A),2));
      setText('spectrumVal','σ(A) = '+eigText(E));
      const cross = v.x*Av.y - v.y*Av.x, norm=Math.hypot(v.x,v.y)*Math.hypot(Av.x,Av.y);
      let eigen = norm>1e-9 ? Math.abs(cross)/norm : 99;
      setText('eigenCheck', eigen<0.035 ? 'u is nearly an eigenvector direction' : 'u changes direction');
    }
    window.addEventListener('resize',update); update();
  };

  window.initDiagonalDemo = function(){
    ['l1','l2'].forEach(id=>syncNumberRange(id,update));
    function update(){
      const l1=+$('l1').value,l2=+$('l2').value,A=matrix(l1,0,0,l2); const E=eig2(A);
      drawVectorDemo('diagCanvas',A,{x:1,y:1},{unit:56}); drawSpectrum('diagSpectrum',E);
      setText('diagMatrix','diag('+fmt(l1,2)+', '+fmt(l2,2)+')'); setText('diagSpectrumText','σ(A) = { '+fmt(l1,2)+', '+fmt(l2,2)+' }');
      setText('diagComment', Math.abs(l1)<0.08 || Math.abs(l2)<0.08 ? 'Near-zero preview: one spectral point is close to 0.' : 'The diagonal entries are the eigenvalues.');
    }
    window.addEventListener('resize',update); update();
  };

  window.initBasisDemo = function(){
    ['theta','scale'].forEach(id=>syncNumberRange(id,update));
    function update(){
      const theta=+$('theta').value*Math.PI/180, s=+$('scale').value;
      const A=matrix(2,1,0,3);
      const S=matrix(Math.cos(theta), -s*Math.sin(theta), Math.sin(theta), s*Math.cos(theta));
      const Ap=mmul(mmul(inv2(S),A),S); const E=eig2(A), Ep=eig2(Ap);
      drawBasisCanvas('basisCanvas',A,S,Ap);
      setText('basisA', matText(A)); setText('basisS', matText(S)); setText('basisAp', matText(Ap));
      setText('basisSpec','σ(A) = '+eigText(E)+'; σ(A′) = '+eigText(Ep));
    }
    function drawBasisCanvas(id,A,S,Ap){
      const canvas=$(id); const {ctx,w,h}=setupCanvas(canvas,820,500); ctx.clearRect(0,0,w,h);
      const left={x:220,y:250}, right={x:610,y:250}, unit=48;
      label(ctx,'basis (e1,e2)',{x:left.x,y:28},navy,18); label(ctx,'basis (f1,f2)',{x:right.x,y:28},navy,18);
      drawAxes(ctx,left,unit,{w:410,h,lim:3}); drawOriginalGrid(ctx,left,unit,2); drawTransformedGrid(ctx,A,left,unit,2,blue);
      arrow(ctx,mapPoint({x:0,y:0},left,unit),mapPoint({x:1,y:0},left,unit),navy,3); label(ctx,'e1',mapPoint({x:1.25,y:-.2},left,unit),navy,16);
      arrow(ctx,mapPoint({x:0,y:0},left,unit),mapPoint({x:0,y:1},left,unit),navy,3); label(ctx,'e2',mapPoint({x:-.25,y:1.25},left,unit),navy,16);
      ctx.save(); ctx.translate(390,0); drawAxes(ctx,{x:220,y:250},unit,{w:410,h,lim:3}); ctx.restore();
      // Right: draw same A transformed grid and f basis vectors
      drawOriginalGrid(ctx,right,unit,2,'#f1f4f8'); drawTransformedGrid(ctx,A,right,unit,2,blue);
      const f1={x:S.a,y:S.c}, f2={x:S.b,y:S.d};
      arrow(ctx,mapPoint({x:0,y:0},right,unit),mapPoint(f1,right,unit),navy,3); label(ctx,'f1',mapPoint({x:f1.x*1.15,y:f1.y*1.15},right,unit),navy,16,'left');
      arrow(ctx,mapPoint({x:0,y:0},right,unit),mapPoint(f2,right,unit),navy,3); label(ctx,'f2',mapPoint({x:f2.x*1.15,y:f2.y*1.15},right,unit),navy,16,'left');
      arrow(ctx,{x:380,y:250},{x:440,y:250},gold,4); label(ctx,'A′ = S⁻¹AS',{x:410,y:212},gold,18);
      label(ctx,'same operator geometry; different coordinates',{x:w/2,y:h-26},gray,15);
    }
    window.addEventListener('resize',update); update();
  };

  window.initEigenDemo = function(){
    ['ea','eb','ec','ed','angle'].forEach(id=>syncNumberRange(id,update));
    function update(){
      const A=getMatrix(['ea','eb','ec','ed']); const ang=+$('angle').value*Math.PI/180; const u={x:Math.cos(ang),y:Math.sin(ang)}; const Au=mul(A,u); const E=eig2(A);
      const canvas=$('eigenCanvas'); const {ctx,w,h}=setupCanvas(canvas,760,520); ctx.clearRect(0,0,w,h);
      const center={x:w/2,y:h/2+20}, unit=86; drawAxes(ctx,center,unit,{w,h,lim:3}); drawEigenDirections(ctx,A,center,unit);
      // draw several directions
      for(let deg=-140; deg<=150; deg+=35){
        const r=deg*Math.PI/180, v={x:Math.cos(r),y:Math.sin(r)}, Av=mul(A,v);
        arrow(ctx,mapPoint({x:0,y:0},center,unit),mapPoint({x:v.x*.75,y:v.y*.75},center,unit),navy,1.6,false);
        arrow(ctx,mapPoint({x:0,y:0},center,unit),mapPoint({x:Av.x*.45,y:Av.y*.45},center,unit),gray,1.6,true);
      }
      arrow(ctx,mapPoint({x:0,y:0},center,unit),mapPoint({x:u.x*1.15,y:u.y*1.15},center,unit),red,4,false); label(ctx,'u',mapPoint({x:u.x*1.35,y:u.y*1.35},center,unit),red,19,'left');
      arrow(ctx,mapPoint({x:0,y:0},center,unit),mapPoint({x:Au.x*.6,y:Au.y*.6},center,unit),gold,4,true); label(ctx,'Au',mapPoint({x:Au.x*.68,y:Au.y*.68},center,unit),gold,19,'left');
      const cross=u.x*Au.y-u.y*Au.x, n=Math.hypot(Au.x,Au.y); const ratio=n?Math.abs(cross)/n:99;
      setText('eigenStatus', ratio<0.035 ? 'Au is almost collinear with u: eigenvector direction.' : 'Au is not collinear with u: direction changes.');
      setText('eigenMatrix', matText(A)); setText('eigenSpectrum', 'σ(A) = '+eigText(E));
    }
    window.addEventListener('resize',update); update();
  };

  window.initSameSpectrumDemo = function(){
    function update(){
      const I=matrix(1,0,0,1), J=matrix(1,1,0,1);
      drawCompareCanvas('sameCanvas',I,J); setText('sameSpec','σ(I) = σ(J) = { 1 }');
    }
    function drawCompareCanvas(id,A,B){
      const canvas=$(id); const {ctx,w,h}=setupCanvas(canvas,820,430); ctx.clearRect(0,0,w,h);
      const left={x:220,y:220}, right={x:610,y:220}, unit=55;
      label(ctx,'Identity operator I',{x:left.x,y:34},navy,20); label(ctx,'Jordan/shear operator J',{x:right.x,y:34},navy,20);
      drawAxes(ctx,left,unit,{w:410,h,lim:2}); drawOriginalGrid(ctx,left,unit,2); drawTransformedGrid(ctx,A,left,unit,2,gold);
      ctx.save(); ctx.translate(390,0); drawAxes(ctx,{x:220,y:220},unit,{w:410,h,lim:2}); ctx.restore(); drawOriginalGrid(ctx,right,unit,2); drawTransformedGrid(ctx,B,right,unit,2,blue);
      label(ctx,'same spectrum, different action',{x:w/2,y:h-28},red,18);
    }
    window.addEventListener('resize',update); update();
  };

  window.initNearZeroDemo = function(){
    ['eps'].forEach(id=>syncNumberRange(id,update));
    function update(){
      const e=+$('eps').value, A=matrix(e,0,0,1), E=eig2(A);
      drawVectorDemo('nzCanvas',A,{x:1,y:1},{unit:58}); drawSpectrum('nzSpectrum',E);
      setText('nzMatrix','diag('+fmt(e,4)+', 1)'); setText('nzSpec','σ(Aε) = { '+fmt(e,4)+', 1 }');
      if(Math.abs(e)<1e-6) setText('nzComment','Exact zero mode preview: 0 ∈ σ(Aε).');
      else if(Math.abs(e)<.12) setText('nzComment','Near-zero preview: |ε| ≪ 1, but ε is still nonzero.');
      else setText('nzComment','Move ε toward 0 to see a spectral point approach zero.');
    }
    window.addEventListener('resize',update); update();
  };
})();
