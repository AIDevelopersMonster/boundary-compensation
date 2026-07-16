import math,itertools,functools
import numpy as np
A=math.pi/12
CRIT=10

def z(n): return np.zeros(n+1,float)
def c(x,n): a=z(n);a[0]=x;return a
def mul(a,b):
 n=len(a)-1;return np.array([math.fsum(a[k]*b[i-k] for k in range(i+1)) for i in range(n+1)])
def inv(a):
 n=len(a)-1;b=z(n);b[0]=1/a[0]
 for i in range(1,n+1):b[i]=-math.fsum(a[k]*b[i-k] for k in range(1,i+1))/a[0]
 return b
def div(a,b):return mul(a,inv(b))
def sqr(a):
 n=len(a)-1;b=z(n);b[0]=math.sqrt(a[0])
 for i in range(1,n+1):b[i]=(a[i]-math.fsum(b[k]*b[i-k] for k in range(1,i)))/(2*b[0])
 return b
def sinj(m,t,n):return np.array([m**r*math.sin(m*t+r*math.pi/2)/math.factorial(r) for r in range(n+1)])
@functools.lru_cache(None)
def qnt(k,t,n):return tuple(z(n) if k==0 else div(sinj(k,t,n),sinj(1,t,n)))
def qnjet(k,t,n):return np.array(qnt(k,round(t,15),n))
@functools.lru_cache(None)
def qft(k,t,n):
 if k<0:raise ValueError(k)
 a=c(1.,n)
 for r in range(1,k+1):a=mul(a,qnjet(r,t,n))
 return tuple(a)
def qfjet(k,t,n):return np.array(qft(k,round(t,15),n))
def hs(*a):
 s=sum(a)
 if s%2:raise ValueError(a)
 return s//2
def delt(a,b,d,t,n):
 u,v,w=hs(a,b,-d),hs(a,-b,d),hs(-a,b,d);s=hs(a,b,d)+1
 if min(u,v,w)<0:return z(n)
 return sqr(div(mul(mul(qfjet(u,t,n),qfjet(v,t,n)),qfjet(w,t,n)),qfjet(s,t,n)))
def q6(a,b,e,d,f,g,t,n):
 p=c(1.,n)
 for x in ((a,b,e),(a,f,g),(d,b,g),(d,f,e)):p=mul(p,delt(*x,t,n))
 L=(hs(a,b,e),hs(a,f,g),hs(d,b,g),hs(d,f,e));U=(hs(a,b,d,f),hs(a,d,e,g),hs(b,f,e,g));S=z(n)
 for r in range(max(L),min(U)+1):
  q=(-1)**r*qfjet(r+1,t,n)
  for x in tuple(r-y for y in L)+tuple(y-r for y in U):q=div(q,qfjet(x,t,n))
  S+=q
 return mul(p,S)
def pair(a,b):return range(abs(a-b),a+b+1,2)
def common(a,b,c,d):return sorted(set(pair(a,b))&set(pair(c,d)))
def chans(J):a,b,c,d=J;return common(a,b,c,d),common(b,c,a,d)
def zm(J):
 a,b,c,d=J;E,F=chans(J)
 return max(min(hs(a,b,c,d),hs(a,c,e,f),hs(b,d,e,f))+1 for e in E for f in F)
def raw(J,t,n):
 a,b,d,f=J;E,F=chans(J);ph=(-1)**hs(*J);C=[np.zeros((2,2)) for _ in range(n+1)]
 for i,e in enumerate(E):
  for j,g in enumerate(F):
   x=ph*mul(sqr(mul(qnjet(e+1,t,n),qnjet(g+1,t,n))),q6(a,b,e,d,f,g,t,n))
   for r,v in enumerate(x):C[r][i,j]=v
 return C
def gauge(J):
 M=raw(J,A,0)[0];G=np.eye(2)
 if np.linalg.det(M)<0:G=np.diag([1.,-1.])@G
 if (G@M)[0,0]<0:G=-G
 return G
def fj(J,t,n,G=None):
 G=gauge(J) if G is None else G
 return [G@x for x in raw(J,t,n)]
