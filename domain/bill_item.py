from domain.item import Item


class BillItem(Item):
    def __init__(self):
        super().__init__()
        self.__quantity = 1
        self.__total = 0

    def get_total(self):
        return self.__total

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_total(self, total):
        self.__total = total

    def calc_total(self):
        self.__total = self.__quantity * self.get_price()

    def increment_quantity(self):
        self.__quantity += 1

    def import_from_item(self, item):
        self.set_name(item.get_name())
        self.set_discount(item.get_discount())
        self.set_price(item.get_price())
        self.set_currency(item.get_currency())
        self.set_percent_discount(item.get_percent_discount())
        self.set_description((item.get_description()))
