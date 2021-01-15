import unittest
from repository.customer_repo import CustomerRepo
from domain.company import Company


class TestCompanyRepo(unittest.TestCase):
    def test_company_repo(self):
        company = Company("La Gigi", "RO0231", "6859662")
        company.set_id(1)
        company.set_first_name("Gigi")
        company.set_last_name("Petre")
        company.set_phone_number("0756234123")
        company.set_email_address("lagigi123@yahoo.com")
        company_repo = CustomerRepo(Company)
        company_repo.store(company)
        self.assertEqual(company_repo.get(1), company)

        company.set_company_name("La Gigi Acasa")
        company.set_id(2)
        company_repo.update(company_repo.get(1), company)
        self.assertEqual(company_repo.get(2), company)
        company_repo.delete(2)
        self.assertEqual(company_repo.get_all(), [])
