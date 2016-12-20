import networkx as nx

"""This is the (decreasing convex) function
   you can modify this for different experiments"""
def f_of(r):
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
    cost = 0
    for v in sigma:
        cost+=f_of(r_value(v,G,sigma))
    return cost
