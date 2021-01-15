from repository.repo_interface import IRepo
import copy


class CurrencyRepo(IRepo):
    def __init__(self):
        self._list = []

    def store(self, currency):
        self._list.append(copy.deepcopy(currency))

    def delete(self, currency_id):
        for currency in self.get_all():
            if currency.get_id() == currency_id:
                self._list.remove(currency)

    def get_all(self):
        return self._list

    def get(self, currency_id):
        for currency in self.get_all():
            if currency.get_id() == currency_id:
                return currency

    def update(self, old_currency, new_currency):
        for currency in self.get_all():
            if currency.get_id() == old_currency.get_id():
                currency.set_id(new_currency.get_id())
                currency.set_code(new_currency.get_code())
                currency.set_name(new_currency.get_name())
                currency.set_symbol(new_currency.get_symbol())
