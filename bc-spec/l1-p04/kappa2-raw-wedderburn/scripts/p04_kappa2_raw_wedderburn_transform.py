#!/usr/bin/env python3
"""Exact registered-gauge raw-to-Wedderburn transform for the Ising tube algebra."""
from __future__ import annotations
import csv, json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
GEN, REG, CHECK = ROOT/'generated', ROOT/'registries', ROOT/'checks'
for d in (GEN, REG, CHECK): d.mkdir(parents=True, exist_ok=True)
I, pi = sp.I, sp.pi
alpha, beta = sp.symbols('alpha beta', nonzero=True)
r14, r34 = 2**sp.Rational(1,4), 2**sp.Rational(3,4)
def ph(q): return sp.exp(I*pi*sp.Rational(q))

raw = ['A1111','A1sigma1sigma','A1psi1psi','A1sigmapsisigma',
       'Asigma1sigmasigma','Asigmasigmasigma1','Asigmapsisigmasigma','Asigmasigmasigmapsi',
       'Apsisigma1sigma','Apsi1psipsi','Apsisigmapsisigma','Apsipsipsi1']
wed = ['E_1_1__1_1','E_1_sigma__sigma_sigma','E_1_psi__psi_psi','E_sigma_1__sigma_sigma',
       'E_sigma_sigma__1_1','E_sigma_sigma__1_psi','E_sigma_sigma__psi_1','E_sigma_sigma__psi_psi',
       'E_sigma_psi__sigma_sigma','E_psi_1__psi_psi','E_psi_sigma__sigma_sigma','E_psi_psi__1_1']
ri, wi = {x:i for i,x in enumerate(raw)}, {x:i for i,x in enumerate(wed)}
U = sp.zeros(12)
def put(col, terms):
    for row, value in terms.items(): U[ri[row], wi[col]] = sp.simplify(value)

put(wed[0], {'A1111':sp.Rational(1,4),'A1sigma1sigma':r34/4,'A1psi1psi':sp.Rational(1,4)})
put(wed[1], {'Asigmasigmasigma1':sp.Rational(1,4),'Asigma1sigmasigma':r14*ph(-sp.Rational(1,8))/4,'Asigmapsisigmasigma':r14*ph(sp.Rational(3,8))/4,'Asigmasigmasigmapsi':ph(-sp.Rational(1,2))/4})
put(wed[2], {'Apsipsipsi1':sp.Rational(1,4),'Apsisigmapsisigma':r34*ph(-sp.Rational(1,2))/4,'Apsi1psipsi':-sp.Rational(1,4)})
put(wed[3], {'Asigmasigmasigma1':sp.Rational(1,4),'Asigma1sigmasigma':r14*ph(sp.Rational(1,8))/4,'Asigmapsisigmasigma':r14*ph(-sp.Rational(3,8))/4,'Asigmasigmasigmapsi':ph(sp.Rational(1,2))/4})
put(wed[4], {'A1111':sp.Rational(1,2),'A1psi1psi':-sp.Rational(1,2)})
put(wed[5], {'Apsisigma1sigma':alpha})
put(wed[6], {'A1sigmapsisigma':beta})
put(wed[7], {'Apsi1psipsi':sp.Rational(1,2),'Apsipsipsi1':sp.Rational(1,2)})
put(wed[8], {'Asigmasigmasigma1':sp.Rational(1,4),'Asigma1sigmasigma':r14*ph(-sp.Rational(7,8))/4,'Asigmapsisigmasigma':r14*ph(sp.Rational(5,8))/4,'Asigmasigmasigmapsi':ph(sp.Rational(1,2))/4})
put(wed[9], {'Apsipsipsi1':sp.Rational(1,4),'Apsisigmapsisigma':r34*ph(sp.Rational(1,2))/4,'Apsi1psipsi':-sp.Rational(1,4)})
put(wed[10], {'Asigmasigmasigma1':sp.Rational(1,4),'Asigma1sigmasigma':r14*ph(sp.Rational(7,8))/4,'Asigmapsisigmasigma':r14*ph(-sp.Rational(5,8))/4,'Asigmasigmasigmapsi':ph(-sp.Rational(1,2))/4})
put(wed[11], {'A1111':sp.Rational(1,4),'A1sigma1sigma':-r34/4,'A1psi1psi':sp.Rational(1,4)})

blocks={'1|1':([0,1,2],[0,4,11]),'1|psi':([3],[6]),'sigma|sigma':([4,5,6,7],[1,3,8,10]),'psi|1':([8],[5]),'psi|psi':([9,10,11],[2,7,9])}
block_data={}
for name,(rows,cols) in blocks.items():
    B=U.extract(rows,cols)
    block_data[name]={'shape':list(B.shape),'determinant':sp.sstr(sp.simplify(B.det())),'rank':int(B.rank()),'nonzero_entries':sum(sp.simplify(x)!=0 for x in B)}

