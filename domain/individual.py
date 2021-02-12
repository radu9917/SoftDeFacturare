from domain.customer import Customer


class Individual(Customer):
    def __init__(self):
        super().__init__(None, None, None, None, None)
        self.__cnp = None

    def get_cnp(self):
        return self.__cnp

    def set_cnp(self, cnp):
        self.__cnp = cnp

    def __eq__(self, other):
        super().__eq__(other)
        if self.get_cnp() != other.get_cnp():
            return False
        return True

    def __str__(self):
        individual_base = "Individual {first_name} {last_name}"
        formated_individual = individual_base.format(first_name=self.get_first_name(),last_name=self.get_last_name())
        return formated_individual
