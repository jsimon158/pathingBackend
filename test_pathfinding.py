from unittest import TestCase

from pathfinding import Graph


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
