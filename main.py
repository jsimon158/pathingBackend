from flask import Flask
from flask_restful import Api

import pathfindingEndpoint

app = Flask(__name__)
api = Api(app)

api.add_resource(pathfindingEndpoint.PathfindingEndpoint, '/pathfinding')

if __name__ == '__main__':
    app.run()
