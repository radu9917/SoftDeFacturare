from repository.json_item_repo import JsonItemRepo
from domain.item import Item
from domain.currency import Currency
import unittest


class TestItemJson(unittest.TestCase):
    def test_json(self):
        item_repo = JsonItemRepo("test_json_item_repo.json")
        currency = Currency("Leu", "Leu", "RON")
        item = Item()
        item.set_name("Pear")
        item.set_currency(currency)
        item.set_price(3)
        item.set_discount(0)
        item.set_percent_discount(False)
        item.set_description("A sweet fruit")
        item2 = item
        item2.set_name("Apple")
