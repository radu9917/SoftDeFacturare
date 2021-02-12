
# address1 , judet ,cod postal, tara

class Address:
    def __init__(self):
        self.__address = None
        self.__county = None
        self.__postal_code = None
        self.__country = None

    def get_address(self):
        return self.__address

    def get_county(self):
        return self.__county

    def get_country(self):
        return self.__country

    def get_postal_code(self):
        return self.__postal_code

    def set_address(self, address):
        self.__address = address

    def set_county(self, county):
        self.__county = county

    def set_country(self, country):
        self.__country = country

    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code

    def __str__(self):
        address_base = "{address}\n{county}, {postal_code}\n{country}\n"
        formated_address = address_base.format(
                address=self.__address,
                county=self.__county,
                country=self.__country,
                postal_code=self.__postal_code
        )
        return formated_address