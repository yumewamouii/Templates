from datetime import datetime
from typing import List

from src.start_nomenclature_factory import StartNomenclatureFactory
from src.models.measurement_unit import MeasurementUnit
from src.models.storage import Storage
from src.models.store_transaction import StoreTransaction, StoreTransactionType


class StartStoreFactory:
    """
    Factory for creating initial store data including storages and store transactions.
    """

    def __init__(self, nomenclatures_factory: StartNomenclatureFactory):
        """
        Args:
            nomenclatures_factory (StartNomenclatureFactory): Factory providing base nomenclature items.
        """
        self._nomenclatures_factory = nomenclatures_factory

    def storages(self) -> List[Storage]:
        """
        Returns a list of predefined storages.
        """
        return [
            Storage('Москва, ул. Ленина, 7'),
            Storage('Новосибирск, ул. Кирова, 15'),
        ]

    def storage_transactions(self) -> List[StoreTransaction]:
        """
        Returns a list of predefined store transactions with income and expense entries.
        """
        wheat_flour = self._nomenclatures_factory.wheat_flour()
        milk = self._nomenclatures_factory.milk()

        return [
            StoreTransaction(
                store=self.storages()[0],
                nomenclature=wheat_flour,
                amount=MeasurementUnit(50.0, wheat_flour.unit),
                transaction_type=StoreTransactionType.INCOME,
                time=datetime(2020, 1, 1, 1, 5, 9)
            ),
            StoreTransaction(
                store=self.storages()[1],
                nomenclature=wheat_flour,
                amount=MeasurementUnit(50.0, wheat_flour.unit),
                transaction_type=StoreTransactionType.EXPENSE,
                time=datetime(2020, 1, 3, 6, 3, 7)
            ),
            StoreTransaction(
                store=self.storages()[0],
                nomenclature=wheat_flour,
                amount=MeasurementUnit(50.0, wheat_flour.unit),
                transaction_type=StoreTransactionType.EXPENSE,
                time=datetime(2020, 1, 5, 5, 8, 2)
            ),
            StoreTransaction(
                store=self.storages()[1],
                nomenclature=milk,
                amount=MeasurementUnit(1.0, milk.unit),
                transaction_type=StoreTransactionType.INCOME,
                time=datetime(2020, 1, 5, 5, 8, 2)
            ),
            StoreTransaction(
                store=self.storages()[0],
                nomenclature=milk,
                amount=MeasurementUnit(1.0, milk.unit),
                transaction_type=StoreTransactionType.EXPENSE,
                time=datetime(2020, 1, 5, 5, 8, 2)
            ),
        ]
