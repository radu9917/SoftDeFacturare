from builder.bill_builder import BillBuilder
from domain.company import Company
from domain.individual import Individual
from domain.bill_item import BillItem
from domain.currency import Currency
from domain.fiscal_bill import FiscalBill
from domain.address import Address
import unittest


class TestBuilder(unittest.TestCase):
    def test_builder(self):
        builder = BillBuilder()
        with self.assertRaises(Exception):
            builder.build()
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
        builder.create_issuer(company.get_company_name(), company.get_last_name(),
                              company.get_first_name(), company.get_email_address(),
                              company.get_phone_number(), company.get_fiscal_no(), company.get_registration_number())
        builder.create_company_customer(company.get_company_name(), company.get_last_name(),
                              company.get_first_name(), company.get_email_address(),
                              company.get_phone_number(), company.get_fiscal_no(), company.get_registration_number())

        address = Address()
        address.set_address("Strada Academiei nr. 7")
        address.set_county("Bucuresti")
        address.set_country("Romania")
        address.set_postal_code("123456")


        individual = Individual()
        individual.set_cnp("1971209075425")
        individual.set_id(1)
        individual.set_first_name("Petre")
        individual.set_last_name("Vasile")
        individual.set_phone_number("0745321784")
        individual.set_email_address("petre.vasileboss@yahoo.com")
        builder.create_individual_customer(individual.get_cnp(), individual.get_last_name(),
                                           individual.get_first_name(),
                                           individual.get_email_address(), individual.get_phone_number())
        builder.create_customer_address(address.get_address(), address.get_county(),
                                        address.get_postal_code(), address.get_country())
        builder.create_issuer_address(address.get_address(), address.get_county(),
                                      address.get_postal_code(), address.get_country())
        builder.create_customer_address(address.get_address(), address.get_county(),
                                        address.get_postal_code(), address.get_country())
        currency = Currency("$", "Dollar", "USD")
        currency.set_exchange_rate(4.5)
        builder.create_bill_currency(currency.get_symbol(), currency.get_name(),
                                     currency.get_code(), currency.get_exchange_rate())
        bill_item = BillItem()
        bill_item.set_currency(currency)
        bill_item.set_name("McChicken")
        bill_item.set_description("Chicken hamburger")
        bill_item.set_price(3)
        bill_item.set_discount(0)
        bill_item.set_percent_discount(False)
        bill_item.set_description("Fast food")
        bill_item.calc_total()
        builder.add_item_to_list(bill_item.get_quantity(), bill_item.get_name(), bill_item.get_description(),
                                 bill_item.get_price(), bill_item.get_discount(), bill_item.get_percent_discount(),
                                 currency.get_name(), currency.get_code(), currency.get_symbol(),
                                 currency.get_exchange_rate())
        bill = FiscalBill()
        individual.set_address(address)
        company.set_address(address)
        bill.set_customer(individual)
        bill.set_currency(currency)
        bill.set_id(1)
        bill.set_issuer(company)
        bill.set_issue_date("24.01.2021")
        bill.set_due_date("10.02.2021")
        bill.set_notes("Platiti la Banca Transilvania")
        bill.add_items(bill_item)
        builder.create_bill(FiscalBill, bill.get_issue_date(), bill.get_due_date(),
                            bill.get_notes(), bill.get_id(), bill.get_total())
        self.assertEqual(bill, builder.build())
