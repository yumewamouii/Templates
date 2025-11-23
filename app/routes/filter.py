import json


import flask
from flask import Blueprint, jsonify


from src.models.filter import Filter


from src.factories.storage_factory import StorageFactory


from src.serialization.model_serializer import ModelSerializer


def create_blueprint(service):
    bp = Blueprint('filter_bp', __name__)


    @bp.route('/<entity>', methods=['POST'])
    def filter(entity):
            """
        Fetch entities filtered by the specified filters.
        ---
        parameters:
        - in: body
            name: filter
            required: true
        - name: entity
            in: path
            type: string
            enum: ['nomenclature', 'nomenclature_group', 'unit', 'recipe']
            required: true
            default: nomenclature
        responses:
        200:
            description: A list of entities
            schema:
            type: array
        """

            storage = StorageFactory.get_storage(entity)

            if storage.is_left:
                return storage.left

            serializer = ModelSerializer()
            filters = serializer.deserialize(flask.request.json, Filter)
            return serializer.serialize(storage.right.get_filtered(filters))