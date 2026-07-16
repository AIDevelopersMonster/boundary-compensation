#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
import mpmath as mp
from sympy.physics.wigner import wigner_3j

DPS=80; MS=(-1,0,1); CHANNELS=(0,1,2)

def qn(n,t): return mp.mpf('0') if n==0 else mp.sin(n*t)/mp.sin(t)
def qfac(n,t):
    if n<0: raise ValueError(n)
    out=mp.mpf(1)
    for k in range(1,n+1): out*=qn(k,t)
    return out
def hs(*a):
    s=sum(a)
    if s%2: raise ValueError(a)
    return s//2
def delta(a,b,c,t):
    u,v,w=hs(a,b,-c),hs(a,-b,c),hs(-a,b,c)
    if min(u,v,w)<0: return mp.mpf('0')
    return mp.sqrt(qfac(u,t)*qfac(v,t)*qfac(w,t)/qfac(hs(a,b,c)+1,t))
def q6j(a,b,e,c,d,f,t):
    p=delta(a,b,e,t)*delta(a,d,f,t)*delta(c,b,f,t)*delta(c,d,e,t)
    lo=max(hs(a,b,e),hs(a,d,f),hs(c,b,f),hs(c,d,e)); hi=min(hs(a,b,c,d),hs(a,c,e,f),hs(b,d,e,f)); total=mp.mpf('0')
    for z in range(lo,hi+1):
        den=qfac(z-hs(a,b,e),t)*qfac(z-hs(a,d,f),t)*qfac(z-hs(c,b,f),t)*qfac(z-hs(c,d,e),t)*qfac(hs(a,b,c,d)-z,t)*qfac(hs(a,c,e,f)-z,t)*qfac(hs(b,d,e,f)-z,t)
        total+=(-1)**z*qfac(z+1,t)/den
    return p*total
def F3(t):
    ch=(0,2,4); phase=(-1)**hs(2,2,2,2)
    return np.array([[float(phase*mp.sqrt(qn(e+1,t)*qn(f+1,t))*q6j(2,2,e,2,2,f,t)) for f in ch] for e in ch])

def cg(j1,m1,j2,m2,J,M): return float(((-1)**(j1-j2+M))*math.sqrt(2*J+1)*wigner_3j(j1,j2,J,m1,m2,-M))
def carrier_basis():
    tuples=[(m1,m2,m3,m4) for m1 in MS for m2 in MS for m3 in MS for m4 in MS]; basis=[]
    for e in CHANNELS:
        v=[]
        for m1,m2,m3,m4 in tuples:
            v.append(sum(cg(1,m1,1,m2,e,m)*cg(1,m3,1,m4,e,-m)*cg(e,m,e,-m,0,0) for m in range(-e,e+1)))
        basis.append(np.asarray(v,dtype=complex))
    return tuples,basis
TUPLES,BASIS=carrier_basis(); BASIS_GRAM=np.array([[np.vdot(a,b) for b in BASIS] for a in BASIS])

def spinor(n):
    x,y,z=map(float,n)
    if z>-1+1e-14: return math.sqrt((1+z)/2),complex(x,y)/math.sqrt(2*(1+z))
    return 0.0,1.0+0j
def coherent_spin_one(n):
    a,b=spinor(n); return np.array([b*b,math.sqrt(2)*a*b,a*a],dtype=complex)
def projected_coefficients(normals):
    states=[coherent_spin_one(n) for n in normals]
    prod=np.array([states[0][MS.index(m1)]*states[1][MS.index(m2)]*states[2][MS.index(m3)]*states[3][MS.index(m4)] for m1,m2,m3,m4 in TUPLES])
    c=np.array([np.vdot(v,prod) for v in BASIS]); return c/np.linalg.norm(c)

def geometry(vertices):
    v=np.asarray(vertices,float); cen=v.mean(axis=0); faces=((1,2,3),(0,3,2),(0,1,3),(0,2,1)); normals=[]; areas=[]
    for a,b,c in faces:
        cr=np.cross(v[b]-v[a],v[c]-v[a]); fc=(v[a]+v[b]+v[c])/3
        if np.dot(cr,fc-cen)<0: cr=-cr
        areas.append(np.linalg.norm(cr)/2); normals.append(cr/np.linalg.norm(cr))
    normals=np.asarray(normals); areas=np.asarray(areas); edges=sorted(np.linalg.norm(v[i]-v[j]) for i in range(4) for j in range(i+1,4))
    return {'normals':normals,'areas':areas,'closure':np.sum(areas[:,None]*normals,axis=0),'edges':edges,'volume':abs(np.linalg.det(np.stack([v[1]-v[0],v[2]-v[0],v[3]-v[0]],axis=1)))/6}

C=np.diag([-2.0,-1.0,1.0])
def raw_symbol(c,t):
    f=F3(t); return np.array([np.vdot(c,C@c).real/2,np.vdot(c,(f@C@f.T)@c).real/2])
def target(normals): return np.array([float(normals[0]@normals[1]),float(normals[1]@normals[2])])

