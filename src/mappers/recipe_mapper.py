from src.models.recipe import Recipe


from src.dtos.recipe_dto import RecipeDTO


from src.utils.validator import Validator


class RecipeMapper:
    @staticmethod
    def from_dto(dto: RecipeDTO, cache: dict):
        Validator.validate(dto, RecipeDTO)
        Validator.validate(cache, dict)


        pass


        item = Recipe.create(dto.name, dto.cooking_time, dto.servings)