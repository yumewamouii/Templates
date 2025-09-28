import unittest
from unittest import mock
import os
import tempfile
import json


from src.settings_manager import SettingManager
from src.models.settings import Settings


class testLoad(unittest.TestCase):
    def setUp(self):
        self.sm = SettingManager()
        self.sm._settings = Settings()
        self.sample_dict = {
            'company': {
                'tin': 123456789012,
                'account': 12345678901,
                'corr_account': 12345678901,
                'bic': 123456789,
                'name': 'Пога и Попыта',
                'ownership_type': 'ООООО'
            }
        }
    

    def test_load_from_json(self):
        self.sm.load_from_json('settings2.json')
        self.assertEqual(self.sm._settings.company.name, 'Пога и Попыта')
        self.assertEqual(self.sm._settings.company.tin, 123456789012)
        self.assertEqual(self.sm._settings.company.bic, 123456789)
        self.assertEqual(self.sm._settings.company.account, 12345678901)
        self.assertEqual(self.sm._settings.company.corr_account, 12345678901)
        self.assertEqual(self.sm._settings.company.ownership_type, 'ООООО')
    

    def test_convert(self):
        self.sm.convert(self.sample_dict)
        self.assertEqual(self.sm._settings.company.name, 'Пога и Попыта')
        self.assertEqual(self.sm._settings.company.tin, 123456789012)
