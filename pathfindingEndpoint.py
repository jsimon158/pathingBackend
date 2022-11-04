from flask_restful import Resource, reqparse
from pathfinding import FindPath, Graph

mapTest = {"firstMap": {"0": {"1": 4, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 8, "8": 0},
                     "1": {"0": 4, "2": 8, "3": 0, "4": 0, "5": 0, "6": 0, "7": 11, "8": 0},
                     "2": {"0": 0, "1": 8, "3": 7, "4": 0, "5": 4, "6": 0, "7": 0, "8": 2},
                     "3": {"0": 0, "1": 0, "2": 7, "4": 9, "5": 14, "6": 0, "7": 0, "8": 0},
                     "4": {"0": 0, "1": 0, "2": 0, "3": 9, "5": 10, "6": 0, "7": 0, "8": 0},
                     "5": {"0": 0, "1": 0, "2": 4, "3": 14, "4": 10, "6": 2, "7": 0, "8": 0},
                     "6": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 2, "7": 1, "8": 6},
                     "7": {"0": 8, "1": 11, "2": 0, "3": 0, "4": 0, "5": 0, "6": 1, "8": 7},
                     "8": {"0": 0, "1": 0, "2": 2, "3": 0, "4": 0, "5": 0, "6": 6, "7": 7, }}
           }

class PathfindingEndpoint(Resource):

    def get(self):
        return "Hello"


    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('map', required=True)
        parser.add_argument('currentLocation', required=True)
        parser.add_argument('destination', required=True)

        # parse arguments to dictionary
        args = parser.parse_args()

        # map will be a key to an internal map ?
        thisMap = args['map']
        thisGraph = mapTest[thisMap]

        nodes = list(thisGraph.keys())
        graph = Graph(nodes, thisGraph)

        findPath = FindPath(graph, args['currentLocation'])

        path = findPath.traverseBack(args['destination'])

        return path
