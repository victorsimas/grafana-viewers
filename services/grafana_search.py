from flask_restful import Resource, Api, reqparse
from flask import Flask, request, Response
from http import HTTPStatus
from services.grafana_service import GrafanaService, GrafanaImageService
from modules.grafana_mounter import GrafanaMounter
import json


class GrafanaSearch(Resource):
    def __init__(self):
        self.service = GrafanaService()
        self.mounter = GrafanaMounter()

    def get(self):
        try:
            search = self.service.get(endpoint="/api/search", params=request.args)
            search_data = json.loads(search.data)
            dash = self.mounter.mount_dashs(search_data=search_data)
            if isinstance(dash, list):
                return Response(response=json.dumps(dash),
                                status=HTTPStatus.PARTIAL_CONTENT,
                                content_type='application/json')
            images = self.mounter.mount_image_from_panel(dash=dash)
            return Response(response=images, status=HTTPStatus.OK,
                            content_type='image/png')
        except(Exception) as exception:
            return Response(
                      response="Não foi possivel localizar dashboard ou painel",
                      status=HTTPStatus.NOT_FOUND)
