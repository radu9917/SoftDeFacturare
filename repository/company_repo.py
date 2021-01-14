from repository.repo_interface import IRepo


class CompanyRepo(IRepo):
    def __init__(self):
        self._list = []

    def store(self, company):
        self._list.append(company)

    def delete(self, index):
        for company in self.get_all():
            if company.get_id() == index:
                self._list.remove(company)

    def get_all(self):
        return self._list

    def get(self, index):
        for company in self.get_all():
            if company.get_id() == index:
                return company

    def update(self, old_company, new_company):
        for company in self.get_all():
            if company.get_id() == old_company.get_id():
                company.set_id(new_company.get_id())
                company.set_company_name(new_company.get_company_name())
                company.set_email_address(new_company.get_email_address())
                company.set_phone_number(new_company.get_phone_number())
                company.set_first_name(new_company.get_first_name())
                company.set_last_name(new_company.get_last_name())
                company.set_fiscal_no(new_company.get_fiscal_no())
                company.set_registration_number(new_company.get_registration_number())
