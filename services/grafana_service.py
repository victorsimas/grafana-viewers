from flask_restful import Resource, Api, reqparse
from flask import Flask, request,jsonify, make_response, Response
from http import HTTPStatus
from requests.exceptions import HTTPError
import os
import requests

class GrafanaService():
    def get(self, endpoint :str, params) -> Response:
        header = { 'Authorization' : f"Bearer {os.environ['TOKEN_GRAFANA']}"}
        url= f"{os.environ['HOST_GRAFANA']}{endpoint}"
        try:
            response = requests.get(url, headers=header, verify=False, params=params, timeout=10)
            return make_response(jsonify(response.json()), HTTPStatus.OK)
        except (Exception) as exception:
            raise
        
class GrafanaImageService():
    def get(self, endpoint :str, params) -> bytes:
        header = { 'Authorization' : f"Bearer {os.environ['TOKEN_GRAFANA']}"}
        url= f"{os.environ['HOST_GRAFANA']}{endpoint}"
        try:
            response = requests.get(url, headers=header, verify=False, params=params, stream=True, timeout=10)
            return response.content
        except (Exception) as exception:
            raise
