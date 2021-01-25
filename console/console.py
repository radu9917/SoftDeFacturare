from service.service import Service
from repository.currency_repo import CurrencyRepo
from domain.individual import Individual
from domain.company import Company
from domain.currency import Currency
from domain.item import Item
from domain.fiscal_bill import FiscalBill
from domain.invoice import Invoice


class Console:
    def __init__(self):
        self.__service = Service(CurrencyRepo())

    # Customer options
    def customer_menu(self):
        print("Choose an option:\n1.Create customer\n2.Delete customer")
        print("3.Modify customer\n4.See customer list")
        options = {
            "1": self.create_customer,
            "2": self.delete_customer,
            "3": self.modify_customer,
            "4": self.view_customers
        }
        option = input()
        options[option]()

    def create_customer(self):
        number = int(input("How many customers do you want to create"))
        option = self.choose_customer_type()
        while number != 0:

            try:
                if isinstance(option, Individual):
                    self.__service.create_customer(self.create_individual())
                if isinstance(option, Company):
                    self.__service.create_customer(self.create_company())
            except Exception as exp:
                print(exp)

    def create_individual(self):
        individual = Individual()
        individual.set_cnp(input("Cnp: "))
        individual.set_first_name(input("First Name: "))
        individual.set_last_name(input("Last Name: "))
        individual.set_phone_number(input("Phone Number: "))
        individual.set_email_address(input("Email Address: "))
        return individual

    def create_company(self):
        company = Company()
        company.set_first_name(input("First Name: "))
        company.set_last_name(input("Last Name: "))
        company.set_phone_number(input("Phone Number: "))
        company.set_email_address(input("Email Address: "))
        company.set_company_name(input("Company Name: "))
        company.set_fiscal_no(input("Fiscal Number: "))
        company.set_registration_number(input("Registration Number: "))
        return company

    def delete_customer(self):
        index = int(input("What customer do you want to delete?"))
        customer = self.choose_customer_type()
        customer.set_id(index)
        self.__service.delete_customer(customer)

    def modify_customer(self):
        option = self.choose_customer_type()
        print("What customer do you want to change?")
        index = input("Give id: ")
        option.set_id(index)
        print("Create the customer you want to add")
        if isinstance(option, Individual):
            new_customer = self.create_individual()
        if isinstance(option, Company):
            new_customer = self.create_company()
        self.__service.modify_customer(option, new_customer)

    def choose_customer_type(self):
        option = input("What type of customer database do you want to access?\nIndividual or Company customers?\n")
        options = {
            "Individual": Individual,
            "Company": Company
        }
        return options[option]()

    def view_customers(self):
        option = self.choose_customer_type()
        if isinstance(option, Individual):
            for customer in self.__service.view_all_individual_customer():
                print(customer + "\n")
        if isinstance(option, Company):
            for customer in self.__service.view_all_company_customer():
                print(customer + "\n")


    # Item Options
    def item_menu(self):
        print("1.Create item\n2.Delete item\n3.Modify item\n4.See all items")
        options = {
            "1": self.create_item,
            "2": self.delete_item,
            "3": self.modify_item,
            "4": self.view_items
        }
        option = input("Choose an option:")
        options[option]()

    def create_item(self):
        item = self.input_item()
        self.__service.create_item(item)

    def input_item(self):
        item = Item()
        item.set_name(input("Give name: "))
        item.set_description(input("Give description"))
        item.set_price(input("Give price"))
        item.set_discount(input("Give discount"))
        item.set_currency(self.choose_currency())
        return item

    def delete_item(self):
        print("Choose item to delete:")
        option = int(input("Give id: "))
        self.__service.delete_item(option)

    def modify_item(self):
        old_item = int(input("Choose item to delete"))
        new_item = self.input_item()
        self.__service.modify_item(old_item, new_item)

    def view_items(self):
        for item in self.__service.view_items():
            print(item)

    # Currency Options
    def currency_menu(self):
        print("1. Create currency\n2.Delete currency\n3.Modify currency\n4.View all curency")
        option = input("Choose an option: ")
        options = {
            "1": self.create_currency,
            "2": self.delete_currency,
            "3": self.modify_currency,
            "4": self.view_all_currency
        }
        options[option]()

    def create_currency(self):
        self.__service.create_currency(self.input_currency())

    def input_currency(self):
        symbol = input("Give currency symbol")
        name = input("Give currency name")
        code = input("Give currency code")
        return Currency(symbol, name, code)

    def delete_currency(self):
        option = int(input("What currency do you wish to delete?\nGive id: "))
        self.__service.delete_currency(option)

    def modify_currency(self):
        old_currency = Currency("a", "a", "a")
        old_currency.set_id(input("Which currency do you wish to delete"))
        new_currency = self.input_currency()
        self.__service.modify_currency(old_currency, new_currency)

    def view_all_currency(self):
        for currency in self.__service.view_currency():
            print(currency + "\n")

    def choose_currency(self):
        print("Choose the desired currency from:")
        self.view_all_currency()
        return self.__service.get_currency(input("Give id: "))


    # Bill Options

    def bill_menu(self):
        print("1.Create bill\n2.Delete bill\n3.Modify bill")
        option = input("Choose option:")
        options = {
            "1": self.create_bill,
            "2": self.delete_bill,
            "3": self.modify_bill,
            # "4": self.print_bill
        }

    def choose_bill_type(self):
        option = input("What type of bill database do you want to access? \nInvoices or Fiscal Bills")
        options = {
            "Fiscal Bills": FiscalBill,
            "Invoice": Invoice
        }
        return options[option]()

    def create_bill(self):
        bill_type = self.choose_bill_type()
        bill = self.input_bill(bill_type)
        self.__service.create_bill(bill)

    def input_bill(self, bill):
        # bill.set_currency()
        # bill.set_customer()
        # bill.set_issuer()
        bill.set_issue_date(input("Give issue date: "))
        bill.set_due_date(input("Give due date: "))
        bill.set_notes(input("Notes:"))
        return bill

    def delete_bill(self):
        bill = self.choose_bill_type()
        bill.set_id(int(input("Which bill do you wish to delete")))
        self.__service.delete_bill(bill)

    def modify_bill(self):
        print("Create the new bill:")
        new_bill = self.input_bill(self.choose_bill_type())
        old_bill = input("What bill do you want to change?")
        self.__service.modify_bill(old_bill, new_bill)