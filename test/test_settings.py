import unittest


from src.models.settings import Settings
from src.exceptions.validation import ArgumentException


class TestModelSettings(unittest.TestCase):
    def setUp(self):
        self.settings = Settings()
        self.settings_first = Settings()
        self.settings_two = Settings()
    

    def test_create_settings(self):
        self.assertIsInstance(self.settings, Settings)