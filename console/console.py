from service.service import Service
from repository.currency_repo import CurrencyRepo
from domain.individual import Individual
from domain.company import Company
from domain.currency import Currency
from domain.item import Item
from domain.fiscal_bill import FiscalBill
from domain.invoice import Invoice
from validator.validator import Validator
from validator.exceptions import OptionError


class Console:
    def __init__(self):
        self.__service = Service()
        self.__validator = Validator.get_instance()

    # Customer options
    def customer_menu(self):
        print("Choose an option:\n1.Create customer\n2.Delete customer")
        print("3.Modify customer\n4.See customer list")
        try:
            options = {
                "1": self.create_customer,
                "2": self.delete_customer,
                "3": self.modify_customer,
                "4": self.view_customers
            }
            option = input()
            self.__validator.option_check(option, 4)
            options[option]()
        except OptionError as exp:
            print(exp)

    def create_customer(self):
        number = int(input("How many customers do you want to create"))
        option = self.choose_customer_type()
        while number != 0:

            try:
                if isinstance(option, Individual):
                    self.__service.create_customer(self.create_individual())
                if isinstance(option, Company):
                    self.__service.create_customer(self.create_company())
                number -= 1
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
        try:
            index = int(input("What customer do you want to delete?"))
            customer = self.choose_customer_type()
            customer.set_id(index)
            self.__service.delete_customer(customer)
        except Exception as exp:
            print(exp)

    def modify_customer(self):
        new_customer = None
        try:
            option = self.choose_customer_type()
            print("What customer do you want to change?")
            index = int(input("Give id: "))
            option.set_id(index)
            print("Create the customer you want to add")
            if isinstance(option, Individual):
                new_customer = self.create_individual()
            if isinstance(option, Company):
                new_customer = self.create_company()
            self.__service.modify_customer(option.get_id(), new_customer)
        except Exception as exp:
            print(exp)

    def choose_customer_type(self):
        option = input("What type of customer database do you want to access?\n1-Individual or 2-Company customers?\n")
        options = {
            "1": Individual,
            "2": Company
        }
        return options[option]()

    def view_customers(self):
        option = self.choose_customer_type()
        if isinstance(option, Individual):
            for customer in self.__service.view_all_individual_customer():
                print(customer)
        if isinstance(option, Company):
            for customer in self.__service.view_all_company_customer():
                print(customer)

    def choose_customer(self, customer_type):
        if isinstance(customer_type, Individual):
            print("What individual do you want to pick?")
            return self.__service.get_individual_customer(int(input("Give id: ")))
        if isinstance(customer_type, Company):
            print("What company do you want to pick?")
            return self.__service.get_company_customer(int(input("Give id: ")))

    # Item Options
    def item_menu(self):
        print("1.Create item\n2.Delete item\n3.Modify item\n4.See all items")
        try:
            options = {
                "1": self.create_item,
                "2": self.delete_item,
                "3": self.modify_item,
                "4": self.view_items
            }
            option = input("Choose an option:")
            self.__validator.option_check(option, 4)
            options[option]()
        except OptionError as exp:
            print(exp)

    def create_item(self):
        try:
            item = self.input_item()
            self.__service.create_item(item)
        except Exception as exp:
            print(exp)

    def input_item(self):
        item = Item()
        item.set_name(input("Give name: "))
        item.set_description(input("Give description: "))
        item.set_price(int(input("Give price: ")))
        item.set_discount(int(input("Give discount: ")))
        print("Is the discount a percent?\nYes of No")
        percent = input()
        if percent == "Yes":
            item.set_percent_discount(True)
        else:
            item.set_percent_discount(False)
        item.set_currency(self.choose_currency())
        return item

    def delete_item(self):
        try:
            print("Choose item to delete:")
            option = int(input("Give id: "))
            self.__service.delete_item(option)
        except Exception as exp:
            print(exp)

    def modify_item(self):
        try:
            old_item = int(input("Choose item to delete"))
            new_item = self.input_item()
            self.__service.modify_item(old_item, new_item)
        except OptionError as exp:
            print(exp)

    def view_items(self):
        for item in self.__service.view_items():
            print(item)

    def choose_item(self):
        self.view_items()
        option = input("Choose desired item")
        return option

    # Currency Options
    def currency_menu(self):
        print("1. Create currency\n2.Delete currency\n3.Modify currency\n4.View all curency")
        option = input("Choose an option: ")
        try:
            self.__validator.option_check(option, 4)
            options = {
                "1": self.create_currency,
                "2": self.delete_currency,
                "3": self.modify_currency,
                "4": self.view_all_currency
            }
            options[option]()
        except OptionError as exp:
            print(exp)

    def create_currency(self):
        try:
            self.__service.create_currency(self.input_currency())
        except Exception as exp:
            print(exp)

    def input_currency(self):
        symbol = input("Give currency symbol: ")
        name = input("Give currency name: ")
        code = input("Give currency code: ")
        exchange_rate = float(input("Give exchange rate from created currency to RON"))
        currency = Currency(symbol, name, code)
        currency.set_exchange_rate(exchange_rate)
        return currency

    def delete_currency(self):
        try:
            option = int(input("What currency do you wish to delete?\nGive id: "))
            self.__service.delete_currency(option)
        except Exception as exp:
            print(exp)

    def modify_currency(self):
        try:
            old_currency = input("Which currency do you wish to change")
            new_currency = self.input_currency()
            self.__service.modify_currency(old_currency, new_currency)
        except Exception as exp:
            print(exp)

    def view_all_currency(self):
        for currency in self.__service.view_currency():
            print(currency)

    def choose_currency(self):
        print("Choose the desired currency from:")
        self.view_all_currency()
        return self.__service.get_currency(int(input("Give id: ")))

    # Bill Options

    def bill_menu(self):
        print("1.Create bill\n2.Delete bill\n3.Modify bill")
        print("4.Print bill\n5.Add item to bill\n6.Create a invoice as a fiscal bill")
        option = input("Choose option:")
        try:
            self.__validator.option_check(option, 6)
            options = {
                "1": self.create_bill,
                "2": self.delete_bill,
                "3": self.modify_bill,
                "4": self.print_bill,
                "5": self.add_items_to_bill,
                "6": self.invoice_to_fiscal,
            }
            options[option]()
        except OptionError as exp:
            print(exp)

    def print_bill(self):
        bill = self.choose_bill_type()
        if bill == Invoice:
            print(self.__service.print_invoice(input("Give id: ")))
        if bill == FiscalBill:
            print(self.__service.print_fiscal_bill(input("Give id: ")))

    def choose_bill_type(self):
        correct = False
        option = None
        options = {
            "2": FiscalBill,
            "1": Invoice
                }
        while not correct:
            try:
                option = input("What type of bill database do you want to access? \n1-Invoices or 2-Fiscal Bills")
                self.__validator.option_check(option, 2)
                correct = True
            except Exception as exp:
                print(exp)
        return options[option]

    def create_bill(self):
        try:
            bill_type = self.choose_bill_type()
            bill = self.input_bill(bill_type)
            self.__service.create_bill(bill)
        except Exception as exp:
            print(exp)

    def input_bill(self, bill_type):
        bill = None
        if bill_type == FiscalBill:
            bill = FiscalBill()
        if bill_type == Invoice:
            bill = Invoice()

        bill.set_customer(self.choose_customer(self.choose_customer_type()))
        company = Company()
        bill.set_issuer(self.choose_customer(company))
        bill.set_currency(self.choose_currency())
        bill.set_issue_date(input("Give issue date: "))
        bill.set_due_date(input("Give due date: "))
        bill.set_notes(input("Notes:"))
        return bill

    def delete_bill(self):
        try:
            bill = None
            bill_type = self.choose_bill_type()
            if bill_type == FiscalBill:
                bill = FiscalBill()
            if bill_type == Invoice:
                bill = Invoice()
            bill_id = int(input("Which bill do you wish to delete"))
            bill.set_id(bill_id)
            self.__service.delete_bill(bill)
        except Exception as exp:
            print(exp)

    def modify_bill(self):
        try:
            print("Create the new bill:")
            new_bill = self.input_bill(self.choose_bill_type())
            old_bill = int(input("What bill do you want to change?"))
            self.__service.modify_bill(old_bill, new_bill)
        except Exception as exp:
            print(exp)

    def add_items_to_bill(self):
        bill = None
        bill_type = self.choose_bill_type()
        if bill_type == FiscalBill:
            bill = self.__service.get_fiscal(input("Give id: "))
        if bill_type == Invoice:
            bill = self.__service.get_invoice(input("Give id: "))
        number = int(input("How many items do you wish to add?"))
        while number != 0:
            try:
                self.__service.add_item_to_bill(self.choose_item(), bill)
                number -= 1
            except Exception as exp:
                print(exp)

    def invoice_to_fiscal(self):
        invoice_id = int(input("What invoice do you want to choose?\nGive id: "))
        self.__service.invoice_to_fiscal(invoice_id)

    def run(self):
        while True:
            print("1.Customer menu\n2.Items menu\n3.Currency menu\n"
                  "4.Bill menu\n5.Exit\n")
            option = input()
            try:
                self.__validator.option_check(option, 5)
                options = {
                    "1": self.customer_menu,
                    "2": self.item_menu,
                    "3": self.currency_menu,
                    "4": self.bill_menu,
                    "5": exit
                }
                options[option]()
            except OptionError as exp:
                print(exp)
