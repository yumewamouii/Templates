import datetime
from enum import Enum


from src.exceptions.validation import ArgumentException


from src.models.base_model import BaseModel
from src.models.measurement_unit import MeasurementUnit
from src.models.nomenclature import Nomenclature
from src.models.storage import Storage


from src.utils.enum_meta import EnumMeta
from src.utils.fields import ValidatedField


class StoreTransactionType(Enum, metaclass = EnumMeta):
    INCOME = 1
    EXPENSE = 2


class StoreTransaction(BaseModel):
    storage = ValidatedField(expected_type = Storage, nullable = True, default = None)
    nomenclature = ValidatedField(expected_type = Nomenclature, nullable = True, default = None)
    amount = ValidatedField(expected_type = int, nullable = True, blank = True, default = 0)
    measurement_unit = ValidatedField(expected_type = MeasurementUnit, nullable = True, default = None)
    transaction_type = ValidatedField(expected_type = StoreTransactionType, nullable = True, default = None)
    date = ValidatedField(expected_type = datetime.datetime, nullable = True, default = None)


    def __init__(self, storage: Storage = None, nomenclature: Nomenclature = None, amount: int = 0,
                measurement_unit: MeasurementUnit = None, transaction_type: StoreTransactionType = None, date: datetime.datetime = None):
        super().__init__()


        self.storage = storage
        self.nomenclature = nomenclature
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date