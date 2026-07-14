#!/usr/bin/env python3
"""Cross-audit historical v0.1.5 registries against v0.1.4-r1."""
from __future__ import annotations
import csv, json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/'registries'; GEN=ROOT/'generated'; CHECK=ROOT/'checks'; HIST=ROOT/'historical-cross-audit'; SRC=HIST/'source-v015'
for d in (CHECK,HIST,SRC): d.mkdir(parents=True,exist_ok=True)
label={0:'1',1:'sigma',2:'psi'}

def old_t_to_a(r):
    i,j,x,m=(int(r[k]) for k in ('i','j','x','m'))
    return f"A{label[i]}{label[m]}{label[j]}{label[x]}"

def read_matrix(path):
    with path.open(newline='',encoding='utf-8') as f: rows=list(csv.reader(f))
    return [r[0] for r in rows[1:]],rows[0][1:],sp.Matrix([[sp.sympify(x,locals={'I':sp.I}) for x in r[1:]] for r in rows[1:]])

def write_matrix(path,corner,rows,cols,M):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow([corner]+cols)
        for i,name in enumerate(rows): w.writerow([name]+[sp.sstr(sp.simplify(M[i,j])) for j in range(M.cols)])

def sparse_to_matrix(entries):
    M=sp.zeros(12)
    for e in entries: M[int(e['row']),int(e['column'])]=sp.sympify(str(e['value']),locals={'I':sp.I})
    return M

def matrix_to_sparse(M):
    return [{'row':i,'column':j,'value':sp.sstr(sp.simplify(M[i,j]))} for i in range(12) for j in range(12) if sp.simplify(M[i,j])!=0]

registry=json.loads((REG/'p04_kappa2_raw_wedderburn_transform_v014r1.json').read_text(encoding='utf-8'))
new_raw=registry['raw_basis_order']; new_wed=registry['wedderburn_basis_order']
with (SRC/'p04_raw_tube_basis.csv').open(newline='',encoding='utf-8') as f: old_rows=list(csv.DictReader(f))
old_ids=[r['id'] for r in old_rows]; old_as_a=[old_t_to_a(r) for r in old_rows]
assert set(old_as_a)==set(new_raw)
old_to_new=[new_raw.index(x) for x in old_as_a]
assert old_to_new==[0,1,2,3,5,4,6,7,8,11,10,9]
Q=sp.zeros(12)
for old_i,new_i in enumerate(old_to_new): Q[old_i,new_i]=1
assert Q*Q.T==sp.eye(12)
raw_rows,wed_cols,U=read_matrix(GEN/'p04_U_raw_from_wedderburn_canonical.csv')
wed_rows,raw_cols,Uinv=read_matrix(GEN/'p04_U_inverse_wedderburn_from_raw_canonical.csv')
assert raw_rows==new_raw and raw_cols==new_raw and wed_rows==new_wed and wed_cols==new_wed
Uold=sp.simplify(Q*U); Uoldinv=sp.simplify(Uinv*Q.T)
assert sp.simplify(Uold*Uoldinv-sp.eye(12))==sp.zeros(12)
assert sp.simplify(Uold.det()-U.det())==0
write_matrix(HIST/'p04_U_raw_from_wedderburn_v015_raw_order.csv','old_raw\\wed',old_ids,new_wed,Uold)
write_matrix(HIST/'p04_U_inverse_wedderburn_from_v015_raw_order.csv','wed\\old_raw',new_wed,old_ids,Uoldinv)
with (HIST/'p04_raw_basis_permutation_v015_to_v014r1.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['old_index','new_index','v015_id','v014r1_id'])
    for oi,ni in enumerate(old_to_new): w.writerow([oi,ni,old_ids[oi],new_raw[ni]])
with (SRC/'p04_lambda_matrix_unit_basis.csv').open(newline='',encoding='utf-8') as f: old_wed=[r['id'] for r in csv.DictReader(f)]
assert old_wed==new_wed
expected={'1|1':[new_wed[0]],'1|sigma':[new_wed[1]],'1|psi':[new_wed[2]],'sigma|1':[new_wed[3]],'sigma|sigma':[new_wed[4],new_wed[7]],'sigma|psi':[new_wed[8]],'psi|1':[new_wed[9]],'psi|sigma':[new_wed[10]],'psi|psi':[new_wed[11]]}
with (SRC/'p04_kappa2_central_projectors.csv').open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
for r in rows: assert json.loads(r['central_projector'])==expected[r['sector_id']]
payload=json.loads((GEN/'p04_central_projectors_raw_regular_v014r1.json').read_text(encoding='utf-8')); old_projectors={}
for sec,entries in payload.items():
    Z=sp.simplify(Q*sparse_to_matrix(entries)*Q.T); assert sp.simplify(Z*Z-Z)==sp.zeros(12); old_projectors[sec]=matrix_to_sparse(Z)
(HIST/'p04_central_projectors_v015_raw_order.json').write_text(json.dumps(old_projectors,indent=2),encoding='utf-8')
identity=sp.zeros(12)
with (SRC/'p04_kappa2_physical_cylinder_identity.csv').open(newline='',encoding='utf-8') as f:
    for r in csv.DictReader(f): identity[int(r['row']),int(r['column'])]=int(r['value'])
assert identity==sp.eye(12)
assert sp.simplify(Uoldinv*identity*Uold-sp.eye(12))==sp.zeros(12)
with (SRC/'p04_v015_map_type_registry.csv').open(newline='',encoding='utf-8') as f: map_rows=list(csv.DictReader(f))
assert any(r['type_id']=='T0_PRODUCT_CYLINDER_PHYSICAL' and r['canonical_map']=='identity' for r in map_rows)
report={'registry_id':'BC-SPEC-L1-P04-HISTORICAL-CROSS-AUDIT-001','comparison':'v0.1.5 historical registries versus v0.1.4-r1 registered transform','raw_basis_sets_equal':True,'wedderburn_basis_order_equal':True,'old_to_new_raw_permutation':old_to_new,'permutation_is_even':int(Q.det())==1,'determinant_preserved':True,'inverse_pass_in_v015_order':True,'central_projector_sector_registry_matches':True,'central_projectors_transported_to_v015_order':True,'historical_product_cylinder_identity_file_checked':True,'historical_product_cylinder_is_identity':True,'map_type_registry_checked':True,'no_shared_registry_contradiction':True,'claim_boundary':['coordinate compatibility after a registered permutation','legacy TQFT Gram identification open','nontrivial physical edge-star operator open'],'pass':True}
(CHECK/'p04_historical_cross_audit_v015_vs_v014r1.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('HISTORICAL CROSS-AUDIT PASS')
print(json.dumps(report,indent=2))
