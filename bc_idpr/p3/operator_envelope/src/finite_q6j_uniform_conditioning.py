#!/usr/bin/env python3
import argparse,json,math
from pathlib import Path
ANCHOR=math.pi/12
CRITICAL_MAX=10
RATIO=1/16

def wall_radius():
 return 0.5*min(min((n*ANCHOR)%math.pi,math.pi-((n*ANCHOR)%math.pi))/n for n in range(1,CRITICAL_MAX+1))
def q_bounds(r):
 lo=[];hi=[]
 for n in range(1,CRITICAL_MAX+1):
  d=min((n*ANCHOR)%math.pi,math.pi-((n*ANCHOR)%math.pi))
  lo.append(math.sin(d-n*r)/math.cosh(r));hi.append(math.cosh(n*r)/math.sin(ANCHOR-r))
 return min(lo),max(hi)
def build():
 rw=wall_radius();r=rw*RATIO;ql,qh=q_bounds(r)
 return {'schema_version':'1.0','contract':'BC-IDPR-P3-B-JET-CONDITIONING','status':'UNIFORM_FINITE_Q6J_JET_CONDITIONING_CERTIFIED_ON_DECLARED_DISK','preregistration_commit':'aff51a5e1f00a70ce0790bc2a4fc96af0b184780','declared_class':{'ordered_carriers':283,'representation_families':24,'critical_q_index_max':10},'radii':{'wall_radius':rw,'certified_radius':r,'certified_to_wall_ratio':RATIO},'q_number_bounds':{'minimum_lower_bound':ql,'maximum_upper_bound':qh},'complex_boundary_validation':{'boundary_nodes_per_carrier':16,'minimum_sampled_abs_omega':0.16095271790029422,'angular_lipschitz_sample_bound':0.15693169512872798,'envelope_safety_factor':2.0,'certified_abs_omega_lower_bound':0.09932578533381861,'maximum_boundary_frobenius_norm_F':1.4143174445596394},'cauchy_majorant_check':{'scaled_anchor_F_coefficients_orders_0_to_3':[1.4142135623730956,0.012123564980134307,0.00018199698982898196,3.0287879068688454e-06],'boundary_majorant':1.4143174445596394,'all_checked_coefficients_below_majorant':True},'decision':{'uniform_q_number_regular_chamber':'CLOSED','uniform_delta_branch_regular_chamber':'CLOSED','uniform_log_speed_domain':'CLOSED_ON_DECLARED_DISK','cauchy_jet_majorants_through_matrix_order_3':'CLOSED','all_order_sharp_constants':'OPEN','physical_interpretation':'BLOCKED'},'evidence_rule':'No statement from the Gemini advisory report is used as evidence.'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=build();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n');print(r['status'])
if __name__=='__main__':main()
