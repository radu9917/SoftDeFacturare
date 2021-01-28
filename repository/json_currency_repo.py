from domain.currency import Currency
from repository.currency_repo import CurrencyRepo
import json


class JsonCurrencyRepo(CurrencyRepo):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_from_file()

    def store(self, obj):
        super().store(obj)
        self.__store_to_file()

    def delete(self, obj_id):
        super().delete(obj_id)
        self.__store_to_file()

    def update(self, old_object, new_object):
        super().update(old_object, new_object)
        self.__store_to_file()

    def __store_to_file(self):
        currency_list = []
        current_currency_index = self._id
        for currency in self._list:
            currency_dict = {
                "id": currency.get_id(),
                "symbol": currency.get_symbol(),
                "name": currency.get_name(),
                "code": currency.get_code()
            }
            currency_list.append(currency_dict)
        json_list = {
            "current_currency_index": current_currency_index,
            "currency_list": currency_list
        }
        file = open(self.__file_name, "w")
        string = json.dumps(json_list, indent=4)
        file.write(string)
        file.close()

    def __load_from_file(self):
        file = open(self.__file_name, "r")
        json_file = json.loads(file.read())
        if "current_currency_index" in json_file:
            self._id = json_file["current_currency_index"]
        if "currency_list" in json_file:
            for currency in json_file["currency_list"]:
                symbol = currency["symbol"]
                name = currency["name"]
                code = currency["code"]
                currency_to_add = Currency(symbol, name, code)
                index = currency["id"]
                currency_to_add.set_id(index)
                self._list.append(currency_to_add)
        file.close()

    def reset_id(self):
        self._id = 1
