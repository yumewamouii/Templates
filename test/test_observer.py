import unittest


import uuid


from src.managers.nomenclature_manager import NomenclatureManager
from src.managers.start_manager import StartManager


from src.factories.nomenclature_factory import NomenclatureFactory


class TestPrimitiveSerializer(unittest.TestCase):
    def setUp(self):
        self.start_manager = StartManager()
        self.manager = NomenclatureManager()
        self.nomenclature = NomenclatureFactory().wheat_flour()
    

    def test_nomenclature_added(self):
        self.start_manager.init()
        self.nomenclature.id = str(uuid.uuid4())


        self.assertIs(self.manager.delete_nomenclature(str(uuid.uuid4())), True)
    

    def test_nomenclature_not_added_with_existing_reference(self):
        self.start_manager.init()


        self.assertIs(self.manager.delete_nomenclature(self.nomenclature.id), False)
