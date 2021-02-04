class Entity:
    def __init__(self):
        self.__index = 1

    def get_id(self):
        return self.__index

    def set_id(self, index):
        self.__index = index
