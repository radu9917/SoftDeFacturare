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
        return None

    def get_all(self):
        return copy.deepcopy(self._list)

    def delete(self, item_to_delete):
        for item in self.get_all():
            if item.get_id() == item_to_delete.get_id():
                self._list.remove(item)
                return item

    def update(self, old_item, new_item):
        for item in self._list:
            if item.get_id() == old_item.get_id():
                self.delete(old_item)
                self.store(new_item)
                return old_item
