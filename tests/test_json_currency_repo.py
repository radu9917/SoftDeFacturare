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
        for currency in currency_list1:
            if currency in currency_list2:
                assert True
            else:
                assert False
        currency2.set_name("Leu romanesc")
        currency_repo.update(2, currency2)
        self.assertEqual(currency_repo.get(2), currency2)
        currency_repo2.reset_id()
        currency_repo2.delete(1)
        currency_repo2.delete(2)
