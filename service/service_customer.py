from repository.customer_repo import CustomerRepo
from domain.individual import Individual
from domain.company import Company


class CustomerService:
    def __init__(self):
        self.__individual_repo = CustomerRepo(Individual)
        self.__company_repo = CustomerRepo(Company)

    def create_customer(self, customer):
        if isinstance(customer, Individual):
            self.__individual_repo.store(customer)
        if isinstance(customer, Company):
            self.__company_repo.store(customer)

    def delete_customer(self, customer):
        if isinstance(customer, Individual):
            self.__individual_repo.delete(customer.get_id())
        if isinstance(customer, Company):
            self.__company_repo.delete(customer.get_id())

    def update_customer(self, old_customer, new_customer):
        if isinstance(new_customer, Individual):
            self.__individual_repo.update(self.__individual_repo.get(old_customer), new_customer)
        if isinstance(new_customer, Company):
            self.__company_repo.update(self.__company_repo.get(old_customer), new_customer)

    def choose_individual_customer(self, customer_id):
        return self.__individual_repo.get(customer_id)

    def choose_company_customer(self, customer_id):
        return self.__company_repo.get(customer_id)
