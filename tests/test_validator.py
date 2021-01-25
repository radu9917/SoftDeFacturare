from validator.validator import Validator
from domain.individual import Individual
from domain.item import Item
from domain.currency import Currency
from domain.company import Company
from domain.bill import Bill
import unittest


class TestValidator(unittest.TestCase):
    def test_validator(self):
        validator = Validator.get_instance()
        customer = Individual("198121203415")
        customer.set_last_name("Dan")
        customer.set_first_name("Popescu")
        customer.set_phone_number("0756234876")
        customer.set_email_address("popescu.dan12@gmail.com")
        item = Item()
        currency = Currency("$", "dollar", "USD")
        item.set_name("Apple")
        item.set_price(2)
        item.set_discount(0)
        item.set_currency(currency)
        company = Company("La Geani", "RO0123", "523647")
        company.set_email_address("la_geani@gmail.com")
        company.set_first_name("Ion")
        company.set_last_name("Bogdan")
        company.set_phone_number("0752314567")
        company.set_fiscal_no("0000012345678")
        company.set_registration_number("RO01923")
        bill = Bill()
        bill.set_currency(currency)
        bill.set_customer(customer)
        bill.set_issuer(company)
        bill.set_issue_date("21.12.2020")
        bill.set_due_date("21.02.2021")
        bill.add_items(item)

        validator.validate_bill(bill)

