from flask_restful import Resource, Api, reqparse
from flask import Flask, request
from services.GrafanaService import Grafana_Service

class Grafana_Search(Resource):
    def get(self):
        return Grafana_Service.grafanaService(self, "/api/search")

class Grafana_Data(Resource):
    def get(self):
        return "Okay"

class Grafana_Dash(Resource):
    def get(self):
        return "Okay"