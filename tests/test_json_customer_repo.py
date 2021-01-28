from repository.json_customer_repo import JsonCustomerRepo
from domain.company import Company
from domain.individual import Individual
import unittest


class TestJson(unittest.TestCase):
    def test_json_individual(self):
        individual_repo = JsonCustomerRepo("json_test.json", Individual)
        individual = Individual()
        individual.set_first_name("Ion")
        individual.set_last_name("Radu")
        individual.set_id(1)
        individual.set_email_address("ion.radu17@yahoo.com")
        individual.set_phone_number("0756456452")
        individual.set_cnp("1991217654455")
        individual_repo.store(individual)
        self.assertEqual(individual_repo.get(1), individual)
        individual.set_last_name("Dan")
        individual_repo.update(1, individual)
        individual_repo2 = JsonCustomerRepo("json_test.json", Individual)
        self.assertEqual(individual_repo.get(1), individual_repo2.get(1))
        individual_repo.reset_id()
        individual_repo.delete(1)

    def test_json_company(self):
        company_repo = JsonCustomerRepo("json_test.json", Company)
        company = Company()
        company.set_id(1)
        company.set_first_name("Ion")
        company.set_last_name("Radu")
        company.set_email_address("ion.radu17@yahoo.com")
        company.set_phone_number("0756456452")
        company.set_fiscal_no("0000123456789")
        company.set_company_name('MDFK')
        company.set_registration_number("RO01234")
        company_repo.store(company)
        self.assertEqual(company, company_repo.get(1))
        company.set_company_name("La 3 pasi")
        company_repo.update(1, company)
        company_repo2 = JsonCustomerRepo("json_test.json", Company)
        self.assertEqual(company_repo.get(1), company_repo2.get(1))
        company_repo.reset_id()
        company_repo.delete(1)