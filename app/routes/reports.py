import json


import flask
from flask import Blueprint, jsonify


from src.reports.base_report import BaseReport
from src.reports.report_format import ReportFormat
from src.reports.report_factory import ReportFactory


from src.exceptions.either import Either


from src.utils.response_factory import ResponseFactory


from src.settings_manager import SettingManager


from src.repositories.nomenclature_repository import NomenclatureRepository


from src.factories.measurement_units_factory import MeasurementUnitsFactory


def _get_report() -> Either[object, BaseReport]:
    report_name = flask.request.args.get('format').upper()
    if report_name not in ReportFormat:
        return Either.with_left(ResponseFactory.error('Unknown report format: {}'.format(report_name)))
    
    report_format = ReportFormat[report_name]


    settings = SettingManager().state.settings
    return Either.with_right(ReportFactory().create(report_format, settings))


def create_blueprint(service):
    bp = Blueprint('report_bp', __name__)


    @bp.route('/format', methods=['GET'])
    def formats():
        """
        Retrieve available report formats.
        ---
        responses:
        200:
            description: A list of report formats
            schema:
            type: array
            items:
                type: string
            """
        return [e.name for e in ReportFormat]
    

    @bp.route('/nomenclature', methods=['GET'])
    def nomenclature():
        """
        Retrieve nomenclature report in the specified format.
        ---
        parameters:
        - name: format
            in: query
            type: string
            required: true
            description: ReportFormat key name
        responses:
        200:
            description: Nomenclature report
        400:
            description: Invalid report format
        """
        res = _get_report()
        if res.is_left:
            return res.left
        report = res.right
        nomenclature = NomenclatureRepository().get_nomenclatures()

        return report.create(nomenclature)
    

    @bp.route('/nomenclature_groups', methods=['GET'])
    def nomenclature_groups():
        """
        Retrieve nomenclature groups report in the specified format.
    ---
    parameters:
      - name: format
        in: query
        type: string
        required: true
        description: ReportFormat key name
    responses:
      200:
        description: Nomenclature Groups report
      400:
        description: Invalid report format
        """
        res = _get_report()
        if res.is_left:
            return res.left
        report = res.right
        nomenclature = NomenclatureRepository.get_nomenclature_groups()

        return report.create(nomenclature)
    

    @bp.route('/units', methods=['GET'])
    def units():
        """
        Retrieve units report in the specified format.
        ---
        parameters:
        - name: format
            in: query
            type: string
            required: true
            description: ReportFormat key name
        responses:
        200:
            description: Units report
        400:
            description: Invalid report format
        """
        res = _get_report()
        if res.is_left:
            return res.left
        report = res.right
        units = MeasurementUnitsFactory().get_units()

        return report.create(units)