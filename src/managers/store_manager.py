from src.managers.base_manager import BaseManager
from src.managers.base_state import BaseState


from src.repositories.nomenclature_repository import NomenclatureRepository
from src.store.store_repository import StoreRepository


from src.store.nomenclature_storage_finder import NomenclatureStorageFinder


from src.models.nomenclature import Nomenclature


from src.utils.stream.base_observable import StreamSubscription


class StoreManager(BaseManager[BaseState]):
    _nomenclature_repository: NomenclatureRepository
    _store_repository: StoreRepository
    _nomenclature_storage_finder: NomenclatureStorageFinder
    _nomenclature_updates_subscription: StreamSubscription


    def __init__(self, nomenclature_repository, store_repository, nomenclature_storage_finder):
        super().__init__(BaseState())
        self._nomenclature_repository = nomenclature_repository
        self._store_repository = store_repository
        self._nomenclature_storage_finder = nomenclature_storage_finder
    

    def init(self):
        self._nomenclature_updates_subscription = self._nomenclature_repository.watch_nomenclature_updates().subscribe(self._on_nomenclature_updated)
    

    def _on_nomenclature_updated(self, nomenclature: Nomenclature):
        transactions = self._nomenclature_storage_finder.find_dependant_transactions(nomenclature.id)


        for transaction in transactions:
            transaction.nomenclature = nomenclature
            self._store_repository.update_transaction(transaction.id, transaction)


    def close(self):
        self._nomenclature_updates_subscription.close()