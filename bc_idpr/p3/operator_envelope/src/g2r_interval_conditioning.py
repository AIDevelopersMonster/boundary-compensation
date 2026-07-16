#!/usr/bin/env python3
import argparse,itertools,json,time
from pathlib import Path
from flint import arb, ctx

ORDER=50
PRIMARY_PREC=192
CONTROL_PREC=256
PREREG='535de38c4f0ed4393747510b7c15ccd6dd1fd977'

def zero(n): return [arb(0) for _ in range(n+1)]
def const(x,n): a=zero(n);a[0]=arb(x);return a
def add(a,b): return [x+y for x,y in zip(a,b)]
def mul(a,b):
 n=len(a)-1
 return [sum((a[k]*b[i-k] for k in range(i+1)),arb(0)) for i in range(n+1)]
def inv(a):
 n=len(a)-1;b=zero(n);b[0]=1/a[0]
 for i in range(1,n+1): b[i]=-sum((a[k]*b[i-k] for k in range(1,i+1)),arb(0))/a[0]
 return b
def div(a,b): return mul(a,inv(b))
def sqrtj(a):
 n=len(a)-1;b=zero(n);b[0]=a[0].sqrt()
 for i in range(1,n+1): b[i]=(a[i]-sum((b[k]*b[i-k] for k in range(1,i)),arb(0)))/(2*b[0])
 return b
def sinj(m,t,n):
 out=[];fact=arb(1);mpow=arb(1);s=(m*t).sin();c=(m*t).cos();cyc=(s,c,-s,-c)
 for r in range(n+1):
  if r: fact*=r;mpow*=m
  out.append(mpow*cyc[r%4]/fact)
 return out
def qnjet(k,t,n): return zero(n) if k==0 else div(sinj(k,t,n),sinj(1,t,n))
def qfjet(k,t,n,cache):
 key=(k,n)
 if key in cache:return cache[key]
 if k<0:raise ValueError(k)
 a=const(1,n)
 for r in range(1,k+1):a=mul(a,qnjet(r,t,n))
 cache[key]=a;return a
def hs(*a):
 s=sum(a)
 if s%2:raise ValueError(a)
 return s//2
def delt(a,b,d,t,n,cache):
 u,v,w=hs(a,b,-d),hs(a,-b,d),hs(-a,b,d);s=hs(a,b,d)+1
 if min(u,v,w)<0:return zero(n)
 return sqrtj(div(mul(mul(qfjet(u,t,n,cache),qfjet(v,t,n,cache)),qfjet(w,t,n,cache)),qfjet(s,t,n,cache)))
def q6(a,b,e,d,f,g,t,n,cache):
 p=const(1,n)
 for x in ((a,b,e),(a,f,g),(d,b,g),(d,f,e)):p=mul(p,delt(*x,t,n,cache))
 L=(hs(a,b,e),hs(a,f,g),hs(d,b,g),hs(d,f,e));U=(hs(a,b,d,f),hs(a,d,e,g),hs(b,f,e,g));S=zero(n)
 for r in range(max(L),min(U)+1):
  q=[((-1)**r)*x for x in qfjet(r+1,t,n,cache)]
  for x in tuple(r-y for y in L)+tuple(y-r for y in U):q=div(q,qfjet(x,t,n,cache))
  S=add(S,q)
 return mul(p,S)
def pair(a,b):return range(abs(a-b),a+b+1,2)
def common(a,b,c,d):return sorted(set(pair(a,b))&set(pair(c,d)))
def chans(J):a,b,c,d=J;return common(a,b,c,d),common(b,c,a,d)
def candidate(J):
 if sum(J)%2:return False
 E,F=chans(J)
 if len(E)!=2 or len(F)!=2:return False
 try:
  for e in E:
   for g in F:
    a,b,d,f=J;L=(hs(a,b,e),hs(a,f,g),hs(d,b,g),hs(d,f,e));U=(hs(a,b,d,f),hs(a,d,e,g),hs(b,f,e,g))
    if max(L)>min(U):return False
    for r in range(max(L),min(U)+1):
     args=tuple(r-y for y in L)+tuple(y-r for y in U)
     if min(args)<0 or r+1>10:return False
  return True
 except ValueError:return False
