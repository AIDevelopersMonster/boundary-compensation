import itertools, math, heapq, time, statistics, platform, json
import csv

# ---------- factor families ----------

def qaoa_path(q, gamma=0.7, beta=0.4, gammas=None, betas=None):
    if gammas is None: gammas=[gamma]*(q-1)
    if betas is None: betas=[beta]*q
    labels=[('C',e) for e in range(q-1)] + [('M',v) for v in range(q)]
    n=len(labels)
    w=[[0.0]*n for _ in range(n)]
    for i,(typ,a) in enumerate(labels):
        for j in range(i+1,n):
            typ2,b=labels[j]
            val=0.0
            if typ=='C' and typ2=='M':
                e,v=a,b
                if v in (e,e+1): val=abs(math.sin(gammas[e]/2.0)*math.sin(betas[v]))
            elif typ=='M' and typ2=='C':
                v,e=a,b
                if v in (e,e+1): val=abs(math.sin(gammas[e]/2.0)*math.sin(betas[v]))
            w[i][j]=w[j][i]=val
    return labels,w

def xyz_chain(L, h=0.25, Jx=1.0, Jy=1.0, Jz=1.0):
    J={'X':Jx,'Y':Jy,'Z':Jz}
    labels=[]
    for b in range(L-1):
        for a in ('X','Y','Z'):
            labels.append((a,b))
    n=len(labels)
    w=[[0.0]*n for _ in range(n)]
    for i,(a,b) in enumerate(labels):
        for j in range(i+1,n):
            c,d=labels[j]
            val=0.0
            if abs(b-d)==1 and a!=c:
                val=abs(math.sin(h*J[a])*math.sin(h*J[c]))
            w[i][j]=w[j][i]=val
    return labels,w

# ---------- permutation geometry ----------

def inv_pairs(sigma,tau):
    pos_s={x:i for i,x in enumerate(sigma)}
    pos_t={x:i for i,x in enumerate(tau)}
    n=len(sigma)
    out=[]
    items=list(sigma)
    for a_idx in range(n):
        a=items[a_idx]
        for b_idx in range(a_idx+1,n):
            b=items[b_idx]
            if (pos_s[a]-pos_s[b])*(pos_t[a]-pos_t[b])<0:
                out.append((a,b))
    return out

def closed_D(sigma,tau,w):
    inv=inv_pairs(sigma,tau)
    return max((w[i][j] for i,j in inv), default=0.0)

def minimax_dijkstra(start,w,target=None,target_pred=None):
    assert (target is None) != (target_pred is None)
    n=len(start)
    best={start:0.0}
    pq=[(0.0,start)]
    popped=0
    while pq:
        d,s=heapq.heappop(pq)
        if d != best[s]: continue
        popped += 1
        if (target is not None and s==target) or (target_pred is not None and target_pred(s)):
            return d,popped
        s=list(s)
        for k in range(n-1):
            a,b=s[k],s[k+1]
            nd=max(d,w[a][b])
            ns=s.copy(); ns[k],ns[k+1]=ns[k+1],ns[k]
            ns=tuple(ns)
            if nd < best.get(ns,float('inf')) - 1e-15:
                best[ns]=nd; heapq.heappush(pq,(nd,ns))
    raise RuntimeError('target unreachable')

# ---------- precedence threshold ----------

def acyclic(n, edges):
    adj=[[] for _ in range(n)]; indeg=[0]*n
    seen=set()
    for u,v in edges:
        if u==v: return False
        if (u,v) in seen: continue
        seen.add((u,v)); adj[u].append(v); indeg[v]+=1
    stack=[i for i,d in enumerate(indeg) if d==0]
    cnt=0
    while stack:
        u=stack.pop(); cnt+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0: stack.append(v)
    return cnt==n

