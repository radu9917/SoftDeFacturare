from repository.repo_interface import IRepo
from domain.fiscal_bill import FiscalBill
from domain.invoice import Invoice
import copy


class BillRepo(IRepo):
    def __init__(self, repo_type):
        self._list = []
        self._repo_type = repo_type
        self._implemented_objects = [FiscalBill, Invoice]

    def store(self, bill):
        if not type(bill) in self._implemented_objects:
            raise Exception("Type is not allowed")
        self._list.append(copy.deepcopy(bill))

    def get_all(self):
        return copy.deepcopy(self._list)

    def get(self, bill_id):
        for bill in self.get_all():
            if bill.get_bill_id() == bill_id:
                return copy.deepcopy(bill)

    def delete(self, bill_id):
        for bill in self.get_all():
            if bill.get_bill_id() == bill_id:
                self._list.remove(bill)

    def update(self, old_obj, new_obj):
        if not type(old_obj) in self._implemented_objects:
            raise Exception("Type is not allowed")
        if not type(new_obj) in self._implemented_objects:
            raise Exception("Type is not allowed")

        for bill in self._list:
            if old_obj.get_bill_id() == bill.get_bill_id():
                bill.set_issuer(new_obj.get_issuer())
                bill.set_customer(new_obj.get_customer())
                bill.set_issue_date(new_obj.get_issue_date())
                bill.set_due_date(new_obj.get_due_date())
                bill.set_items(new_obj.get_items())
                bill.set_currency(new_obj.get_currency())
                bill.set_notes(new_obj.get_notes())
                bill.set_tax(new_obj.get_tax())
                bill.set_bill_id(new_obj.get_bill_id())
