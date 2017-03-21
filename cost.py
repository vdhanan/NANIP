import networkx as nx

<<<<<<< HEAD
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
=======
def cost_function(r):
    pass

def r_value(v,G,sigma):
    
>>>>>>> 1d4c5b9d7381fe6eb3fe788c818c6407e4c17b3b
