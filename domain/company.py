from domain.customer import Customer


class Company(Customer):
    def __init__(self, company_name, registration_no, fiscal_code):
        super().__init__(None, None, None, None)
        self.__company_name = company_name
        self.__registration_no = registration_no
        self.__fiscal_code = fiscal_code

    # GETTERS
    def get_company_name(self):
        return self.__company_name

    def get_registration_number(self):
        return self.__registration_no

    def get_fiscal_no(self):
        return self.__fiscal_code

    # SETTERS
    def set_company_name(self, name):
        self.__company_name = name

    def set_registration_number(self, registration_number):
        self.__registration_no = registration_number

    def set_fiscal_no(self, fiscal_number):
        self.__fiscal_code = fiscal_number
