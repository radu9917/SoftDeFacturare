from repository.repo_interface import IRepo
import copy


class CurrencyRepo(IRepo):
    def __init__(self):
        self._list = []
        self._id = 1

    def store(self, currency):
        currency_copy = copy.deepcopy(currency)
        currency_copy.set_id(self._id)
        self._id += 1
        self._list.append(currency_copy)
        return currency_copy

    def delete(self, currency_to_delete):
        for currency in self.get_all():
            if currency.get_id() == currency_to_delete:
                self._list.remove(currency)
                return currency
        return None

    def get_all(self):
        return copy.deepcopy(self._list)

    def get(self, currency_id):
        for currency in self.get_all():
            if currency.get_id() == currency_id:
                return currency
        return None

    def update(self, old_currency, new_currency):
        deleted_currency = self.get(old_currency)
        deleted_curr = self.delete(old_currency)

        if deleted_curr is not None:
            old = self._id
            self._id = old_currency
            self.store(new_currency)
            self._id = old
            return deleted_currency
