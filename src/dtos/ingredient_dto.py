from dataclasses import dataclass


from src.dtos.base_dto import BaseDTO


@dataclass
class IngredientDTO(BaseDTO):
    nomenclature_id: str
    measurement_unit_id: str
    value: int