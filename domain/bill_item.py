from domain.item import Item


class BillItem(Item):
    def __init__(self):
        super().__init__()
        self.__quantity = 1

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def increment_quantity(self):
        self.__quantity += 1

    def import_from_item(self, item):
        self.set_name(item.get_name())
        self.set_discount(item.get_discount())
        self.set_price(item.get_price())
        self.set_currency(item.get_currency())
        self.set_percent_discount(item.get_percent_discount())
        self.set_description((item.get_description()))
