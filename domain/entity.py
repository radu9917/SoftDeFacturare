class Entity:
    def __init__(self, index):
        self.__index = index

    def get_id(self):
        return self.__index

    def set_id(self, index):
        self.__index = index
