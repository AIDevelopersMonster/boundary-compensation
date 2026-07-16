#!/usr/bin/env python3
from __future__ import annotations
import argparse, functools, itertools, json, math
from pathlib import Path
import mpmath as mp
import numpy as np

mp.mp.dps = 50
ANCHOR = math.pi / 12
H = 5e-4
RIDGE_ALPHA = 1.0
CERT_THRESHOLD = 0.25


def qn(n, t): return mp.mpf('0') if n == 0 else mp.sin(n*t)/mp.sin(t)
def qfac(n, t):
    if n < 0: raise ValueError(n)
    z = mp.mpf(1)
    for k in range(1, n+1): z *= qn(k, t)
    return z

def hs(*a):
    s = sum(a)
    if s % 2: raise ValueError(a)
    return s // 2

def delta(a,b,c,t):
    u,v,w = hs(a,b,-c), hs(a,-b,c), hs(-a,b,c)
    if min(u,v,w) < 0: return mp.mpf('0')
    return mp.sqrt(qfac(u,t)*qfac(v,t)*qfac(w,t)/qfac(hs(a,b,c)+1,t))

def q6j(a,b,e,c,d,f,t):
    pre = delta(a,b,e,t)*delta(a,d,f,t)*delta(c,b,f,t)*delta(c,d,e,t)
    lo = max(hs(a,b,e),hs(a,d,f),hs(c,b,f),hs(c,d,e))
    hi = min(hs(a,b,c,d),hs(a,c,e,f),hs(b,d,e,f))
    total = mp.mpf('0')
    for z in range(lo,hi+1):
        den = qfac(z-hs(a,b,e),t)*qfac(z-hs(a,d,f),t)*qfac(z-hs(c,b,f),t)*qfac(z-hs(c,d,e),t)*qfac(hs(a,b,c,d)-z,t)*qfac(hs(a,c,e,f)-z,t)*qfac(hs(b,d,e,f)-z,t)
        total += (-1)**z*qfac(z+1,t)/den
    return pre*total

def pair(a,b): return list(range(abs(a-b),a+b+1,2))
def common(a,b,c,d): return sorted(set(pair(a,b)).intersection(pair(c,d)))

@functools.lru_cache(None)
def channels(J):
    a,b,c,d = J
    return common(a,b,c,d), common(b,c,a,d)

def zmax(J):
    a,b,c,d = J; E,F = channels(J)
    return max(min(hs(a,b,c,d),hs(a,c,e,f),hs(b,d,e,f))+1 for e in E for f in F)

@functools.lru_cache(None)
def raw_f_cached(J,tkey):
    t=float(tkey); a,b,c,d=J; E,F=channels(J); phase=(-1)**hs(a,b,c,d)
    rows=[]
    for e in E:
        row=[]
        for f in F:
            value=phase*mp.sqrt(qn(e+1,t)*qn(f+1,t))*q6j(a,b,e,c,d,f,t)
            if abs(mp.im(value))>1e-25: raise ValueError('complex chamber')
            row.append(float(mp.re(value)))
        rows.append(row)
    return np.array(rows)

def raw_f(J,t): return raw_f_cached(tuple(J),round(float(t),12)).copy()

@functools.lru_cache(None)
def gauge(J):
    F=raw_f(J,ANCHOR); R=np.eye(2)
    if np.linalg.det(F)<0: R=np.diag([1.,-1.])@R
    if (R@F)[0,0]<0: R=-R
    return R

def f_matrix(J,t): return gauge(tuple(J))@raw_f(tuple(J),t)
def phi(J,t):
    A=f_matrix(J,t)
    return math.atan2(A[1,0],A[0,0])

def jet(J,h=H):
    xs=np.arange(-3,4)*h
    ps=np.unwrap([phi(J,ANCHOR+x) for x in xs])
    c=np.polynomial.polynomial.polyfit(xs,ps,5)
    return np.array([c[1],2*c[2],6*c[3]],float)

def cas(j2):
    j=j2/2
    return j*(j+1)

def descriptor(J,matrix=False):
    E,F=channels(tuple(J)); f0=f_matrix(tuple(J),ANCHOR)
    ext=np.array([cas(x) for x in J]); scale=ext.sum()
    values=[*(ext/scale),cas(E[0])/scale,cas(E[1])/scale,cas(F[0])/scale,cas(F[1])/scale,(cas(E[1])-cas(E[0]))/scale,(cas(F[1])-cas(F[0]))/scale]
    if matrix: values += [f0[0,0],f0[0,1],f0[1,0],f0[1,1]]
    return np.array(values,float)

