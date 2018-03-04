from EnderGraph import Graph
import random

g = Graph() #Declare a new graph
numNodes = eval(input("How many nodes would you like?"))
for k in range(numNodes): 
	g.addNode(k) #Add numNodes nodes
for k in range(numNodes-1):
	for i in range(k+1, numNodes):
		g.addEdge(k, i, random.randint(1,5)) #Create the complete graph of numNodes, with each edge having a weight between 1 and 5
g.removeEdge(*eval(input("Specify an edge to remove in the format [node_a, node_b]"))) #Remove an edge
nodeToCheck = eval(input("What node would you like to check?")) #Node to test functions on
edges = g.getEdgesConnectedToNode(nodeToCheck) #Grab all edges connect to node
print(edges)
edgeToTest = random.choice(edges) #Choose a random edge
g.setEdgeWeight(edgeToTest[0], edgeToTest[1], 10) #Set its weight to 10
print(g.getEdgesConnectedToNode(nodeToCheck)) #Print updated edges
g.display(200,40) #Display graph