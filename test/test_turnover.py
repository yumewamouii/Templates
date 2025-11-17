import unittest
from datetime import datetime


from src.models.measured_value import MeasuredValue
from src.models.measurement_unit import MeasurementUnit
from src.models.nomenclature import Nomenclature
from src.models.storage import Storage
from src.models.store_transaction import StoreTransaction, StoreTransactionType
from src.utils.turnovers_from_transactions import TurnoversFromTransactionsPrototype



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

    def test_turnover_calculation(self):
        process = TurnoversFromTransactionsPrototype()
        turnover = process.calculate(self.transactions, ['nomenclature', 'store'])

        expected = MeasuredValue(25.0, self.kg)
        self.assertEqual(turnover[0].turnover, expected)

    def test_turnover_calculation_with_different_nomenclature(self):
        process = TurnoversFromTransactionsPrototype()

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