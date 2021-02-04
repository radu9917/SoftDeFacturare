from repository.repo_interface import IRepo
from domain.individual import Individual
from domain.company import Company
import copy


class CustomerRepo(IRepo):
    def __init__(self, repo_type):
        self._list = []
        self._repo_type = repo_type
        self._implemented_objects = [Company, Individual]
        self._id = 1

    def store(self, customer):
        if type(customer) != self._repo_type:
            raise TypeError("Type is not allowed")
        customer.set_id(self._id)
        self._id += 1
        self._list.append(copy.deepcopy(customer))
        return customer

    def delete(self, index):
        for customer in self.get_all():
            if customer.get_id() == index:
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
        if not type(new_customer) in self._implemented_objects:
            raise TypeError("Type is not allowed")

        for customer in self._list:
            if old_customer == customer.get_id():
                old = self._id
                self._id = old_customer
                self.delete(old_customer)
                self.store(new_customer)
                self._id = old
                return old_customer
