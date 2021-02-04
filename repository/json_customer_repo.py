from repository.customer_repo import CustomerRepo
from domain.individual import Individual
from domain.company import Company
import json


class JsonCustomerRepo(CustomerRepo):
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
        individual_list = []
        company_list = []
        for customer in self._list:
            first_name = customer.get_first_name()
            last_name = customer.get_last_name()
            phone_number = customer.get_phone_number()
            index = customer.get_id()
            email_address = customer.get_email_address()
            if self._repo_type == Individual:
                cnp = customer.get_cnp()
                individual_dict = {
                    "id": index,
                    "first_name": first_name,
                    "last_name": last_name,
                    "cnp": cnp,
                    "phone_number": phone_number,
                    "email_address": email_address
                }
                individual_list.append(individual_dict)
            if self._repo_type == Company:
                company_name = customer.get_company_name()
                fiscal_no = customer.get_fiscal_no()
                registration_number = customer.get_registration_number()
                company_dict = {
                    "id": index,
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "email_address": email_address,
                    "company_name": company_name,
                    "fiscal_no": fiscal_no,
                    "registration_number": registration_number
                }
                company_list.append(company_dict)
        file = open(self.__file_name, "r")
        json_file = json.loads(file.read())
        file.close()
        current_company_index = 1
        current_individual_index = 1
        if self._repo_type == Individual:
            if "company_list" in json_file:
                company_list = json_file["company_list"]
            if "current_company_id" in json_file:
                current_company_index = json_file["current_company_id"]
            current_individual_index = self._id
        if self._repo_type == Company:
            if "individual_list" in json_file:
                individual_list = json_file["individual_list"]
            if "current_individual_id" in json_file:
                current_individual_index = json_file["current_individual_id"]
            current_company_index = self._id
        json_list = {
            "current_company_id": current_company_index,
            "current_individual_id": current_individual_index,
            "individual_list": individual_list,
            "company_list": company_list
        }
        file = open(self.__file_name, "w")
        string = json.dumps(json_list, indent=4)
        file.write(string)
        file.close()

    def __load_from_file(self):
        index = "current_index"
        list_type = None
        if self._repo_type == Individual:
            index = "current_individual_id"
            list_type = "individual_list"
        if self._repo_type == Company:
            index = "current_company_id"
            list_type = "company_list"
        file = open(self.__file_name, "r")
        json_file = json.loads(file.read())
        if index in json_file:
            self._id = json_file[index]
        if list_type in json_file:
            for customer in json_file[list_type]:
                index = customer["id"]
                first_name = customer["first_name"]
                last_name = customer["last_name"]
                phone_number = customer["phone_number"]
                email_address = customer["email_address"]
                if self._repo_type == Individual:
                    cnp = customer["cnp"]
                    customer_to_add = Individual()
                    customer_to_add.set_cnp(cnp)
                    customer_to_add.set_id(index)
                    customer_to_add.set_first_name(first_name)
                    customer_to_add.set_last_name(last_name)
                    customer_to_add.set_phone_number(phone_number)
                    customer_to_add.set_email_address(email_address)
                if self._repo_type == Company:
                    company_name = customer["company_name"]
                    fiscal_no = customer["fiscal_no"]
                    registration_number = customer["registration_number"]
                    customer_to_add = Company()
                    customer_to_add.set_id(index)
                    customer_to_add.set_first_name(first_name)
                    customer_to_add.set_last_name(last_name)
                    customer_to_add.set_phone_number(phone_number)
                    customer_to_add.set_email_address(email_address)
                    customer_to_add.set_company_name(company_name)
                    customer_to_add.set_fiscal_no(fiscal_no)
                    customer_to_add.set_registration_number(registration_number)
                self._list.append(customer_to_add)
        file.close()

    def reset_id(self):
        self._id = 1
