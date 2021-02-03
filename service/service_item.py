from repository.json_item_repo import JsonItemRepo
from validator.validator import Validator


class ItemService:
    def __init__(self):
        self.__item_repo = JsonItemRepo("database/item.json")
        self.__validator = Validator.get_instance()

    def create_item(self, item):
        self.__validator.validate_item(item)
        self.__item_repo.store(item)

    def delete_item(self, item_id):
        self.__item_repo.delete(item_id)

    def modify_item(self, old_item, new_item):
        self.__validator.find_id(str(old_item), self.__item_repo.get_all())
        self.__validator.validate_item(new_item)
        self.__item_repo.update(old_item, new_item)

    def view_all_item(self):
        return self.__item_repo.get_all()

    def choose_item(self, item_id):
        self.__validator.find_id(str(item_id), self.__item_repo.get_all())
        return self.__item_repo.get(int(item_id))
