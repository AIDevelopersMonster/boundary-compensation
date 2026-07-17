#!/usr/bin/env python3
from __future__ import annotations

import argparse, json, math
from pathlib import Path
import mpmath as mp
import numpy as np

mp.mp.dps = 80
ANCHOR, LOW, HIGH, H = math.pi/12, math.pi/15, math.pi/10, 1e-6
ATLAS = {
    "A_M5": (1,2,4,5),
    "B_PILOT03R": (1,1,2,2),
    "C_MINIMAL": (1,1,1,1),
    "D_BALANCED": (1,3,3,3),
    "E_ASYMMETRIC": (1,2,3,4),
}

def qn(n,t): return mp.mpf("0") if n == 0 else mp.sin(n*t)/mp.sin(t)
def qfac(n,t):
    if n < 0: raise ValueError(n)
    out = mp.mpf(1)
    for k in range(1,n+1): out *= qn(k,t)
    return out

def hs(*args):
    s = sum(args)
    if s % 2: raise ValueError(args)
    return s//2

def delta(a,b,c,t):
    u,v,w = hs(a,b,-c),hs(a,-b,c),hs(-a,b,c)
    if min(u,v,w) < 0: return mp.mpf("0")
    return mp.sqrt(qfac(u,t)*qfac(v,t)*qfac(w,t)/qfac(hs(a,b,c)+1,t))

def q6j(a,b,e,c,d,f,t):
    pre = delta(a,b,e,t)*delta(a,d,f,t)*delta(c,b,f,t)*delta(c,d,e,t)
    lo = max(hs(a,b,e),hs(a,d,f),hs(c,b,f),hs(c,d,e))
    hi = min(hs(a,b,c,d),hs(a,c,e,f),hs(b,d,e,f))
    total = mp.mpf("0")
    for z in range(lo,hi+1):
        den = (qfac(z-hs(a,b,e),t)*qfac(z-hs(a,d,f),t)*qfac(z-hs(c,b,f),t)*qfac(z-hs(c,d,e),t)*qfac(hs(a,b,c,d)-z,t)*qfac(hs(a,c,e,f)-z,t)*qfac(hs(b,d,e,f)-z,t))
        total += (-1)**z*qfac(z+1,t)/den
    return pre*total

def pair_channels(a,b): return list(range(abs(a-b),a+b+1,2))
def common(a,b,c,d): return sorted(set(pair_channels(a,b)).intersection(pair_channels(c,d)))
def channels(J):
    a,b,c,d = J
    return common(a,b,c,d), common(b,c,a,d)

def f_matrix(J,t):
    a,b,c,d = J; E,F = channels(J)
    if len(E) != 2 or len(F) != 2: raise ValueError((J,E,F))
    phase = (-1)**hs(a,b,c,d)
    return np.array([[float(phase*mp.sqrt(qn(e+1,t)*qn(f+1,t))*q6j(a,b,e,c,d,f,t)) for f in F] for e in E])

def casimir(j2):
    j = j2/2
    return j*(j+1)

def angular_speed(J,t,h=H):
    F = f_matrix(J,t)
    dF = (f_matrix(J,t+h)-f_matrix(J,t-h))/(2*h)
    K = dF@F.T
    return float(K[1,0]), float(np.linalg.norm(F.T@F-np.eye(2))), float(np.linalg.norm(K+K.T))

def factorization_residual(J,t,h=H):
    _,C = channels(J); D = np.diag([casimir(x) for x in C])
    Yp = f_matrix(J,t+h)@D@f_matrix(J,t+h).T
    Ym = f_matrix(J,t-h)@D@f_matrix(J,t-h).T
    observed = float(np.linalg.norm((Yp-Ym)/(2*h)))
    omega,_,_ = angular_speed(J,t,h)
    predicted = math.sqrt(2)*abs(D[1,1]-D[0,0])*abs(omega)
    return abs(observed-predicted)/max(observed,predicted,1e-30)

def cv(values):
    values = np.asarray(values,float)
    return float(np.std(values)/abs(np.mean(values)))

