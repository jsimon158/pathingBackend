import sys
from collections import deque


class Graph(object):

    def __init__(self, nodes, graph):
        self.nodes = nodes
        self.graph = self.makeGraph(nodes, graph)

    def makeGraph(self, nodes, initialGraph):

        graph = {}
        for i in nodes:
            graph[i] = {}

        graph.update(initialGraph)

        for node, edges in graph.items():
            for neighbor_node, val in edges.items():
                if not graph[neighbor_node].get(node, False):
                    graph[neighbor_node][node] = val

        return graph

    def getNodes(self):
        return self.nodes

    def getNeighbors(self, node):
        neighbors = []
        for neighbor in self.nodes:
            if self.graph[node].get(neighbor, False):
                neighbors.append(neighbor)

        return neighbors

    def edgeValue(self, node1, node2):
        return self.graph[node1][node2]


class FindPath(object):
    def __init__(self, graph, startNode=None):
        self.startNode = startNode
        self.graph = graph
        self.startNode = startNode

        self.shortestPaths, self.traceback = None, None

    def traverseBack(self, destinationNode):
        if self.traceback is None:
            print("Pathfinding function has not run, attempting to run it now")
            self.pathfinding()

        path = [destinationNode]

        while self.traceback[destinationNode] is not self.startNode:
            destinationNode = self.traceback[destinationNode]
            path.append(destinationNode)

        path.append(self.startNode)

        return path[::-1]

    def pathfinding(self, startNode=None):
        if startNode is not None:
            self.startNode = startNode
        elif startNode is None and self.startNode is None:
            return "Error, no start node defined"

        nodesToVisit = deque()

        visitedNode = []

        shortestPath = {}
        self.traceback = {}

        maxVal = sys.maxsize
        for node in self.graph.getNodes():
            shortestPath[node] = maxVal

        shortestPath[self.startNode] = 0

        nodesToVisit.append(self.startNode)

        while nodesToVisit:
            currentNode = nodesToVisit.popleft()

            visitedNode.append(currentNode)
            edges = self.graph.getNeighbors(currentNode)

            for edge in edges:
                if edge not in visitedNode:

                    nodesToVisit.append(edge)

                    if self.graph.edgeValue(edge, currentNode) + shortestPath[currentNode] < shortestPath[edge]:
                        shortestPath[edge] = self.graph.edgeValue(edge, currentNode) + shortestPath[currentNode]
                        self.traceback[edge] = currentNode

        self.shortestPaths = shortestPath
