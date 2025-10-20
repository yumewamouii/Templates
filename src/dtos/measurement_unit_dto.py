from dataclasses import dataclass


from src.dtos.base_dto import BaseDTO


@dataclass
class MeasurementUnitDTO(BaseDTO):
    id: str
    name: str
    basic_unit_id: str | None
    conversion_factor: int