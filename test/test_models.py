from src.models.settings import Settings
import unittest


class testModels(unittest.TestCase):

    def test_empty_createmodel_company_model_test(self):
        model = Settings()
        self.assertEqual(model.name, "")

    def test_notEmpty_createmodel_company_model_test(self):
        model = Settings()
        model.name = "test"
        self.assertNotEqual(model.name, "bebebe")
    
if __name__ == "__main__":
    unittest.main()
