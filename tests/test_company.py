import unittest
from domain.company import Company


class TestCompanyDomain(unittest.TestCase):

    def test_company_getters(self):
        company = Company("La Rica", "RO0123", "123456")
        self.assertEqual(company.get_company_name(), "La Rica")
        self.assertEqual(company.get_registration_number(), "RO0123")
        self.assertEqual(company.get_fiscal_no(), "123456")

    def test_company_setters(self):
        company = Company("La Rica", "RO0123", "123456")
        company.set_company_name("Pleso Academy")
        company.set_fiscal_no("RO2345")
        company.set_registration_number("12345")
        self.assertEqual(company.get_company_name(), "Pleso Academy")
        self.assertEqual(company.get_registration_number(), "12345")
        self.assertEqual(company.get_fiscal_no(), "RO2345")