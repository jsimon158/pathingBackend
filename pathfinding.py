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


def pathfinding(graph, startNode):
    nodesToVisit = deque()

    visitedNode = []

    shortestPath = {}
    prev = {}

    maxVal = sys.maxsize
    for node in graph.getNodes():
        shortestPath[node] = maxVal

    shortestPath[startNode] = 0

    nodesToVisit.append(startNode)

    while nodesToVisit:
        currentNode = nodesToVisit.popleft()

        visitedNode.append(currentNode)
        edges = graph.getNeighbors(currentNode)

        for edge in edges:
            if edge not in visitedNode:

                nodesToVisit.append(edge)

                if graph.edgeValue(edge, currentNode) + shortestPath[currentNode] < shortestPath[edge]:
                    shortestPath[edge] = graph.edgeValue(edge, currentNode) + shortestPath[currentNode]
                    prev[edge] = currentNode

    return shortestPath, prev


class FindPath(object):
    def __init__(self, graph, startNode):
        self.shortestPaths, self.traceback = pathfinding(graph, startNode)
