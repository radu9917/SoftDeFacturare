import unittest
from repository.bill_repo import BillRepo
from domain.invoice import Invoice
from domain.customer import Customer
from domain.item import Item
from domain.currency import Currency


class TestBillRepo(unittest.TestCase):
    def test_bill_repo(self):
        invoice_repo = BillRepo(Invoice)

        invoice = Invoice()
        customer = Customer("Ion", "Radu", "ion.radu17@yahoo.com", "0758245170")
        item = Item()
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
        invoice.set_tax(2)
        invoice.set_issuer("Minimarket")
        invoice.set_id(1)
        invoice.set_issue_date("12.12.2020")
        invoice.set_due_date("16.12.2020")
        invoice.set_customer(customer)
        invoice_repo.store(invoice)
        self.assertEqual(invoice_repo.get(1), invoice)
        invoice.set_items([item, item])
        invoice.set_tax(4)
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
        try:
            invoice_repo.update(1, 1)
            self.assertFalse(True)
        except Exception as exp:
            self.assertFalse(False)
            try:
                invoice_repo.store(1)
                self.assertFalse(True)
            except Exception as exp:
                self.assertFalse(False)