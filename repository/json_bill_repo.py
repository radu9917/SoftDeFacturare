from repository.bill_repo import BillRepo
from domain.company import Company
from domain.individual import Individual
from domain.currency import Currency
from domain.item import Item
from domain.fiscal_bill import FiscalBill
from domain.invoice import Invoice
import json


class JsonBillRepo(BillRepo):
    def __init__(self, file_name, repo_type):
        super().__init__(repo_type)
        self.__file_name = file_name
        self.__load_from_file()

    def store(self, obj):
        super().store(obj)
        self.__store_to_file()

    def delete(self, obj_id):
        super().delete(obj_id)
        self.__store_to_file()

    def update(self, old_object, new_object):
        super().update(old_object, new_object)
        self.__store_to_file()

    def __store_to_file(self):
        invoice_list = []
        fiscal_bill_list = []
        bill_list = []
        for bill in self._list:
            company = bill.get_issuer()
            issuer = {
                "company_name": company.get_company_name(),
                "fiscal_no": company.get_fiscal_no(),
                "registration_number": company.get_registration_number(),
                "first_name": company.get_first_name(),
                "last_name": company.get_last_name(),
                "phone_number": company.get_phone_number(),
                "email_address": company.get_email_address()
            }
            customer = bill.get_customer()
            if isinstance(customer, Individual):
                customer_dict = {
                    "cnp": customer.get_cnp(),
                    "first_name": customer.get_first_name(),
                    "last_name": customer.get_last_name(),
                    "phone_number": customer.get_phone_number(),
                    "email_address": customer.get_email_address()
                }
            if isinstance(customer, Company):
                customer_dict = {
                    "company_name": customer.get_company_name(),
                    "fiscal_no": customer.get_fiscal_no(),
                    "registration_number": customer.get_registration_number(),
                    "first_name": customer.get_first_name(),
                    "last_name": customer.get_last_name(),
                    "phone_number": customer.get_phone_number(),
                    "email_address": customer.get_email_address()
                }
            issue_date = bill.get_issue_date()
            due_date = bill.get_due_date()
            item_dict_list = []
            item_list = bill.get_items()
            for item in item_list:
                currency = item[0].get_currency()
                currency_dict = {
                    "symbol": currency.get_symbol(),
                    "name": currency.get_name(),
                    "code": currency.get_code(),
                    "exchange_rate": currency.get_exchange_rate()
                }
                item_dict = {
                    "currency": currency_dict,
                    "name": item[0].get_name(),
                    "price": item[0].get_price(),
                    "description": item[0].get_description(),
                    "discount": item[0].get_discount(),
                    "percent_discount": item[0].get_percent_discount()
                }
                item_dict_list.append(item_dict)
            currency = bill.get_currency()
            symbol = currency.get_symbol()
            name = currency.get_name()
            code = currency.get_code()
            exchange_rate = currency.get_exchange_rate()
            currency_dict = {
                "symbol": symbol,
                "name": name,
                "code": code,
                "exchange_rate": exchange_rate
            }
            notes = bill.get_notes()
            tax = bill.get_tax()
            bill_id = bill.get_id()
            bill_dict = {
                "id": bill_id,
                "issuer": issuer,
                "customer": customer_dict,
                "issue_date": issue_date,
                "due_date": due_date,
                "item_list": item_dict_list,
                "currency": currency_dict,
                "notes": notes,
                "tax": tax
            }
            bill_list.append(bill_dict)
        file = open(self.__file_name, "r")
        json_file = json.loads(file.read())
        file.close()
        current_fiscal_bill_id = None
        current_invoice_id = None
        if self._repo_type == FiscalBill:
            fiscal_bill_list = bill_list
            current_fiscal_bill_id = self._id
            if "invoice_list" in json_file and json_file["invoice_list"] != []:
                invoice_list = json_file["invoice_list"]
            if "current_invoice_id" in json_file:
                current_invoice_id = json_file["current_invoice_id"]
            else:
                current_invoice_id = 1

        if self._repo_type == Invoice:
            invoice_list = bill_list
            current_invoice_id = self._id
            if "fiscal_bill_list" in json_file and json_file["fiscal_bill_list"] != []:
                fiscal_bill_list = json_file["fiscal_bill_list"]
            if "current_fiscal_bill_id" in json_file:
                current_fiscal_bill_id = json_file["current_fiscal_bill_id"]
            else:
                current_fiscal_bill_id = 1
        json_list = {
            "current_fiscal_bill_id": current_fiscal_bill_id,
            "current_invoice_id": current_invoice_id,
            "invoice_list": invoice_list,
            "fiscal_bill_list": fiscal_bill_list
        }
        file = open(self.__file_name, "w")
        string = json.dumps(json_list, indent=4)
        file.write(string)
        file.close()

    def __load_from_file(self):
        list_type = None
        bill_to_add = None
        file = open(self.__file_name, "r")
        json_file = json.loads(file.read())
        file.close()
        if self._repo_type == FiscalBill:
            if "current_fiscal_bill_id" in json_file:
                self._id = json_file["current_fiscal_bill_id"]
            list_type = "fiscal_bill_list"
        if self._repo_type == Invoice:
            if "current_invoice_id" in json_file:
                self._id = json_file["current_invoice_id"]
            list_type = "invoice_list"
        if list_type in json_file:
            for bill in json_file[list_type]:
                bill_id = bill["id"]
                if self._repo_type == FiscalBill:
                    bill_to_add = FiscalBill()
                if self._repo_type == Invoice:
                    bill_to_add = Invoice()
                issuer = Company()
                issuer.set_company_name(bill["issuer"]["company_name"])
                issuer.set_fiscal_no(bill["issuer"]["fiscal_no"])
                issuer.set_registration_number(bill["issuer"]["registration_number"])
                issuer.set_first_name(bill["issuer"]["first_name"])
                issuer.set_last_name(bill["issuer"]["last_name"])
                issuer.set_phone_number(bill["issuer"]["phone_number"])
                issuer.set_email_address(bill["issuer"]["email_address"])
                bill_to_add.set_issuer(issuer)
                customer = None
                if "cnp" in bill["customer"]:
                    customer = Individual()
                    customer.set_first_name(bill["customer"]["first_name"])
                    customer.set_cnp(bill["customer"]["cnp"])
                    customer.set_last_name(bill["customer"]["last_name"])
                    customer.set_phone_number(bill["customer"]["phone_number"])
                    customer.set_email_address(bill["customer"]["email_address"])
                if "company_name" in bill["customer"]:
                    customer = Company()
                    customer.set_company_name(bill["customer"]["company_name"])
                    customer.set_fiscal_no(bill["customer"]["fiscal_no"])
                    customer.set_registration_number(bill["customer"]["registration_number"])
                    customer.set_first_name(bill["customer"]["first_name"])
                    customer.set_last_name(bill["customer"]["last_name"])
                    customer.set_phone_number(bill["customer"]["phone_number"])
                    customer.set_email_address(bill["customer"]["email_address"])
                bill_to_add.set_customer(customer)
                item_list = []
                for item in bill["item_list"]:
                    item_to_add = Item()
                    symbol = item["currency"]["symbol"]
                    name = item["currency"]["name"]
                    code = item["currency"]["code"]
                    currency = Currency(symbol, name, code)
                    exchange_rate = item["currency"]["exchange_rate"]
                    currency.set_exchange_rate(exchange_rate)
                    item_to_add.set_name(item["name"])
                    item_to_add.set_price(item["price"])
                    item_to_add.set_discount(item["discount"])
                    item_to_add.set_description(item["description"])
                    item_to_add.set_percent_discount(item["percent_discount"])
                    item_to_add.set_currency(currency)
                    item_list.append((item_to_add,1))
                bill_to_add.set_id(bill_id)
                bill_to_add.set_items(item_list)
                bill_to_add.set_notes(bill["notes"])
                bill_to_add.set_issue_date(bill["issue_date"])
                bill_to_add.set_due_date(bill["due_date"])
                bill_to_add.set_tax(bill["tax"])
                symbol = bill["currency"]["symbol"]
                name = bill["currency"]["name"]
                code = bill["currency"]["code"]
                currency = Currency(symbol, name, code)
                exchange_rate = bill["currency"]["exchange_rate"]
                currency.set_exchange_rate(exchange_rate)
                bill_to_add.set_currency(currency)
                self._list.append(bill_to_add)

    def reset_id(self):
        self._id = 1
