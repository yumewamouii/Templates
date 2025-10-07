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


    # Cache for unique unit instances (Singleton like)
    # Singleton cache
    __registry: dict[str, 'MeasurementUnit'] = {}

    @classmethod
    def create(cls, name: str, factor: int = 1, base: 'MeasurementUnit' | None = None) -> 'MeasurementUnit':
        key = name.lower()

        # Return existing instance if present
        if key in cls.__registry:
            return cls.__registry[key]

        unit = cls()
        unit.name = name

        if base is None:
            unit.basic_unit = name
            unit.conversion_factor = 1
        else:
            unit.basic_unit = base.basic_unit
            unit.conversion_factor = factor

        cls.__registry[key] = unit
        return unit

    

    # Factory methods using shared cache
    @classmethod
    def create_g(cls) -> 'MeasurementUnit':
        return cls.create('g', 1)
    

    @classmethod
    def create_kg(cls) -> 'MeasurementUnit':
        g = cls.create_g()
        return cls.create('kg', 1000, g)


    @classmethod
    def create_piece(cls) -> 'MeasurementUnit':
        g = cls.create_g()
        return cls.create('pcs', 55, g)
        

    def __str__(self):
        return (f'Identification number: {self.id}\n'
                f'Unit name: {self.name}\n'
                f'Basic unit of measurement: {self.basic_unit}\n'
                f'Conversion factor: {self.conversion_factor}')