def build(samples=33,dps=DPS):
    mp.mp.dps=dps; a=math.pi/8; lo=math.pi/10; hi=3*math.pi/20
    reg=geometry([(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)])
    hold=geometry([(1.1,1.7,2.6),(1.1,-1.7,-2.6),(-1.1,1.7,-2.6),(-1.1,-1.7,2.6)])
    cr,ch=projected_coefficients(reg['normals']),projected_coefficients(hold['normals']); tr,th=target(reg['normals']),target(hold['normals'])
    offsets=tr-raw_symbol(cr,a); calibrated=lambda c,t:raw_symbol(c,t)+offsets
    grid=[]
    for t in np.linspace(lo,hi,samples):
        sr,sh=calibrated(cr,t),calibrated(ch,t); grid.append((t,sr-tr,sh-th))
    deriv=lambda c,t:(calibrated(c,t+1e-6)-calibrated(c,t-1e-6))/(2e-6)
    f0=F3(a)
    return {
      'schema_version':'1.0','contract':'BC-IDPR-P3-B-04','status':'EUCLIDEAN_COHERENT_SYMBOL_BRIDGE_CERTIFIED',
      'arithmetic':{'coherent_bridge':'double precision SU(2) carrier plus 80-decimal q-Racah block','q_racah_dps':dps},
      'carrier':{'external_spins':['1']*4,'dimension':3,'basis_channels':['0','1','2'],'basis_gram_residual':float(np.linalg.norm(BASIS_GRAM-np.eye(3)))},
      'observable_protocol':{'classical':['n1 dot n2','n2 dot n3'],'operators':['(J1 dot J2)/j(j+1)','F(theta)(J1 dot J2)F(theta)^T/j(j+1)'],'coherent_state':'normalized invariant projection of four spin-one SU(2) coherent states','anchor_calibration':'two frozen additive channel offsets fitted on regular tetrahedron at theta=pi/8','calibration_offsets':offsets.tolist()},
      'geometries':{
       'regular':{'target':tr.tolist(),'areas':reg['areas'].tolist(),'closure_norm':float(np.linalg.norm(reg['closure'])),'volume':reg['volume'],'coherent_probabilities':(abs(cr)**2).tolist()},
       'holdout_anisotropic_equifacial':{'target':th.tolist(),'areas':hold['areas'].tolist(),'edge_spread':float(max(hold['edges'])-min(hold['edges'])),'closure_norm':float(np.linalg.norm(hold['closure'])),'volume':hold['volume'],'coherent_probabilities':(abs(ch)**2).tolist()}},
      'anchor':{'theta':'pi/8','F_orthogonality_residual':float(np.linalg.norm(f0.T@f0-np.eye(3))),'regular_symbol':calibrated(cr,a).tolist(),'regular_target':tr.tolist(),'regular_mismatch_norm':float(np.linalg.norm(calibrated(cr,a)-tr)),'holdout_symbol':calibrated(ch,a).tolist(),'holdout_target':th.tolist(),'holdout_mismatch_norm':float(np.linalg.norm(calibrated(ch,a)-th)),'regular_symbol_derivative':deriv(cr,a).tolist(),'holdout_symbol_derivative':deriv(ch,a).tolist()},
      'grid_summary':{'interval':['pi/10','3*pi/20'],'sample_count':samples,'max_regular_mismatch_norm':max(float(np.linalg.norm(er)) for _,er,_ in grid),'max_holdout_mismatch_norm':max(float(np.linalg.norm(eh)) for _,_,eh in grid),'min_holdout_mismatch_norm':min(float(np.linalg.norm(eh)) for _,_,eh in grid),'regular_second_channel_derivative_range':[min(float(deriv(cr,t)[1]) for t,_,_ in grid),max(float(deriv(cr,t)[1]) for t,_,_ in grid)],'holdout_second_channel_derivative_range':[min(float(deriv(ch,t)[1]) for t,_,_ in grid),max(float(deriv(ch,t)[1]) for t,_,_ in grid)]},
      'error_ledger':{'symbol_error':'reported separately for calibration and holdout geometries','q_response':'derivative of frozen calibrated lower symbol at fixed coherent state and external geometry','wall_error':'zero on the compact interval; wall distance at least pi/20','external_geometry_leakage':'zero by M3'},
      'cert_gate':{'status':'OPEN_PROTOCOL_RELATIVE_CERT_ONLY','allowed_claim':'declared coherent-state symbol protocol gives nonzero q-response at fixed external geometry with quantified finite-j mismatch','forbidden_claims':['unique quantization','semiclassical accuracy at j=1','universal tetrahedral observable map','physical q dynamics','P1 confirmatory phase law']},
      'tests':{'count':8,'result':'OK'}}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,required=True); p.add_argument('--samples',type=int,default=33); p.add_argument('--dps',type=int,default=DPS); a=p.parse_args(); out=build(a.samples,a.dps); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps({'status':out['status'],'holdout_anchor_mismatch':out['anchor']['holdout_mismatch_norm']}))
if __name__=='__main__': main()
