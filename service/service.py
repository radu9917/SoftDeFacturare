from domain.invoice import Invoice
from domain.company import Company
from domain.fiscal_bill import FiscalBill
from domain.individual import Individual


class Service:
    def __init__(self, invoice_repo, fiscal_bill_repo, currency_repo, item_repo, company_repo, individual_repo):
        self.__invoice_repo = invoice_repo
        self.__fiscal_bill_repo = fiscal_bill_repo
        self.__currency_repo = currency_repo
        self.__item_repo = item_repo
        self.__individual_repo = individual_repo
        self.__company_repo = company_repo

    # Customer options
    def create_customer(self, customer):
        if isinstance(customer, Company):
            self.__company_repo.store(customer)
        if isinstance(customer, Individual):
            self.__individual_repo.store(customer)

    def delete_customer(self, customer, customer_type):
        if customer_type == Company:
            self.__company_repo.delete(self.__company_repo.get(customer))
        if customer_type == Individual:
            self.__individual_repo.delete(self.__individual_repo.get(customer))

    def modify_customer(self, old_customer, new_customer):
        if isinstance(new_customer, Company):
            self.__company_repo.update(self.__company_repo.get(old_customer), new_customer)
        if isinstance(new_customer, Individual):
            self.__individual_repo.update(self.__individual_repo.get(old_customer), new_customer)

    def view_customer(self, customer_type):
        if customer_type == Company:
            return self.__company_repo.get_all()
        if customer_type == Individual:
            return self.__individual_repo.get_all()

    # Item Options
    def create_item(self, item):
        self.__item_repo.store(item)

    def delete_item(self, item_id):
        self.__item_repo.delete(item_id)

    def modify_item(self, old_item, new_item):
        self.__item_repo.update(self.__item_repo.get(old_item), new_item)

    def view_item(self):
        return self.__item_repo.get_all()

    # Currency Options
    def create_currency(self, currency):
        self.__currency_repo.store(currency)

    def delete_currency(self, currency_id):
        self.__currency_repo.delete(currency_id)

    def modify_currency(self, old_currency, new_currency):
        self.__currency_repo.update(self.__currency_repo.get(old_currency), new_currency)

    def view_currency(self):
        return self.__currency_repo.get_all()

    # Bill Options
    def create_bill(self, bill):
        if isinstance(bill, FiscalBill):
            self.__fiscal_bill_repo.store(bill)
        if isinstance(bill, Invoice):
            self.__invoice_repo.store(bill)

    def delete_bill(self, bill_id, bill_type):
        if bill_type == FiscalBill:
            self.__fiscal_bill_repo.delete(bill_id)
        if bill_type == Invoice:
            self.__invoice_repo.delete(bill_id)

    def modify_bill(self, old_bill, new_bill):
        if isinstance(new_bill, FiscalBill):
            self.__fiscal_bill_repo.update(self.__fiscal_bill_repo.get(old_bill), new_bill)
        if isinstance(new_bill, Invoice):
            self.__invoice_repo.update(self.__invoice_repo.get(old_bill), new_bill)
