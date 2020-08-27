from flask_restful import Resource, Api, reqparse
from flask import Flask, request,jsonify, make_response
from http import HTTPStatus
import os
import requests

class Grafana_Service():
    def grafanaService(self, endpoint):
        header = { 'Authorization' : f"Bearer {os.environ['TOKEN_GRAFANA']}"}
        data = request.json
        url= f"{os.environ['HOST_GRAFANA']}{endpoint}"
        responseGrafana = requests.get(url, data, headers=header, verify=False)
        response = make_response(jsonify(responseGrafana.json()), HTTPStatus.OK)
        return response