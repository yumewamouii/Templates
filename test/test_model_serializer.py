import unittest


from src.serialization.model_serializer import ModelSerializer


from src.models.company import Company


class TestModelSerializer(unittest.TestCase):
    def setUp(self) -> None:
        self.serializer = ModelSerializer()
        self.company = Company()
    

    def test_model_serializer(self):
        result = self.serializer.serialize(self.company)
        self.assertEqual(result['name'], self.company.name)
        self.assertEqual(result['tin'], self.company.tin)
        self.assertEqual(result['bic'], self.company.bic)
        self.assertEqual(result['account'], self.company.account)
        self.assertEqual(result['corr_account'], self.company.corr_account)
        self.assertEqual(result['ownership_type'], self.company.ownership_type)
        