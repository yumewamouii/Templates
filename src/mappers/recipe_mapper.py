from src.models.recipe import Recipe


from src.dtos.recipe_dto import RecipeDTO
from src.dtos.ingredient_dto import IngredientDTO


from src.mappers.ingredient_mapper import IngredientMapper


from src.utils.validator import Validator


class RecipeMapper:
    @staticmethod
    def from_dto(dto: RecipeDTO, cache: dict):
        Validator.validate(dto, RecipeDTO)
        Validator.validate(cache, dict)


        item = Recipe()
        item.id = dto.id
        item.name = dto.name
        item.nomenclature_groups = dto.nomenclature_groups
        item.measurement_units = dto.measurement_units
        item.nomenclatures = dto.nomenclatures
        item.servings = dto.servings
        item.cooking_time = dto.cooking_time


        item.ingredients = []
        for ing in dto.ingredients or []:
            ing_dto = IngredientDTO.create(ing)
            ing_obj = IngredientMapper.from_dto(ing_dto, cache)
            item.ingredients.append(ing_obj)


        item.steps = []
        for step in dto.steps or []:
            Validator.validate(step, str)
            if step.strip():
                item.steps.append(step)



        return item