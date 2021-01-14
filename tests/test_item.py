import unittest
from domain.item import Item
from domain.currency import Currency


class TestItemDomain(unittest.TestCase):
    def test_item_getters_and_setters(self):
        item = Item()
        currency = Currency("$", "Dollar", "USD")
        item.set_name("Apple")
        item.set_price(1)
        item.set_discount(0)
        item.set_currency(currency)
        item.set_description("A round fruit")
        self.assertEqual(item.get_name(), "Apple")
        self.assertEqual(item.get_price(), 1)
        self.assertEqual(item.get_discount(), 0)
        self.assertEqual(item.get_currency(), currency)
        self.assertEqual(item.get_description(), "A round fruit")
