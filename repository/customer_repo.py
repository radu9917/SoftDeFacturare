from repository.repo_interface import IRepo
from domain.individual import Individual
from domain.company import Company
import copy


class CustomerRepo(IRepo):
    def __init__(self, repo_type):
        self._list = []
        self._repo_type = repo_type
        self._implemented_objects = [Company, Individual]

    def store(self, customer):
        if type(customer) != self._repo_type:
            raise Exception("Type is not allowed")
        self._list.append(copy.deepcopy(customer))
        return customer

    def delete(self, index):
        for customer in self.get_all():
            if customer.get_id() == index.get_id():
                self._list.remove(customer)
                return customer

    def get_all(self):
        return copy.deepcopy(self._list)

    def get(self, index):
        for customer in self.get_all():
            if index == customer.get_id():
                return customer
        return None

    def update(self, old_customer, new_customer):
        if not type(old_customer) in self._implemented_objects:
            raise Exception("Type is not allowed")
        if not type(new_customer) in self._implemented_objects:
            raise Exception("Type is not allowed")

        for customer in self._list:
            if old_customer.get_id() == customer.get_id():
                self.delete(old_customer.get_id())
                self.store(new_customer)
                return old_customer
