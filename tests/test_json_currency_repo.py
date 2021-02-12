from domain.currency import Currency
from repository.json_currency_repo import JsonCurrencyRepo
import unittest


class TestJsonCurrency(unittest.TestCase):
    def test_json(self):
        currency_repo = JsonCurrencyRepo("json_test.json")
        currency1 = Currency("$", "DOLLAR", "USD")
        currency2 = Currency("LEU", "Leu", "RON")
        currency_repo.store(currency1)
        currency_repo.store(currency2)
        currency_repo2 = JsonCurrencyRepo("json_test.json")
        currency_list1 = currency_repo.get_all()
        currency_list2 = currency_repo2.get_all()
        self.assertEqual(currency_list1, currency_list2)
        currency2.set_name("Leu romanesc")
        print(currency_repo.get(2))
        currency_repo.update(2, currency2)
        currency2.set_id(2)
        print(currency_repo.get(2))
        self.assertEqual(currency_repo.get(2), currency2)
        currency_repo2.reset_id()
        currency_repo2.delete(1)
        currency_repo2.delete(2)
