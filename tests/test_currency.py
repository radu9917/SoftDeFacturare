import unittest
from domain.currency import Currency
import copy


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

    def test_equal(self):
        currency = Currency("$", "Dollar", "USD")
        currency.set_id(1)
        currency.set_exchange_rate(4.5)
        currency2 = copy.deepcopy(currency)
        currency2.set_id(2)
        self.assertNotEqual(currency, currency2)
        currency2.set_id(1)
        currency2.set_name("leu")
        self.assertNotEqual(currency, currency2)
        currency2.set_name(currency.get_name())
        currency2.set_code("RON")
        self.assertNotEqual(currency, currency2)
        currency2.set_code(currency.get_code())
        currency2.set_symbol("RON")
        self.assertNotEqual(currency, currency2)
        currency2.set_symbol(currency.get_symbol())
        currency2.set_exchange_rate(1)
        self.assertNotEqual(currency, currency2)
