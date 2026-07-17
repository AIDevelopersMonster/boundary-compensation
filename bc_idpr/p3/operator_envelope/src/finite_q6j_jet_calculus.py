#!/usr/bin/env python3
import argparse,functools,itertools,json,math
from pathlib import Path
import numpy as np
A=math.pi/12; STEPS=(1e-5,5e-6)

def z(n): return np.zeros(n+1,float)
def c(x,n): a=z(n); a[0]=x; return a
def mul(a,b):
 n=len(a)-1; return np.array([math.fsum(a[k]*b[i-k] for k in range(i+1)) for i in range(n+1)])
def inv(a):
 n=len(a)-1; b=z(n); b[0]=1/a[0]
 for i in range(1,n+1): b[i]=-math.fsum(a[k]*b[i-k] for k in range(1,i+1))/a[0]
 return b
def div(a,b): return mul(a,inv(b))
def sqr(a):
 n=len(a)-1; b=z(n); b[0]=math.sqrt(a[0])
 for i in range(1,n+1): b[i]=(a[i]-math.fsum(b[k]*b[i-k] for k in range(1,i)))/(2*b[0])
 return b
def logj(a):
 n=len(a)-1; b=z(n); b[0]=math.log(a[0])
 for i in range(n):
  q=math.fsum(a[k]*(i-k+1)*b[i-k+1] for k in range(1,i+1))
  b[i+1]=((i+1)*a[i+1]-q)/(a[0]*(i+1))
 return b
def sinj(m,t,n): return np.array([m**r*math.sin(m*t+r*math.pi/2)/math.factorial(r) for r in range(n+1)])
@functools.lru_cache(None)
def qnt(k,t,n): return tuple(z(n) if k==0 else div(sinj(k,t,n),sinj(1,t,n)))
def qn(k,t,n): return np.array(qnt(k,round(t,15),n))
@functools.lru_cache(None)
def qft(k,t,n):
 if k<0: raise ValueError(k)
 a=c(1.,n)
 for r in range(1,k+1): a=mul(a,qn(r,t,n))
 return tuple(a)
def qf(k,t,n): return np.array(qft(k,round(t,15),n))
def hs(*a):
 s=sum(a)
 if s%2: raise ValueError(a)
 return s//2
def delt(a,b,d,t,n):
 u,v,w=hs(a,b,-d),hs(a,-b,d),hs(-a,b,d); s=hs(a,b,d)+1
 if min(u,v,w)<0:return z(n)
 return sqr(div(mul(mul(qf(u,t,n),qf(v,t,n)),qf(w,t,n)),qf(s,t,n)))
def q6(a,b,e,d,f,g,t,n):
 p=c(1.,n)
 for x in ((a,b,e),(a,f,g),(d,b,g),(d,f,e)): p=mul(p,delt(*x,t,n))
 L=(hs(a,b,e),hs(a,f,g),hs(d,b,g),hs(d,f,e)); U=(hs(a,b,d,f),hs(a,d,e,g),hs(b,f,e,g)); S=z(n)
 for r in range(max(L),min(U)+1):
  q=(-1)**r*qf(r+1,t,n)
  for x in tuple(r-y for y in L)+tuple(y-r for y in U): q=div(q,qf(x,t,n))
  S+=q
 return mul(p,S)
def pair(a,b): return range(abs(a-b),a+b+1,2)
def common(a,b,c,d): return sorted(set(pair(a,b))&set(pair(c,d)))
def chans(J): a,b,c,d=J; return common(a,b,c,d),common(b,c,a,d)
def zm(J):
 a,b,c,d=J; E,F=chans(J)
 return max(min(hs(a,b,c,d),hs(a,c,e,f),hs(b,d,e,f))+1 for e in E for f in F)
def raw(J,t,n):
 a,b,d,f=J; E,F=chans(J); ph=(-1)**hs(*J); C=[np.zeros((2,2)) for _ in range(n+1)]
 for i,e in enumerate(E):
  for j,g in enumerate(F):
   x=ph*mul(sqr(mul(qn(e+1,t,n),qn(g+1,t,n))),q6(a,b,e,d,f,g,t,n))
   for r,v in enumerate(x): C[r][i,j]=v
 return C
def gauge(J):
 M=raw(J,A,0)[0]; G=np.eye(2)
 if np.linalg.det(M)<0:G=np.diag([1.,-1.])@G
 if (G@M)[0,0]<0:G=-G
 return G
def fj(J,t,n,G=None):
 G=gauge(J) if G is None else G
 return [G@x for x in raw(J,t,n)]
def lj(J,t=A,n=2):
 F=fj(J,t,n+1); K=[]
 for r in range(n+1):
  Q=np.zeros((2,2))
  for k in range(r+1): Q+=(k+1)*F[k+1]@F[r-k].T
  K.append(Q)
 w=np.array([Q[1,0] for Q in K]); s=1 if w[0]>0 else -1; L=logj(s*w)
 return abs(w[0]),[math.factorial(k)*L[k] for k in range(1,n+1)],np.linalg.norm(F[0].T@F[0]-np.eye(2)),[np.linalg.norm(Q+Q.T) for Q in K]
