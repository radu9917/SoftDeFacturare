from domain.individual import Individual
from domain.company import Company
from domain.bill_item import BillItem
from domain.fiscal_bill import FiscalBill
from domain.invoice import Invoice
from domain.currency import Currency
from domain.address import Address
import copy


class BillBuilder:
    def __init__(self):
        self.__bill = None
        self.__customer = None
        self.__issuer = None
        self.__item_list = None
        self.__currency = None
        self.__customer_address = None
        self.__issuer_address = None
        self.__issue_date = None
        self.__due_date = None
        self.__notes = None
        self.__total = None
        self.__bill_id = None

    def __create_address(self, address, county, postal_code, country):
        created_address = Address()
        created_address.set_address(address)
        created_address.set_county(county)
        created_address.set_postal_code(postal_code)
        created_address.set_country(country)
        return created_address

    def create_customer_address(self, address, county, postal_code, country):
        self.__customer_address = self.__create_address(address, county, postal_code, country)

    def create_issuer_address(self, address, county, postal_code, country):
        self.__issuer_address = self.__create_address(address, county, postal_code, country)

    def create_individual_customer(self, cnp, last_name, first_name, email_address, phone_number):
        customer = Individual()
        customer.set_cnp(cnp)
        customer.set_last_name(last_name)
        customer.set_first_name(first_name)
        customer.set_email_address(email_address)
        customer.set_phone_number(phone_number)
        self.__customer = customer

    def _create_company(self, name, last_name, first_name, email_address,
                        phone_number, fiscal_no, registration_number):
        customer = Company()
        customer.set_company_name(name)
        customer.set_last_name(last_name)
        customer.set_first_name(first_name)
        customer.set_email_address(email_address)
        customer.set_phone_number(phone_number)
        customer.set_fiscal_no(fiscal_no)
        customer.set_registration_number(registration_number)

        return customer

    def create_company_customer(self, name, last_name, first_name, email_address,
                                phone_number, fiscal_no, registration_number):
        self.__customer = self._create_company(name, last_name,
                                               first_name, email_address, phone_number,
                                               fiscal_no, registration_number)

    def create_issuer(self, name, last_name, first_name, email_address, phone_number, fiscal_no,
                      registration_number):
        self.__issuer = self._create_company(name, last_name,
                                             first_name, email_address, phone_number,
                                             fiscal_no, registration_number)

    def __create_currency(self, symbol, name, code, exchange_rate):
        currency = Currency(symbol, name, code)
        currency.set_exchange_rate(exchange_rate)
        return currency

    def add_item_to_list(self, quantity, name, description, price, discount, percent_discount,
                         currency_name, currency_code, currency_symbol, currency_exchange_rate):
        if self.__item_list is None:
            self.__item_list = []
        item = BillItem()
        item.set_name(name)
        item.set_description(description)
        item.set_price(price)
        item.set_quantity(quantity)
        item.set_discount(discount)
        item.set_percent_discount(percent_discount)
        item.calc_total()
        currency = self.__create_currency(currency_symbol, currency_name, currency_code, currency_exchange_rate)
        item.set_currency(currency)
        self.__item_list.append(item)

    def create_bill_currency(self, symbol, name, code, exchange_rate):
        self.__currency = self.__create_currency(symbol, name, code, exchange_rate)

    def create_bill(self, bill_type, issue_date, due_date, notes, identifier, total):
        bill = None
        if bill_type == FiscalBill:
            bill = FiscalBill()
        if bill_type == Invoice:
            bill = Invoice()
        if bill is None:
            raise TypeError("Wrong Bill Type")
        self.__bill = bill
        self.__issue_date = issue_date
        self.__due_date = due_date
        self.__notes = notes
        self.__bill_id = identifier
        self.__total = total

    def validate_components(self):
        errors = []
        if self.__bill is None:
            errors.append("Bill not created")
        if self.__item_list is None:
            errors.append("Item list not created")
        if self.__customer is None:
            errors.append("Customer not created")
        if self.__issuer is None:
            errors.append("Issuer not created")
        if self.__currency is None:
            errors.append("Currency not created")
        if self.__customer_address is None:
            errors.append("Customer address not created")
        if self.__issuer_address is None:
            errors.append("Issuer address not created")
        if self.__issue_date is None:
            errors.append("Issue date not created")
        if self.__due_date is None:
            errors.append("Due date not created")
        if self.__notes is None:
            errors.append("Notes not created")
        if self.__total is None:
            errors.append("Total not created")
        if self.__bill_id is None:
            errors.append("Bill id not created")
        if errors:
            raise Exception(errors)

    def reset_components(self):
        self.__bill = None
        self.__customer = None
        self.__issuer = None
        self.__item_list = None
        self.__currency = None
        self.__customer_address = None
        self.__issuer_address = None
        self.__issue_date = None
        self.__due_date = None
        self.__notes = None
        self.__total = None
        self.__bill_id = None
    def build(self):
        self.validate_components()
        bill = copy.deepcopy(self.__bill)
        self.__issuer.set_address(self.__issuer_address)
        self.__customer.set_address(self.__customer_address)
        bill.set_issuer(self.__issuer)
        bill.set_customer(self.__customer)
        bill.set_id(self.__bill_id)
        bill.set_notes(self.__notes)
        bill.set_issue_date(self.__issue_date)
        bill.set_items(self.__item_list)
        bill.set_currency(self.__currency)
        bill.set_due_date(self.__due_date)
        bill.set_total(self.__total)
        self.reset_components()
        return bill
