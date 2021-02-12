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
        stored_object = super().store(obj)
        self.__store_to_file()
        return stored_object

    def delete(self, obj_id):
        deleted_object = super().delete(obj_id)
        self.__store_to_file()
        return deleted_object

    def update(self, old_object, new_object):
        updated_object = super().update(old_object, new_object)
        self.__store_to_file()
        return updated_object

    def __store_to_file(self):
        item_list = []
        for item in self._list:
            item_id = item.get_id()
            item_name = item.get_name()
            description = item.get_description()
            discount = item.get_discount()
            price = item.get_price()
            currency = item.get_currency()
            percent_discount = item.get_percent_discount()
            currency_dict = {
                "symbol": currency.get_symbol(),
                "name": currency.get_name(),
                "code": currency.get_code(),
                "exchange_rate": currency.get_exchange_rate()
            }
            item_dict = {
                "id": item_id,
                "name": item_name,
                "description": description,
                "discount": discount,
                "price": price,
                "currency": currency_dict,
                "percent_discount": percent_discount
            }
            item_list.append(item_dict)
        json_list = {
            "current_item_index": self._id,
            "item_list": item_list
            }
        file = open(self.__file_name, "w")
        string = json.dumps(json_list, indent=4)
        file.write(string)
        file.close()

    def __load_from_file(self):
        file = open(self.__file_name, "r")
        json_file = json.loads(file.read())
        if "current_item_index" in json_file:
            self._id = json_file["current_item_index"]
        if "item_list" in json_file:
            for item in json_file["item_list"]:
                symbol = item["currency"]["symbol"]
                name = item["currency"]["name"]
                code = item["currency"]["code"]
                currency = Currency(symbol, name, code)
                exchange_rate = item["currency"]["exchange_rate"]
                currency.set_exchange_rate(exchange_rate)
                item_to_store = Item()
                item_to_store.set_id(item["id"])
                item_to_store.set_name(item["name"])
                item_to_store.set_price(item["price"])
                item_to_store.set_discount(item["discount"])
                item_to_store.set_description(item["description"])
                item_to_store.set_percent_discount(item["percent_discount"])
                item_to_store.set_currency(currency)
                self._list.append(item_to_store)
        file.close()

    def reset_id(self):
        self._id = 1