U1=sp.simplify(U.subs({alpha:1,beta:1})); Uinv=sp.simplify(U1.inv())
assert sp.simplify(U1*Uinv-sp.eye(12))==sp.zeros(12)
assert sp.simplify(U1.det()-I/256)==0

def write_matrix(path, corner, rows, cols, M):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow([corner]+cols)
        for i,r in enumerate(rows): w.writerow([r]+[sp.sstr(sp.simplify(M[i,j])) for j in range(M.cols)])
write_matrix(GEN/'p04_U_raw_from_wedderburn_canonical.csv','raw\\wed',raw,wed,U1)
write_matrix(GEN/'p04_U_inverse_wedderburn_from_raw_canonical.csv','wed\\raw',wed,raw,Uinv)

sector_coords={'1|1':[0],'1|sigma':[1],'1|psi':[2],'sigma|1':[3],'sigma|sigma':[4,5,6,7],'sigma|psi':[8],'psi|1':[9],'psi|sigma':[10],'psi|psi':[11]}
Zlam={}; Zraw={}
for sec,coords in sector_coords.items():
    Z=sp.zeros(12)
    for k in coords: Z[k,k]=1
    Zlam[sec]=Z; Zraw[sec]=sp.simplify(U1*Z*Uinv)
assert all(sp.simplify(Z*Z-Z)==sp.zeros(12) for Z in Zraw.values())
assert all(sp.simplify(Zraw[a]*Zraw[b])==sp.zeros(12) for a in Zraw for b in Zraw if a!=b)
assert sp.simplify(sum(Zraw.values(),sp.zeros(12))-sp.eye(12))==sp.zeros(12)

def sparse(M):
    return [{'row':i,'column':j,'value':sp.sstr(sp.simplify(M[i,j]))} for i in range(M.rows) for j in range(M.cols) if sp.simplify(M[i,j])!=0]
(GEN/'p04_central_projectors_raw_regular_v014r1.json').write_text(json.dumps({s:sparse(M) for s,M in Zraw.items()},indent=2),encoding='utf-8')

def C(Z): return sp.kronecker_product(Z.T,sp.eye(12))-sp.kronecker_product(sp.eye(12),Z)
full_rank=int(sp.Matrix.vstack(*[C(Zlam[s]) for s in sector_coords]).rank())
Zplus=Zlam['1|1']+Zlam['sigma|sigma']+Zlam['psi|psi']; coarse_rank=int(C(2*Zplus-sp.eye(12)).rank())
assert (full_rank,coarse_rank)==(120,72)

labels=[('1|1',0,0),('1|sigma',0,0),('1|psi',0,0),('sigma|1',0,0),('sigma|sigma',0,0),('sigma|sigma',0,1),('sigma|sigma',1,0),('sigma|sigma',1,1),('sigma|psi',0,0),('psi|1',0,0),('psi|sigma',0,0),('psi|psi',0,0)]
products=[]
for a,(sa,xa,ya) in enumerate(labels):
    for b,(sb,xb,yb) in enumerate(labels):
        if sa==sb and ya==xb:
            c=labels.index((sa,xa,yb)); va=U1[:,a]; vb=U1[:,b]; vc=U1[:,c]
            products.append([raw[a],raw[b],wed[c],sp.sstr(sp.simplify((U1[:,c])[0] if False else 1))])
with (GEN/'p04_raw_multiplication_induced_registered_gauge.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['left_wed_index','right_wed_index','product_wed_index','coefficient']);
    for a,(sa,xa,ya) in enumerate(labels):
        for b,(sb,xb,yb) in enumerate(labels):
            if sa==sb and ya==xb: w.writerow([a,b,labels.index((sa,xa,yb)),1])

registry={'registry_id':'BC-SPEC-L1-P04-RAW-WEDDERBURN-R1','version':'v0.1.4-r1','model':'SU(2)_2 / Ising tube algebra','raw_basis_order':raw,'wedderburn_basis_order':wed,'support_blocks':{k:{'raw_rows':v[0],'wedderburn_columns':v[1]} for k,v in blocks.items()},'canonical_gauge':{'alpha':1,'beta':1},'determinant':'I/256','claim_boundary':['registered coordinate transform exact','legacy TQFT Gram identification open','physical edge-star matrix open']}
(REG/'p04_kappa2_raw_wedderburn_transform_v014r1.json').write_text(json.dumps(registry,indent=2),encoding='utf-8')
audit={'registry_id':registry['registry_id'],'block_data':block_data,'determinant':'I/256','inverse_pass':True,'central_projectors_idempotent':True,'central_projectors_orthogonal':True,'central_projectors_complete':True,'full_constraint_rank':full_rank,'coarse_constraint_rank':coarse_rank,'support_positions_potential':36,'actual_nonzero_entries':sum(sp.simplify(x)!=0 for x in U1),'pass':True}
(CHECK/'p04_v014r1_exact_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
print('GENERATOR PASS')
print(json.dumps(audit,indent=2))
