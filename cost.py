import networkx as nx

"""This is the (decreasing convex) function
   you can modify this for different experiments"""
def f_of(r):
    return "f(%d)" %r

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
    function = ""
    for f in num:
        if num[f] == 1:
            n = ""
        else:
            n = num[f]
        function += str(n)+f
        function += "+"
    return function