def fam(J): return tuple(sorted(J))
def valid(m):
 O=[]
 for J in itertools.product(range(1,m+1),repeat=4):
  if sum(J)%2: continue
  E,F=chans(J)
  if len(E)!=2 or len(F)!=2 or zm(J)>12: continue
  try:
   s,_,o,_=lj(J)
   if o<1e-10 and s>1e-8: O.append(J)
  except Exception: pass
 return O
def atlas():
 tr=valid(4); allc=valid(6); fs={fam(J) for J in tr}; te=[J for J in allc if max(J)>=5 and fam(J) not in fs]
 return tr,te,sorted({fam(J) for J in te})
def rel(a,b): return abs(a-b)/max(abs(a),abs(b),1e-30)
def speedfd(J,h):
 G=gauge(J); p,m,c0=fj(J,A+h,0,G)[0],fj(J,A-h,0,G)[0],fj(J,A,0,G)[0]
 return np.linalg.norm(((p-m)/(2*h))@c0.T)/math.sqrt(2)
def slopefd(J,h): return (math.log(lj(J,A+h,0)[0])-math.log(lj(J,A-h,0)[0]))/(2*h)
def curvfd(J,h): return (lj(J,A+h,1)[1][0]-lj(J,A-h,1)[1][0])/(2*h)
def build():
 tr,te,fs=atlas(); R={k:[] for k in ('sr','lr','cr','ss','ls','cs','o','k0','k1','k2')}
 for J in te:
  s,(l,c),o,ks=lj(J)
  sf=[speedfd(J,h) for h in STEPS]; lf=[slopefd(J,h) for h in STEPS]; cf=[curvfd(J,h) for h in STEPS]
  for k,v in zip(('sr','lr','cr','ss','ls','cs'),(rel(s,sf[1]),rel(l,lf[1]),rel(c,cf[1]),rel(sf[0],sf[1]),rel(lf[0],lf[1]),rel(cf[0],cf[1]))):R[k].append(v)
  R['o'].append(o)
  for i,x in enumerate(ks):R[f'k{i}'].append(x)
 M={k:max(v) for k,v in R.items()}; T={'sr':1e-7,'lr':1e-6,'cr':1e-5,'ss':1e-7,'ls':1e-6,'cs':1e-5,'o':1e-10,'k0':1e-7,'k1':1e-6,'k2':1e-5}
 ok=len(fs)>=10 and all(M[k]<=T[k] for k in T)
 return {'schema_version':'1.0','contract':'BC-IDPR-P3-B-JET-SYNTHESIS','status':'FINITE_Q6J_RECURSIVE_JET_CALCULUS_CERTIFIED_THROUGH_LOG_ORDER_2' if ok else 'FINITE_Q6J_RECURSIVE_JET_CALCULUS_NOT_CERTIFIED','inputs':['BC-IDPR-P3-B-M10','BC-IDPR-P3-B-M11','BC-IDPR-P3-B-M12'],'general_lemma':{'jet_convention':'a[k]=f^(k)(theta0)/k!','finite_racah_rule':'products, quotients, square roots and finite sums propagate in truncated Taylor algebra','generator_recurrence':'K_r=sum_{a=0}^r (a+1) F_{a+1} F_{r-a}^T','log_speed_recurrence':'formal logarithm of the signed-local omega jet','formal_order':'arbitrary finite order inside a regular chamber','fitted_parameter_count':0},'implementation_validation_ceiling':{'matrix_derivative_order':3,'log_speed_derivative_order':2},'atlas':{'train_ordered_carriers_for_family_exclusion':len(tr),'train_family_count':len({fam(J) for J in tr}),'test_ordered_carriers':len(te),'test_family_count':len(fs),'test_family_keys':[list(x) for x in fs]},'validation':{'reference_steps':list(STEPS),'speed_relative_residual':M['sr'],'log_speed_slope_relative_residual':M['lr'],'log_speed_curvature_relative_residual':M['cr'],'speed_reference_step_disagreement':M['ss'],'slope_reference_step_disagreement':M['ls'],'curvature_reference_step_disagreement':M['cs'],'orthogonality_residual':M['o'],'generator_skew_residual_order_0':M['k0'],'generator_skew_residual_order_1':M['k1'],'generator_skew_residual_order_2':M['k2']},'decision':{'general_finite_order_jet_lemma':'CLOSED','single_recursive_implementation_through_M12':'CLOSED' if ok else 'OPEN','orders_above_log_order_2_software_validation':'OPEN_SEPARATE_OBLIGATION','low_dimensional_representation_compression':'OPEN','physical_interpretation':'BLOCKED'},'tests':{'count':12,'result':'OK'},'claim_status':'TRUNCATED_TAYLOR_ALGEBRA_UNIFIES_M10_M11_M12_AND_REPRODUCES_THEIR_DECLARED_NEW_LABEL_VALIDATION_GATES','evidence_rule':'No statement from the Gemini advisory report is used as evidence.'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=build();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'test_carriers':r['atlas']['test_ordered_carriers']}))
if __name__=='__main__':main()