def carriers():return [J for J in itertools.product(range(1,7),repeat=4) if candidate(J)]
def raw(J,t,n):
 a,b,d,f=J;E,F=chans(J);ph=(-1)**hs(*J);C=[[[arb(0) for _ in range(2)] for _ in range(2)] for _ in range(n+1)];cache={}
 for i,e in enumerate(E):
  for j,g in enumerate(F):
   x=mul(sqrtj(mul(qnjet(e+1,t,n),qnjet(g+1,t,n))),q6(a,b,e,d,f,g,t,n,cache))
   if ph<0:x=[-v for v in x]
   for r,v in enumerate(x):C[r][i][j]=v
 return C
def matmulT(A,B):return [[sum((A[i][k]*B[j][k] for k in range(2)),arb(0)) for j in range(2)] for i in range(2)]
def omega_coeffs(J,t,N):
 F=raw(J,t,N+1);w=[]
 for r in range(N+1):
  q=[[arb(0),arb(0)],[arb(0),arb(0)]]
  for k in range(r+1):
   p=matmulT(F[k+1],F[r-k])
   for i in range(2):
    for j in range(2):q[i][j]+=(k+1)*p[i][j]
  w.append(q[1][0])
 return w
def delta_n(n,t):
 rem=n%12
 return min(rem,12-rem)*arb.pi()/12
def q_b(n,r,t):
 dn=delta_n(n,t);d1=delta_n(1,t)
 lo=(dn-n*r).sin()/r.cosh();hi=(n*r).cosh()/(d1-r).sin()
 b1=n*(n*r).cosh()/(dn-n*r).sin()+r.cosh()/(d1-r).sin()
 b2=n*n/((dn-n*r).sin()**2)+1/((d1-r).sin()**2)
 return lo,hi,b1,b2
def make_bounds(r,t):
 qb={n:q_b(n,r,t) for n in range(1,11)};fac={0:(arb(1),arb(1),arb(0),arb(0))}
 for n in range(1,11):
  lo=arb(1);hi=arb(1);b1=arb(0);b2=arb(0)
  for k in range(1,n+1):qlo,qhi,q1,q2=qb[k];lo*=qlo;hi*=qhi;b1+=q1;b2+=q2
  fac[n]=(lo,hi,b1,b2)
 return qb,fac
def delta_bound(a,b,c,qb,fac):
 u,v,w=hs(a,b,-c),hs(a,-b,c),hs(-a,b,c);s=hs(a,b,c)+1
 return (fac[u][1]*fac[v][1]*fac[w][1]/fac[s][0]).sqrt(),(fac[u][2]+fac[v][2]+fac[w][2]+fac[s][2])/2,(fac[u][3]+fac[v][3]+fac[w][3]+fac[s][3])/2
def q6_bounds(a,b,e,d,f,g,qb,fac):
 ds=[delta_bound(*x,qb,fac) for x in ((a,b,e),(a,f,g),(d,b,g),(d,f,e))];P=arb(1);P1=arb(0);P2=arb(0)
 for x in ds:P*=x[0];P1+=x[1];P2+=x[2]
 L=(hs(a,b,e),hs(a,f,g),hs(d,b,g),hs(d,f,e));U=(hs(a,b,d,f),hs(a,d,e,g),hs(b,f,e,g));S0=S1=S2=arb(0)
 for zz in range(max(L),min(U)+1):
  args=tuple(zz-y for y in L)+tuple(y-zz for y in U);ut=fac[zz+1][1]
  for x in args:ut/=fac[x][0]
  b1=fac[zz+1][2]+sum((fac[x][2] for x in args),arb(0));b2=fac[zz+1][3]+sum((fac[x][3] for x in args),arb(0));S0+=ut;S1+=ut*b1;S2+=ut*(b1*b1+b2)
 return P*S0,P*(P1*S0+S1),P*((P1*P1+P2)*S0+2*P1*S1+S2)
