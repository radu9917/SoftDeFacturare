import unittest
from repository.currency_repo import CurrencyRepo
from domain.currency import Currency


class TestCurrencyRepo(unittest.TestCase):
    def test_currency_repo(self):
        currency_repo = CurrencyRepo()
        currency = Currency("$", "Dollar", "USD")
        currency.set_id(1)
        currency_repo.store(currency)
        self.assertEqual(len(currency_repo.get_all()), 1)
        self.assertEqual(currency_repo.get(1), currency)
        currency2 = Currency("LEU", "Leu", "RON")
        currency2.set_id(2)
        currency_repo.update(currency, currency2)
        self.assertEqual(currency_repo.get(2), currency2)
        currency_repo.delete(2)
        self.assertEqual(currency_repo.get_all(), [])
