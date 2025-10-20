from src.models.base_model import BaseModel
from src.models.nomenclature_group import NomenclatureGroup
from src.models.measurement_unit import MeasurementUnit
from src.utils.fields import ValidatedField


class Nomenclature(BaseModel):
    fullname = ValidatedField(str, max_length = 255, strip = True, nullable = True, blank = False, default = 'nomenclaturefullname')
    nomenclature_group = ValidatedField(NomenclatureGroup | None, nullable = True, blank = False)
    measurement_unit = ValidatedField(MeasurementUnit | None, nullable = True, blank = False)


    @staticmethod
    def create(id: str, name: str, nomenclature_group: NomenclatureGroup, measurement_unit: MeasurementUnit):
        item = Nomenclature()
        item.id = id
        item.fullname = name
        item.nomenclature_group = nomenclature_group
        item.measurement_unit = measurement_unit


    