from src.exceptions.validation import ArgumentException


from src.models.base_model import BaseModel
from src.models.measurement_unit import MeasurementUnit


from src.utils.fields import ValidatedField


class StoreTurnover(BaseModel):
    turnover = ValidatedField(MeasurementUnit, nullable = True, default = None)
    group = ValidatedField(dict[str, object], nullable = True, default = None)


    def __init__(self, turnover: MeasurementUnit = None, group: dict[str, object] = None):
        super().__init__()


        self.turnover = turnover
        self.group = group
    

    @staticmethod
    def default_grouping() -> list[str]:
        return ['nomenclature.id', 'store.id']