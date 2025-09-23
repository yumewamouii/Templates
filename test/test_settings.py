import unittest


from src.models.settings import Settings
from src.settings_manager import settingManager


class testSettings(unittest.TestCase):
    def test_tin_empty(self):
        settings = Settings()
        self.assertEqual(settings.tin, '')


    def test_tin_valid(self):
        settings = Settings()
        settings.tin = '123456789012'
        self.assertEqual(settings.tin, '123456789012')


    def test_tin_invalid(self):
        settings = Settings()
        with self.assertRaises(ValueError, msg='TIN must be string and contain 12 characters.'):
            settings.tin = '123456'
    

    def test_account_empty(self):
        settings = Settings()
        self.assertEqual(settings.account, '')
    

    def test_account_valid(self):
        settings = Settings()
        settings.account = '12345678901'
        self.assertEqual(settings.account, '12345678901')
    

    def test_account_invalid(self):
        settings = Settings()
        with self.assertRaises(ValueError, msg='account must be string and contain 11 characters.'):
            settings.account = '123456'
    

    def test_corr_account_empty(self):
        settings = Settings()
        self.assertEqual(settings.corr_account, '')
    

    def test_corr_account_valid(self):
        settings = Settings()
        settings.corr_account = '12345678901'
        self.assertEqual(settings.corr_account, '12345678901')
    

    def test_corr_account_invalid(self):
        settings = Settings()
        with self.assertRaises(ValueError, msg='correspondent account must be string and contain 11 characters.'):
            settings.corr_account = '123456'
    

    def test_bic_empty(self):
        settings = Settings()
        self.assertEqual(settings.bic, '')
    

    def test_bic_valid(self):
        settings = Settings()
        settings.bic = '123456789'
        self.assertEqual(settings.bic, '123456789')
    

    def test_bic_invalid(self):
        settings = Settings()
        with self.assertRaises(ValueError, msg='BIC must be string and contain 9 characters.'):
            settings.bic = '1234567'
    

    def test_name_empty(self):
        settings = Settings()
        self.assertEqual(settings.name, '')
    

    def test_name_valid(self):
        settings = Settings()
        settings.name = 'Пога и попыта'
        self.assertEqual(settings.name, 'Пога и попыта')
    

    def test_name_invalid(self):
        settings = Settings()
        with self.assertRaises(ValueError, msg='name must be string.'):
            settings.name = 123
    

    def test_ownership_type_empty(self):
        settings = Settings()
        self.assertEqual(settings.ownership_type, '')
    

    def test_ownership_type_valid(self):
        settings = Settings()
        settings.ownership_type = 'ООООО'
        self.assertEqual(settings.ownership_type, 'ООООО')
    

    def test_ownership_type_invalid(self):
        settings = Settings()
        with self.assertRaises(ValueError, msg='ownership type must be string.'):
            settings.ownership_type = 123