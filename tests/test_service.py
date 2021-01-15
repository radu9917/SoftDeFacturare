from repository.item_repo import ItemRepo
from repository.bill_repo import BillRepo
from repository.currency_repo import CurrencyRepo
from repository.customer_repo import CustomerRepo
from domain.invoice import Invoice
from domain.company import Company
from domain.fiscal_bill import FiscalBill
from domain.individual import Individual
from domain.item import Item
from domain.currency import Currency
from service.service import Service
import unittest


class TestService(unittest.TestCase):
    def test_item_options(self):
        service = Service(BillRepo(Invoice), BillRepo(FiscalBill), CurrencyRepo(), ItemRepo(), CustomerRepo(Company),
                          CustomerRepo(Individual))
        item = Item()
        currency = Currency("$", "Dollar", "USD")
        item.set_id(1)
        item.set_currency(currency)
        item.set_name("McChicken")
        item.set_description("Chicken hamburger")
        item.set_price(2)
        item.set_discount(0)
        service.create_item(item)
        self.assertEqual([item], service.view_item())
        item.set_price(3)
        item.set_id(2)
        service.modify_item(1, item)
        self.assertEqual(service.view_item(), [item])
        service.delete_item(item)
        self.assertEqual(service.view_item(), [])

    def test_currency_options(self):
        service = Service(BillRepo(Invoice), BillRepo(FiscalBill), CurrencyRepo(), ItemRepo(), CustomerRepo(Company),
                          CustomerRepo(Individual))
        currency = Currency("$", "Dollar", "USD")
        currency.set_id(1)
        service.create_currency(currency)
        self.assertEqual(service.view_currency(), [currency])
        currency.set_id(2)
        currency.set_name("US Dollar")
        service.modify_currency(1, currency)
        self.assertEqual(service.view_currency(), [currency])
        service.delete_currency(currency)
        self.assertEqual(service.view_currency(), [])

    def test_customer_options(self):
        self.test_individual_customer()
        # self.test_company_customer()

    def test_individual_customer(self):
        service = Service(BillRepo(Invoice), BillRepo(FiscalBill), CurrencyRepo(), ItemRepo(), CustomerRepo(Company),
                          CustomerRepo(Individual))
        individual = Individual("1971209075425")
        individual.set_id(1)
        individual.set_first_name("Petre")
        individual.set_last_name("Vasile")
        individual.set_phone_number("0745321784")
        individual.set_email_address("petre.vasileboss@yahoo.com")
        service.create_customer(individual)
        self.assertEqual(service.view_individual_customer(1), individual)
        individual.set_id(2)
        individual.set_last_name("Miron")
        individual.set_cnp("1900920076523")
        service.modify_customer(1, individual)
        self.assertEqual(service.view_individual_customer(2), individual)
        service.delete_customer(individual)
        self.assertEqual(service.view_individual_customer(1), None)

    def test_company_customer(self):
        service = Service(BillRepo(Invoice), BillRepo(FiscalBill), CurrencyRepo(), ItemRepo(), CustomerRepo(Company),
                          CustomerRepo(Individual))
        company = Company("La Geani", "RO0123", "523647")
        company.set_id(1)
        company.set_first_name("Petre")
        company.set_last_name("Vasile")
        company.set_phone_number("0745321784")
        company.set_email_address("petre.vasileboss@yahoo.com")
        service.create_customer(company)
        self.assertEqual(service.view_company_customer(1), company)
        company.set_id(2)
        company.set_last_name("Miron")
        service.modify_customer(1, company)
        self.assertEqual(service.view_company_customer(2), company)
        service.delete_customer(2)
        self.assertEqual(service.view_company_customer(1), None)
