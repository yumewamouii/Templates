from src.managers.base_manager import BaseManager
from src.managers.base_state import BaseState


from src.repositories.nomenclature_repository import NomenclatureRepository
from src.repositories.recipe_repository import RecipeRepository


from src.store.nomenclature_storage_finder import NomenclatureStorageFinder


from src.models.nomenclature import Nomenclature


from utils.observer.base_observable import StreamSubscription


class RecipeManager(BaseManager[BaseState]):
    """
    A recipe manager that tracks changes in the product range.
    Automatically updates ingredients in recipes when the item is updated.
    """
    _nomenclature_repository: NomenclatureRepository
    _recipe_repository: RecipeRepository
    _nomenclature_storage_finder: NomenclatureStorageFinder
    _nomenclature_updates_subscription: StreamSubscription[Nomenclature]


    def __init__(self, nomenclature_repository, recipe_repository, nomenclature_storage_finder):
        super().__init__(BaseState())
        self._nomenclature_repository = nomenclature_repository
        self._recipe_repository = recipe_repository
        self._nomenclature_storage_finder = nomenclature_storage_finder
    

    def init(self):
        """
        Starts listening for item updates.
        Subscribes to the stream of changes.
        """
        self._nomenclature_updates_subscription = self._nomenclature_repository.watch_nomenclature_updates().subscribe(self._on_nomenclature_updated)
    

    def _on_nomenclature_updated(self, nomenclature: Nomenclature):
        """
        The item update handler.
        Updates all recipes that contain this item as ingredients.

        Args:
            nomenclature: The updated item item.
        """
        recipes = self._nomenclature_storage_finder.find_dependant_recipes(nomenclature.id)


        for recipe in recipes:
            updated = False
            for ingredient in recipe.ingredients:
                if ingredient.nomenclature.id == nomenclature.id:
                    ingredient.nomenclature = nomenclature
                    updated = True
            if updated:
                self._recipe_repository.update_recipe(recipe.id, recipe)
    

    def close(self):
        """
        Stops listening for item updates.
        Closes the active subscription.
        """
        if self._nomenclature_updates_subscription:
            self._nomenclature_updates_subscription.close()
            self._nomenclature_updates_subscription = None