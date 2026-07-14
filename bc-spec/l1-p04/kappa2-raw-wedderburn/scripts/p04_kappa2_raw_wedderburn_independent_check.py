#!/usr/bin/env python3
"""Independent reconstruction checks from serialized v0.1.4-r1 artifacts."""
from __future__ import annotations
import csv, json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]; GEN=ROOT/'generated'; CHECK=ROOT/'checks'; CHECK.mkdir(parents=True,exist_ok=True)
def read_matrix(path):
    with path.open(newline='',encoding='utf-8') as f: rows=list(csv.reader(f))[1:]
    return sp.Matrix([[sp.sympify(x,locals={'I':sp.I}) for x in r[1:]] for r in rows])
def sparse_matrix(entries):
    M=sp.zeros(12)
    for e in entries: M[int(e['row']),int(e['column'])]=sp.sympify(str(e['value']),locals={'I':sp.I})
    return M
def C(Z): return sp.kronecker_product(Z.T,sp.eye(12))-sp.kronecker_product(sp.eye(12),Z)

U=read_matrix(GEN/'p04_U_raw_from_wedderburn_canonical.csv')
Uinv=read_matrix(GEN/'p04_U_inverse_wedderburn_from_raw_canonical.csv')
inverse_pass=sp.simplify(U*Uinv-sp.eye(12))==sp.zeros(12); detU=sp.simplify(U.det())
payload=json.loads((GEN/'p04_central_projectors_raw_regular_v014r1.json').read_text(encoding='utf-8'))
projectors={s:sparse_matrix(e) for s,e in payload.items()}
idempotent=all(sp.simplify(Z*Z-Z)==sp.zeros(12) for Z in projectors.values())
orthogonal=all(sp.simplify(projectors[a]*projectors[b])==sp.zeros(12) for a in projectors for b in projectors if a!=b)
complete=sp.simplify(sum(projectors.values(),sp.zeros(12))-sp.eye(12))==sp.zeros(12)
coords={'1|1':[0],'1|sigma':[1],'1|psi':[2],'sigma|1':[3],'sigma|sigma':[4,5,6,7],'sigma|psi':[8],'psi|1':[9],'psi|sigma':[10],'psi|psi':[11]}
Zlam={}
for sec,inds in coords.items():
    Z=sp.zeros(12)
    for k in inds: Z[k,k]=1
    Zlam[sec]=Z
full_rank=int(sp.Matrix.vstack(*[C(Zlam[s]) for s in coords]).rank())
Gamma=2*(Zlam['1|1']+Zlam['sigma|sigma']+Zlam['psi|psi'])-sp.eye(12)
coarse_rank=int(C(Gamma).rank()); actual_nonzero=sum(sp.simplify(x)!=0 for x in U)
report={'source_registry_id':'BC-SPEC-L1-P04-RAW-WEDDERBURN-R1','inverse_pass':inverse_pass,'determinant_exact':sp.sstr(detU),'determinant_expected':'I/256','determinant_pass':sp.simplify(detU-sp.I/256)==0,'central_projectors_idempotent':idempotent,'central_projectors_orthogonal':orthogonal,'central_projectors_complete':complete,'full_constraint_rank':full_rank,'coarse_constraint_rank':coarse_rank,'support_positions_potential':36,'actual_nonzero_entries':actual_nonzero}
report['pass']=all([inverse_pass,report['determinant_pass'],idempotent,orthogonal,complete,full_rank==120,coarse_rank==72,actual_nonzero==34])
(CHECK/'independent_check_v014r1.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
assert report['pass']
print('INDEPENDENT CHECK PASS')
print(json.dumps(report,indent=2))
