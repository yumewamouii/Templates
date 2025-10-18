import unittest


from src.start_service import StartService


from src.models.measurement_unit import MeasurementUnit
from src.models.nomenclature import Nomenclature
from src.models.nomenclature_group import NomenclatureGroup
from src.models.recipe import Recipe, Ingredient, RecipeStep


from src.repository import Repository


class TestStartService(unittest.TestCase):
    def setUp(self):
        self.service = StartService()
        self.repository = self.service._StartService__repository


        # Cleaning the repository before each test
        for key in self.service.data():
            self.service.data()[key] = []
    

    def test_singleton(self):
        service1 = StartService()
        service2 = StartService()
        self.assertIs(service1, service2)
    

    def test_default_keys_initialized(self):
        keys = [
            self.repository.range_measurement_unit_key(),
            self.repository.range_nomenclature_group_key(),
            self.repository.range_nomenclature_key(),
            self.repository.range_recipe()
        ]


        for key in keys:
            self.assertIn(key, self.service.data())
            self.assertIsInstance(self.service.data()[key], list)
    

    def test_create_measurement_units(self):
        self.service._StartService__default_create_measurement_units()
        units = self.service.data()[Repository.range_measurement_unit_key()]
        self.assertEqual(len(units), 3)
        basic_units = {u.name for u in units}
        self.assertIn('g', basic_units)
        self.assertIn("kg", basic_units)
        self.assertIn("piece", basic_units)
    

    def test_create_nomenclature_group(self):
        self.service._StartService__default_create_nomenclature_groups()
        groups = self.service.data()[self.repository.range_nomenclature_group_key()]
        self.assertEqual(len(groups), 1)
        self.assertIsInstance(groups[0], NomenclatureGroup)
        self.assertEqual(groups[0].name, "Food Products")
    

    def test_create_nomenclature(self):
        self.service._StartService__default_create_measurement_units()
        self.service._StartService__default_create_nomenclature_groups()
        self.service._StartService__default_create_nomenclatures()
        nomenclatures = self.service.data()[self.repository.range_nomenclature_key()]
        self.assertEqual(len(nomenclatures), 1)
        n = nomenclatures[0]
        self.assertIsInstance(n, Nomenclature)
        self.assertEqual(n.fullname, "Sample Nomenclature")
        self.assertIsInstance(n.nomenclature_group, NomenclatureGroup)
        self.assertIsInstance(n.measurement_unit, MeasurementUnit)
    

    def test_same_unit_instance_for_multiple_ingredients(self):
        # Create shared MeasurementUnit
        g = MeasurementUnit.create_g()
        
        # Create recipe and add multiple ingredients using the same g
        recipe = Recipe(title="Test Recipe", servings="2 servings")
        ingredient1 = Ingredient(fullname="Flour", value=200, unit=g)
        ingredient2 = Ingredient(fullname="Water", value=120, unit=g)
        recipe.add_ingredient(ingredient1)
        recipe.add_ingredient(ingredient2)

        # Check that both ingredients reference the same MeasurementUnit object
        self.assertIs(recipe.ingredients[0].unit, recipe.ingredients[1].unit,
                      msg="Ingredients should reference the same MeasurementUnit instance")
        self.assertEqual(recipe.ingredients[0].unit.name, "g")
        self.assertEqual(recipe.ingredients[1].unit.name, "g")

        # Optional: verify conversion factor remains correct
        self.assertEqual(recipe.ingredients[0].unit.conversion_factor, 1)
        self.assertEqual(recipe.ingredients[1].unit.conversion_factor, 1)

    

    def test_start_method_idempotent(self):
        # The start method should work once and not duplicate data.
        self.service.start()
        first_counts = {k: len(v) for k, v in self.service.data().items()}
        self.service.start()
        second_counts = {k: len(v) for k, v in self.service.data().items()}
        self.assertEqual(first_counts, second_counts)
    

    def test_create_generic(self):
        test_obj = "test_object"
        self.service.create("custom_key", test_obj)
        self.assertIn("custom_key", self.service.data())
        self.assertIn(test_obj, self.service.data()["custom_key"])