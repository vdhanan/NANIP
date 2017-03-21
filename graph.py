import networkx as nx
import greedy
import cost
import random
# import matplotlib.pyplot as plt


# In MM, the first line has row, column, edge weight
# for now we don't care about the weight
def parse(file,blackstart):
	G = nx.Graph()
	
	""" read in a file and create the corresponding graph """
	print("\nReading input file...\n")
	f = open (file, 'r')

	# skip lines starting with %, those are comments
	param = f.readline()
	while(param[0]=='%'):
		param = f.readline()
	
	params = param.split()
	# print "params are %s \n" %params
	if len(params) != 3 or params[0] != params[1] :
		print "\nInterrupted: \nFile not clean, please double check.\n"
		return
	numNode = int(params[0])
	numEdge = int(params[2])
	for index in range (0, numEdge):
		newEdge = f.readline().split()
		# we don't accept edges from v to v itself
		if int(newEdge[0]) != int(newEdge[1]):
			G.add_edge(int(newEdge[0]),int(newEdge[1]))

	# if G.number_of_nodes()!= numNode or G.number_of_edges()!=numEdge-numNode:
	# 	print("Parsing error")
	# 	return

	# nx.draw(G)
	# plt.savefig("path.png")
	sigma = greedy.normal_greedy(G,blackstart)
	c = cost.cost_function(G, sigma)

	print "Normal greedy: \n"
	print "Installation order is %s \n" %sigma
	print "The cost of this order is %s \n" %c

	sigma2 = greedy.percentage_greedy(G,blackstart)
	c2 = cost.cost_function(G, sigma2)

	print "Percentage greedy: \n"
	print "Installation order is %s \n" %sigma2
	print "The cost of this order is %s \n" %c2

	# read in the number of rows and columns and number of edges


# test using random trees
# seems to be working
def test():
	n = random.randint(10,200)
	seq = nx.random_powerlaw_tree_sequence(n,3,None,500)
	g = nx.degree_sequence_tree(seq)
	sig = greedy.normal_greedy(g,random.randint(0,n))
	cos = cost.cost_function(g,sig)
	print n
	print "Installation order is %s \n" %sig
	print "The cost of this order is %s \n" %cos

def minCost(
