from repository.customer_repo import CustomerRepo
from domain.individual import Individual
from domain.company import Company
from validator.validator import Validator


class CustomerService:
    def __init__(self):
        self.__individual_repo = CustomerRepo(Individual)
        self.__company_repo = CustomerRepo(Company)
        self.__validator = Validator.get_instance()

    def create_customer(self, customer):
        if isinstance(customer, Individual):
            self.__validator.is_id(customer.get_id(), self.__individual_repo.get_all())
            self.__individual_repo.store(customer)
            self.__validator.validate_individual(customer)
        if isinstance(customer, Company):
            self.__validator.is_id(customer.get_id(), self.__company_repo.get_all())
            self.__validator.validate_company(customer)
            self.__company_repo.store(customer)

    def delete_customer(self, customer):
        if isinstance(customer, Individual):
            self.__validator.find_id(customer.get_id(), self.__individual_repo.get_all())
            self.__individual_repo.delete(customer.get_id())
        if isinstance(customer, Company):
            self.__validator.find_id(customer.get_id(), self.__company_repo.get_all())
            self.__company_repo.delete(customer.get_id())

    def update_customer(self, old_customer, new_customer):
        if isinstance(new_customer, Individual):
            self.__validator.find_id(old_customer, self.__individual_repo.get_all())
            self.__individual_repo.update(self.__individual_repo.get(old_customer), new_customer)
        if isinstance(new_customer, Company):
            self.__validator.find_id(old_customer, self.__company_repo.get_all())
            self.__company_repo.update(self.__company_repo.get(old_customer), new_customer)

    def choose_individual_customer(self, customer_id):
        self.__validator.find_id(customer_id, self.__individual_repo.get_all())
        return self.__individual_repo.get(customer_id)

    def choose_company_customer(self, customer_id):
        self.__validator.find_id(customer_id, self.__company_repo.get_all())
        return self.__company_repo.get(customer_id)

    def view_all_individual(self):
        return self.__individual_repo.get_all()

    def view_all_company(self):
        return self.__company_repo.get_all()