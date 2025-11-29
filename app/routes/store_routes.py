import json

import flask
from flask import Blueprint, jsonify


from src.serialization.model_serializer import ModelSerializer


from src.utils.request_parser import RequestParser


from src.dtos.transaction_request_dto import TransactionsRequestDto


from src.models.filter import Filter
from src.models.range import RangeModel
from src.models.filter_type import FilterType


from src.store.store_repository import StoreRepository


from src.models.store_turnover import StoreTurnover


from src.settings_manager import SettingManager


def create_blueprint(service):
    bp = Blueprint('store_bp', __name__)

    @bp.route('/', methods=['POST'])
    def turnovers():
        """
    Calculate turnovers for the specified period.
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
        request = RequestParser.parse_body(flask.request.json, TransactionsRequestDto)

        if request.is_left:
            return request.left

        request = request.right

        filters = request.filters
        filters.append(Filter('time', RangeModel(request.date_from, request.date_to), FilterType.BETWEEN))


        settings_manager = SettingManager()
        blocking_date = settings_manager.settings.blocking_date

        turnovers = StoreRepository.get_turnovers(filters, StoreTurnover.default_grouping(), blocking_date)

        return serializer.serialize(turnovers)