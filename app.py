from flask import Flask, request
from flask import request
from services.grafana_search import *

app = Flask(__name__)
api = Api(app)

api.add_resource(GrafanaSearch, '/grafana/search')

if __name__ == '__main__':
     app.run(host='0.0.0.0',port='6000')