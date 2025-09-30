import unittest


from src.models.company import Company
from src.exceptions.validation import ArgumentException


class TestModelCompany(unittest.TestCase):
    def setUp(self):
        self.company = Company()
    

    def test_create_model_company(self):
        self.assertIsInstance(self.company, Company)
    

    def test_equal_properties_model_company(self):
        company_first = Company()
        company_second = Company()

        self.assertEqual(
            (company_first.name, company_first.tin, company_first.account, 
                company_first.corr_account, company_first.bic, company_first.ownership_type),
            (company_second.name, company_second.tin, company_second.account, 
                company_second.corr_account, company_second.bic, company_second.ownership_type)
        )
    

    def test_equals_id_model_company(self):
        company_first = Company()
        company_second = Company()

        self.assertNotEqual(id(company_first), id(company_second))
    

    def test_model_company_blank_name(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.name = ''
        self.assertEqual(str(e.exception), 
                        'ArgumentException: This argument can not be blank')
    

    def test_model_company_none_name(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.name = None
        self.assertEqual(str(e.exception), 
                        f'ArgumentException: Field can not be None')
    

    def test_model_company_invalid_name(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.name = 12345
        self.assertEqual(str(e.exception), 
                        "ArgumentException: Incorrect type. <class 'str'> is expected. Current type is <class 'int'>")
    

    def test_model_company_valid_name(self):
        self.company.name = 'Valve'
        self.assertEqual(self.company.name, 'Valve')
    

    def test_model_company_blank_tin(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.tin = 0
        self.assertEqual(str(e.exception), 
                        'ArgumentException: This argument can not be blank')
    

    def test_model_company_none_tin(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.tin = None
        self.assertEqual(str(e.exception), 
                        f'ArgumentException: Field can not be None')
    

    def test_model_company_invalid_length_tin(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.tin = 123456
        self.assertEqual(str(e.exception), 
                        'ArgumentException: Incorrect length of argument. The length of this argument should be 12')
    

    def test_model_company_valid_length_tin(self):
        self.company.tin = 123456654321
        self.assertEqual(len(str(self.company.tin)), 12)
    

    def test_model_company_invalid_tin(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.tin = 'something'
        self.assertEqual(str(e.exception), 
                        "ArgumentException: Incorrect type. <class 'int'> is expected. Current type is <class 'str'>")
    

    def test_model_company_valid_tin(self):
        self.company.tin = 123456789013
        self.assertEqual(self.company.tin, 123456789013)
    

    def test_model_company_blank_account(self):
        self.company.account = 0
        self.assertEqual(self.company.account, 0)
    

    def test_model_company_none_account(self):
        self.company.account = None
        self.assertEqual(self.company.account, 0)
    

    def test_model_company_invalid_length_account(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.account = 123456
        self.assertEqual(str(e.exception), 
                         'ArgumentException: Incorrect length of argument. The length of this argument should be 11')
    

    def test_model_company_valid_length_account(self):
        self.company.account = 12345678901
        self.assertEqual(len(str(self.company.account)), 11)
    

    def test_model_company_invalid_account(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.account = 'something'
        self.assertEqual(str(e.exception), 
                        "ArgumentException: Incorrect type. <class 'int'> is expected. Current type is <class 'str'>")
    

    def test_model_company_valid_account(self):
        self.company.account = 12345654321
        self.assertEqual(self.company.account, 12345654321)
    

    def test_model_company_blank_corr_account(self):
        self.company.corr_account = 0
        self.assertEqual(self.company.corr_account, 0)
    

    def test_model_company_none_corr_account(self):
        self.company.corr_account = None
        self.assertEqual(self.company.corr_account, 0)
    

    def test_model_company_invalid_length_corr_account(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.corr_account = 123456
        self.assertEqual(str(e.exception), 
                         'ArgumentException: Incorrect length of argument. The length of this argument should be 11')
    

    def test_model_company_valid_length_corr_account(self):
        self.company.corr_account = 12345678901
        self.assertEqual(len(str(self.company.corr_account)), 11)
    

    def test_model_company_invalid_corr_account(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.corr_account = 'something'
        self.assertEqual(str(e.exception), 
                        "ArgumentException: Incorrect type. <class 'int'> is expected. Current type is <class 'str'>")
    

    def test_model_company_valid_corr_account(self):
        self.company.corr_account = 12345654321
        self.assertEqual(self.company.corr_account, 12345654321)
    

    def test_model_company_blank_bic(self):
        self.company.bic = 0
        self.assertEqual(self.company.bic, 0)
    

    def test_model_company_none_bic(self):
        self.company.bic = None
        self.assertEqual(self.company.bic, 0)
    

    def test_model_company_invalid_length_bic(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.bic = 123456
        self.assertEqual(str(e.exception), 
                         'ArgumentException: Incorrect length of argument. The length of this argument should be 9')
    

    def test_model_company_valid_length_bic(self):
        self.company.bic = 123456789
        self.assertEqual(len(str(self.company.bic)), 9)
    

    def test_model_company_invalid_bic(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.bic = 'something'
        self.assertEqual(str(e.exception), 
                        "ArgumentException: Incorrect type. <class 'int'> is expected. Current type is <class 'str'>")
    

    def test_model_company_valid_bic(self):
        self.company.bic = 123456789
        self.assertEqual(self.company.bic, 123456789)
    

    def test_model_company_ownership_type_blank(self):
        self.company.ownership_type = ''
        self.assertEqual(self.company.ownership_type, '')
    

    def test_model_company_ownership_type_none(self):
        self.company.ownership_type = None
        self.assertEqual(self.company.ownership_type, '')
    

    def test_model_company_invalid_length_ownership_type(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.ownership_type = 'something'
        self.assertEqual(str(e.exception), 
                         'ArgumentException: Incorrect length of argument. The length of this argument should be 5')
    

    def test_model_company_valid_length_ownership_type(self):
        self.company.ownership_type = 'ООООО'
        self.assertEqual(len(str(self.company.ownership_type)), 5)
    

    def test_model_company_invalid_ownership_type(self):
        with self.assertRaises(ArgumentException) as e:
            self.company.ownership_type = 12345
        self.assertEqual(str(e.exception), 
                        "ArgumentException: Incorrect type. <class 'str'> is expected. Current type is <class 'int'>")


    def test_model_company_valid_ownership_type(self):
        self.company.ownership_type = 'ООООО'
        self.assertEqual(self.company.ownership_type, 'ООООО')


