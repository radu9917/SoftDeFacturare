import unittest
from domain.bill import Bill


class TestDomainBill(unittest.TestCase):
    def test_bill_getters_and_setters(self):
        bill = Bill()
        bill.set_currency("Dollar")
        bill.set_tax("10")
        bill.set_issuer("Dan SRL")
        bill.set_items(["Lopata"])
        bill.set_notes("asdf")
        bill.set_issue_date("14.01.2021")
        bill.set_due_date("17.01.2021")
        bill.set_customer("Ion")
        self.assertEqual(bill.get_currency(), "Dollar")
        self.assertEqual(bill.get_tax(), "10")
        self.assertEqual(bill.get_issuer(), "Dan SRL")
        self.assertEqual(bill.get_items(), ["Lopata"])
        self.assertEqual(bill.get_notes(), "asdf")
        self.assertEqual(bill.get_issue_date(), "14.01.2021")
        self.assertEqual(bill.get_due_date(), "17.01.2021")
        self.assertEqual(bill.get_customer(), "Ion")