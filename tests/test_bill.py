import unittest
from domain.bill import Bill
from domain.item import Item


class TestDomainBill(unittest.TestCase):
    def test_bill_getters_and_setters(self):
        bill = Bill()
        item = Item()
        item.set_name("Apple")
        item.set_id(1)
        item.set_price(2)
        bill.set_currency("Dollar")
        bill.set_tax(10)
        bill.set_issuer("Dan SRL")

        bill.set_items([(item, 1)])
        bill.set_notes("asdf")
        bill.set_issue_date("14.01.2021")
        bill.set_due_date("17.01.2021")
        bill.set_customer("Ion")
        self.assertEqual(bill.get_currency(), "Dollar")
        self.assertEqual(bill.get_tax(), 10)
        self.assertEqual(bill.get_issuer(), "Dan SRL")
        self.assertEqual(bill.get_items(), [(item, 1)])
        self.assertEqual(bill.get_notes(), "asdf")
        self.assertEqual(bill.get_issue_date(), "14.01.2021")
        self.assertEqual(bill.get_due_date(), "17.01.2021")
        self.assertEqual(bill.get_customer(), "Ion")
        bill.add_items(item)
        self.assertEqual(bill.get_items()[0][1], 2)
