from repository.repo_interface import IRepo
import copy


class ItemRepo(IRepo):
    def __init__(self):
        self._list = []
        self._id = 1

    def store(self, item):
        item.set_id(self._id)
        self._id += 1
        self._list.append(copy.deepcopy(item))
        return item

    def get(self, item_id):
        for item in self.get_all():
            if item.get_id() == item_id:
                return item
        return None

    def get_all(self):
        return copy.deepcopy(self._list)

    def delete(self, item_to_delete):
        for item in self.get_all():
            if item.get_id() == item_to_delete:
                self._list.remove(item)
                return item

    def update(self, old_item, new_item):
        for item in self._list:
            if item.get_id() == old_item:
                old = self._id - 1
                self._id = old_item
                self.delete(old_item)
                self.store(new_item)
                self._id = old
                return item
