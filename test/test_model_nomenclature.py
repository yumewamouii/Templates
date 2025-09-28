import unittest


from src.models.nomenclature import Nomenclature
from src.exceptions.validation import ArgumentException


class TestNomenclature(unittest.TestCase):
    def setUp(self):
        self.nomenclature = Nomenclature()
        self.nomenclature_first = Nomenclature()
        self.nomenclature_second = Nomenclature()
    

    def test_create_nomenclature(self):
        self.assertIsInstance(self.nomenclature, Nomenclature)
    

    def test_not_equal_nomenclatures(self):
        self.assertNotEqual(self.nomenclature_first, self.nomenclature_second)
    

    def test_not_equal_ids_nomenclatures(self):
        self.assertNotEqual(self.nomenclature_first.id, self.nomenclature_second.id)
    

    def test_invalid_fullname_nomenclature(self):
        with self.assertRaises(ArgumentException) as e:
            self.nomenclature.fullname = 123
        self.assertEqual(str(e),
                          "ArgumentException: Incorrect type. <class 'str'> is expected. Current type is <class 'int'>")