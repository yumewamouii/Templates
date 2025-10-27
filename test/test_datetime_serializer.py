import unittest
import datetime


from src.serialization.datetime_serializer import DatetimeSerializer


class TestDatetimeSerializer(unittest.TestCase):
    def setUp(self):
        self.serializer = DatetimeSerializer()
    
    def test_create_datetime_serializer(self):
        self.assertIsInstance(self.serializer, DatetimeSerializer)
    

    def test_datetime_serializer_for_datetime(self):
        self.assertEqual(self.serializer.serialize(datetime.datetime(2025, 10, 26)), {'value': '2025-10-26T00:00:00'})