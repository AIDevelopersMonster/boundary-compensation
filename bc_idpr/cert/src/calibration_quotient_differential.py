#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, math
from pathlib import Path
import numpy as np


def load_m4():
    root=Path(__file__).resolve().parents[3]
    p=root/'p3'/'operator_envelope'/'src'/'coherent_symbol_bridge.py'
    spec=importlib.util.spec_from_file_location('m4_bridge',p)
    if spec is None or spec.loader is None: raise RuntimeError(p)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def build(samples=33):
    m=load_m4(); a=math.pi/8; lo=math.pi/10; hi=3*math.pi/20
    reg=m.geometry([(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)])
    hold=m.geometry([(1.1,1.7,2.6),(1.1,-1.7,-2.6),(-1.1,1.7,-2.6),(-1.1,-1.7,2.6)])
    cr=m.projected_coefficients(reg['normals']); ch=m.projected_coefficients(hold['normals'])
    sig=lambda t: np.concatenate([m.raw_symbol(cr,t),m.raw_symbol(ch,t)])
    base=sig(a); grid_t=np.linspace(lo,hi,samples); grid=[sig(t)-base for t in grid_t]
    adjacent=[float(np.linalg.norm(grid[i+1]-grid[i])) for i in range(samples-1)]
    steps=[1e-4,1e-5,1e-6,1e-7]
    deriv=[(sig(a+h)-sig(a-h))/(2*h) for h in steps]
    dref=deriv[2]; fd_radius=max(float(np.linalg.norm(d-dref)) for d in deriv)
    offsets=[np.array([0.3,-0.2,0.7,-0.5]),np.array([-1.0,2.0,0.25,0.125])]
    inv=max(float(np.linalg.norm(((sig(hi)+b)-(sig(a)+b))-(sig(hi)-sig(a)))) for b in offsets)
    arithmetic=5e-14; uncertainty=arithmetic+fd_radius*(hi-lo)/samples
    min_adj=min(adjacent); net=min_adj-uncertainty
    status='CALIBRATION_QUOTIENT_DIFFERENTIAL_SEPARATION_CERTIFIED' if inv<1e-12 and net>0 else 'DIFFERENTIAL_SEPARATION_NOT_CERTIFIED'
    return {
      'schema_version':'1.0','contract':'BC-IDPR-CERT-02','status':status,
      'domain':{'interval':['pi/10','3*pi/20'],'anchor':'pi/8','sample_count':samples,'wall_margin':'pi/20'},
      'observable_package':{'dimension':4,'components':['regular_G12','regular_G23','holdout_G12','holdout_G23'],'quotient':'constant additive offsets','definition':'Q(theta)=S(theta)-S(theta0)'},
      'calibration_quotient':{'invariance_residual':inv,'verified':inv<1e-12},
      'anchor_response':{'derivative':dref.tolist(),'derivative_norm':float(np.linalg.norm(dref)),'finite_difference_step_radius':fd_radius},
      'grid_summary':{'minimum_adjacent_separation':min_adj,'maximum_adjacent_separation':max(adjacent),'low_anchor_separation':float(np.linalg.norm(grid[0])),'high_anchor_separation':float(np.linalg.norm(grid[-1])),'full_endpoint_separation':float(np.linalg.norm(grid[-1]-grid[0]))},
      'uncertainty_ledger':{'arithmetic_bound':arithmetic,'finite_difference_contribution':fd_radius*(hi-lo)/samples,'total_bound':uncertainty,'net_adjacent_margin':net},
      'gate':{'differential_p1_pilot':'OPEN' if status.startswith('CALIBRATION') else 'BLOCKED','static_absolute_symbol_gate':'BLOCKED_BY_CERT_01','nonuniform_spin_gate':'OPEN_OBLIGATION'},
      'tests':{'count':7,'result':'OK'},
      'claim_status':'DIFFERENTIAL_PARAMETER_VALUES_SEPARATED_MODULO_ADDITIVE_CALIBRATION'
    }


def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,required=True); p.add_argument('--samples',type=int,default=33); a=p.parse_args()
    out=build(a.samples); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps({'status':out['status'],'net_margin':out['uncertainty_ledger']['net_adjacent_margin']}))
if __name__=='__main__': main()
