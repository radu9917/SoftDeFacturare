from repository.repo_interface import IRepo
from domain.fiscal_bill import FiscalBill
from domain.invoice import Invoice
import copy


class BillRepo(IRepo):
    def __init__(self, repo_type):
        self._list = []
        self._repo_type = repo_type
        self._implemented_objects = [FiscalBill, Invoice]
        self._id = 1

    def store(self, bill):
        bill_copy = copy.deepcopy(bill)
        if not type(bill_copy) in self._implemented_objects:
            raise TypeError("Type is not allowed")
        bill_copy.set_id(self._id)
        self._id += 1
        self._list.append(bill_copy)
        return bill_copy

    def get_all(self):
        return copy.deepcopy(self._list)

    def get(self, bill_id):
        for bill in self.get_all():
            if bill.get_id() == bill_id:
                return bill
        return None

    def delete(self, bill_id):
        for bill in self.get_all():
            if bill.get_id() == bill_id:
                self._list.remove(bill)
                return bill
        return None

    def update(self, old_obj, new_obj):
        if not type(new_obj) in self._implemented_objects:
            raise TypeError("Type is not allowed")
        old_bill = self.get(old_obj)
        if self.delete(old_obj):
            current_id = self._id
            self._id = old_obj
            self.store(new_obj)
            self._id = current_id
            return old_bill
        return None
