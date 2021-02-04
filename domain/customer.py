from domain.entity import Entity


class Customer(Entity):
    def __init__(self, first_name, last_name, email_address, phone_number):
        super().__init__()
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email_address = email_address
        self.__phone_number = phone_number
    # GETTERS

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email_address(self):
        return self.__email_address

    def get_phone_number(self):
        return self.__phone_number

    # SETTERS
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def __eq__(self, other):
        if self.__last_name != other.get_last_name():
            return False
        if self.__first_name != other.get_first_name():
            return False
        if self.__phone_number != other.get_phone_number():
            return False
        if self.__email_address != other.get_email_address():
            return False
        if self.get_id() != other.get_id():
            return False
        return True
