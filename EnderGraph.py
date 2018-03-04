import turtle
import math

class Graph:
	def __init__(self):
		self.__edges = [] #An edge is a relationship between two nodes. it is defined as: [node_a, node_b, weight] with weight defaulting to 1
		self.__nodes = [] #A node is defined to be any 1 object.
		self.__isWeighted = False
		pass
	
	def getNodes(self):
		return self.__nodes[:]
	
	def addNode(self, node):
		if node in self.__nodes:
			raise(ValueError(str(node) + " is already in the graph!"))
		else:
			self.__nodes.append(node)
	
	def addEdge(self, node_a, node_b, weight=1):
		if self.checkEdge != -1 and node_a in self.__nodes and node_b in self.__nodes:
			self.__edges.append([node_a, node_b, weight])
			if(weight!=1):
				self.__isWeighted = True
	
	def removeEdge(self, node_a, node_b):
		edgeIndex = self.checkEdge(node_a, node_b)
		if(edgeIndex == -1):
			raise(IndexError("You cannot remove an edge that does not exist!"))
		else:
			del self.__edges[edgeIndex]
	
	def getEdges(self):
		return self.__edges[:]
	
	def getEdgesConnectedToNode(self, node):
		pass #NOT YET IMPLEMENTED
	
	def getNodeDegrees(self, node):
		pass #NOT YET IMPLEMENTED
	
	def setEdgeWeight(self, node_a, node_b):
		pass #NOT YET IMPLEMENTED
	
	def makeComplete(self):
		numNodes = len(self.__nodes)
		for k in range(numNodes-1):
			for i in range(k+1, numNodes):
				if(self.checkEdge(self.__nodes[k], self.__nodes[i]) == -1):
					self.addEdge(self.__nodes[k], self.__nodes[i])
				
	
	def checkEdge(self, node_a, node_b):
		for i, edge in enumerate(self.__edges):
			if edge[0] == node_a and edge[1] == node_b:
				return i
			elif edge[1] == node_a and edge[0] == node_b:
				return i
		return -1
		
	def display(self, spread = 200, nodeSize = 20):
		'''(spread, nodeSize) where spread is the radius of the inner circle, and nodeSize is the radius of node's'''
		screen = turtle.Screen() #Create a screen
		pen = turtle.RawPen(screen) #Create a turtle
		pen.speed(10000) #Fast moving
		screen.tracer(0,0) #Don't update until told.
		nodeCoordinates = {} # FORMAT: {node = Vec2}
		numNodes = len(self.__nodes)
		for i, node in enumerate(self.__nodes):
			#DRAWING
			pen.pu() #Pick up pen
			pen.home() #Move to center of screen
			currentNodePercent = i/numNodes #Percentage of way through nodes at i index
			pen.left(currentNodePercent*360) #Rotate that percent through the circle
			pen.forward(spread) #Move spread px out from center
			pen.seth(0) #Reset angle
			pen.pd() #Start Drawing
			pen.circle(nodeSize) #Draw circle with radius nodeSize
			#SAVE INFORMATION
			pen.pu() #Stop drawing
			pen.sety(pen.ycor()+nodeSize) #Move to center of circle
			nodeCoordinates[node]= pen.position() #save coordinates
			print(nodeCoordinates[node]) #Print for debugging
			pen.sety(pen.ycor()-4)
			pen.write(node, align="center") #Write contents of node to string.
		for edge in self.__edges:
			print(edge) #Print for debugging
			pen.pu() #Stop Drawing
			pen.setpos(nodeCoordinates[edge[0]]) #Go to center of node_a
			pen.seth(pen.towards(nodeCoordinates[edge[1]])) #Look at node_b
			pen.forward(nodeSize) #Move to edge of node_a's circle
			pen.pd() #Start Drawing
			#Move towards node_b, stopping 10 px before you reach coordinates
			if not(self.__isWeighted):
				pen.forward(math.sqrt((pen.position()-nodeCoordinates[edge[1]])[0]**2+(pen.position()-nodeCoordinates[edge[1]])[1]**2)-nodeSize)
			else:
				pen.forward((math.sqrt((pen.position()-nodeCoordinates[edge[1]])[0]**2+(pen.position()-nodeCoordinates[edge[1]])[1]**2)-nodeSize)/2) #Move halfway
				pen.write(edge[2]) #Display edge weight
				pen.forward(math.sqrt((pen.position()-nodeCoordinates[edge[1]])[0]**2+(pen.position()-nodeCoordinates[edge[1]])[1]**2)-nodeSize)
				
			pen.pu() #Stop drawing
		pen.ht() #Hide turtle
		screen.update() #Display results
		screen.exitonclick()