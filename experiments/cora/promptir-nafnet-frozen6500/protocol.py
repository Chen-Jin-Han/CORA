from common import DEGS

def jobs(c):
    out=[]
    for t in c['tasks']:
        out.append((t,'clean',None,'clean'))
        for method in ['raw','aco','smfa']:
            out.append((t,'markov',None,method))
            out.extend((t,'single',k,method) for k,_ in DEGS)
    return out
