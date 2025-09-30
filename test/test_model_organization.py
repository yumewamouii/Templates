import unittest


from src.models.organization import Organization
from src.settings_manager import SettingManager
from src.models.company import Company


class TestOrganization(unittest.TestCase):
    def setUp(self):
        self.organization = Organization()
        self.organization_first = Organization()
        self.organization_second = Organization()
    

    def test_create_organization(self):
        self.assertIsInstance(self.organization, Organization)
    

    def test_not_equal_organizations(self):
        self.assertNotEqual(self.organization_first, self.organization_second)
    

    def test_not_equal_ids_organizations(self):
        self.assertNotEqual(self.organization_first.id, self.organization_second.id)
    

    def test_equal_properties_without_id_organizations(self):
        self.assertEqual(self.organization_first.name, self.organization_second.name)
        self.assertEqual(self.organization_first.tin, self.organization_second.tin)
        self.assertEqual(self.organization_first.bic, self.organization_second.bic)
        self.assertEqual(self.organization_first.account, self.organization_second.account)
        self.assertEqual(self.organization_first.ownership_type, self.organization_second.ownership_type)
    

    def test_initialization(self):
        manager = SettingManager()
        manager.load_from_json('settings.json')
        company = Organization(manager.settings)
        self.assertEqual((self.organization.tin, self.organization.bic,
                        self.organization.account, self.organization.ownership_type), 
                        (company.tin, company.bic, company.account, company.ownership_type))