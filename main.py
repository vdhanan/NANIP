import networkx as nx
import greedy
import cost

G = nx.Graph()
G.add_node(0)
for i in [1,2,3,4,5,6]:
    G.add_node(i)

G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(2,5)
G.add_edge(2,6)

G.add_edge(1,2)
G.add_edge(3,4)

order = greedy.greedy(G,0)
cost = cost.cost_function(G,[0,1,3,2,4,5,6])
print cost
