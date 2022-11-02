from unittest import TestCase

from pathfinding import Graph, pathfinding


class TestGraph(TestCase):
    nodes = ["test", "cat", "dog"]
    graphTest = {"test": {"cat": 5, "dog": 4}, "cat": {"dog": 1}, "dog": {}}

    def test_makeGraph(self):
        graph = Graph(self.nodes, self.graphTest)
        assert graph.graph

    def test_getNeighbors(self):
        graph = Graph(self.nodes, self.graphTest)
        assert graph.getNeighbors("test") == ['cat', 'dog']

    def test_getNodes(self):
        graph = Graph(self.nodes, self.graphTest)
        assert graph.getNodes() == ['test', 'cat', 'dog']

    def test_edgeValues(self):
        graph = Graph(self.nodes, self.graphTest)
        assert graph.edgeValue("test", "cat") == 5


class TestPathfinding(TestCase):
    def test_pathfinding(self):
        nodes = ["test", "cat", "dog"]
        graphTest = {"test": {"cat": 5, "dog": 3}, "cat": {"dog": 1}, "dog": {}}

        graph = Graph(nodes, graphTest)

        pathfinding(graph, "test", "cat")

    def test_pathfindingBigGraph(self):
        nodes = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        graphTest = {"0": {"1": 4, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 8, "8": 0},
                     "1": {"0": 4, "2": 8, "3": 0, "4": 0, "5": 0, "6": 0, "7": 11, "8": 0},
                     "2":{"0":0, "1":8, "3":7, "4":0, "5":4, "6":0, "7":0, "8":2},
                     "3":{"0":0, "1":0, "2":7, "4":9, "5":14, "6":0, "7":0, "8":0},
                     "4":{"0":0, "1":0, "2":0, "3":9, "5":10, "6":0, "7":0, "8":0},
                     "5":{"0":0, "1":0, "2":4, "3":14, "4":10, "6":2, "7":0, "8":0},
                     "6":{"0":0,"1": 0,"2": 0, "3":0, "4":0, "5":2, "7":1, "8":6},
                     "7":{"0":8, "1":11,"2": 0, "3":0, "4":0, "5":0, "6":1, "8":7},
                     "8":{"0":0, "1":0, "2":2, "3":0, "4":0, "5":0, "6":6, "7":7,}}

        graph = Graph(nodes, graphTest)
        pathfinding(graph, "0")