def omega_majorant(J,qb,fac):
 a,b,d,f=J;E,F=chans(J);B0=[[arb(0),arb(0)],[arb(0),arb(0)]];B1=[[arb(0),arb(0)],[arb(0),arb(0)]]
 for i,e in enumerate(E):
  for j,g in enumerate(F):
   q0,q1,_=q6_bounds(a,b,e,d,f,g,qb,fac);amp=(qb[e+1][1]*qb[g+1][1]).sqrt();a1=(qb[e+1][2]+qb[g+1][2])/2;B0[i][j]=amp*q0;B1[i][j]=amp*(a1*q0+q1)
 return sum((B1[1][j]*B0[0][j] for j in range(2)),arb(0))
def lower_float(x):return float(x.lower())
def upper_float(x):return float(x.upper())
def worker(args):
 prec,J=args;ctx.prec=prec;t=arb.pi()/12;Rout=arb.pi()/120;Rcert=arb.pi()/1200;q=Rcert/Rout;qb,fac=make_bounds(Rout,t);w=omega_coeffs(J,t,ORDER);M=omega_majorant(J,qb,fac)
 lower=w[0].abs_lower();poly=sum((w[k].abs_upper()*(Rcert**k) for k in range(1,ORDER+1)),arb(0));tail=M.abs_upper()*(q**(ORDER+1))/(1-q);L=lower-poly-tail
 return lower_float(L),J,lower_float(lower),upper_float(poly),upper_float(tail),upper_float(M),min(lower_float(qb[n][0]) for n in qb)
def family_representatives():
 O=carriers();reps={}
 for J in O:reps.setdefault(tuple(sorted(J)),J)
 return O,reps
def run(prec):
 O,reps=family_representatives();rows=[worker((prec,J)) for J in reps.values()];rows.sort()
 return {'precision_bits':prec,'ordered_carriers_covered_by_symmetry':len(O),'canonical_family_representatives_evaluated':len(rows),'representation_families':len(reps),'minimum_lower_bound':rows[0][0],'worst_carrier':list(rows[0][1]),'worst_components':{'omega0_abs_lower':rows[0][2],'taylor_variation_upper':rows[0][3],'cauchy_tail_upper':rows[0][4],'outer_majorant_upper':rows[0][5]},'all_positive':all(x[0]>0 for x in rows),'outer_disk_minimum_q_number_lower_bound':min(x[6] for x in rows)}
def build():
 start=time.time();p=run(PRIMARY_PREC);c=run(CONTROL_PREC);ok=p['ordered_carriers_covered_by_symmetry']==283 and p['representation_families']==24 and p['all_positive'] and c['all_positive'] and p['worst_carrier']==c['worst_carrier']
 return {'schema_version':'1.0','contract':'BC-IDPR-P3-B-G2-R','status':'RIGOROUS_ARB_UNIFORM_CONDITIONING_CERTIFIED' if ok else 'RIGOROUS_ARB_UNIFORM_CONDITIONING_NOT_CERTIFIED','preregistration_commit':PREREG,'arithmetic':{'backend':'python-flint Arb','primary_precision_bits':PRIMARY_PREC,'control_precision_bits':CONTROL_PREC,'outward_rounding':True},'proof_family':{'outer_radius':'pi/120','confirmatory_radius':'pi/1200','taylor_order':ORDER,'symmetry_reduction':'tetrahedral q-6j symmetry induces constant signed row/column permutations and optional transpose, preserving absolute angular speed and its zero set'},'primary_run':p,'control_run':c,'decision':{'float64_blocker':'CLOSED' if ok else 'OPEN','uniform_nonvanishing_theorem':'RIGOROUSLY_CERTIFIED' if ok else 'NOT_CERTIFIED','holomorphic_logarithm_on_common_disk':'CLOSED' if ok else 'OPEN','G2_overall':'PASS' if ok else 'BLOCKED'},'runtime_seconds':time.time()-start,'evidence_rule':'No statement from the Gemini advisory report is used as evidence.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();r=build();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'minimum':r['primary_run']['minimum_lower_bound'],'runtime':r['runtime_seconds']}))
if __name__=='__main__':main()
