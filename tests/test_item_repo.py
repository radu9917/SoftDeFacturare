import unittest
from repository.item_repo import ItemRepo
from domain.item import Item
from domain.currency import Currency


class TestItemRepo(unittest.TestCase):
    def test_item_repo(self):
        item1 = Item()
        currency = Currency("$", "Dollar", "USD")
        item1.set_id(1)
        item1.set_name("Apple")
        item1.set_discount(0)
        item1.set_price(2)
        item1.set_currency(currency)
        item1.set_description("A fruit")
        item_repo = ItemRepo()
        item_repo.store(item1)
        self.assertEqual(len(item_repo.get_all()), 1)
        item2 = Item()
        item2.set_id(2)
        item2.set_name("Pear")
        item2.set_currency(currency)
        item2.set_price(3)
        item2.set_discount(0)
        item2.set_description("A fruit")
        item_repo.update(item1, item2)
        self.assertEqual(item_repo.get(2), item2)
        item_repo.delete(2)
        self.assertEqual(item_repo.get_all(), [])
