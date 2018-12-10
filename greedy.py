import networkx as nx
import heapq
import numpy

# assume cost function is decreasing convex
def normal_greedy(G, blackstart):
    """
     conducts a greedy on the given graph G with blackstart and
     size n using given heuristic f
     installs nodes that have the lowest installation cost,
     which is to say, nodes that have the most installed neighbors
     """
    toInstall = [] # priority queue for things to be visited
    order = [] # order of installation given by this algorithm
    element_finder = {} # mapping of nodes to pairs (num_installed, node)

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
                    toInstall.remove(pair)
                    element_finder.pop(n)
                    # push the relaxed value, minus one since we use -numNeighbor as priority
                    newPair = (numN-1,n)
                else:
                    newPair = (-1,n)
                element_finder[n] = newPair
                heapq.heappush(toInstall, newPair)

    return order

def normal_greedy_random(G, blackstart):
    """
     conducts a greedy on the given graph G with blackstart and
     size n using given heuristic f
     installs nodes that have the lowest installation cost,
     which is to say, nodes that have the most installed neighbors
     """
    toInstall = [] # priority queue for things to be visited
    order = [] # order of installation given by this algorithm
    element_finder = {} # mapping of nodes to pairs (num_installed, node)

    #put the blackstart in
    elt = (0,blackstart)
    element_finder[blackstart] = elt
    heapq.heappush(toInstall, elt)

    # while there are node to install
    while toInstall:
        # pop out the(a) node with lowest cost
        list_nip = numpy.array(zip(*toInstall)[0])
        list_nip_size = len(list_nip)
        if list_nip_size == 1:
            cur = heapq.heappop(toInstall)[1]
        else:
            list_nip_size_float = float(list_nip_size)
            list_nip = (list_nip / list_nip_size_float) * -1
            next_cur = numpy.random.choice(range(list_nip_size), 1, list_nip.tolist())
            cur = toInstall[next_cur][1]
            node_removed = toInstall[next_cur]
            toInstall.remove(node_removed)
            heapq.heapify(toInstall)
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
                    toInstall.remove(pair)
                    element_finder.pop(n)
                    # push the relaxed value, minus one since we use -numNeighbor as priority
                    newPair = (numN-1,n)
                else:
                    newPair = (-1,n)
                element_finder[n] = newPair
                heapq.heappush(toInstall, newPair)
    print len(order)
    return order

# assume cost function is decreasing convex
def percentage_greedy(G, blackstart):
    """
     conducts a greedy on the given graph G with blackstart and
     size n using given heuristic f
     installs nodes that have the lowest installation percentage cost,
     which is to say, nodes that have the most installed neighbor percentage
     """
    toInstall = [] # priority queue for things to be visited
    order = [] # order of installation given by this algorithm
    element_finder = {} # mapping of nodes to (num_installed, node)
    percent_finder = {} # mapping of nodes to (percentage_installed, node)

    #put the blackstart in
    elt = (0,blackstart)
    element_finder[blackstart] = elt
    percent_finder[blackstart] = elt
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
                    pair = percent_finder[n]
                    numN = element_finder[n][0]
                    # print (n,numN)
                    # remove pair from heap and dict
                    toInstall.remove(pair)
                    element_finder.pop(n)
                    percent_finder.pop(n)
                    numNeighbor = len(G.neighbors(n))
                    # print (n, numNeighbor)
                    newPerPair = ((numN-1.0)/numNeighbor,n)
                    newNumPair = (numN-1,n)
                else:
                    numNeighbor = len(G.neighbors(n))
                    # print (n,numNeighbor)
                    newPerPair = (-1.0/numNeighbor,n)
                    newNumPair = (-1,n)
                element_finder[n] = newNumPair
                percent_finder[n] = newPerPair
                heapq.heappush(toInstall, newPerPair)

    return order
