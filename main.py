import networkx as nx
import greedy
import cost

G = nx.Graph()
G.add_node(0)
for i in [1,2,3,4,5]:
    G.add_node(i)
    G.add_edge(0,i)

G.add_edge(2,4)
G.add_edge(3,4)

order = greedy.greedy(G,0)
cost = cost.cost_function(G,order)
print cost
