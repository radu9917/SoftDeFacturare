import unittest
from repository.company_repo import CompanyRepo
from domain.company import Company


class TestCompanyRepo(unittest.TestCase):
    def test_company_repo(self):
        company = Company("La Gigi", "RO0231", "6859662")
        company.set_id(1)
        company.set_first_name("Gigi")
        company.set_last_name("Petre")
        company.set_phone_number("0756234123")
        company.set_email_address("lagigi123@yahoo.com")
        company_repo = CompanyRepo()
        company_repo.store(company)
        self.assertEqual(company_repo.get(1), company)
        company2 = company
        company2.set_company_name("La Gigi Acasa")
        company2.set_id(2)
        company_repo.update(company, company2)
        self.assertEqual(company_repo.get(2), company2)
        company_repo.delete(2)
        self.assertEqual(company_repo.get_all(), [])
