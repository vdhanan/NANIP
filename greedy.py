import networkx as nx
import heapq

# assume cost function is decreasing convex
def greedy(G, blackstart):
    """
     conducts a greedy on the given graph G with blackstart and
     size n using given heuristic f
     installs nodes that have the lowest installation cost,
     which is to say, nodes that have the most installed neighbors
     """
    toInstall = [] # priority queue for things to be visited
    order = [] # order of installation given by this algorithm
    element_finder = {} # mapping of nodes to pairs [IS THIS NECESSARY?]

    #put the blackstart in
    elt = (0,blackstart)
    element_finder[blackstart] = elt
    heapq.heappush(toInstall, elt)

    # while there are node to install
    while toInstall:
        # pop out the(a) node with lowest cost
        cur = heapq.heappop(toInstall)[1]
        order.append(cur)

        # for each of cur's neighbors, if it's not in toInstall, add it, otherwise update
        nb = G.neighbors(cur)
        for n in nb:
            if(n not in order):
                if toInstall and n in zip(*toInstall)[1]:
                    # get the pair and the number of neighbors installed
                    pair = element_finder[n]
                    numN = pair[0]
                    # remove pair from heap and dict
                    toInstall.remove(element_finder[n])
                    element_finder.pop(n)
                    # push the relaxed value, minus one since we use -numNeighbor as priority
                    newPair = (numN-1,n)
                else:
                    newPair = (-1,n)
                element_finder[n] = newPair
                heapq.heappush(toInstall, newPair)

    print order
        
        
