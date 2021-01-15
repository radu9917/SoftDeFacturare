from repository.repo_interface import IRepo
import copy


class ItemRepo(IRepo):
    def __init__(self):
        self._list = []

    def store(self, item):
        self._list.append(copy.deepcopy(item))

    def get(self, item_id):
        for item in self.get_all():
            if item.get_id() == item_id:
                return item

    def get_all(self):
        return copy.deepcopy(self._list)

    def delete(self, item_id):
        for item in self.get_all():
            if item.get_id() == item_id:
                self._list.remove(item)

    def update(self, old_item, new_item):
        for item in self._list:
            if item.get_id() == old_item.get_id():
                item.set_name(new_item.get_name())
                item.set_id(new_item.get_id())
                item.set_currency(new_item.get_currency())
                item.set_description(new_item.get_description())
                item.set_price(new_item.get_price())
                item.set_discount(new_item.get_discount())

