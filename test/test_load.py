import unittest
from unittest import mock
import os
import tempfile
import json


from src.settings_manager import settingManager
from src.models.settings import Settings


class testLoad(unittest.TestCase):
    def setUp(self):
        self.sm = settingManager()
        self.sm._settingManager__settings = Settings()
        self.sample_dict = {
            'company': {
                'tin': '123456789012',
                'account': '12345678901',
                'corr_account': '12345678901',
                'bic': '123456789',
                'name': 'Пога и Попыта',
                'ownership_type': 'ООООО'
            }
        }
    

    def test_load_from_json_custom_path(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, "settings2.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(self.sample_dict, f)

            self.sm.load_from_json(file_path)

            self.assertEqual(self.sm.settings.name, 'Пога и попыта')
            self.assertEqual(self.sm.settings.tin, '123456789012')
    

    def test_load_from_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, 'settings2.json')
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.sample_dict, f)
            with mock.patch('os.path.join', return_value = file_path):
                self.sm.load_from_json()
            
            self.assertEqual(self.sm.settings.name, 'Пога и попыта')
            self.assertEqual(self.sm.settings.tin, '123456789012')
    

    def test_load_from_dict(self):
        self.sm.load_from_dict(self.sample_dict)
        self.assertEqual(self.sm.settings.name, 'Пога и попыта')
        self.assertEqual(self.sm.settings.tin, '123456789012')