def omega_anchor(J):
 F=fj(J,A,1); return float((F[1]@F[0].T)[1,0])
def fam(J):return tuple(sorted(J))
def valid(m):
 O=[]
 for J in itertools.product(range(1,m+1),repeat=4):
  if sum(J)%2:continue
  E,F=chans(J)
  if len(E)!=2 or len(F)!=2 or zm(J)>12:continue
  try:
   om=omega_anchor(J);M=fj(J,A,0)[0]
   if np.linalg.norm(M.T@M-np.eye(2))<1e-10 and abs(om)>1e-8:O.append(J)
  except Exception:pass
 return O

def delta_n(n):
 x=(n*A)%math.pi
 return min(x,math.pi-x)
def q_b(n,r):
 lo=math.sin(delta_n(n)-n*r)/math.cosh(r)
 hi=math.cosh(n*r)/math.sin(delta_n(1)-r)
 b1=n*math.cosh(n*r)/math.sin(delta_n(n)-n*r)+math.cosh(r)/math.sin(delta_n(1)-r)
 b2=n*n/(math.sin(delta_n(n)-n*r)**2)+1/(math.sin(delta_n(1)-r)**2)
 return lo,hi,b1,b2
def make_bounds(r):
 qb={n:q_b(n,r) for n in range(1,CRIT+1)}
 fac={0:(1.,1.,0.,0.)}
 for n in range(1,CRIT+1):
  lo=hi=1.;b1=b2=0.
  for k in range(1,n+1):
   qlo,qhi,q1,q2=qb[k];lo*=qlo;hi*=qhi;b1+=q1;b2+=q2
  fac[n]=(lo,hi,b1,b2)
 return qb,fac
def delta_bound(a,b,c,r,qb,fac):
 u,v,w=hs(a,b,-c),hs(a,-b,c),hs(-a,b,c);s=hs(a,b,c)+1
 if min(u,v,w)<0:return (0,0,0)
 U=math.sqrt(fac[u][1]*fac[v][1]*fac[w][1]/fac[s][0])
 B1=.5*(fac[u][2]+fac[v][2]+fac[w][2]+fac[s][2])
 B2=.5*(fac[u][3]+fac[v][3]+fac[w][3]+fac[s][3])
 return U,B1,B2
def q6_bounds(a,b,e,d,f,g,r,qb,fac):
 ds=[delta_bound(*x,r,qb,fac) for x in ((a,b,e),(a,f,g),(d,b,g),(d,f,e))]
 P=math.prod(x[0] for x in ds);P1=sum(x[1] for x in ds);P2=sum(x[2] for x in ds)
 L=(hs(a,b,e),hs(a,f,g),hs(d,b,g),hs(d,f,e));U=(hs(a,b,d,f),hs(a,d,e,g),hs(b,f,e,g))
 S0=S1=S2=0.
 for zz in range(max(L),min(U)+1):
  args=tuple(zz-y for y in L)+tuple(y-zz for y in U)
  ut=fac[zz+1][1]
  for x in args:ut/=fac[x][0]
  b1=fac[zz+1][2]+sum(fac[x][2] for x in args)
  b2=fac[zz+1][3]+sum(fac[x][3] for x in args)
  S0+=ut;S1+=ut*b1;S2+=ut*(b1*b1+b2)
 Q0=P*S0
 Q1=P*(P1*S0+S1)
 Q2=P*((P1*P1+P2)*S0+2*P1*S1+S2)
 return Q0,Q1,Q2
def f_entry_bounds(J,r,qb,fac):
 a,b,d,f=J;E,F=chans(J);B0=np.zeros((2,2));B1=np.zeros((2,2));B2=np.zeros((2,2))
 for i,e in enumerate(E):
  for j,g in enumerate(F):
   q0,q1,q2=q6_bounds(a,b,e,d,f,g,r,qb,fac)
   amp=math.sqrt(qb[e+1][1]*qb[g+1][1])
   a1=.5*(qb[e+1][2]+qb[g+1][2]);a2=.5*(qb[e+1][3]+qb[g+1][3])
   B0[i,j]=amp*q0
   B1[i,j]=amp*(a1*q0+q1)
   B2[i,j]=amp*((a1*a1+a2)*q0+2*a1*q1+q2)
 return B0,B1,B2
