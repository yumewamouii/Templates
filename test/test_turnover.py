import unittest
import random
import time
from datetime import datetime


from src.models.measured_value import MeasuredValue
from src.models.measurement_unit import MeasurementUnit
from src.models.nomenclature import Nomenclature
from src.models.storage import Storage
from src.models.store_transaction import StoreTransaction, StoreTransactionType
from src.models.range import RangeModel
from src.models.filter import Filter
from src.models.filter_type import FilterType
from src.models.store_turnover import StoreTurnover
from src.mappers.absolute_mapper import AbsoluteMapper
from src.utils.turnovers_from_transactions import TurnoversFromTransactions
from src.store.start_store_factory import StartStoreFactory
from src.store.store_repository import StoreRepository
from src.store.store_transaction_storage import StoreTransactionStorage
from src.store.list_filterer import ListFilterer




class TestTurnoversFromTransactionsPrototype(unittest.TestCase):
    def setUp(self):
        # Создаём базовые данные без DI
        self.kg = MeasurementUnit('kg', 1000)
        self.liter = MeasurementUnit('l', 1)

        self.sugar = Nomenclature(name='Sugar', unit=self.kg)
        self.milk = Nomenclature(name='Milk', unit=self.liter)

        self.store = Storage(name='Main storage')

        self.transactions: list[StoreTransaction] = [
            StoreTransaction(
                store=self.store,
                nomenclature=self.sugar,
                amount=MeasuredValue(50.0, self.kg),
                transaction_type=StoreTransactionType.INCOME,
                time=datetime(2020, 1, 1, 1, 5, 9),
            ),
            StoreTransaction(
                store=self.store,
                nomenclature=self.sugar,
                amount=MeasuredValue(25.0, self.kg),
                transaction_type=StoreTransactionType.EXPENSE,
                time=datetime(2020, 1, 3, 6, 3, 7),
            ),
        ]

    def generated_transaction(self):
        storages = StartStoreFactory().storages()
        result = []


        for i in range(10000):
            transaction_type = random.randint(0, 1)
            if transaction_type == 0:
                transaction_type = StoreTransactionType.INCOME
            else:
                transaction_type = StoreTransactionType.EXPENSE
        
            result.append(
                StoreTransaction(
                   store = storages[i % len(storages)],
                   nomenclature=self.sugar,
                   amount = MeasuredValue(random.randint(1, 100), self.kg),
                   transaction_type = transaction_type,
                   time = datetime.fromtimestamp(0)
                )
            )
        

        return result
    
    
    
    def test_turnover_calculation(self):
        process = TurnoversFromTransactions()
        turnover = process.calculate(self.transactions, ['nomenclature', 'store'])

        expected = MeasuredValue(25.0, self.kg)
        self.assertEqual(turnover[0].turnover, expected)
    

    def test_cached_calculation(self, generated_transaction):
        repo = StoreRepository()
        trans = StoreTransactionStorage()
        for transaction in generated_transaction:
            trans.create(transaction)
        

        t = time.process_time()
        no_caching_result = repo.get_turnovers(
            [Filter('time', RangeModel(datetime.fromtimestamp(0), datetime.now()), FilterType.BETWEEN)],
            StoreTurnover.default_grouping(), datetime.now()
        )
        t1 = time.process_time() - t


        t = time.process_time()
        caching_result = repo.get_turnovers(
            [Filter('time', RangeModel(datetime.fromtimestamp(0), datetime.now()), FilterType.BETWEEN)],
            StoreTurnover.default_grouping(), datetime.now()
        )

        t2 = time.process_time() - t


        print()


        print('Без кэша:', 'Время выполнения:', t1)
        print('С кэшем: ', 'Время выполнения:', t2)


        assert len(caching_result) == len(no_caching_result)
        assert t2 < t1

    def test_turnover_calculation_with_different_nomenclature(self):
        process = TurnoversFromTransactions()

        self.transactions.append(
            StoreTransaction(
                store=self.store,
                nomenclature=self.milk,
                amount=MeasuredValue(1.0, self.liter),
                transaction_type=StoreTransactionType.EXPENSE,
                time=datetime(2020, 1, 5, 5, 8, 2),
            )
        )

        turnover = process.calculate(self.transactions, ['nomenclature', 'store'])

        self.assertEqual(len(turnover), 2)
        self.assertEqual(turnover[0].turnover, MeasuredValue(25.0, self.kg))
        self.assertEqual(turnover[1].turnover, MeasuredValue(-1.0, self.liter))