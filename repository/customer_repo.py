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

    def delete(self, index):
        for customer in self.get_all():
            if customer.get_id() == index:
                self._list.remove(customer)

    def get_all(self):
        return copy.deepcopy(self._list)

    def get(self, index):
        for customer in self.get_all():
            if index == customer.get_id():
                return customer

    def update(self, old_customer, new_customer):
        if not type(old_customer) in self._implemented_objects:
            raise Exception("Type is not allowed")
        if not type(new_customer) in self._implemented_objects:
            raise Exception("Type is not allowed")

        for customer in self._list:
            if old_customer.get_id() == customer.get_id():
                customer.set_id(new_customer.get_id())
                customer.set_phone_number(new_customer.get_phone_number())
                customer.set_first_name(new_customer.get_first_name())
                customer.set_last_name(new_customer.get_last_name())
                customer.set_email_address(new_customer.get_email_address())
            if isinstance(customer, Individual):
                customer.set_cnp(new_customer.get_cnp())
            if isinstance(customer, Company):
                customer.set_company_name(new_customer.get_company_name())
                customer.set_registration_number(new_customer.get_registration_number())
                customer.set_fiscal_no(new_customer.get_fiscal_no())
