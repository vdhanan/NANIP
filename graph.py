import networkx as nx
import greedy
import cost
import random
import sys
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
	print "The cost of this order is %s \n" %cost.print_cost(c)

	sigma2 = greedy.percentage_greedy(G,blackstart)
	c2 = cost.cost_function(G, sigma2)

	print "Percentage greedy: \n"
	print "Installation order is %s \n" %sigma2
	print "The cost of this order is %s \n" %cost.print_cost(c2)

	#diff = cost.cost_diff(c,c2)
	#print "cost1 - cost2 is %s"%cost.print_cost(diff)

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

def testK1():
	print "running on K4 to K10 with two edges sharing a vertex removed:"
	for n in range(4,11):
		print n
		Gn = nx.complete_graph(n)
		ran = random.randint(0,n-1)
		Gn.remove_edge(ran,(ran+1)%n)
		Gn.remove_edge((ran+1)%n,(ran+2)%n)
		blackstart = random.randint(0,n-1)
		while(blackstart == ran or blackstart == (ran+1)%n or blackstart == (ran+2)%n):
			blackstart = random.randint(0,n-1)
		print "blackstart is",blackstart
		sig1 = greedy.normal_greedy(Gn,blackstart)
		cos1 = cost.cost_function(Gn,sig1)
		sig2 = greedy.percentage_greedy(Gn,blackstart)
		cos2 = cost.cost_function(Gn,sig2)
		print "Greedy cost for almost complete K", n,  "is", cos1
		# print "PGreedy cost for almost complete K%s is \n" %n 
		# print cos2

def testK2():
	print "running on K4 to K10 with two edges mpt sharing a vertex removed:"
	for n in range(6,20):
		print n
		Gn = nx.complete_graph(n)
		ran = random.randint(0,n-1)
		a = ran
		b = (ran+1)%n
		c = (ran+2)%n
		d = (ran+3)%n
		Gn.remove_edge(a,b)
		Gn.remove_edge(c,d)
		blackstart = random.randint(0,n-1)
		while(blackstart == ran or blackstart == (ran+1)%n or blackstart == (ran+2)%n):
			blackstart = random.randint(0,n-1)
		print "blackstart is",blackstart
		sig1 = greedy.normal_greedy(Gn,blackstart)
		cos1 = cost.cost_function(Gn,sig1)
		sig2 = greedy.percentage_greedy(Gn,blackstart)
		cos2 = cost.cost_function(Gn,sig2)
		print "Greedy cost for almost complete K", n,  "is", cos1
		# print "PGreedy cost for almost complete K%s is \n" %n 
		# print cos2

def testJ1():
	n = random.randint(10,50)
	seq = nx.random_powerlaw_tree_sequence(n,3,None,500)
	tree = nx.degree_sequence_tree(seq)
	a = random.randint(0,n)
	b = random.randint(0,n)
	while(b==a or tree.has_edge(a,b)):
		b = random.randint(0,n)
	tree.add_edge(a,b)
	print "running on a", n, "node tree with (",a,",",b, ") added\n"
	blackstart = random.randint(0,n-1)
	sig1 = greedy.normal_greedy(tree,blackstart)
	cos1 = cost.cost_function(tree,sig1)
	sig2 = greedy.percentage_greedy(tree,blackstart)
	cos2 = cost.cost_function(tree,sig2)
	print "Greedy cost for distinct cycle is", cos1
	# print "PGreedy cost for distinct cycle is", cos2

# for i in range(0,10):
# 	testJ1()

# def minCost(G,blackstart):
	
n = int(sys.stdin.readline())
for i in range(1,n+1):
	print "running on network number %d"%i
	filename = sys.stdin.readline().rstrip('\n')
	parse(filename,1)
