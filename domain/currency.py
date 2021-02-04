from domain.entity import Entity


class Currency(Entity):
    def __init__(self, symbol, name, code):
        super().__init__()
        self.__symbol = symbol
        self.__name = name
        self.__code = code
        self.__exchange_rate = 1

    # GETTERS
    def get_symbol(self):
        return self.__symbol

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def get_exchange_rate(self):
        return self.__exchange_rate

    # SETTERS
    def set_symbol(self, symbol):
        self.__symbol = symbol

    def set_code(self, code):
        self.__code = code

    def set_name(self, name):
        self.__name = name

    def set_exchange_rate(self, exchange_rate):
        self.__exchange_rate = exchange_rate

    def __eq__(self, other):
        if self.get_id() != other.get_id():
            return False
        if self.get_code() != other.get_code():
            return False
        if self.get_name() != other.get_name():
            return False
        if self.get_symbol() != other.get_symbol():
            return False
        if self.__exchange_rate != other.get_exchange_rate():
            return False
        return True

    def __str__(self):
        return str(self.get_id()) + ". " + self.__code
