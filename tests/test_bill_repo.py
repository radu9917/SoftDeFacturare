import unittest
from repository.bill_repo import BillRepo
from domain.invoice import Invoice
from domain.customer import Customer
from domain.bill_item import BillItem
from domain.currency import Currency
from domain.company import Company
from domain.address import Address

class TestBillRepo(unittest.TestCase):
    def test_bill_repo(self):
        invoice_repo = BillRepo(Invoice)

        invoice = Invoice()
        address = Address()
        address.set_address("Strada Academiei nr. 7")
        address.set_county("Bucuresti")
        address.set_country("Romania")
        address.set_postal_code("010011")
        customer = Customer("Ion", "Radu", "ion.radu17@yahoo.com", "0758245170", address)
        company = Company()
        company.set_address(address)
        company.set_first_name("Plesoiu")
        company.set_last_name("Alexandru")
        company.set_fiscal_no("RO0123")
        company.set_registration_number("123456")
        company.set_company_name("Pleso Academy")
        company.set_fiscal_no("RO2345")
        company.set_registration_number("0000123456789")
        item = BillItem()
        currency = Currency("LEU", "Leu", "RON")
        item.set_name("Water")
        item.set_currency(currency)
        item.set_price(2)
        item.set_discount(0)
        item.set_description("Drinkabale liquid")
        item.set_id(1)
        customer.set_id(1)
        invoice.set_currency(currency)
        invoice.set_items([item])
        invoice.set_total(2)
        invoice.set_issuer(company)
        invoice.set_id(1)
        invoice.set_issue_date("12.12.2020")
        invoice.set_due_date("16.12.2020")
        invoice.set_customer(customer)
        invoice_repo.store(invoice)
        self.assertEqual(invoice_repo.get(1), invoice)
        item.set_quantity(2)
        invoice.set_items([item])
        invoice.set_total(4)
        invoice_repo.update(1, invoice)
        self.assertEqual(invoice_repo.get(1), invoice)
        invoice_repo.delete(1)
        self.assertEqual(invoice_repo.get_all(), [])
        self.assertEqual(invoice_repo.get(69), None)
        try:
            repo = BillRepo("asdas")
            self.assertFalse(True)
        except Exception as exp:
            self.assertFalse(False)

        with self.assertRaises(TypeError):
            invoice_repo.update(1, 1)

        with self.assertRaises(TypeError):
            invoice_repo.store(1)
