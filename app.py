from flask import Flask, request
from flask import request
from controllers.GrafanaController import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Grafana_Search, '/grafana/search')
api.add_resource(Grafana_Data, '/grafana/data')
api.add_resource(Grafana_Dash, '/grafana/dash')

if __name__ == '__main__':
     app.run(port='6000')