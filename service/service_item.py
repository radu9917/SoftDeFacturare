from repository.item_repo import ItemRepo


class ItemService:
    def __init__(self):
        self.__item_repo = ItemRepo()

    def create_item(self, item):
        self.__item_repo.store(item)

    def delete_item(self, item_id):
        self.__item_repo.delete(item_id)

    def modify_item(self, old_item, new_item):
        self.__item_repo.update(self.__item_repo.get(old_item), new_item)

    def view_item(self):
        return self.__item_repo.get_all()

    def choose_item(self, item_id):
        return self.__item_repo.get(item_id)
