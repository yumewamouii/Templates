from src.store.base_memory_storage import BaseMemoryStorage


from src.models.recipe import Recipe


class RecipeStorage(BaseMemoryStorage[str, Recipe]):
    pass