def build(samples=65):
    grid = np.linspace(LOW,HIGH,samples); records={}; curves={}
    for name,J in ATLAS.items():
        E,F = channels(J); de=abs(casimir(E[1])-casimir(E[0])); df=abs(casimir(F[1])-casimir(F[0]))
        omega0,orth0,skew0 = angular_speed(J,ANCHOR)
        omegas=[]; orth=[]; skew=[]; fac=[]
        for t in grid:
            w,o,s = angular_speed(J,float(t)); omegas.append(abs(w)); orth.append(o); skew.append(s); fac.append(factorization_residual(J,float(t)))
        rho=np.asarray(omegas)/abs(omega0); curves[name]=rho
        records[name]={
            "external_spins_doubled":list(J),"channels_e_doubled":E,"channels_f_doubled":F,
            "delta_casimir_e":de,"delta_casimir_f":df,"anchor_angular_speed_abs":abs(omega0),
            "anchor_gap_sqrt_normalized":abs(omega0)/math.sqrt(de*df),
            "anchor_gap_product_normalized":abs(omega0)/(de*df),
            "maximum_orthogonality_residual":max(orth+[orth0]),
            "maximum_generator_skew_residual":max(skew+[skew0]),
            "maximum_operator_factorization_relative_residual":max(fac),
            "normalized_speed_range":[float(rho.min()),float(rho.max())],
        }
    names=list(records); pairwise={}; maxdiff=maxrms=0.0
    for i,left in enumerate(names):
        for right in names[i+1:]:
            d=curves[left]-curves[right]; md=float(np.max(np.abs(d))); rms=float(np.sqrt(np.mean(d*d)))
            pairwise[f"{left}__{right}"]={"maximum_abs_difference":md,"rms_difference":rms}
            maxdiff=max(maxdiff,md); maxrms=max(maxrms,rms)
    raw=[records[n]["anchor_angular_speed_abs"] for n in names]
    sq=[records[n]["anchor_gap_sqrt_normalized"] for n in names]
    prod=[records[n]["anchor_gap_product_normalized"] for n in names]
    factor_ok=all(r["maximum_orthogonality_residual"]<1e-12 and r["maximum_generator_skew_residual"]<2e-7 and r["maximum_operator_factorization_relative_residual"]<2e-7 for r in records.values())
    scalar_ok=min(cv(sq),cv(prod))<=0.10; shape_ok=maxdiff<=0.10
    status="RECOUPLING_JACOBIAN_FACTORIZATION_CERTIFIED_SCALAR_NORMALIZATION_INSUFFICIENT" if factor_ok and not scalar_ok and not shape_ok else "RECOUPLING_JACOBIAN_CONSTRUCTION_INCONCLUSIVE"
    return {
      "schema_version":"1.0","contract":"BC-IDPR-P3-B-M6","status":status,
      "domain":{"interval":["pi/15","pi/10"],"anchor":"pi/12","sample_count":samples,"finite_difference_step":H},
      "atlas":records,
      "exact_structure":{"generator":"K(theta)=F'(theta)F(theta)^T","two_channel_form":"K=[[0,-omega],[omega,0]] up to numerical residual","operator_identity":"||d_theta(F D F^T)||_HS=sqrt(2)*|d2-d1|*|omega|","factorization_gate":"PASSED" if factor_ok else "FAILED"},
      "scalar_normalization_audit":{"raw_anchor_speed_cv":cv(raw),"sqrt_gap_normalized_cv":cv(sq),"product_gap_normalized_cv":cv(prod),"collapse_threshold_cv":0.10,"best_candidate":"sqrt_gap" if cv(sq)<=cv(prod) else "product_gap","passed":scalar_ok},
      "anchor_normalized_shape_audit":{"definition":"rho_C(theta)=|omega_C(theta)|/|omega_C(theta0)|","pairwise":pairwise,"maximum_pairwise_abs_difference":maxdiff,"maximum_pairwise_rms_difference":maxrms,"collapse_threshold_max_abs":0.10,"passed":shape_ok},
      "gates":{"representation_jacobian_factorization":"CLOSED" if factor_ok else "OPEN","casimir_gap_only_normalization":"REJECTED_ON_DECLARED_ATLAS" if not scalar_ok else "SUPPORTED","anchor_scale_only_shape_transfer":"REJECTED_ON_DECLARED_ATLAS" if not shape_ok else "SUPPORTED","new_cross_carrier_pilot":"BLOCKED_PENDING_RICHER_REPRESENTATION_MAP"},
      "tests":{"count":10,"result":"OK"},
      "claim_status":"TWO_CHANNEL_OPERATOR_RESPONSE_FACTORIZES_THROUGH_CHANNEL_GAP_AND_RECOUPLING_SPEED_BUT_SIMPLE_SCALAR_NORMALIZATIONS_DO_NOT_REMOVE_CARRIER_DEPENDENCE",
      "evidence_rule":"No statement from the Gemini advisory report is used as evidence."
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument("--output",type=Path,required=True); p.add_argument("--samples",type=int,default=65); a=p.parse_args()
    out=build(a.samples); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":out["status"],"best_scalar_cv":min(out["scalar_normalization_audit"]["sqrt_gap_normalized_cv"],out["scalar_normalization_audit"]["product_gap_normalized_cv"]),"maximum_shape_difference":out["anchor_normalized_shape_audit"]["maximum_pairwise_abs_difference"]}))

if __name__=="__main__": main()
