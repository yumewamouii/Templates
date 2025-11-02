import unittest


from src.serialization.primitive_serializer import PrimitiveSerializer


class TestPrimitiveSerializer(unittest.TestCase):
    def setUp(self):
        self.serializer = PrimitiveSerializer()
    def test_create_primitive_serializer(self):
        self.assertIsInstance(self.serializer, PrimitiveSerializer)
    

    def test_primitive_serializer_for_str(self):
        self.assertEqual(self.serializer.serialize('yooo'), {'value': 'yooo'})
    

    def test_primitive_serializer_for_int(self):
        self.assertEqual(self.serializer.serialize(52), {'value': 52})
    

    def test_primitive_serializer_for_float(self):
        self.assertEqual(self.serializer.serialize(13.37), {'value': 13.37})
    

    def test_primitive_serializer_for_bool(self):
        self.assertEqual(self.serializer.serialize(False), {'value': False})


    