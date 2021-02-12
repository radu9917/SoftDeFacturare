from service.service_customer import CustomerService
from service.service_bill import BillService
from service.service_item import ItemService
from domain.invoice import Invoice
from domain.fiscal_bill import FiscalBill
from domain.individual import Individual
from domain.company import Company
from repository.json_bill_repo import JsonBillRepo
from repository.json_customer_repo import JsonCustomerRepo
from repository.json_currency_repo import JsonCurrencyRepo
from validator.validator import Validator
from domain.bill_item import BillItem
from service.service_currency import CurrencyService
from repository.json_item_repo import JsonItemRepo
import copy
import pdfkit



class Service:
    def __init__(self, currency_file, item_file, customer_file, bill_file):
        self.__currency_service = CurrencyService(JsonCurrencyRepo(currency_file))
        self.__item_service = ItemService(JsonItemRepo(item_file))
        self.__customer_service = CustomerService(JsonCustomerRepo(customer_file, Individual), JsonCustomerRepo(customer_file, Company))
        self.__bill_service = BillService(JsonBillRepo(bill_file, Invoice), JsonBillRepo(bill_file, FiscalBill))
        self.__validator = Validator.get_instance()

    # Customer options
    def create_customer(self, customer):
        self.__customer_service.create_customer(customer)

    def delete_customer(self, customer):
        self.__customer_service.delete_customer(customer)

    def modify_customer(self, old_customer, new_customer):
        self.__customer_service.update_customer(old_customer, new_customer)

    def view_all_individual_customer(self):
        return self.__customer_service.view_all_individual()

    def view_all_company_customer(self):
        return self.__customer_service.view_all_company()

    def get_individual_customer(self, customer_id):
        return self.__customer_service.get_individual_customer(customer_id)

    def get_company_customer(self, customer_id):
        return self.__customer_service.get_company_customer(customer_id)

    # Item Options
    def create_item(self, item):
        self.__validator.validate_item(item)
        self.__item_service.create_item(item)

    def delete_item(self, item_id):
        self.__validator.find_id(item_id, self.__item_service.view_all_item())
        self.__item_service.delete_item(item_id)

    def modify_item(self, old_item, new_item):
        self.__validator.validate_item(new_item)
        self.__item_service.modify_item(old_item, new_item)

    def view_items(self):
        return self.__item_service.view_all_item()

    def choose_item(self, item_id):
        return self.__item_service.choose_item(item_id)

    # Currency Options
    def create_currency(self, currency):
        self.__currency_service.create_currency(currency)

    def delete_currency(self, currency_id):
        self.__currency_service.delete_currency(int(currency_id))

    def modify_currency(self, old_currency, new_currency):
        self.__currency_service.modify_currency(int(old_currency), new_currency)

    def view_currency(self):
        return self.__currency_service.view_currency()

    def get_currency(self, index):
        return self.__currency_service.get_currency(index)

    # Bill Options
    def create_bill(self, bill):
        self.__validator.validate_bill(bill)
        self.__bill_service.create_bill(bill)

    def delete_bill(self, bill):
        self.__bill_service.delete_bill(bill)

    def invoice_to_fiscal(self, bill_id):
        self.__bill_service.invoice_to_fiscal(bill_id)

    def modify_bill(self, old_bill, new_bill):
        self.__validator.validate_bill(new_bill)
        self.__bill_service.update_bill(old_bill, new_bill)

    def get_fiscal(self, bill_id):
        return self.__bill_service.get_fiscal(int(bill_id))

    def get_invoice(self, bill_id):
        return self.__bill_service.get_invoice(int(bill_id))

    def add_item_to_bill(self, item_id, bill):
        bill_copy = copy.deepcopy(bill)
        item = self.choose_item(int(item_id))
        bill_item = BillItem()
        bill_item.import_from_item(item)
        bill_copy.add_items(bill_item)
        self.__bill_service.update_bill(bill_copy.get_id(), bill_copy)

    def export_bill_as_txt(self, bill, template):
        return self.__bill_service.render_bill(bill, template)

    def render_bill(self, bill_name, bill, template):
        with open("bills/html/"+bill_name+str(bill.get_id())+".html", "w") as file:
            file.write(self.export_bill_as_txt(bill, template))
        pdfkit.from_file("bills/html/"+bill_name+str(bill.get_id())+".html",
                         "bills/pdf/"+bill_name+str(bill.get_id())+".pdf")
