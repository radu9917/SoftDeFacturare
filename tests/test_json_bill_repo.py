from repository.json_bill_repo import JsonBillRepo
from domain.company import Company
from domain.individual import Individual
from domain.item import Item
from domain.currency import Currency
from domain.invoice import Invoice
from domain.fiscal_bill import FiscalBill
import unittest


class TestJsonBill(unittest.TestCase):
    def test_json_repo(self):
        invoice_repo = JsonBillRepo("json_test.json",Invoice)
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
        item = Item()
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
        invoice.set_items([(item, 1)])
        invoice.set_id(1)
        invoice.set_tax(item.get_price())
        invoice.set_issuer(company)
        invoice.set_issue_date("24.01.2021")
        invoice.set_due_date("10.02.2021")
        invoice.set_notes("Platiti la Banca Transilvania")
        invoice_repo.store(invoice)
        self.assertEqual(invoice, invoice_repo.get(1))
        invoice.add_items(item)
        invoice_repo.update(1,invoice)
        self.assertEqual(invoice_repo.get(1),invoice)
        invoice_repo.reset_id()
        invoice_repo.delete(1)
