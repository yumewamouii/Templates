from src.models.measurement_unit import MeasurementUnit


from src.dtos.measurement_unit_dto import MeasurementUnitDTO


from src.utils.validator import Validator


class MeasurementUnitMapper:
    @staticmethod
    def from_dto(dto: MeasurementUnitDTO, cache: dict):
        Validator.validate(cache, dict)
        if dto.basic_unit_id in cache:
            basic_unit = cache[dto.basic_unit_id]
        else:
            basic_unit = None
        item = MeasurementUnit.create(dto.name, dto.conversion_factor, basic_unit)
        return item