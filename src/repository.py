from typing import Any


from src.models.measurement_unit import MeasurementUnit
from src.models.recipe import Recipe


from src.utils.fields import ValidatedField


from src.serialization.model_serializer import ModelSerializer
from src.serialization.serializer_factory import SerializerFactory


class Repository:
    # Central storage container for all application data.
    # The repository pattern decouples data management from business logic.
    data = ValidatedField(dict, nullable = False)


    def __init__(self):
        # Initialize repository with empty collections for all supported entity types
        self.data = {}
        for key in (
            self.range_measurement_unit_key(),
            self.range_nomenclature_group_key(),
            self.range_nomenclature_key(),
            self.range_recipe()
        ):
            self.data[key] = []

    # --- Keys used to organize entities inside the repository ---

    @staticmethod
    def range_measurement_unit_key() -> str:
        # Key for measurement units (e.g., g, kg, pcs)
        return 'measurement_units'
    

    @staticmethod
    def range_nomenclature_key() -> str:
        # Key for nomenclatures (items linked to groups and units)
        return 'nomenclatures'
    

    @staticmethod
    def range_nomenclature_group_key() -> str:
        # Key for nomenclature groups (e.g., Food Products)
        return 'nomenclature_groups'
    

    @staticmethod
    def range_recipe() -> str:
        # Key for storing recipes with ingredients and steps
        return 'recipes'
    
    # TODO: Need to implement Generic CRUD-like operations
    def add(self, key: str, obj: object):
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(obj)
    

    def get_recipes(self) -> Recipe:
        serializer = SerializerFactory()
        return [serializer.get_serializer(recipe) for recipe in self.data['recipes']]
    

    def get_recipe_by_id(self, recipe_id: str) -> dict[str, Any]:
        serializer = SerializerFactory()
        for recipe in self.data['recipes']:
            if recipe.id == recipe_id:
                return serializer.get_serializer(recipe)
        return None
    

    def add_recipe(self, recipe: Recipe) -> None:
        # Convenience method for adding recipes, avoids passing keys explicitly.
        self.add(self.range_recipe(), recipe)