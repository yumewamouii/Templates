from src.models.recipe import Ingredient


from src.dtos.ingredient_dto import IngredientDTO


from src.utils.validator import Validator


class IngredientMapper:
    @staticmethod
    def from_dto(dto: IngredientDTO, cache: dict):
        Validator.validate(dto, IngredientDTO)
        Validator.validate(cache, dict)


        if dto.measurement_unit_id in cache:
            measurement_unit = cache[dto.measurement_unit_id]
        else:
            measurement_unit = None
        

        if dto.nomenclature_id in cache:
            nomenclature = cache[dto.nomenclature_id]
        else:
            nomenclature = None
        

        item = Ingredient.create(nomenclature, dto.value, measurement_unit)
        return item
        