def source_poset_edges(source,w,lam):
    pos={x:i for i,x in enumerate(source)}
    n=len(source); edges=[]
    for i in range(n):
        for j in range(i+1,n):
            if w[i][j] > lam + 1e-15:
                if pos[i]<pos[j]: edges.append((i,j))
                else: edges.append((j,i))
    return edges

def threshold_opt(source,w,Qedges):
    crit=sorted(set([0.0]+[w[i][j] for i in range(len(w)) for j in range(i+1,len(w)) if w[i][j]>0]))
    lo,hi=0,len(crit)-1
    def feasible(lam): return acyclic(len(source), source_poset_edges(source,w,lam)+list(Qedges))
    if feasible(crit[0]): return crit[0]
    while lo<hi:
        mid=(lo+hi)//2
        if feasible(crit[mid]): hi=mid
        else: lo=mid+1
    return crit[lo]

def qaoa_m_before_c_edges(labels):
    Ms=[i for i,x in enumerate(labels) if x[0]=='M']
    Cs=[i for i,x in enumerate(labels) if x[0]=='C']
    return [(m,c) for m in Ms for c in Cs]

def xyz_x_before_y_edges(labels):
    X=[i for i,x in enumerate(labels) if x[0]=='X']
    Y=[i for i,x in enumerate(labels) if x[0]=='Y']
    return [(x,y) for x in X for y in Y]

def target_pred_edges(edges):
    edges=list(edges)
    def pred(state):
        pos={x:i for i,x in enumerate(state)}
        return all(pos[u]<pos[v] for u,v in edges)
    return pred

def reachable_count(source,w,lam):
    strong=source_poset_edges(source,w,lam)
    n=len(source)
    count=0
    for p in itertools.permutations(range(n)):
        pos={x:i for i,x in enumerate(p)}
        if all(pos[u]<pos[v] for u,v in strong): count+=1
    return count

# ---------- timing ----------

def median_time(fn, repeats=100):
    vals=[]; ret=None
    for _ in range(repeats):
        t=time.perf_counter(); ret=fn(); vals.append(time.perf_counter()-t)
    return statistics.median(vals), ret

def median_exhaustive(fn, repeats=3):
    vals=[]; ret=None
    for _ in range(repeats):
        t=time.perf_counter(); ret=fn(); vals.append(time.perf_counter()-t)
    return statistics.median(vals), ret

# ---------- benchmarks ----------

