from flask import Flask, request
from flask import request
from services.grafana_search import *
from healthcheck import HealthCheck
from services.grafana_service import GrafanaService

app = Flask(__name__)
health = HealthCheck()
api = Api(app)
service = GrafanaService()

def grafana():
    service.get('/api/health', None)
    return True, "Grafana esta de pé e respondendo"

health.add_check(grafana)

api.add_resource(GrafanaSearch, '/grafana/search')

app.add_url_rule("/hc", "healthcheck", view_func=lambda: health.run())

if __name__ == '__main__':
     app.run(host='0.0.0.0',port='5000')