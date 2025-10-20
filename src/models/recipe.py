from src.models.base_model import BaseModel
from src.models.measurement_unit import MeasurementUnit
from src.models.nomenclature import Nomenclature


from src.utils.fields import ValidatedField


class Ingredient(Nomenclature):
    # Represents a single ingredient with a name, quantity (value),
    # and a measurement unit (e.g., grams, kilograms, pieces).
    #fullname = ValidatedField(str, max_length = 100, strip = True, nullable = False, blank = True, default = '')
    value = ValidatedField(int, nullable = False, default = 0)
    #measurement_unit = ValidatedField(MeasurementUnit)
    

    def __init__(self):
        super().__init__()
    

    @staticmethod
    def create(fullname: str, value: int, unit: MeasurementUnit):
        item = Ingredient


        item.fullname = fullname
        item.value = value
        item.measurement_unit = unit


        return item


    def __str__(self):
        # Human-readable representation: e.g. "200 g Flour"
        return f'{self.value} {self.unit.basic_unit} {self.fullname}'


class RecipeStep(BaseModel):
    # Describes one step in the cooking process.
    description = ValidatedField(str, strip = True, nullable = False)


class Recipe(Nomenclature):
    # Represents a complete recipe, including metadata (title, servings),
    # a list of ingredients, and step-by-step instructions.
    #title = ValidatedField(str, max_length = 150, strip = True, nullable = False)

    servings = ValidatedField(int, max_length = 50, strip = True, nullable = False, default = 0)
    ingredients = ValidatedField(list, nullable = False, default = [])
    steps = ValidatedField(list, nullable = False, default = [])
    cooking_time = ValidatedField(str, max_length = 50, strip = True, nullable = False, blank = True, default = '')


    def add_ingredient(self, ingredient: Ingredient) -> None:
        self.ingredients.append(ingredient)
    

    def add_step(self, step: RecipeStep) -> None:
        self.steps.append(step)
    

    @staticmethod
    def create(name: str, cooking_time: str, servings: int) -> 'Recipe':
        item = Recipe()


        item.fullname = name
        item.cooking_time = cooking_time
        item.servings = servings


        return item
