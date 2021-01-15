from repository.repo_interface import IRepo
import copy


class CustomerRepo(IRepo):
    def __init__(self):
        self._list =[]

    def store(self, customer):
        self._list.append(copy.deepcopy(customer))

    def delete(self, index):
        for customer in self.get_all():
            if customer.get_id() == index:
                self._list.remove(customer)

    def get_all(self):
        return self._list

    def get(self, index):
        for customer in self.get_all():
            if index == customer.get_id():
                return customer

    def update(self, old_customer, new_customer):
        for customer in self.get_all():
            if old_customer.get_id() == customer.get_id():
                customer.set_id(new_customer.get_id())
                customer.set_phone_number(new_customer.get_phone_number())
                customer.set_first_name(new_customer.get_first_name())
                customer.set_last_name(new_customer.get_last_name())
                customer.set_email_address(new_customer.get_email_address())
