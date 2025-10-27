from dataclasses import dataclass


from src.dtos.base_dto import BaseDTO


@dataclass
class RecipeDTO(BaseDTO):
    id: str
    name: str
    nomenclature_groups: list
    measurement_units: list
    nomenclatures: list
    ingredients: list
    servings: int
    cooking_time: str
    steps: list
