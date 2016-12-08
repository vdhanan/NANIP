import networkx as nx
import greedy
G = nx.Graph()
G.add_node(0)
for i in [1,2,3,4,5]:
    G.add_node(i)
    G.add_edge(0,i)

G.add_edge(2,4)
G.add_edge(3,4)

greedy.greedy(G,0)
