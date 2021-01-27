from validator.exceptions import DataError
from validator.exceptions import IdError
from validator.exceptions import OptionError
from domain.individual import Individual
from domain.company import Company


class Validator:
    __instance = None
    @staticmethod
    def get_instance():
        if not Validator.__instance:
            Validator()
        return Validator.__instance

    def __init__(self):
        if Validator.__instance:
            raise Exception("Instance already created")
        Validator.__instance = self

    # DATA CHECKS
    def validate_customer(self, customer):
        if not customer.get_last_name().isalpha():
            raise DataError("Invalid First Name")
        if not customer.get_first_name().isalpha():
            raise DataError("Invalid Last Name")
        if len(customer.get_phone_number()) > 10:
            raise DataError("Phone number too long")
        if not customer.get_phone_number().isdecimal():
            raise DataError("Invalid Phone number")

    def validate_individual(self, individual):
        self.validate_customer(individual)
        cnp = individual.get_cnp()
        if len(cnp) > 13:
            raise DataError("CNP too long")
        if not cnp.isdecimal():
            raise DataError("Invalid CNP")

    def validate_company(self, company):
        self.validate_customer(company)
        if not company.get_company_name().replace(" ", "").isalnum():
            raise DataError("Invalid Name")
        if not company.get_registration_number().isalnum():
            raise DataError("Invalid Registration Number")
        if len(company.get_fiscal_no()) != 13:
            raise DataError("Fiscal number has inadequate length")
        if not company.get_fiscal_no().isdecimal():
            raise DataError("Invalid Fiscal Number")

    def validate_currency(self, currency):
        if len(currency.get_code()) != 3:
            raise DataError("Invalid code length")
        if not currency.get_code().isalpha():
            raise DataError("Invalid code")

    def validate_item(self, item):
        self.validate_currency(item.get_currency())
        if not item.get_name().isalnum():
            raise DataError("Invalid item name")
        if type(item.get_price()) != int:
            raise DataError("Invalid price")
        if type(item.get_discount()) != int:
            raise DataError("Invalid discount")

    def validate_date(self, date):
        if not date.replace(".", "").isdecimal():
            raise DataError("Invalid date")
        date_split = date.split(".")
        if int(date_split[0]) > 31:
            raise DataError("Invalid date day")
        if int(date_split[1]) > 12:
            raise DataError("Invalid date month")
        if int(date_split[2]) < 2000:
            raise DataError("Invalid date year")

    def validate_bill(self, bill):
        customer = bill.get_customer()
        if isinstance(customer, Individual):
            self.validate_individual(customer)
        if isinstance(customer, Company):
            self.validate_company(customer)
        self.validate_currency(bill.get_currency())
        for item in bill.get_items():
            self.validate_item(item[0])
        self.validate_company(bill.get_issuer())
        self.validate_date(bill.get_due_date())
        self.validate_date(bill.get_issue_date())
        if type(bill.get_tax()) != int:
            raise DataError("Invalid tax")

    # ID CHECK
    def find_id(self, index, obj_list):
        found = False
        if not str(index).isdecimal():
            raise IdError("Invalid Id")
        for ob in obj_list:
            if ob.get_id() == int(index):
                found = True
        if not found:
            raise IdError("Id does not exist")

    # OPTION CHECK
    def option_check(self, option, set_max):
        if not option.isdecimal():
            raise OptionError("Invalid option")
        if int(option) > set_max :
            raise OptionError("Option does not exist")
