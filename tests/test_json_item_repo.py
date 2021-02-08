from repository.json_item_repo import JsonItemRepo
from domain.item import Item
from domain.currency import Currency
import unittest
import copy


class TestItemJson(unittest.TestCase):
    def test_json(self):
        item_repo = JsonItemRepo("json_test.json")
        currency = Currency("Leu", "Leu", "RON")
        item1 = Item()
        item1.set_name("Pear")
        item1.set_currency(currency)
        item1.set_price(3)
        item1.set_discount(0)
        item1.set_percent_discount(False)
        item1.set_description("A sweet fruit")
        item2 = copy.deepcopy(item1)
        item2.set_name("Apple")
        item1.set_price(2)
        item_repo.store(item1)
        item_repo.store(item2)
        item_repo2 = JsonItemRepo("json_test.json")
        item_list2 = item_repo2.get_all()
        item_list = item_repo.get_all()
        self.assertEqual(item_list, item_list2)
        item2.set_name("Green Apple")
        item_repo2.update(2, item2)
        self.assertEqual(item_repo2.get(2), item2)
        item_repo.reset_id()
        item_repo.delete(1)
        item_repo.delete(2)
