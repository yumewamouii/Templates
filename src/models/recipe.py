from src.models.base_model import BaseModel
from src.models.measurement_unit import MeasurementUnit
from src.models.nomenclature import Nomenclature


from src.utils.fields import ValidatedField


class Ingredient(Nomenclature):
    # Represents a single ingredient with a name, quantity (value),
    # and a measurement unit (e.g., grams, kilograms, pieces).
<<<<<<< Updated upstream
    value = ValidatedField(int, nullable = False)
   

    def __init__(self, fullname: str, value: int, unit: MeasurementUnit):
        # Explicit constructor for convenience, allows creating Ingredient
        # instances without relying solely on reflection from Nomenclature.
        super().__init__()
        self.fullname = fullname
        self.value = value
        self.unit = unit
=======
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
>>>>>>> Stashed changes


    def __str__(self):
        # Human-readable representation: e.g. "200 g Flour"
        return f'{self.value} {self.unit.basic_unit} {self.fullname}'


<<<<<<< Updated upstream
class RecipeStep(Nomenclature):
    # Describes one step in the cooking process.
    step_number = ValidatedField(int, nullable = False)
    description = ValidatedField(str, strip = True, nullable = False)


    def __init__(self, step_number: int, description: str):
        # Constructor ensures every step has both an order and description.
        super().__init__()
        self.step_number = step_number
        self.description = description


=======
class RecipeStep(BaseModel):
    # Describes one step in the cooking process.
    '''step_number = ValidatedField(int, nullable = False)'''
    description = ValidatedField(str, strip = True, nullable = False)


>>>>>>> Stashed changes
class Recipe(Nomenclature):
    # Represents a complete recipe, including metadata (title, servings),
    # a list of ingredients, and step-by-step instructions.
    #title = ValidatedField(str, max_length = 150, strip = True, nullable = False)
<<<<<<< Updated upstream
    servings = ValidatedField(str, max_length = 50, strip = True, nullable = False)
    ingredients = ValidatedField(list, nullable = False, default = [])
    steps = ValidatedField(list, nullable = False, default = [])


    def __init__(self, title: str, servings: str):
        # Initialize recipe metadata and ensure clean empty lists
        # for ingredients and steps (avoids shared mutable defaults).
        super().__init__()
        self.title = title
        self.servings = servings
        self.ingredients = []
        self.steps = []
=======
    servings = ValidatedField(int, max_length = 50, strip = True, nullable = False, default = 0)
    ingredients = ValidatedField(list, nullable = False, default = [])
    steps = ValidatedField(list, nullable = False, default = [])
    cooking_time = ValidatedField(str, max_length = 50, strip = True, nullable = False, blank = True, default = '')
>>>>>>> Stashed changes


    def add_ingredient(self, ingredient: Ingredient) -> None:
        self.ingredients.append(ingredient)
    

    def add_step(self, step: RecipeStep) -> None:
<<<<<<< Updated upstream
        self.steps.append(step)
=======
        self.steps.append(step)
    

    @staticmethod
    def create(name: str, cooking_time: str, servings: int) -> 'Recipe':
        item = Recipe()


        item.fullname = name
        item.cooking_time = cooking_time
        item.servings = servings


        return item
>>>>>>> Stashed changes
