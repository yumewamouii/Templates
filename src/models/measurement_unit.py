from __future__ import annotations
import uuid



from src.models.base_model import BaseModel
from src.utils.fields import ValidatedField


class MeasurementUnit(BaseModel):
    basic_unit = ValidatedField(str, strip = True, nullable = True, max_length = 50)
    conversion_factor = ValidatedField(int, nullable = False, blank = False, default = 1)


    @classmethod
    def range_model(cls, name: str, factor: int = 1, base_unit: 'MeasurementUnit' | None = None) -> 'MeasurementUnit':
        unit = cls()
        unit.basic_unit = name


        if base_unit is None:
            unit.conversion_factor = 1
        else:
            unit.conversion_factor = factor
            unit.basic_unit = base_unit.basic_unit


        return unit

    def __str__(self):
        return (f'Идентификационный номер: {self.id}\n'
                f'Базовая единица измерения: {self.basic_unit}\n'
                f'Коэффициент пересчета: {self.conversion_factor}')


