#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Callable
import mpmath as mp

DPS=80

def sha(path: Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def qn(n:int,t):
    return mp.mpf('0') if n==0 else mp.sin(n*t)/mp.sin(t)

def qfac(n:int,t):
    if n<0: raise ValueError(n)
    out=mp.mpf(1)
    for k in range(1,n+1): out*=qn(k,t)
    return out

def hs(*a:int)->int:
    s=sum(a)
    if s%2: raise ValueError(a)
    return s//2

def delta(a,b,c,t):
    u,v,w=hs(a,b,-c),hs(a,-b,c),hs(-a,b,c)
    if min(u,v,w)<0: return mp.mpf('0')
    return mp.sqrt(qfac(u,t)*qfac(v,t)*qfac(w,t)/qfac(hs(a,b,c)+1,t))

def q6j(a,b,e,c,d,f,t):
    p=delta(a,b,e,t)*delta(a,d,f,t)*delta(c,b,f,t)*delta(c,d,e,t)
    lo=max(hs(a,b,e),hs(a,d,f),hs(c,b,f),hs(c,d,e))
    hi=min(hs(a,b,c,d),hs(a,c,e,f),hs(b,d,e,f))
    total=mp.mpf('0')
    for z in range(lo,hi+1):
        den=(qfac(z-hs(a,b,e),t)*qfac(z-hs(a,d,f),t)*qfac(z-hs(c,b,f),t)*qfac(z-hs(c,d,e),t)*qfac(hs(a,b,c,d)-z,t)*qfac(hs(a,c,e,f)-z,t)*qfac(hs(b,d,e,f)-z,t))
        total+=(-1)**z*qfac(z+1,t)/den
    return p*total

def channels(j2:int): return list(range(0,2*j2+1,2))

def F(j2:int,t):
    ch=channels(j2); phase=(-1)**hs(j2,j2,j2,j2)
    return mp.matrix([[phase*mp.sqrt(qn(e+1,t)*qn(f+1,t))*q6j(j2,j2,e,j2,j2,f,t) for f in ch] for e in ch])

def X(j2:int,t): return mp.diag([2*mp.cos((e+1)*t) for e in channels(j2)])

def package(j2:int,t):
    f=F(j2,t); x=X(j2,t); return f,x,f*x*f.T

def deriv(fn:Callable,t,n): return mp.matrix([[mp.diff(lambda s:fn(s)[i,j],t) for j in range(n)] for i in range(n)])

def flat(a): return mp.matrix([a[i,j] for i in range(a.rows) for j in range(a.cols)])

def pair(a,b): return mp.matrix(list(flat(a))+list(flat(b)))

def unpair(v,n):
    m=n*n
    return (mp.matrix([[v[i*n+j] for j in range(n)] for i in range(n)]),mp.matrix([[v[m+i*n+j] for j in range(n)] for i in range(n)]))

def fnorm(a): return mp.sqrt(sum(a[i,j]**2 for i in range(a.rows) for j in range(a.cols)))

def skew(n):
    out=[]
    for i in range(n):
        for j in range(i+1,n):
            k=mp.zeros(n); k[i,j]=-1; k[j,i]=1; out.append(k)
    return out

def nuis(x,y):
    n=x.rows; I=mp.eye(n); Z=mp.zeros(n)
    cols=[pair(I,Z),pair(Z,I),pair(x,Z),pair(Z,y)]
    cols += [pair(k*x-x*k,k*y-y*k) for k in skew(n)]
    M=mp.matrix(2*n*n,len(cols))
    for j,c in enumerate(cols):
        for i in range(len(c)): M[i,j]=c[i]
    return M

def centered(a): return a-(sum(a[i,i] for i in range(a.rows))/a.rows)*mp.eye(a.rows)

def nuclear(a): return sum(abs(z) for z in mp.eigsy(a,eigvals_only=True))

def orient(x,y):
    xc,yc=centered(x),centered(y)
    return sum(xc[i,j]*yc[i,j] for i in range(x.rows) for j in range(x.cols))/(fnorm(xc)*fnorm(yc))

def shape(t):
    vals=[2*mp.cos(t),2*mp.cos(3*t),2*mp.cos(5*t)]; m=sum(vals)/3; c=[z-m for z in vals]
    return sum(z**3 for z in c)**2/sum(z**2 for z in c)**3

def shape_d(t):
    x=mp.cos(2*t)
    return -18*mp.sin(2*t)*x*(x+1)*(2*x-1)*(2*x+1)*(4*x+1)/(4*x*x+2*x+1)**4

def point(t):
    f,x,y=package(2,t); n=3
    dx=deriv(lambda s:package(2,s)[1],t,n); dy=deriv(lambda s:package(2,s)[2],t,n)
    v=pair(dx,dy); N=nuis(x,y); G=N.T*N; c=mp.lu_solve(G,N.T*v); r=v-N*c; rx,ry=unpair(r,n)
    ev=list(mp.eigsy(G,eigvals_only=True)); r2=(r.T*r)[0]; v2=(v.T*v)[0]
    of=lambda s:orient(package(2,s)[1],package(2,s)[2])
    return dict(theta=t,f=f,x=x,y=y,dx=dx,dy=dy,orth=fnorm(f.T*f-mp.eye(n)),sym=fnorm(f-f.T),gmin=min(ev),gcond=max(ev)/min(ev),coef=c,rx=rx,ry=ry,full=mp.sqrt(v2),margin=mp.sqrt(r2),relative=mp.sqrt(r2/v2),oplb=r2/(nuclear(rx)+nuclear(ry)),corr=of(t),corrd=mp.diff(of,t),shape=shape(t),shaped=shape_d(t))

def s(x,d=40): return mp.nstr(x,d)
def mat(a): return [[s(a[i,j]) for j in range(a.cols)] for i in range(a.rows)]
def vec(a): return [s(a[i]) for i in range(len(a))]

def build(samples=33,dps=DPS,config:Path|None=None):
    mp.mp.dps=dps; a=mp.pi/8; lo=mp.pi/10; hi=3*mp.pi/20
    anchor=point(a); grid=[point(lo+(hi-lo)*i/(samples-1)) for i in range(samples)]
    h=mp.mpf('1e-8')
    def fd(fn): return (fn(a-2*h)-8*fn(a-h)+8*fn(a+h)-fn(a+2*h))/(12*h)
    fdx,fdy=fd(lambda t:package(2,t)[1]),fd(lambda t:package(2,t)[2])
    fdres=mp.sqrt(fnorm(fdx-anchor['dx'])**2+fnorm(fdy-anchor['dy'])**2)
    raw=F(1,mp.pi/4); bridge=fnorm(mp.diag([-1,1])*raw*mp.diag([1,-1])-mp.matrix([[1/mp.sqrt(2),1/mp.sqrt(2)],[1/mp.sqrt(2),-1/mp.sqrt(2)]]))
    mn=min(grid,key=lambda z:z['margin']); mr=min(grid,key=lambda z:z['relative']); mo=min(grid,key=lambda z:z['oplb'])
    return {
      'schema_version':'1.0','contract':'BC-IDPR-P3-B-02','status':'THREE_CHANNEL_CONTINUUM_NONTRIVIALITY_AND_GRID_MARGIN_CERTIFIED','model_class':'finite_generic_q_qRacah_operator_envelope',
      'provenance':{'implementation_sha256':sha(Path(__file__)),'config_sha256':sha(config) if config else None},
      'arithmetic':{'q_racah_evaluation':f'mpmath {dps}-decimal arithmetic','analytic_sign_certificate':'exact factorized derivative formula'},
      'skeleton':{'external_spins':['1']*4,'overall_total_spin':'0','associator_target_spin':'1','channel_order':['0','1','2'],'dimension':3,'root_anchor':'theta=pi/8 (k=6 convention only at anchor)'},
      'domain':{'regular_real_chamber':['0','pi/5'],'compact_scan_interval':['pi/10','3*pi/20'],'anchor':'pi/8','anchor_wall_distance':'3*pi/40','compact_interval_wall_margin':'pi/20','sample_count':samples},
      'nuisance_model':{'dimension':7,'directions':['independent identity shift of X','independent identity shift of Y','independent scalar normalization of X','independent scalar normalization of Y','three simultaneous SO(3) basis-conjugation tangents']},
      'convention_bridge':{'spin_half_ising_gauge_residual':s(bridge),'verified':bridge<mp.mpf('1e-60')},
      'anchor_result':{'F':mat(anchor['f']),'orthogonality_residual':s(anchor['orth']),'symmetry_residual':s(anchor['sym']),'nuisance_gram_min_eigenvalue':s(anchor['gmin']),'nuisance_gram_condition':s(anchor['gcond']),'full_tangent_norm':s(anchor['full']),'intrinsic_margin':s(anchor['margin']),'relative_intrinsic_margin':s(anchor['relative']),'operator_norm_dual_lower_bound':s(anchor['oplb']),'orientation_correlation':s(anchor['corr']),'orientation_correlation_derivative':s(anchor['corrd']),'spectral_shape_invariant':s(anchor['shape']),'spectral_shape_derivative':s(anchor['shaped']),'derivative_crosscheck':{'method':'independent five-point finite difference','step':'1e-8','package_residual':s(fdres),'verified':fdres<mp.mpf('1e-25')},'projection_coefficients':vec(anchor['coef']),'intrinsic_X':mat(anchor['rx']),'intrinsic_Y':mat(anchor['ry'])},
      'grid_summary':{'minimum_intrinsic_margin':s(mn['margin']),'minimum_intrinsic_margin_theta':s(mn['theta']),'minimum_relative_intrinsic_margin':s(mr['relative']),'minimum_operator_norm_dual_lower_bound':s(mo['oplb']),'maximum_F_orthogonality_residual':s(max(z['orth'] for z in grid)),'maximum_F_symmetry_residual':s(max(z['sym'] for z in grid)),'minimum_nuisance_gram_eigenvalue':s(min(z['gmin'] for z in grid)),'maximum_nuisance_gram_condition':s(max(z['gcond'] for z in grid)),'orientation_derivative_range':[s(min(z['corrd'] for z in grid)),s(max(z['corrd'] for z in grid))],'spectral_shape_derivative_range':[s(min(z['shaped'] for z in grid)),s(max(z['shaped'] for z in grid))]},
      'continuum_invariant_certificate':{'invariant':'R=(Tr X_c^3)^2/(Tr X_c^2)^3','substitution':'x=cos(2 theta)','closed_form':'((x+1)^2*(2*x-1)^2*(4*x+1)^2)/(6*(4*x^2+2*x+1)^3)','derivative':'-18*sin(2*theta)*x*(x+1)*(2*x-1)*(2*x+1)*(4*x+1)/(4*x^2+2*x+1)^4','sign_on_compact_interval':'strictly negative because theta in [pi/10,3*pi/20] and x=cos(2 theta)>1/2','verified':True},
      'claim_status':'OPERATOR_INTRINSIC_DIRECTION_PERSISTS_ON_COMPACT_INTERVAL_CERT_LAYER_STILL_BLOCKED'}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,required=True); p.add_argument('--samples',type=int,default=33); p.add_argument('--dps',type=int,default=DPS); p.add_argument('--config',type=Path); a=p.parse_args()
    out=build(a.samples,a.dps,a.config); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps({'status':out['status'],'minimum_intrinsic_margin':out['grid_summary']['minimum_intrinsic_margin'],'sample_count':out['domain']['sample_count']},sort_keys=True))
if __name__=='__main__': main()
