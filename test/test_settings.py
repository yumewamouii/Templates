import unittest


from src.models.settings import Settings
from src.exceptions.validation import ArgumentException


class TestModelSettings(unittest.TestCase):
    def setUp(self):
        self.settings = Settings()
        self.settings_first = Settings()
        self.settings_second = Settings()
    

    def test_create_settings(self):
        self.assertIsInstance(self.settings, Settings)
    

    def test_not_equal_settings(self):
        self.assertNotEqual(self.settings_first, self.settings_second)
    

    def test_not_equal_ids_settings(self):
        self.assertNotEqual(self.settings_first.company.id, self.settings_second.company.id)
    

    def test_equal_properties_without_id_settings(self):
        self.assertEqual((self.settings_first.company.name, self.settings_first.company.tin, self.settings_first.company.account,
                          self.settings_first.company.corr_account, self.settings_first.company.bic, 
                          self.settings_first.company.ownership_type),
                          (self.settings_second.company.name, self.settings_second.company.tin, self.settings_second.company.account,
                          self.settings_second.company.corr_account, self.settings_second.company.bic, 
                          self.settings_second.company.ownership_type))