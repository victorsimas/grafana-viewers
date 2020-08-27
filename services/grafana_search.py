from flask_restful import Resource, Api, reqparse
from flask import Flask, request, Response
from http import HTTPStatus
from services.grafana_service import GrafanaService, GrafanaImageService
from grafana_constans import GrafanaConstants as Gconst
import json
import re

class GrafanaSearch(Resource):
    def __init__(self):
        self.service = GrafanaService()  
        self.mounter = GrafanaMounter()  
    def get(self):
        # try:
        search = self.service.get(endpoint="/api/search", params=request.args)
        search_data = json.loads(search.data)
        dash = self.mounter.mount_dashs(search_data=search_data)
        if isinstance(dash,list):
            return Response(response=json.dumps(dash), status=HTTPStatus.PARTIAL_CONTENT, content_type='application/json')
        images = self.mounter.mount_image_from_panel(dash=dash)
        return Response(response=images, status=HTTPStatus.OK, content_type='image/png')
        # except(Exception) as exception:
        #     return Response(response="Não foi possivel localizar dashboard ou painel",
        #                      status=HTTPStatus.NOT_FOUND)
    
class GrafanaMounter():
    def __init__(self):
        self.service = GrafanaService()
        self.image_service = GrafanaImageService() 
        self.constants = Gconst()
        self.queryImage = {
            'orgId' : self.constants.imageQuery['orgId'],
            'from' : self.constants.imageQuery['from'],
            'to' :  self.constants.imageQuery['to'],
            'panelId' :  0,
            'width' :  self.constants.imageQuery['width'],
            'height' :  self.constants.imageQuery['height']
        }
    
    def mount_dashs(self, search_data):
        panels = []
        dash = self.choose_dash_by_pattern(search_data)
        dashboard = self.service.get(endpoint=f"/api/dashboards/uid/{dash['uid']}", 
                                                params=request.args)
        dashboard_data = json.loads(dashboard.data)
        
        for panel in dashboard_data['dashboard']['panels']:
            if panel['datasource'] is not None:
                panels.append(panel)
                
        dashboard_data['dashboard']['panels'] = panels
        dashboard_data['dashboard']['slug'] = dashboard_data['meta']['slug']
        
        dash_type = self.verify_dashboard_type(dashboard_data['dashboard'])
        
        if dash_type is self.constants.dashType[1] and not self.check_if_vars_exists():
            return self.filter_dash_vars(dashboard_data['dashboard'])
        return dashboard_data['dashboard']

    def mount_image_from_panel(self, dash) -> bytes:
        for panel in dash['panels']:
            query = self.choose_panel_by_pattern(panel)
            if query is not None:
                query = self.append_vars_on_query(query)
                image = self.image_service.get(
                    endpoint=f"/render/d-solo/{dash['uid']}/{dash['slug']}", 
                    params=query)
                return image
            pass
        raise 
            
    def choose_dash_by_pattern(self, dashs):
        for dash in dashs:
            if re.search(request.args['tag'], dash['title'], re.IGNORECASE):
                return dash
            pass
        raise
    
    def verify_dashboard_type(self, dash):
        if len(dash['templating']['list']) > 0:
            return self.constants.dashType[1]
        return self.constants.dashType[0]
    
    def filter_dash_vars(self, dash) -> list:
        variables = []
        for template in dash['templating']['list']:
            variables.append(f"var-{template['name']}")
        return variables      
        
    def choose_panel_by_pattern(self, panel):
        validator = []
        titulos = request.args['titulo']
        titulos_list = titulos.split(',')
        for titulo in titulos_list:
            if re.search(titulo, panel['title'], re.IGNORECASE):
                validator.append(True)
            else:
                validator.append(False)
            if len(validator) == len(titulos_list):
                if False in validator:
                    return None
        self.queryImage['panelId'] = panel['id']
        return self.queryImage
    
    def append_vars_on_query(self, query):
        for key, value in request.args.items():
            if re.search('var-', key):
                query[key] = value
        return query
    
    def check_if_vars_exists(self):
        for key, value in request.args.items():
            if re.search('var-', key):
                return True
        return False