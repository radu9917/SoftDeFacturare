from domain.invoice import Invoice
from domain.fiscal_bill import FiscalBill
from validator.validator import Validator
from config.config import Config


class BillService:
    def __init__(self, invoice_repo, fiscal_bill_repo):
        self.__invoice_repo = invoice_repo
        self.__fiscal_bill_repo = fiscal_bill_repo
        self.__validator = Validator.get_instance()

    def create_bill(self, bill):
        self.__validator.validate_bill(bill)
        if isinstance(bill, Invoice):
            self.__invoice_repo.store(bill)
        if isinstance(bill, FiscalBill):
            self.__fiscal_bill_repo.store(bill)

    def delete_bill(self, bill):
        if isinstance(bill, Invoice):
            self.__validator.find_id(str(bill.get_id()), self.__invoice_repo.get_all())
            self.__invoice_repo.delete(bill.get_id())
        if isinstance(bill, FiscalBill):
            self.__validator.find_id(str(bill.get_id()), self.__fiscal_bill_repo.get_all())
            self.__fiscal_bill_repo.delete(bill.get_id())

    def update_bill(self, old_bill, new_bill):
        self.__validator.validate_bill(new_bill)
        if isinstance(new_bill, Invoice):
            self.__validator.find_id(str(old_bill), self.__invoice_repo.get_all())
            self.__invoice_repo.update(old_bill, new_bill)
        if isinstance(new_bill, FiscalBill):
            self.__validator.find_id(str(old_bill), self.__fiscal_bill_repo.get_all())
            self.__fiscal_bill_repo.update(old_bill, new_bill)

    def get_fiscal(self, bill_id):
        self.__validator.find_id(bill_id, self.__fiscal_bill_repo.get_all())
        return self.__fiscal_bill_repo.get(bill_id)

    def get_invoice(self, bill_id):
        self.__validator.find_id(bill_id, self.__invoice_repo.get_all())
        return self.__invoice_repo.get(bill_id)

    def invoice_to_fiscal(self, bill_id):
        fiscal_bill = FiscalBill()
        for bill in self.__invoice_repo.get_all():
            if bill.get_id() == bill_id:
                fiscal_bill.set_issuer(bill.get_issuer())
                fiscal_bill.set_currency(bill.get_currency())
                fiscal_bill.set_total(bill.get_total())
                fiscal_bill.set_items(bill.get_items())
                fiscal_bill.set_customer(bill.get_customer())
                fiscal_bill.set_due_date(bill.get_due_date())
                fiscal_bill.set_issue_date(bill.get_issue_date())
                fiscal_bill.set_notes(bill.get_notes())
                self.__fiscal_bill_repo.store(fiscal_bill)
                return fiscal_bill

    def render_bill(self, bill, template):
        print(template)
        with open(template, "r") as file:
            bill_base = file.read()
        config = Config.get_instance()
        item_list = ""
        index = 1
        with open(config.get_bill_item_template(), "r") as file:
            item_base = file.read()
        items = bill.get_items()
        for item in items:
            item_list += item_base.format(
                index=index,
                item_name=item.get_name(),
                item_description=item.get_description(),
                quantity=item.get_quantity(),
                price=item.get_price(),
                currency_symbol=item.get_currency().get_symbol(),
                item_total=item.get_total()
            )

            index += 1

        formated_bill = bill_base.format(
                id=bill.get_id(),
                customer=str(bill.get_customer()),
                customer_address=str(bill.get_customer().get_address()),
                issuer=str(bill.get_issuer()),
                issuer_address=str(bill.get_issuer().get_address()),
                issue_date=bill.get_issue_date(),
                due_date=bill.get_due_date(),
                bill_items=item_list,
                bill_total=bill.get_total(),
                notes=bill.get_notes()
        )
        return formated_bill