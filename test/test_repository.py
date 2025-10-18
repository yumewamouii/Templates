import unittest


from src.repository import Repository


from src.models.recipe import Recipe
from src.models.measurement_unit import MeasurementUnit


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repository = Repository()
    

    def test_create_repository(self):
        self.assertIsInstance(self.repository, Repository)


    # Ensure all expected default keys exist in the repository
    def test_initial_keys_exists(self):
        expected_keys = [
            self.repository.range_measurement_unit_key(),
            self.repository.range_nomenclature_group_key(),
            self.repository.range_nomenclature_key(),
            self.repository.range_recipe()
        ]
        for key in expected_keys:
            self.assertIn(key, self.repository.data)
    

    # Verify that all default keys are initialized with empty lists
    def test_initialize_repository(self):
        expected_keys = [
            self.repository.range_measurement_unit_key(),
            self.repository.range_nomenclature_group_key(),
            self.repository.range_nomenclature_key(),
            self.repository.range_recipe()
        ]
        for key in expected_keys:
            self.assertEqual(self.repository.data[key], [])
    

    # Ensures repository dynamically creates new lists for new categories
    def test_add_to_unknown_key(self):
        obj = {"test": "value"}
        self.repository.add("custom_key", obj)
        self.assertIn("custom_key", self.repository.data)
        self.assertEqual(self.repository.data["custom_key"], [obj])
    

    # Verifies that objects are correctly stored under proper key
    def test_add_to_measurement_units(self):
        g = MeasurementUnit.create_g()
        self.repository.add(self.repository.range_measurement_unit_key(), g)
        self.assertEqual(len(self.repository.data[self.repository.range_measurement_unit_key()]), 1)
        self.assertIsInstance(self.repository.data[self.repository.range_measurement_unit_key()][0], MeasurementUnit)
    

    # Test adding a Recipe using add_recipe and retrieving via get_recipes
    def test_add_and_get_recipe(self):
        recipe = Recipe(title="Test recipe", servings="2 servings")
        self.repository.add_recipe(recipe)
        recipes = self.repository.get_recipes()
        self.assertEqual(len(recipes), 1)
        self.assertIsInstance(recipes[0], Recipe)
        self.assertEqual(recipes[0].title, "Test recipe")
    

    # Ensure repository can handle multiple objects
    def test_multiple_recipes(self):
        recipe1 = Recipe(title="Test recipe number one", servings="1 serving")
        recipe2 = Recipe(title="Test recipe number two", servings="2 servings")
        self.repository.add_recipe(recipe1)
        self.repository.add_recipe(recipe2)
        recipes = self.repository.get_recipes()
        self.assertEqual(len(recipes), 2)
        self.assertEqual({recipe.title for recipe in recipes}, {"Test recipe number one", "Test recipe number two"})
    

    # Verify behavior when recipe list is empty
    def test_empty_recipes_list(self):
        recipes = self.repository.get_recipes()
        self.assertEqual(recipes, [])
    

    # Ensures repository can handle arbitrary object types under known keys
    def test_add_to_nomenclature_group(self):
        obj = {"name": "Food Products"}
        self.repository.add(self.repository.range_nomenclature_group_key(), obj)
        self.assertIn(obj, self.repository.data[self.repository.range_nomenclature_group_key()])
    

    def test_add_to_nomenclature(self):
        obj = {"fullname": "Milk"}
        self.repository.add(self.repository.range_nomenclature_key(), obj)
        self.assertIn(obj, self.repository.data[self.repository.range_nomenclature_key()])
