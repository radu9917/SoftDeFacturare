from abc import ABC, abstractmethod


class IRepo(ABC):
    @abstractmethod
    def store(self, obj):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def update(self, old_obj, new_obj):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass
