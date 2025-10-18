from __future__ import annotations
import uuid



from src.models.base_model import BaseModel
from src.utils.fields import ValidatedField


class MeasurementUnit(BaseModel):
    name = ValidatedField(str, strip = True, nullable = False, max_length = 50)
    basic_unit = ValidatedField(str, strip = True, nullable = True, max_length = 50)
    conversion_factor = ValidatedField(int, nullable = False, blank = False, default = 1)


    def __init__(self):
        super().__init__()
        self.id = str(uuid.uuid4().hex)


    @classmethod
    def create(cls, name: str, factor: int = 1, base: 'MeasurementUnit' | None = None) -> 'MeasurementUnit':
        unit = cls()
        unit.name = name


        if base is None:
            unit.basic_unit = name
            unit.conversion_factor = 1
        else:
            unit.basic_unit = base.basic_unit
            unit.conversion_factor = factor


        return unit
        

    def __str__(self):
        return (f'Identification number: {self.id}\n'
                f'Unit name: {self.name}\n'
                f'Basic unit of measurement: {self.basic_unit}\n'
                f'Conversion factor: {self.conversion_factor}')


