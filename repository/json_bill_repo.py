from repository.bill_repo import BillRepo
from domain.company import Company
from domain.bill_item import BillItem
from domain.individual import Individual
from domain.currency import Currency
from builder.bill_builder import BillBuilder
from domain.fiscal_bill import FiscalBill
from domain.invoice import Invoice
import json


class JsonBillRepo(BillRepo):
    def __init__(self, file_name, repo_type):
        super().__init__(repo_type)
        self.__file_name = file_name
        self.__load_from_file()

    def store(self, obj):
        returned_obj = super().store(obj)
        self.__store_to_file()
        return returned_obj

    def delete(self, obj_id):
        returned_obj = super().delete(obj_id)
        self.__store_to_file()
        return returned_obj

    def update(self, old_object, new_object):
        returned_obj = super().update(old_object, new_object)
        self.__store_to_file()
        return returned_obj

    def __store_to_file(self):
        invoice_list = []
        fiscal_bill_list = []
        bill_list = []
        for bill in self._list:
            company = bill.get_issuer()
            address = company.get_address()
            issuer_address = {
                "address": address.get_address(),
                "county": address.get_county(),
                "country": address.get_country(),
                "postal_code": address.get_postal_code()
            }
            issuer = {
                "company_name": company.get_company_name(),
                "fiscal_no": company.get_fiscal_no(),
                "registration_number": company.get_registration_number(),
                "first_name": company.get_first_name(),
                "last_name": company.get_last_name(),
                "phone_number": company.get_phone_number(),
                "email_address": company.get_email_address(),
                "address": issuer_address
            }

            customer = bill.get_customer()
            address = customer.get_address()
            customer_address = {
                "address": address.get_address(),
                "county": address.get_county(),
                "country": address.get_country(),
                "postal_code": address.get_postal_code()
            }
            if isinstance(customer, Individual):
                customer_dict = {
                    "cnp": customer.get_cnp(),
                    "first_name": customer.get_first_name(),
                    "last_name": customer.get_last_name(),
                    "phone_number": customer.get_phone_number(),
                    "email_address": customer.get_email_address(),
                    "address": customer_address
                }
            if isinstance(customer, Company):
                customer_dict = {
                    "company_name": customer.get_company_name(),
                    "fiscal_no": customer.get_fiscal_no(),
                    "registration_number": customer.get_registration_number(),
                    "first_name": customer.get_first_name(),
                    "last_name": customer.get_last_name(),
                    "phone_number": customer.get_phone_number(),
                    "email_address": customer.get_email_address(),
                    "address": customer_address
                }
            issue_date = bill.get_issue_date()
            due_date = bill.get_due_date()
            item_dict_list = []
            item_list = bill.get_items()
            for item in item_list:
                currency = item.get_currency()
                currency_dict = {
                    "symbol": currency.get_symbol(),
                    "name": currency.get_name(),
                    "code": currency.get_code(),
                    "exchange_rate": currency.get_exchange_rate()
                }
                item_dict = {
                    "currency": currency_dict,
                    "name": item.get_name(),
                    "price": item.get_price(),
                    "description": item.get_description(),
                    "discount": item.get_discount(),
                    "percent_discount": item.get_percent_discount(),
                    "quantity": item.get_quantity()
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
            tax = bill.get_total()
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
        current_fiscal_bill_id = 1
        current_invoice_id = 1
        if self._repo_type == FiscalBill:
            fiscal_bill_list = bill_list
            current_fiscal_bill_id = self._id
            if "invoice_list" in json_file and json_file["invoice_list"] != []:
                invoice_list = json_file["invoice_list"]
            if "current_invoice_id" in json_file:
                current_invoice_id = json_file["current_invoice_id"]

        if self._repo_type == Invoice:
            invoice_list = bill_list
            current_invoice_id = self._id
            if "fiscal_bill_list" in json_file and json_file["fiscal_bill_list"] != []:
                fiscal_bill_list = json_file["fiscal_bill_list"]
            if "current_fiscal_bill_id" in json_file:
                current_fiscal_bill_id = json_file["current_fiscal_bill_id"]

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
        builder = BillBuilder()
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
                issuer = bill["issuer"]
                builder.create_issuer(issuer["company_name"], issuer["last_name"], issuer["first_name"],
                                      issuer["email_address"], issuer["phone_number"],
                                      issuer["fiscal_no"], issuer["registration_number"])
                issuer_address = issuer["address"]
                builder.create_issuer_address(issuer_address["address"], issuer_address["county"],
                                              issuer_address["postal_code"], issuer_address["country"])
                customer = bill["customer"]
                if "cnp" in customer:
                    builder.create_individual_customer(customer["cnp"], customer["last_name"],
                                                       customer["first_name"], customer["email_address"],
                                                       customer["phone_number"])
                if "company_name" in customer:
                    builder.create_company_customer(customer["company_name"], customer["last-name"],
                                                    customer["first_name"],
                                                    customer["email_address"], customer["phone_number"],
                                                    customer["fiscal_no"], customer["registration_number"])
                customer_address = customer["address"]
                builder.create_customer_address(customer_address["address"], customer_address["county"],
                                                customer_address["postal_code"], customer_address["country"])
                for item in bill["item_list"]:
                    currency = item["currency"]
                    builder.add_item_to_list(item["quantity"], item["name"], item["description"], item["price"],
                                             item["discount"], item["percent_discount"], currency["name"]
                                             , currency["code"], currency["symbol"], currency["exchange_rate"])

                currency = bill["currency"]
                builder.create_bill_currency(currency["symbol"], currency["name"],
                                             currency["code"], currency["exchange_rate"])
                builder.create_bill(self._repo_type, bill["issue_date"], bill["due_date"],
                                    bill["notes"], bill["id"], bill["total"])
                bill_to_add = builder.build()
                self._list.append(bill_to_add)

    def reset_id(self):
        self._id = 1
