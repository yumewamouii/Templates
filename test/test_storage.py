import unittest
import uuid


from src.models.storage import Storage


class TestStorage(unittest.TestCase):
    def text_equals_storage_model_create(self):
        #Preparing
        storage1 = Storage()
        storage2 = Storage()


        #Action GUID


        #Checking
        self.assertEqual(storage1, storage2)