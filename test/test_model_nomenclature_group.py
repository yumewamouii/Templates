import unittest


from src.models.nomenclature_group import NomenclatureGroup


class TestNomenclature(unittest.TestCase):
    def setUp(self):
        self.nomenclature_group = NomenclatureGroup()
        self.nomenclature_group_first = NomenclatureGroup()
        self.nomenclature_group_second = NomenclatureGroup()
    

    def test_create_nomenclature_group(self):
        self.assertIsInstance(self.nomenclature_group, NomenclatureGroup)
    

    def test_not_equal_nomenclature_groups(self):
        self.assertNotEquals(self.nomenclature_group_first, self.nomenclature_group_second)
    

    def test_not_equal_ids_nomenclature_groups(self):
        self.assertNotEquals(self.nomenclature_group_first.id, self.nomenclature_group_second.id)
    

    def test_equal_name_nomenclature_groups(self):
        self.assertEqual(self.nomenclature_group_first.name, self.nomenclature_group_second.name)