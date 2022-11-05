from chalice import Chalice

from chalicelib.pathfinding import Graph, FindPath

app = Chalice(app_name='pathing')

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


@app.route('/pathfinding', methods=['POST'])
def pathfinding():
    inputs = app.current_request.json_body

    currentLocation = inputs['currentLocation']
    destinationLocation = inputs['destination']

    if currentLocation == destinationLocation:
        return "DestinationSameAsCurrentLocation"

    thisMap = inputs['map']
    thisGraph = mapTest[thisMap]

    nodes = list(thisGraph.keys())
    graph = Graph(nodes, thisGraph)

    findPath = FindPath(graph, currentLocation)

    path = findPath.traverseBack(destinationLocation)

    return path
