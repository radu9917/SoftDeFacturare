from repository.item_repo import ItemRepo
from domain.item import Item
from domain.currency import Currency
import json


class JsonItemRepo(ItemRepo):
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
        item_list = []
        for item in self._list:
            item_id = item.get_id()
            item_name = item.get_name()
            description = item.get_description()
            discount = item.get_discount()
            price = item.get_price()
            currency = item.get_currency()
            currency_dict = {
                "symbol": currency.get_symbol(),
                "name": currency.get_name(),
                "code": currency.get_code()
            }
            item_dict = {
                "id": item_id,
                "name": item_name,
                "description": description,
                "discount": discount,
                "price": price,
                "currency": currency_dict
            }
            item_list.append(item_dict)
        file = open(self.__file_name, "w")
        string = json.dumps(item_list, indent=4)
        file.write(string)
        file.close()

    def __load_from_file(self):
        file = open(self.__file_name, "r")
        json_file = json.loads(file.read())
        if "id" in json_file:
            self._id = json_file["id"]
        if "item" in json_file:
            for item in json_file["item_list"]:
                symbol = item["currency"]["symbol"]
                name = item["currency"]["name"]
                code = item["currency"]["code"]
                currency = Currency(symbol, name, code)
                item_to_store = Item()
                item.set_name(item["name"])
                item.set_price(item["price"])
                item.set_discount(item["discount"])
                item.set_description(item["description"])
                item.set_currency(currency)
                self._list.append(item_to_store)
        file.close()
