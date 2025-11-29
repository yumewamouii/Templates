import json


import flask
from flask import Blueprint, jsonify


from src.serialization.model_serializer import ModelSerializer


from src.settings_manager import SettingManager


from app.routes.settings.dto import UpdateBlockingDateRequestDto


from src.utils.request_parser import RequestParser


def create_blueprint(service):
    bp = Blueprint('setting_bp', __name__)
    @bp.route('/', methods = ['GET'])
    def settings():
        """
        Get settings
        ---
        responses:
        200:
            description: A list of turnovers
            schema:
                type: array
                items:
                    type: string
        """
        serializer = ModelSerializer()
        settings = SettingManager().settings


        return serializer.serialize(settings.blocking_date)
    

    @bp.route('/', methods = ['PATCH'])
    def blocking_date():
        """
        Update blocking date
        ---
        parameters:
        - in: body
            name: request
            required: true
        responses:
        200:
            description: A list of turnovers
            schema:
                type: array
                items:
                    type: string
        """
        serializer = ModelSerializer()
        request = RequestParser.parse_body(flask.request.json, UpdateBlockingDateRequestDto)


        if request.is_left:
            return request.left
        

        request = request.right
        settings = SettingManager().change_blocking_date(request.date)


        return serializer.serialize(settings)