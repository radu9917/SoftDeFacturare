from domain.entity import Entity
from domain.currency import Currency


class Item(Entity):
    def __init__(self):
        super().__init__(None)
        self.__name = None
        self.__description = None
        self.__price = None
        self.__discount = None
        self.__currency = None
        self.__quantity = 1

    # SETTERS
    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_currency(self, currency):
        if not isinstance(currency, Currency):
            raise Exception("Not currency")
        self.__currency = currency

    def set_discount(self, discount):
        int(discount)
        self.__discount = discount

    def set_price(self, price):
        int(price)
        self.__price = price

    # GETTERS
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_currency(self):
        return self.__currency

    def get_discount(self):
        return self.__discount

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def __eq__(self, other):
        if self.get_id() != other.get_id():
            return False
        if self.get_name() != other.get_name():
            return False
        if self.get_price() != other.get_price():
            return False
        if self.get_discount() != other.get_discount():
            return False
        if self.get_currency() != other.get_currency():
            return False
        if self.get_description() != other.get_description():
            return False
        return True

    def increase_quantity(self):
        self.__quantity += 1
