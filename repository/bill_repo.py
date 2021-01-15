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
        return None

    def delete(self, bill_id):
        for bill in self.get_all():
            if bill.get_bill_id() == bill_id:
                self._list.remove(bill)
                return bill

    def update(self, old_obj, new_obj):
        if not type(old_obj) in self._implemented_objects:
            raise Exception("Type is not allowed")
        if not type(new_obj) in self._implemented_objects:
            raise Exception("Type is not allowed")
        for bill in self._list:
            if old_obj.get_bill_id() == bill.get_bill_id():
                old_bill = bill
                self.delete(bill.get_bill_id())
                self.store(new_obj)
                return old_bill
