from dataclasses import dataclass


from src.dtos.base_dto import BaseDTO


class RecipeDTO(BaseDTO):
    id: str
    name: str
    servings: int
    ingredients: list
    steps: list
    cooking_time: str
