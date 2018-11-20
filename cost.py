import networkx as nx

"""This is the (decreasing convex) function
   you can modify this for different experiments"""
def f_of(r):
    # return "f(%d)" %r
    return r

def r_value(v,G,sigma):
    index = sigma.index(v)
    neighbors = G.neighbors(v)
    r = len(neighbors)
    for u in neighbors:
        index_u = sigma.index(u)
        if index_u > index:
            r = r - 1
    return r

def cost_function(G,sigma):
    num = dict() # map of number of f(x) and f(x)
    for v in sigma:
        c = f_of(r_value(v,G,sigma))
        if c in num:
            num[c] += 1
        else:
            num[c] = 1
    return num

def print_cost(num):
    function = ""
    cost = 0
    for f in sorted(num.iterkeys()):
        # for f in num:
        #if num[f] == 1:
        #    n = "+"
        #elif num[f] == -1:
        #    n = "-"
        #else:
        #    n = str(num[f])
        #if n[0]!='+' and n[0]!='-':
        #    function += "+"
        #function += str(n)+("f(%d)"%f)
        # function += str(n)+f
        if f != 0:
            cost += (num[f] * 1.0/f)
    #l=len(function)
    #function = 'f(0) + ' + str(cost)
    return cost

def cost_diff(cost1, cost2):
    diff = dict()
    # O(n^2) run time, but shouldn't be too bad
    pos = set(cost1.keys()) - set(cost2.keys())
    neg = set(cost2.keys()) - set(cost1.keys())
    for c in pos:
        diff[c] = cost1[c]
    for c in neg:
        diff[c] = -cost2[c]
    for c in (set(cost1.keys()) & set(cost2.keys())):
        if cost1[c]-cost2[c]!=0:
            diff[c] = cost1[c]-cost2[c]
    return diff


# G = nx.graph()
