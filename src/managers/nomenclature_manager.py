from src.managers.base_manager import BaseManager
from src.managers.base_state import BaseState


from src.repositories.nomenclature_repository import NomenclatureRepository


from src.store.nomenclature_storage_finder import NomenclatureStorageFinder


from src.models.nomenclature import Nomenclature


from src.utils.stream.base_observable import StreamSubscription


class NomenclatureManager(BaseManager[BaseState]):
    _nomenclature_repository: NomenclatureRepository
    _nomenclature_storage_finder: NomenclatureStorageFinder
    _nomenclature_update_subscription: StreamSubscription


    def __init__(self, nomenclature_repository, nomenclature_storage_finder):
        super().__init__(BaseState())
        self._nomenclature_repository = nomenclature_repository
        self._nomenclature_storage_finder = nomenclature_storage_finder
    

    def update_nomenclature(self, nomenclature_id: str, nomenclature: Nomenclature):
        self._nomenclature_repository.update_nomenclature(nomenclature_id, nomenclature)
    

    def delete_nomenclature(self, nomenclature_id: str) -> bool:
        if self._nomenclature_storage_finder.has_nomenclature_dependants(nomenclature_id):
            return False
        self._nomenclature_repository.delete_nomenclature(nomenclature_id)
        return True


    def get_nomenclature(self, nomenclature_id):
        return self._nomenclature_repository.get_nomenclature(nomenclature_id)
    

    def create_nomenclature(self, nomenclature: Nomenclature):
        return self._nomenclature_repository.create_nomenclature(nomenclature)
    

    def close(self):
        self._nomenclature_update_subscription.close()