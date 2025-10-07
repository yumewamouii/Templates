from src.models.measurement_unit import MeasurementUnit
from src.models.nomenclature import Nomenclature
from src.models.nomenclature_group import NomenclatureGroup
from src.models.recipe import Recipe, Ingredient, RecipeStep

from src.repository import Repository
from src.utils.fields import ValidatedField


class StartService:
    __repository: Repository = Repository()

    # Ensure StartService is a singleton – only one instance will exist in the application.
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(StartService, cls).__new__(cls)
        return cls.instance
    

    def __init__(self):
        # Initialize repository with empty lists for all supported data categories
        for key in (
            self.__repository.range_measurement_unit_key(),
            self.__repository.range_nomenclature_key(),
            self.__repository.range_nomenclature_group_key(),
            self.__repository.range_recipe()
        ):
            if key not in self.__repository.data:
                self.__repository.data[key] = []
        # Prevent multiple initializations when calling start() more than once
        self.__started: bool = False
    

    def data(self) -> dict:
        # Expose repository data for inspection or testing
        return self.__repository.data
    

    def __default_create_measurement_units(self):
        # Register commonly used measurement units (g, kg, pcs) into the repository
        self.create(self.__repository.range_measurement_unit_key(), MeasurementUnit.create_g())
        self.create(self.__repository.range_measurement_unit_key(), MeasurementUnit.create_kg())
        self.create(self.__repository.range_measurement_unit_key(), MeasurementUnit.create_piece())


    def __default_create_nomenclature_groups(self):
        # Create a default product group to categorize food-related nomenclatures
        nomenclature_group = NomenclatureGroup()
        nomenclature_group.name = 'Food Products'
        self.create(self.__repository.range_nomenclature_group_key(), nomenclature_group)
    
    
    def __default_create_nomenclatures(self):
        # Create a sample nomenclature and link it with the first available group and unit
        nomenclature = Nomenclature()
        nomenclature.fullname = 'Sample Nomenclature'
        nomenclature.nomenclature_group = self.__repository.data[self.__repository.range_nomenclature_group_key()][0]
        nomenclature.measurement_unit = self.__repository.data[self.__repository.range_measurement_unit_key()][0]
        self.create(self.__repository.range_nomenclature_key(), nomenclature)

    def __default_create_recipes(self):
        # Define a simple demo recipe (Margarita Pizza) with ingredients and preparation steps
        g = MeasurementUnit.create_g()
        pcs = MeasurementUnit.create_piece()

        pizza_recipe = Recipe(title='Margarita Pizza', servings='2 servings')

        # Ingredients with different measurement units
        pizza_recipe.add_ingredient(Ingredient(fullname='Flour', value=200, unit=g))
        pizza_recipe.add_ingredient(Ingredient(fullname='Water', value=120, unit=g))
        pizza_recipe.add_ingredient(Ingredient(fullname='Mozzarella cheese', value=150, unit=g))
        pizza_recipe.add_ingredient(Ingredient(fullname='Eggs', value=2, unit=pcs))

        # Step-by-step preparation process
        pizza_recipe.add_step(RecipeStep(
            step_number=1,
            description='Dissolve the yeast in warm water, add sugar and 1 spoon of flour. '
                        'Let it sit for 10 minutes to activate the yeast.'
        ))
        pizza_recipe.add_step(RecipeStep(
            step_number=2,
            description='In a bowl, mix flour, salt, olive oil, and the yeast mixture. Knead the dough.'
        ))

        self.create(self.__repository.range_recipe(), pizza_recipe)
    

    def start(self):
        # Populate repository with initial demo data on the first call only
        if not self.__started:
            self.__default_create_measurement_units()
            self.__default_create_nomenclature_groups()
            self.__default_create_nomenclatures()
            self.__default_create_recipes()
            self.__started = True
    

    def create(self, key: str, obj: object):
        """
        Generic method to insert an object into the repository under the given key.
        Works for all supported domains: units, nomenclatures, groups, recipes, etc.
        """
        if key not in self.__repository.data:
            self.__repository.data[key] = []
        self.__repository.data[key].append(obj)
