from datetime import datetime
from typing import List

from src.store.start_store_factory import StartStoreFactory
from src.store.store_storage import StoreStorage
from src.store.store_transaction_storage import StoreTransactionStorage
from src.models.filter import Filter
from src.models.storage import Storage
from src.models.store_transaction import StoreTransaction
from src.models.store_turnover import StoreTurnover
from src.utils.turnovers_from_transactions import TurnoversFromTransactionsPrototype


class StoreRepository:
    """
    Repository for managing stores, store transactions, and calculating turnovers.
    Integrates storage layers and provides filtered access to entities.
    """

    def __init__(
        self,
        store_transaction_storage: StoreTransactionStorage,
        store_storage: StoreStorage,
        start_store_factory: StartStoreFactory
    ):
        """
        Args:
            store_transaction_storage (StoreTransactionStorage): Storage layer for store transactions.
            store_storage (StoreStorage): Storage layer for stores.
            start_store_factory (StartStoreFactory): Factory for initial store and transaction data.
        """
        self._store_transaction_storage = store_transaction_storage
        self._store_storage = store_storage
        self._start_store_factory = start_store_factory

    def init_start_stores(self):
        """
        Initialize stores and transactions using StartStoreFactory if storage layers are empty.
        Ensures the system starts with predefined data.
        """
        if self._store_storage.is_empty():
            for store in self._start_store_factory.storages():
                self._store_storage.create(store)

        if self._store_transaction_storage.is_empty():
            for transaction in self._start_store_factory.storage_transactions():
                self._store_transaction_storage.create(transaction)

    def get_stores(self, filters: List[Filter]) -> List[Storage]:
        """
        Retrieve stores filtered according to the provided filters.

        Args:
            filters (List[Filter]): Filters to apply to stores.

        Returns:
            List[Storage]: Filtered list of stores.
        """
        return self._store_storage.get_filtered(filters)

    def get_store_transactions(self, filters: List[Filter]) -> List[StoreTransaction]:
        """
        Retrieve store transactions filtered according to the provided filters.

        Args:
            filters (List[Filter]): Filters to apply to transactions.

        Returns:
            List[StoreTransaction]: Filtered list of transactions.
        """
        return self._store_transaction_storage.get_filtered(filters)

    def get_turnovers(self, filters: List[Filter], grouping: List[str]) -> List[StoreTurnover]:
        """
        Calculate turnovers from store transactions filtered and grouped.

        Args:
            filters (List[Filter]): Filters to apply to transactions.
            grouping (List[str]): Fields to group transactions by.

        Returns:
            List[StoreTurnover]: Calculated turnovers grouped by specified fields.
        """
        transactions = self._store_transaction_storage.get_filtered(filters)
        return TurnoversFromTransactionsPrototype().calculate(transactions, grouping)
