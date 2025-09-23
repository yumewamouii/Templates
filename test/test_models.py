from src.models.company_model import companyModel
import unittest


class testModels(unittest.TestCase):

    def test_empty_createmodel_company_model_test(self):
        model = companyModel()
        self.assertEqual(model.name, "")

    def test_notEmpty_createmodel_company_model_test(self):
        model = companyModel()
        model.name = "test"
        self.assertNotEqual(model.name, "bebebe")
    
if __name__ == "__main__":
    unittest.main()