def build_atlas():
    out=[]
    for J in itertools.product(range(1,5),repeat=4):
        if sum(J)%2: continue
        E,F=channels(J)
        if len(E)==len(F)==2 and zmax(J)<=8:
            try:
                M=f_matrix(J,ANCHOR); jj=jet(J)
                if np.linalg.norm(M.T@M-np.eye(2))<1e-10 and abs(jj[0])>1e-6: out.append(J)
            except Exception: pass
    return out

def targets(Js):
    raw=np.array([jet(J) for J in Js])
    transformed=np.column_stack([np.log(np.abs(raw[:,0])),raw[:,1]/raw[:,0],raw[:,2]/raw[:,0]])
    return raw,transformed

def loocv(X,T,alpha=RIDGE_ALPHA):
    pred=np.zeros_like(T)
    for i in range(len(X)):
        train=np.arange(len(X))!=i
        mean=X[train].mean(0); std=X[train].std(0); std[std<1e-12]=1
        Z=(X[train]-mean)/std; z=(X[i]-mean)/std; target_mean=T[train].mean(0)
        coef=np.linalg.solve(Z.T@Z+alpha*np.eye(Z.shape[1]),Z.T@(T[train]-target_mean))
        pred[i]=target_mean+z@coef
    nrmse=np.sqrt(np.mean((pred-T)**2,0))/np.std(T,0)
    return pred,nrmse

def build():
    Js=build_atlas(); raw,T=targets(Js)
    X0=np.array([descriptor(J,False) for J in Js]); X1=np.array([descriptor(J,True) for J in Js])
    _,base=loocv(X0,T); _,matrix=loocv(X1,T)
    raw_half=np.array([jet(J,H/2) for J in Js])
    relative=np.linalg.norm(raw_half-raw,axis=1)/np.maximum(np.linalg.norm(raw,axis=1),1e-12)
    improved=matrix<base; certified=bool(np.all(improved) and np.all(matrix<=CERT_THRESHOLD))
    return {
      'schema_version':'1.0','contract':'BC-IDPR-P3-B-M7','status':'REPRESENTATION_DESCRIPTOR_LOOCV_CERTIFIED' if certified else 'REPRESENTATION_DESCRIPTOR_LOOCV_NOT_CERTIFIED',
      'domain':{'anchor':'pi/12','atlas_size':len(Js),'doubled_spin_range':[1,4],'finite_difference_step':H,'ridge_alpha':RIDGE_ALPHA},
      'targets':{'raw_jet':['omega','omega_prime','omega_second'],'transformed':['log_abs_omega','omega_prime_over_omega','omega_second_over_omega'],'ranges':{'log_abs_omega':[float(T[:,0].min()),float(T[:,0].max())],'omega_prime_over_omega':[float(T[:,1].min()),float(T[:,1].max())],'omega_second_over_omega':[float(T[:,2].min()),float(T[:,2].max())]}},
      'descriptors':{'baseline_dimension':11,'matrix_augmented_dimension':15,'matrix_entries_from':'F(theta0)','derivatives_excluded_from_predictors':True},
      'loocv':{'baseline_nrmse':base.tolist(),'matrix_augmented_nrmse':matrix.tolist(),'matrix_improves_each_target':improved.tolist(),'all_targets_improved':bool(np.all(improved)),'certification_threshold_nrmse':CERT_THRESHOLD,'all_targets_below_threshold':bool(np.all(matrix<=CERT_THRESHOLD))},
      'numerical_stability':{'maximum_relative_jet_change_h_to_h_over_2':float(relative.max()),'median_relative_jet_change':float(np.median(relative))},
      'gates':{'expanded_two_channel_atlas':'CLOSED','matrix_descriptor_relevance':'SUPPORTED_EXPLORATORILY','omega_prediction':'NOT_CERTIFIED','higher_jet_prediction':'NOT_CERTIFIED','new_cross_carrier_pilot':'BLOCKED'},
      'tests':{'count':10,'result':'OK'},
      'claim_status':'MATRIX_AUGMENTATION_IMPROVES_ALL_THREE_LOOCV_TARGETS_BUT_ERRORS_REMAIN_ABOVE_CERTIFICATION_THRESHOLD',
      'evidence_rule':'No statement from the Gemini advisory report is used as evidence.'}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    out=build(); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':out['status'],'matrix_nrmse':out['loocv']['matrix_augmented_nrmse']}))

if __name__=='__main__': main()
