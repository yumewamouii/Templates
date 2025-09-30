import unittest


from src.models.storage import Storage


class TestStorage(unittest.TestCase):
    def setUp(self) -> None:
        self.storage = Storage()
        self.storage_first = Storage()
        self.storage_second = Storage()
    

    def test_create_storage(self) -> None:
        self.assertIsInstance(self.storage, Storage)
    

    def test_not_equal_storages(self):
        self.assertNotEqual(self.storage_first, self.storage_second)
    

    def test_not_equal_ids_storages(self):
        self.assertNotEqual(self.storage_first.id, self.storage_second.id)
    

    def test_equal_names_storages(self):
        self.assertEqual(self.storage_first.name, self.storage_second.name)