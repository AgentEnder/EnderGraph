import math
import turtle


class Graph:
    def __init__(self):
        self.__edges = []  # An edge is a relationship between two nodes. it is defined as: [node_a, node_b, weight] with weight defaulting to 1
        self.__nodes = []  # A node is defined to be any 1 object.
        self.__isWeighted = True
        self.__debug = False
        pass

    def get_nodes(self):
        return self.__nodes[:]

    def add_node(self, node):
        if node in self.__nodes:
            raise (ValueError(str(node) + " is already in the graph!"))
        else:
            self.__nodes.append(node)

    def remove_node(self, node):
        self.clear_node(node)
        self.__nodes.remove(node)

    def clear_node(self, node):
        indices_to_remove = []
        for edge in self.get_edges_by_node(node):
            indices_to_remove.append(self.check_edge(edge[0], edge[1])[0])
        for idx in sorted(indices_to_remove, reverse=True):
            del self.__edges[idx]

    def add_edge(self, node_a, node_b, weight=1):
        if self.check_edge(node_a, node_b)[0] == -1 and node_a in self.__nodes and node_b in self.__nodes:
            self.__edges.append([node_a, node_b, weight])
            if weight != 1:
                self.__isWeighted = True

    def remove_edge(self, node_a, node_b):
        edge_index = self.check_edge(node_a, node_b)[0]
        if edge_index == -1:
            if self.__debug :
                print(IndexError("You cannot remove an edge that does not exist!"))
        else:
            del self.__edges[edge_index]

    def get_edges(self):
        return self.__edges[:]

    def get_edges_by_node(self, node):
        edges = []
        for edge in self.__edges:
            if node == edge[0] or node == edge[1]:
                edges.append(edge[:])  # Append a copy of the edge to edges
        return edges

    def get_node_degree(self, node):
        return len(self.get_edges_by_node(node))

    def set_edge_weight(self, node_a, node_b, weight):
        if not self.__isWeighted: self.__isWeighted = True
        edge_index = self.check_edge(node_a, node_b)[0]
        if edge_index == -1:
            raise (IndexError("Edge does not exist!"))
        else:
            self.__edges[edge_index][2] = weight

    def make_complete(self):
        num_nodes = len(self.__nodes)
        for k in range(num_nodes - 1):
            for i in range(k + 1, num_nodes):
                if self.check_edge(self.__nodes[k], self.__nodes[i])[0] == -1:
                    self.add_edge(self.__nodes[k], self.__nodes[i])

    def check_edge(self, node_a, node_b):
        for i, edge in enumerate(self.__edges):
            if edge[0] == node_a and edge[1] == node_b:
                return [i, edge[2]]
            elif edge[1] == node_a and edge[0] == node_b:
                return [i, edge[2]]
        return [-1, 0]

    def print_edges(self):
        for edge in self.__edges:
            print("Node 1(" + str(edge[0]) + ")| Node 2 ("  + str(edge[1]) + ")| Weight(" + str(edge[2]) + ")")

    def calculate_avg_weight(self):
        sum = 0
        for edge in self.__edges:
            sum += edge[2]
        return sum/len(self.__edges)

    def get_max_weight(self):
        return max([x[2] for x in self.__edges])

    def display(self, spread=200, node_size=20):
        '''(spread, nodeSize) where spread is the radius of the inner circle, and nodeSize is the radius of node's'''
        screen = turtle.Screen()  # Create a screen
        turtle.TurtleScreen._RUNNING = True
        pen = turtle.RawPen(screen)  # Create a turtle
        pen.speed(10000)  # Fast moving
        screen.tracer(0, 0)  # Don't update until told.
        node_coordinates = {}  # FORMAT: {node = Vec2}
        num_nodes = len(self.__nodes)
        for i, node in enumerate(self.__nodes):
            # DRAWING
            pen.pu()  # Pick up pen
            pen.home()  # Move to center of screen
            current_node_percent = i / num_nodes  # Percentage of way through nodes at i index
            pen.left(current_node_percent * 360)  # Rotate that percent through the circle
            pen.forward(spread)  # Move spread px out from center
            pen.seth(0)  # Reset angle
            pen.pd()  # Start Drawing
            pen.circle(node_size)  # Draw circle with radius nodeSize
            # SAVE INFORMATION
            pen.pu()  # Stop drawing
            pen.sety(pen.ycor() + node_size)  # Move to center of circle
            node_coordinates[node] = pen.position()  # save coordinates
            if self.__debug:
                print(node_coordinates[node])  # Print for debugging
            pen.sety(pen.ycor() - 4)
            pen.write(node, align="center")  # Write contents of node to string.
        for edge in self.__edges:
            if self.__debug:
                print(edge)  # Print for debugging
            pen.pu()  # Stop Drawing
            pen.setpos(node_coordinates[edge[0]])  # Go to center of node_a
            pen.seth(pen.towards(node_coordinates[edge[1]]))  # Look at node_b
            pen.forward(node_size)  # Move to edge of node_a's circle
            pen.pd()  # Start Drawing
            # Move towards node_b, stopping 10 px before you reach coordinates
            if not self.__isWeighted:
                pen.forward(math.sqrt(
                    (pen.position() - node_coordinates[edge[1]])[0] ** 2 + (pen.position() - node_coordinates[edge[1]])[
                        1] ** 2) - node_size)
            else:
                pen.forward((math.sqrt(
                    (pen.position() - node_coordinates[edge[1]])[0] ** 2 + (pen.position() - node_coordinates[edge[1]])[
                        1] ** 2) - node_size) / 2)  # Move halfway
                pen.write(edge[2])  # Display edge weight
                pen.forward(math.sqrt(
                    (pen.position() - node_coordinates[edge[1]])[0] ** 2 + (pen.position() - node_coordinates[edge[1]])[
                        1] ** 2) - node_size)

            pen.pu()  # Stop drawing
        pen.ht()  # Hide turtle
        screen.update()  # Display results
        screen.exitonclick()
        screen = None
        del pen

