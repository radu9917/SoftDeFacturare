from service.service_customer import CustomerService
from service.service_bill import BillService


class Service:
    def __init__(self, currency_repo, item_repo):
        self.__currency_repo = currency_repo
        self.__item_repo = item_repo
        self.__customer_service = CustomerService()
        self.__bill_service = BillService()

    # Customer options
    def create_customer(self, customer):
        self.__customer_service.create_customer(customer)

    def delete_customer(self, customer):
        self.__customer_service.delete_customer(customer)

    def modify_customer(self, old_customer, new_customer):
        self.__customer_service.update_customer(old_customer, new_customer)

    def view_individual_customer(self, customer_id):
        return self.__customer_service.choose_individual_customer(customer_id)

    def view_company_customer(self, customer_id):
        return self.__customer_service.choose_company_customer(customer_id)

    # Item Options
    def create_item(self, item):
        self.__item_repo.store(item)

    def delete_item(self, item_id):
        self.__item_repo.delete(item_id)

    def modify_item(self, old_item, new_item):
        self.__item_repo.update(self.__item_repo.get(old_item), new_item)

    def view_item(self):
        return self.__item_repo.get_all()

    def choose_item(self, item_id):
        return self.__item_repo.get(item_id)

    def add_item_to_bill(self, item_id, bill):
        item = self.choose_item(item_id)
        bill.add_items(item)
        self.__bill_service.create_bill(bill)

    # Currency Options
    def create_currency(self, currency):
        self.__currency_repo.store(currency)

    def delete_currency(self, currency_id):
        self.__currency_repo.delete(currency_id)

    def modify_currency(self, old_currency, new_currency):
        self.__currency_repo.update(self.__currency_repo.get(old_currency), new_currency)

    def view_currency(self):
        return self.__currency_repo.get_all()

    # Bill Options
    def create_bill(self, bill):
        self.__bill_service.create_bill(bill)

    def delete_bill(self, bill_id):
        self.__bill_service.delete_bill(bill_id)

    def modify_bill(self, old_bill, new_bill):
        self.__bill_service.update_bill(old_bill, new_bill)

    def choose_fiscal_bill(self, bill_id):
        return self.__bill_service.choose_fiscal_bill(bill_id)

    def choose_invoice(self, bill_id):
        return self.__bill_service.choose_invoice(bill_id)
