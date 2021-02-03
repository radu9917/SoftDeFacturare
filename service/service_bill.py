from domain.invoice import Invoice
from domain.fiscal_bill import FiscalBill
from repository.json_bill_repo import JsonBillRepo
from validator.validator import Validator


class BillService:
    def __init__(self):
        self.__invoice_repo = JsonBillRepo("bill.json", Invoice)
        self.__fiscal_bill_repo = JsonBillRepo("bill.json", FiscalBill)
        self.__validator = Validator.get_instance()

    def create_bill(self, bill):
        self.__validator.validate_bill(bill)
        if isinstance(bill, Invoice):
            self.__invoice_repo.store(bill)
        if isinstance(bill, FiscalBill):
            self.__fiscal_bill_repo.store(bill)

    def delete_bill(self, bill):

        if isinstance(bill, Invoice):
            self.__validator.find_id(str(bill.get_id()), self.__invoice_repo.get_all())
            self.__invoice_repo.delete(bill.get_id())
        if isinstance(bill, FiscalBill):
            self.__validator.find_id(str(bill.get_id()), self.__fiscal_bill_repo.get_all())
            self.__fiscal_bill_repo.delete(bill.get_id())

    def update_bill(self, old_bill, new_bill):
        self.__validator.validate_bill(new_bill)
        if isinstance(new_bill, Invoice):
            self.__validator.find_id(str(old_bill), self.__invoice_repo.get_all())
            self.__invoice_repo.update(self.__invoice_repo.get(old_bill), new_bill)
        if isinstance(new_bill, FiscalBill):
            self.__validator.find_id(str(old_bill), self.__fiscal_bill_repo.get_all())
            self.__fiscal_bill_repo.update(self.__fiscal_bill_repo.get(old_bill), new_bill)

    def choose_fiscal_bill(self, bill_id):
        self.__validator.find_id(bill_id, self.__fiscal_bill_repo.get_all())
        return self.__fiscal_bill_repo.get(bill_id)

    def choose_invoice(self, bill_id):
        self.__validator.find_id(bill_id, self.__invoice_repo.get_all())
        return self.__invoice_repo.get(bill_id)

    def print_fiscal_bill(self, bill_id):
        self.__validator.find_id(bill_id, self.__fiscal_bill_repo.get_all())
        for bill in self.__fiscal_bill_repo.get_all():
            if bill.get_id() == int(bill_id):
                return bill

    def print_invoice(self, bill_id):
        self.__validator.find_id(bill_id, self.__invoice_repo.get_all())
        for bill in self.__invoice_repo.get_all():
            if bill.get_id() == int(bill_id):
                return bill

    def get_fiscal(self, index):
        return self.__fiscal_bill_repo.get(index)

    def get_invoice(self, index):
        return self.__invoice_repo.get(index)
