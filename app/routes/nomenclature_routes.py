import json
import uuid


import flask
from flask import Blueprint, jsonify


from src.managers.nomenclature_manager import NomenclatureManager


from src.serialization.model_serializer import ModelSerializer


from src.models.nomenclature import Nomenclature


from src.utils.request_parser import RequestParser
from src.utils.response_factory import ResponseFactory


def create_blueprint(service):
    bp = Blueprint('nomenclature_bp', __name__)


    @bp.route('/<id>', methods=['PATCH'])
    def update_nomenclature():
        nomenclature_id = flask.request.args['id']
        request = RequestParser.parse_body(flask.request.json, Nomenclature)


        if request.is_left:
            return request.left
        

        nomenclature = request.right
        nomenclature_manager: NomenclatureManager = NomenclatureManager()
        nomenclature.id = nomenclature_id
        nomenclature_manager.update_nomenclature(nomenclature_id, nomenclature)


        return ResponseFactory.success_no_data()
    

    @bp.route('/<id>', methods=['DELETE'])
    def delete_update_nomenclature():
        nomenclature_id = flask.request.args['id']
        nomenclature_manager: NomenclatureManager = NomenclatureManager()
        result = nomenclature_manager.delete_nomenclature(nomenclature_id)
        if result:
            return ResponseFactory.success_no_data()
        return ResponseFactory.error('Cannot delete this nomenclature', 400)
    

    @bp.route('/<id>', methods=['GET'])
    def get_nomenclature():
        nomenclature_id = flask.request.args['id']
        model_serializer: ModelSerializer = ModelSerializer()


        nomenclature_manager: NomenclatureManager = NomenclatureManager()
        nomenclature = nomenclature_manager.get_nomenclature(nomenclature_id)


        if nomenclature is not None:
            return model_serializer.serialize(nomenclature)
    

        return ResponseFactory.error('No such nomenclature', 404)
    

    @bp.route('/', methods=['PUT'])
    def put_nomenclature():
        request = RequestParser.parse_body(flask.request.json, Nomenclature)


        if request.is_left:
            return request.left
        

        nomenclature = request.right


        nomenclature.id = str(uuid.uuid4())


        nomenclature_manager: NomenclatureManager = NomenclatureManager()
        nomenclature_manager.create_nomenclature(nomenclature)


        return ResponseFactory.success_no_data()