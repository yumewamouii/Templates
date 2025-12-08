import datetime
from typing import List
from copy import deepcopy

from src.store.start_store_factory import StartStoreFactory
from src.store.list_filterer import ListFilterer
from src.store.store_storage import StoreStorage
from src.store.store_transaction_storage import StoreTransactionStorage
from src.store.turnover_storage import TurnoverStorage
from src.models.filter import Filter
from src.models.filter_type import FilterType
from src.models.filter_utils import FilterUtils
from src.models.storage import Storage
from src.models.store_transaction import StoreTransaction
from src.models.store_turnover import StoreTurnover
from src.utils.turnovers_from_transactions import TurnoversFromTransactions


class StoreRepository:
    """
    Repository for managing stores, store transactions, and calculating turnovers.
    Integrates storage layers and provides filtered access to entities.
    """

    def __init__(
        self,
        store_transaction_storage: StoreTransactionStorage,
        store_storage: StoreStorage,
        turnover_storage: TurnoverStorage,
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
        self._turnover_storage = turnover_storage
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
    

    def update_transaction(self, transaction_id: str, transaction: StoreTransaction):
        self._store_transaction_storage.update(transaction_id, transaction)

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

    def get_turnovers(self, filters: List[Filter], grouping: List[str], blocking_date: datetime.datetime) -> List[StoreTurnover]:
        time_filter = FilterUtils.find_filter(filters, 'time', FilterType.BETWEEN)


        if time_filter.value.from_value is not None and time_filter.value.from_value > datetime.datetime.min:
            return TurnoversFromTransactions.calculate(
                self._store_transaction_storage.get_filtered(filters),
                grouping
            )


        cached_turnovers = self._get_cached_turnovers(filters, grouping, blocking_date)
        time_filter.value.from_value = blocking_date
        transactions = self._store_transaction_storage.get_filtered(filters)


        new_turnovers = TurnoversFromTransactions().calculate(transactions, grouping)


        return TurnoversFromTransactions.merge(cached_turnovers, new_turnovers)
    

    def _get_cached_turnovers(self, filters: list[Filter], grouping: list[str], blocking_date: datetime.datetime) -> List[StoreTurnover]:
        turnovers = self._turnover_storage.get(blocking_date.timestamp())


        filters = deepcopy(filters)


        if turnovers is None or grouping != StoreTurnover.default_grouping():
            time_filter = FilterUtils.find_filter(filters, 'time', FilterType.BETWEEN)
            time_filter.value.from_value = datetime.datetime.min
            time_filter.value.to_value = blocking_date
            self._turnover_storage.clear()


            transaction = self._store_transaction_storage.get_filtered(filters)
            turnovers = TurnoversFromTransactions().calculate(transaction, grouping)
            self._turnover_storage.update(blocking_date.timestamp(), turnovers)
        

        filters = FilterUtils.remove_filter(filters, 'time', FilterType.BETWEEN)
        turnovers = ListFilterer.apply_filters(turnovers, filters, value_to_filter = 'group')


        return turnovers
