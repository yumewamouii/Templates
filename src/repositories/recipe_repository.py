from src.store.recipe_storage import RecipeStorage


from src.models.recipe import Recipe


from src.exceptions.validation import ArgumentException


class RecipeRepository:
    def __init__(self, recipe_storage: RecipeStorage, start_recipes: list[Recipe]):
        self._recipe_storage = recipe_storage
        self._start_recipes = start_recipes
    

    def get_recipes(self, recipe_id: str) -> Recipe | None:
        if not isinstance(recipe_id, str):
            raise ArgumentException(str, type(recipe_id))
        return self._recipe_storage.get(recipe_id)
    

    def get_recipes(self, offset: int = 0, limit: int | None = None) -> list[Recipe]:
        return self._recipe_storage.get_all(offset, limit)
    

    def create_recipe(self, recipe: Recipe):
        self._recipe_storage.create(recipe)
    

    def update_recipe(self, recipe_id: str, recipe: Recipe):
        self._recipe_storage.update(recipe_id, recipe)
    

    def delete_recipe(self, recipe_id: str):
        self._recipe_storage.delete(recipe_id)
    

    def init_start_recipes(self):
        if not self._recipe_storage.is_empty():
            return
        for recipe in self._start_recipes:
            self._recipe_storage.create(recipe)