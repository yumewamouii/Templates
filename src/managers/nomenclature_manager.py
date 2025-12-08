from src.managers.base_manager import BaseManager
from src.managers.base_state import BaseState


from src.repositories.nomenclature_repository import NomenclatureRepository


from src.store.nomenclature_storage_finder import NomenclatureStorageFinder


from src.models.nomenclature import Nomenclature


from utils.observer.base_observable import StreamSubscription


class NomenclatureManager(BaseManager[BaseState]):
    """
    The manager for managing the item.
    Provides methods for creating, updating, deleting, and retrieving items.
    """


    _nomenclature_repository: NomenclatureRepository
    _nomenclature_storage_finder: NomenclatureStorageFinder
    _nomenclature_update_subscription: StreamSubscription


    def __init__(self, nomenclature_repository, nomenclature_storage_finder):
        super().__init__(BaseState())
        self._nomenclature_repository = nomenclature_repository
        self._nomenclature_storage_finder = nomenclature_storage_finder
        self._nomenclature_update_subscription = None
    

    def update_nomenclature(self, nomenclature_id: str, nomenclature: Nomenclature):
        """
        Updates the existing nomenclature.
        """
        self._nomenclature_repository.update_nomenclature(nomenclature_id, nomenclature)
    

    def delete_nomenclature(self, nomenclature_id: str) -> bool:
        """
        Deletes an item if there are no dependent objects on it.
        """
        if self._nomenclature_storage_finder.has_nomenclature_dependants(nomenclature_id):
            return False
        self._nomenclature_repository.delete_nomenclature(nomenclature_id)
        return True


    def get_nomenclature(self, nomenclature_id):
        """
        Gets the item by ID.
        """


        return self._nomenclature_repository.get_nomenclature(nomenclature_id)
    

    def create_nomenclature(self, nomenclature: Nomenclature):
        """
        Creates a new nomenclature.
        """
        return self._nomenclature_repository.create_nomenclature(nomenclature)
    

    def close(self):
        """
        Closes the active subscription for item updates (if any).
        """
        if self._nomenclature_update_subscription:
            self._nomenclature_update_subscription.close()
            self._nomenclature_update_subscription = None