def wall_radius():return .5*min(delta_n(n)/n for n in range(1,CRIT+1))
def omega_coeffs(J,N):
 F=fj(J,A,N+1);w=[]
 for r in range(N+1):
  Q=np.zeros((2,2))
  for k in range(r+1): Q+=(k+1)*F[k+1]@F[r-k].T
  w.append(float(Q[1,0]))
 return np.array(w)
def omega_bound(J,r,qb,fac):
 B0,B1,_=f_entry_bounds(J,r,qb,fac)
 return sum(B1[1,j]*B0[0,j] for j in range(2))
def radius_by_taylor(O,N,Rout):
 qb,fac=make_bounds(Rout);data=[]
 for J in O:
  w=omega_coeffs(J,N);M=omega_bound(J,Rout,qb,fac);data.append((J,w,M))
 def lower(r):
  q=r/Rout;worst=(1e300,None,None)
  for J,w,M in data:
   poly=sum(abs(w[k])*r**k for k in range(1,N+1));tail=M*q**(N+1)/(1-q);lo=abs(w[0])-poly-tail
   if lo<worst[0]:worst=(lo,J,(abs(w[0]),poly,tail,M))
  return worst
 lo=0.;hi=Rout*.999
 for _ in range(80):
  mid=(lo+hi)/2
  if lower(mid)[0]>0:lo=mid
  else:hi=mid
 return lo,lower(lo),data

ORDER=50
CONFIRMATORY_RATIO=0.1
PREREGISTRATION_COMMIT='a6148e37a3386bc4d6c65e168f919977de38317e'
def build():
 O=valid(6);R=wall_radius();r_ext,w_ext,data=radius_by_taylor(O,ORDER,R);r=CONFIRMATORY_RATIO*R
 def lower_at(rr):
  q=rr/R;worst=(1e300,None,None)
  for J,w,M in data:
   poly=sum(abs(w[k])*rr**k for k in range(1,ORDER+1));tail=M*q**(ORDER+1)/(1-q);lo=abs(w[0])-poly-tail
   if lo<worst[0]:worst=(lo,J,(abs(w[0]),poly,tail,M))
  return worst
 wc=lower_at(r);ql=min(q_b(n,r)[0] for n in range(1,CRIT+1))
 return {'schema_version':'1.0','contract':'BC-IDPR-P3-B-JET-RADIUS','status':'TAYLOR_CAUCHY_UNIFORM_RADIUS_CERTIFIED','preregistration_commit':PREREGISTRATION_COMMIT,'method':{'taylor_order':ORDER,'proof_family':'cancellation-preserving local omega jet plus analytic outer-disk Cauchy tail','fitted_parameter_count':0},'declared_class':{'ordered_carriers':len(O),'representation_families':len({fam(J) for J in O})},'radii':{'outer_wall_safe_radius':R,'confirmatory_certified_radius':r,'confirmatory_to_wall_ratio':CONFIRMATORY_RATIO,'proof_family_extremal_radius':r_ext,'extremal_to_wall_ratio':r_ext/R},'margins':{'confirmatory_minimum_abs_omega_lower_bound':wc[0],'confirmatory_worst_carrier':list(wc[1]),'proof_family_extremal_margin':w_ext[0],'minimum_q_number_lower_bound_at_confirmatory_radius':ql},'decision':{'uniform_radius_optimized_within_frozen_proof_family':'CLOSED','absolute_maximal_radius':'OPEN','preprint_mathematical_core':'READY','preprint_packaging':'OPEN'},'evidence_rule':'No statement from the Gemini advisory report is used as evidence.'}
def main():
 import argparse,json
 from pathlib import Path
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=build();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'radius':r['radii']['confirmatory_certified_radius']}))
if __name__=='__main__':main()
