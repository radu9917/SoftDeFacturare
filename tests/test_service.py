from domain.invoice import Invoice
from service.service_item import ItemService
from service.service_customer import CustomerService
from repository.customer_repo import CustomerRepo
from repository.item_repo import ItemRepo
from domain.company import Company
from domain.individual import Individual
from domain.item import Item
from domain.bill_item import BillItem
from repository.bill_repo import BillRepo
from service.service_bill import BillService
from domain.currency import Currency
from domain.fiscal_bill import FiscalBill
from service.service_currency import CurrencyService
from repository.currency_repo import CurrencyRepo
import unittest


class TestService(unittest.TestCase):
    def test_item_service(self):
        service = ItemService(ItemRepo())
        item = Item()
        currency = Currency("$", "Dollar", "USD")
        item.set_id(1)
        item.set_currency(currency)
        item.set_name("McChicken")
        item.set_description("Chicken hamburger")
        item.set_price(2)
        item.set_discount(0)
        service.create_item(item)
        self.assertEqual(item, service.choose_item(1))
        item.set_price(3)
        item.set_id(2)
        service.modify_item(1, item)
        self.assertEqual(item, service.choose_item(1))
        service.delete_item(1)
        self.assertEqual(service.view_all_item(), [])

    def test_currency_options(self):
        service = CurrencyService(CurrencyRepo())
        currency = Currency("$", "Dollar", "USD")
        currency.set_id(1)
        service.create_currency(currency)
        self.assertEqual(service.view_currency(), [currency])
        currency.set_name("US Dollar")
        service.modify_currency(1, currency)
        self.assertEqual(service.view_currency(), [currency])
        service.delete_currency(1)
        self.assertEqual(service.view_currency(), [])

    def test_customer_options(self):
        self.test_individual_customer()
        self.test_company_customer()

    def test_individual_customer(self):
        service = CustomerService(CustomerRepo(Individual), CustomerRepo(Company))
        individual = Individual()
        individual.set_id(1)
        individual.set_cnp("190702123433")
        individual.set_first_name("Petre")
        individual.set_last_name("Vasile")
        individual.set_phone_number("0745321784")
        individual.set_email_address("petre.vasileboss@yahoo.com")
        service.create_customer(individual)
        self.assertEqual(service.choose_individual_customer(1), individual)
        individual.set_last_name("Miron")
        individual.set_cnp("191215678876")
        service.update_customer(1, individual)
        self.assertEqual(service.choose_individual_customer(1), individual)
        service.delete_customer(individual)
        self.assertEqual(service.view_all_individual(), [])

    def test_company_customer(self):
        service = CustomerService(CustomerRepo(Individual), CustomerRepo(Company))
        company = Company()
        company.set_company_name("La Geani")
        company.set_registration_number("RO0123")
        company.set_fiscal_no("0000231523647")
        company.set_first_name("Petre")
        company.set_last_name("Vasile")
        company.set_phone_number("0745321784")
        company.set_email_address("petre.vasileboss@yahoo.com")
        service.create_customer(company)
        self.assertEqual(service.choose_company_customer(1), company)
        company.set_id(2)
        company.set_last_name("Miron")
        service.update_customer(1, company)
        self.assertEqual(service.choose_company_customer(1), company)
        service.delete_customer(company)
        self.assertEqual(service.view_all_company(), [])

    def test_invoice_bill(self):
        service = BillService(BillRepo(Invoice), BillRepo(FiscalBill))
        company = Company()
        company.set_company_name("La Geani")
        company.set_registration_number("RO0123")
        company.set_fiscal_no("0000231523647")
        company.set_email_address("la_geani@gmail.com")
        company.set_first_name("Ion")
        company.set_last_name("Bogdan")
        company.set_phone_number("0752314567")
        company.set_fiscal_no("0000012345678")
        company.set_registration_number("RO01923")
        individual = Individual()
        individual.set_cnp("1971209075425")
        individual.set_id(1)
        individual.set_first_name("Petre")
        individual.set_last_name("Vasile")
        individual.set_phone_number("0745321784")
        individual.set_email_address("petre.vasileboss@yahoo.com")
        item = BillItem()
        currency = Currency("$", "Dollar", "USD")
        item.set_id(1)
        item.set_currency(currency)
        item.set_name("McChicken")
        item.set_description("Chicken hamburger")
        item.set_price(2)
        item.set_discount(0)
        invoice = Invoice()
        invoice.set_customer(individual)
        invoice.set_currency(currency)
        invoice.set_items([item])
        invoice.set_id(1)
        invoice.set_issuer(company)
        invoice.set_issue_date("24.01.2021")
        invoice.set_due_date("10.02.2021")
        invoice.set_notes("Platiti la Banca Transilvania")
        service.create_bill(invoice)
        invoice.add_items(item)
        service.update_bill(1, invoice)
        self.assertEqual(service.choose_invoice(1), invoice)
        service.delete_bill(1)
