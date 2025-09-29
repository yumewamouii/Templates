from src.models.base_model import BaseModel
from src.models.nomenclature_group import NomenclatureGroup
from src.models.measurement_unit import MeasurementUnit
from src.utils.fields import ValidatedField


class Nomenclature(BaseModel):
    fullname = ValidatedField(str, max_length = 255, strip = True, nullable = False, blank = False)
    nomenclature_group = ValidatedField(NomenclatureGroup, nullable = False, blank = False)
    measurement_unit = ValidatedField(MeasurementUnit, nullable = False, blank = False)