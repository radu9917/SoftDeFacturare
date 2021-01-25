from domain.customer import Customer


class Individual(Customer):
    def __init__(self):
        super().__init__(None, None, None, None)
        self.__cnp = None

    def get_cnp(self):
        return self.__cnp

    def set_cnp(self, cnp):
        self.__cnp = cnp

    def __eq__(self, other):
        if self.get_last_name() != other.get_last_name():
            return False
        if self.get_first_name() != other.get_first_name():
            return False
        if self.get_phone_number() != other.get_phone_number():
            return False
        if self.get_email_address() != other.get_email_address():
            return False
        if self.get_cnp() != other.get_cnp():
            return False
        return True

    def __str__(self):
        return "Individual " + self.get_first_name() + " " + self.get_last_name()
