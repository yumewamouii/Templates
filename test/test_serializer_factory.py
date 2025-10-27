import unittest
import json
from datetime import datetime

from src.serialization.serializer_factory import SerializerFactory
from src.models.base_model import BaseModel
from src.exceptions.validation import ArgumentException


from src.models.company import Company



class TestSerializerFactory(unittest.TestCase):

    def setUp(self):
        self.factory = SerializerFactory()
        self.company = Company()


    def test_primitive_serializer(self):
        obj = 42
        result = self.factory.get_serializer(obj)
        self.assertEqual(json.loads(result), {'value': 42})

    def test_datetime_serializer(self):
        obj = datetime(2025, 10, 27, 12, 0, 0)
        result = self.factory.get_serializer(obj)
        self.assertEqual(json.loads(result), {'value': obj.isoformat()})

    def test_model_serializer(self):
        result = self.factory.get_serializer(self.company)
        data = json.loads(result)
        self.assertEqual(data['name'], self.company.name)
        self.assertEqual(data['tin'], self.company.tin)
        self.assertEqual(data['bic'], self.company.bic)
        self.assertEqual(data['account'], self.company.account)
        self.assertEqual(data['corr_account'], self.company.corr_account)
        self.assertEqual(data['ownership_type'], self.company.ownership_type)

    def test_unsupported_type_raises_exception(self):
        class Unsupported:
            pass

        obj = Unsupported()
        with self.assertRaises(ArgumentException) as context:
            self.factory.get_serializer(obj)
        self.assertIn("No suitable serializer found", str(context.exception))


if __name__ == "__main__":
    unittest.main()
