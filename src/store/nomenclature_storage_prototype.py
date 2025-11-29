from abc import ABC, abstractmethod
from typing import TypeVar, Generic


from src.store.recipe_storage import RecipeStorage
from src.store.store_transaction_storage import StoreTransactionStorage


from src.models.filter import Filter
from src.models.filter_type import FilterType
from src.models.recipe import Recipe


T = TypeVar('T')


class NomenclatureStoragePrototype(Generic[T], ABC):
    @abstractmethod
    def find(self, nomenclature_id) -> T:
        pass


    @staticmethod
    def _create_nomenclature_filter(key: str, nomenclature_id: str) -> Filter:
        return Filter(
            key,
            nomenclature_id,
            filter_type = FilterType.EQUALS
        )


class RecipePrototype(NomenclatureStoragePrototype[list[Recipe]]):
    _recipe_storage: RecipeStorage


    def __init__(self, recipe_storage):
        self._recipe_storage = recipe_storage
    

    def find(self, nomenclature_id) -> list[Recipe]:
        return self._recipe_storage.get_filtered([
            self._create_nomenclature_filter('ingredients.nomenclature.id', nomenclature_id)
        ])


class StoreTransactionPrototype(NomenclatureStoragePrototype[list[Recipe]]):
    _transaction_storage: StoreTransactionStorage


    def __init__(self, transaction_storage):
        self._transaction_storage = transaction_storage
    

    def find(self, nomenclature_id) -> list[Recipe]:
        return self._transaction_storage.get_filtered([
            self._create_nomenclature_filter('nomenclature.id', nomenclature_id)
        ])