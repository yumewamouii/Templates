from src.managers.base_manager import BaseManager
from src.managers.base_state import BaseState


from src.repositories.nomenclature_repository import NomenclatureRepository
from src.store.store_repository import StoreRepository


from src.store.nomenclature_storage_finder import NomenclatureStorageFinder


from src.models.nomenclature import Nomenclature


from utils.observer.base_observable import StreamSubscription


class StoreManager(BaseManager[BaseState]):
    """
    A storage status manager that monitors item changes.
    When the item is updated, it automatically updates all related transactions.
    """


    _nomenclature_repository: NomenclatureRepository
    _store_repository: StoreRepository
    _nomenclature_storage_finder: NomenclatureStorageFinder
    _nomenclature_updates_subscription: StreamSubscription[Nomenclature]


    def __init__(self, nomenclature_repository, store_repository, nomenclature_storage_finder):
        """
        Initializes the manager with dependent repositories.

        Args:
            nomenclature_repository: A repository for receiving nomenclature updates.
            store_repository: A repository for updating transactions.
            nomenclature_storage_finder: A service for searching for dependent transactions.
        """

        
        super().__init__(BaseState())
        self._nomenclature_repository = nomenclature_repository
        self._store_repository = store_repository
        self._nomenclature_storage_finder = nomenclature_storage_finder
        self._nomenclature_updates_subscription = None
    

    def init(self) -> None:
        """
        Starts listening for item updates.
        Subscribes to the stream of changes.
        """
        self._nomenclature_updates_subscription = self._nomenclature_repository.watch_nomenclature_updates().subscribe(self._on_nomenclature_updated)
    

    def _on_nomenclature_updated(self, nomenclature: Nomenclature) -> None:
        """
        The item change handler.
        Updates all transactions that depend on the specified item.

        Args:
            nomenclature: The updated item item.
        """
        transactions = self._nomenclature_storage_finder.find_dependant_transactions(nomenclature.id)


        for transaction in transactions:
            transaction.nomenclature = nomenclature
            self._store_repository.update_transaction(transaction.id, transaction)


    def close(self) -> None:
        """
        Stops listening for item updates.
        Closes the active subscription.
        """


        if self._nomenclature_updates_subscription:
            self._nomenclature_updates_subscription.close()
            self._nomenclature_updates_subscription = None