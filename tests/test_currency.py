import unittest
from domain.currency import Currency


class TestCurrencyDomain(unittest.TestCase):
    def test_currency_getters(self):
        dollar = Currency("$", "Dollar", "USD")
        self.assertEqual(dollar.get_code(), "USD")
        self.assertEqual(dollar.get_symbol(), "$")
        self.assertEqual(dollar.get_name(), "Dollar")

    def test_currency_setters(self):
        currency = Currency("A", "S", "D")
        currency.set_code("USD")
        currency.set_symbol("$")
        currency.set_name("Dollar")
        self.assertEqual(currency.get_code(), "USD")
        self.assertEqual(currency.get_symbol(), "$")
        self.assertEqual(currency.get_name(), "Dollar")
