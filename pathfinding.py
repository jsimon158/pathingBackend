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

