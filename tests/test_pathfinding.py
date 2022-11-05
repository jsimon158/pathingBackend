from unittest import TestCase

from chalicelib.pathfinding import Graph, FindPath


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


class TestFindPath(TestCase):
    def test_pathfindingBigGraph(self):
        nodes = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        graphTest = {"0": {"1": 4, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 8, "8": 0},
                     "1": {"0": 4, "2": 8, "3": 0, "4": 0, "5": 0, "6": 0, "7": 11, "8": 0},
                     "2": {"0": 0, "1": 8, "3": 7, "4": 0, "5": 4, "6": 0, "7": 0, "8": 2},
                     "3": {"0": 0, "1": 0, "2": 7, "4": 9, "5": 14, "6": 0, "7": 0, "8": 0},
                     "4": {"0": 0, "1": 0, "2": 0, "3": 9, "5": 10, "6": 0, "7": 0, "8": 0},
                     "5": {"0": 0, "1": 0, "2": 4, "3": 14, "4": 10, "6": 2, "7": 0, "8": 0},
                     "6": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 2, "7": 1, "8": 6},
                     "7": {"0": 8, "1": 11, "2": 0, "3": 0, "4": 0, "5": 0, "6": 1, "8": 7},
                     "8": {"0": 0, "1": 0, "2": 2, "3": 0, "4": 0, "5": 0, "6": 6, "7": 7, }}

        graph = Graph(nodes, graphTest)
        findPath = FindPath(graph, "0")
        findPath.pathfinding()

        assert findPath.traceback == {'1': '0', '7': '0', '2': '1', '6': '7', '8': '2', '3': '2', '5': '6', '4': '5'}
        assert findPath.shortestPaths == {'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}

    def test_traverseToNode(self):
        nodes = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        graphTest = {"0": {"1": 4, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 8, "8": 0},
                     "1": {"0": 4, "2": 8, "3": 0, "4": 0, "5": 0, "6": 0, "7": 11, "8": 0},
                     "2": {"0": 0, "1": 8, "3": 7, "4": 0, "5": 4, "6": 0, "7": 0, "8": 2},
                     "3": {"0": 0, "1": 0, "2": 7, "4": 9, "5": 14, "6": 0, "7": 0, "8": 0},
                     "4": {"0": 0, "1": 0, "2": 0, "3": 9, "5": 10, "6": 0, "7": 0, "8": 0},
                     "5": {"0": 0, "1": 0, "2": 4, "3": 14, "4": 10, "6": 2, "7": 0, "8": 0},
                     "6": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 2, "7": 1, "8": 6},
                     "7": {"0": 8, "1": 11, "2": 0, "3": 0, "4": 0, "5": 0, "6": 1, "8": 7},
                     "8": {"0": 0, "1": 0, "2": 2, "3": 0, "4": 0, "5": 0, "6": 6, "7": 7, }}

        graph = Graph(nodes, graphTest)

        findPath = FindPath(graph, "0")
        findPath.pathfinding()

        assert findPath.traverseBack("8") == ['0', '1', '2', '8']

    def test_pathfindingTraversalCallsPathfinding(self):
        nodes = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        graphTest = {"0": {"1": 4, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 8, "8": 0},
                     "1": {"0": 4, "2": 8, "3": 0, "4": 0, "5": 0, "6": 0, "7": 11, "8": 0},
                     "2": {"0": 0, "1": 8, "3": 7, "4": 0, "5": 4, "6": 0, "7": 0, "8": 2},
                     "3": {"0": 0, "1": 0, "2": 7, "4": 9, "5": 14, "6": 0, "7": 0, "8": 0},
                     "4": {"0": 0, "1": 0, "2": 0, "3": 9, "5": 10, "6": 0, "7": 0, "8": 0},
                     "5": {"0": 0, "1": 0, "2": 4, "3": 14, "4": 10, "6": 2, "7": 0, "8": 0},
                     "6": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 2, "7": 1, "8": 6},
                     "7": {"0": 8, "1": 11, "2": 0, "3": 0, "4": 0, "5": 0, "6": 1, "8": 7},
                     "8": {"0": 0, "1": 0, "2": 2, "3": 0, "4": 0, "5": 0, "6": 6, "7": 7, }}

        graph = Graph(nodes, graphTest)
        findPath = FindPath(graph, "0")
        assert findPath.traverseBack("7") == ['0', '7']

    def test_failPathfinding(self):
        with self.assertRaises((TypeError, AttributeError)):
            FindPath.pathfinding()
