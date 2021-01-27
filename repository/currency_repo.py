from repository.repo_interface import IRepo
import copy


class CurrencyRepo(IRepo):
    def __init__(self):
        self._list = []
        self._id = 1

    def store(self, currency):
        currency.set_id(self._id)
        self._id += 1
        self._list.append(copy.deepcopy(currency))
        return currency

    def delete(self, currency_to_delete):
        for currency in self.get_all():
            if currency.get_id() == currency_to_delete:
                self._list.remove(currency)
                return currency

    def get_all(self):
        return copy.deepcopy(self._list)

    def get(self, currency_id):
        for currency in self.get_all():
            if currency.get_id() == currency_id:
                return currency
        return None

    def update(self, old_currency, new_currency):
        for currency in self._list:
            if currency.get_id() == old_currency:
                self.delete(old_currency)
                old = self._id
                self._id = old_currency
                self.store(new_currency)
                self._id = old
                return old_currency