def run():
    fixed=[]; precedence=[]
    for q in [2,3,4,5]:
        labels,w=qaoa_path(q)
        n=len(labels); source=tuple(range(n)); target=tuple(reversed(source))
        t_closed,D=median_time(lambda: closed_D(source,target,w), repeats=2000)
        t_ex,(Dex,popped)=median_exhaustive(lambda: minimax_dijkstra(source,w,target=target), repeats=3)
        assert abs(D-Dex)<1e-12
        fixed.append(['QAOA MaxCut path',q,n,math.factorial(n),D,t_closed,t_ex,popped])
        Q=qaoa_m_before_c_edges(labels)
        t_th,lam=median_time(lambda: threshold_opt(source,w,Q), repeats=1000)
        t_ep,(lam_ex,pop2)=median_exhaustive(lambda: minimax_dijkstra(source,w,target_pred=target_pred_edges(Q)), repeats=3)
        assert abs(lam-lam_ex)<1e-12
        precedence.append(['QAOA MaxCut: mixers before costs',q,n,math.factorial(n),lam,t_th,t_ep,pop2])
    for L in [3,4]:
        labels,w=xyz_chain(L)
        n=len(labels); source=tuple(range(n)); target=tuple(reversed(source))
        t_closed,D=median_time(lambda: closed_D(source,target,w), repeats=2000)
        t_ex,(Dex,popped)=median_exhaustive(lambda: minimax_dijkstra(source,w,target=target), repeats=3)
        assert abs(D-Dex)<1e-12
        fixed.append(['Heisenberg isotropic',L,n,math.factorial(n),D,t_closed,t_ex,popped])

        labels2,w2=xyz_chain(L,Jx=1.0,Jy=0.7,Jz=1.3)
        Q=xyz_x_before_y_edges(labels2)
        t_th,lam=median_time(lambda: threshold_opt(source,w2,Q), repeats=1000)
        t_ep,(lam_ex,pop2)=median_exhaustive(lambda: minimax_dijkstra(source,w2,target_pred=target_pred_edges(Q)), repeats=3)
        assert abs(lam-lam_ex)<1e-12
        precedence.append(['XYZ: all X before all Y',L,n,math.factorial(n),lam,t_th,t_ep,pop2])

    scaling=[]
    for q in [5,10,20,40,80,120,160,240,320]:
        labels,w=qaoa_path(q)
        n=len(labels); source=tuple(range(n)); Q=qaoa_m_before_c_edges(labels)
        reps=200 if q<=80 else 50
        t,lam=median_time(lambda: threshold_opt(source,w,Q), repeats=reps)
        scaling.append([q,n,math.lgamma(n+1)/math.log(10),lam,t])

    labels,w=xyz_chain(4,Jx=1.0,Jy=0.7,Jz=1.3)
    source=tuple(range(len(labels)))
    crit=sorted(set([0.0]+[w[i][j] for i in range(len(w)) for j in range(i+1,len(w)) if w[i][j]>0]))
    filtration=[[lam,reachable_count(source,w,lam)] for lam in crit]

    gammas=[0.25,0.45,0.70,0.95]
    betas=[0.20,0.35,0.50,0.65,0.80]
    labels,w=qaoa_path(5,gammas=gammas,betas=betas)
    source=tuple(range(len(labels)))
    crit_ma=sorted(set([0.0]+[w[i][j] for i in range(len(w)) for j in range(i+1,len(w)) if w[i][j]>0]))
    ma=[[lam,reachable_count(source,w,lam)] for lam in crit_ma]

    def write(name, header, rows):
        with open(name,'w',newline='') as f:
            cw=csv.writer(f); cw.writerow(header); cw.writerows(rows)
    write('operator_order_fixed_target_benchmark_v020.csv', ['family','physical_size','gate_count_n','permutation_states_n_factorial','D_U','closed_form_median_seconds','exhaustive_median_seconds','states_popped'],fixed)
    write('operator_order_precedence_benchmark_v020.csv', ['task_family','physical_size','gate_count_n','permutation_states_n_factorial','lambda_star','threshold_median_seconds','exhaustive_median_seconds','states_popped'],precedence)
    write('operator_order_scaling_v020.csv', ['qaoa_qubits','gate_count_n','log10_n_factorial','lambda_star','threshold_median_seconds'],scaling)
    write('heisenberg_xyz_filtration_v020.csv',['lambda','reachable_permutations'],filtration)
    write('ma_qaoa_filtration_v020.csv',['lambda','reachable_permutations'],ma)

    env={
        'python':platform.python_version(),
        'platform':platform.platform(),
        'processor':platform.processor(),
        'timing':'time.perf_counter; medians; exhaustive 3 repeats, exact repeated as described in script',
        'qaoa_standard':{'gamma':0.7,'beta':0.4,'convention':'C_e=(I-Z_i Z_j)/2; cost factor e^{-i gamma C_e} up to global phase; mixer e^{-i beta X_i}','factor_order':'all path cost factors, then all X mixers'},
        'xyz':{'h':0.25,'isotropic_J':1.0,'anisotropic':{'Jx':1.0,'Jy':0.7,'Jz':1.3},'factor_order':'bond-major X,Y,Z'},
        'ma_qaoa':{'q':5,'gammas':gammas,'betas':betas,'convention':'independent MaxCut clause angles gamma_e and mixer angles beta_v','factor_order':'all path cost factors, then all X mixers'},
    }
    with open('operator_order_benchmark_environment_v020.json','w') as f: json.dump(env,f,indent=2)

if __name__=='__main__': run()
