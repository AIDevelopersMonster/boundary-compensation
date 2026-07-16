#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'p3' / 'operator_envelope' / 'src'))
from coherent_symbol_bridge import geometry, projected_coefficients, raw_symbol, target

PROTOCOLS=('regular_anchor_offset','zero_offset','midpoint_anchor_offset','holdout_anchor_offset')

def build(samples: int = 33):
    a=math.pi/8; lo=math.pi/10; hi=3*math.pi/20
    reg=geometry([(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)])
    hold=geometry([(1.1,1.7,2.6),(1.1,-1.7,-2.6),(-1.1,1.7,-2.6),(-1.1,-1.7,2.6)])
    rn=reg['normals']; hn=hold['normals']
    cr,ch=projected_coefficients(rn),projected_coefficients(hn)
    tr,th=target(rn),target(hn)
    raw_ra,raw_ha=raw_symbol(cr,a),raw_symbol(ch,a)
    offsets={
      'regular_anchor_offset':tr-raw_ra,
      'zero_offset':np.zeros(2),
      'midpoint_anchor_offset':0.5*((tr-raw_ra)+(th-raw_ha)),
      'holdout_anchor_offset':th-raw_ha,
    }
    grid=np.linspace(lo,hi,samples)
    rows={}
    for name,b in offsets.items():
        sr=np.array([raw_symbol(cr,t)+b for t in grid]); sh=np.array([raw_symbol(ch,t)+b for t in grid])
        ar,ah=raw_ra+b,raw_ha+b
        rows[name]={
          'max_regular_response_from_anchor':float(np.max(np.linalg.norm(sr-ar,axis=1))),
          'max_holdout_response_from_anchor':float(np.max(np.linalg.norm(sh-ah,axis=1))),
          'max_regular_mismatch':float(np.max(np.linalg.norm(sr-tr,axis=1))),
          'max_holdout_mismatch':float(np.max(np.linalg.norm(sh-th,axis=1))),
          'anchor_regular_mismatch':float(np.linalg.norm(ar-tr)),
          'anchor_holdout_mismatch':float(np.linalg.norm(ah-th)),
        }
    base=np.array([raw_symbol(ch,t)+offsets['regular_anchor_offset'] for t in grid])
    alt=np.stack([np.array([raw_symbol(ch,t)+b for t in grid]) for b in offsets.values()])
    ia=int(np.argmin(np.abs(grid-a)))
    response=np.linalg.norm(base-base[ia],axis=1)
    mismatch=np.linalg.norm(base-th,axis=1)
    protocol_radius=np.max(np.linalg.norm(alt-base[None,:,:],axis=2),axis=0)
    net=response-mismatch-protocol_radius
    status='SEPARATION_NOT_CERTIFIED' if float(np.max(net))<=0 else 'SEPARATION_CERTIFIED_ON_GRID'
    return {
      'schema_version':'1.0','contract':'BC-IDPR-CERT-01','status':status,
      'domain':{'interval':['pi/10','3*pi/20'],'anchor':'pi/8','sample_count':samples,'wall_margin':'pi/20'},
      'protocol_family':list(PROTOCOLS),'protocol_results':rows,
      'uncertainty_ledger':{'arithmetic_uncertainty':'below displayed decimal precision for this finite calculation','finite_difference_uncertainty':'not used in the decision statistic','symbol_mismatch':'holdout lower-symbol mismatch','protocol_variation':'maximum displacement over four frozen additive calibrations','external_geometry_leakage':'zero by M3','nuisance_equivalence_margin':'positive by M2/M3 but not convertible into lower-symbol units without an additional Lipschitz bridge'},
      'decision':{'response_definition':'holdout lower-symbol displacement from nearest-grid anchor','error_budget':'holdout mismatch plus maximum alternative frozen-calibration displacement','max_response':float(np.max(response)),'min_holdout_mismatch':float(np.min(mismatch)),'max_protocol_radius':float(np.max(protocol_radius)),'maximum_net_margin':float(np.max(net)),'minimum_net_margin':float(np.min(net)),'p1_gate':'BLOCKED'},
      'claim_status':'NONZERO_PROTOCOL_RESPONSE_BUT_NO_POSITIVE_OBSERVABLE_SEPARATION_MARGIN'
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,required=True); p.add_argument('--samples',type=int,default=33); a=p.parse_args()
    out=build(a.samples); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps({'status':out['status'],'maximum_net_margin':out['decision']['maximum_net_margin']}))
if __name__=='__main__': main()
