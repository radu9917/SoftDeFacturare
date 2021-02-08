class Bill:
    def __init__(self):
        self.__issuer = None
        self.__customer = None
        self.__issue_date = None
        self.__due_date = None
        self.__items = []
        self.__currency = None
        self.__notes = None
        self.__tax = 0.0
        self.__bill_id = None

    # GETTERS
    def get_id(self):
        return self.__bill_id

    def get_issuer(self):
        return self.__issuer

    def get_customer(self):
        return self.__customer

    def get_issue_date(self):
        return self.__issue_date

    def get_due_date(self):
        return self.__due_date

    def get_items(self):
        return self.__items

    def get_currency(self):
        return self.__currency

    def get_notes(self):
        return self.__notes

    def get_tax(self):
        return self.__tax

    # SETTERS
    def set_id(self, bill_id):
        self.__bill_id = bill_id

    def set_issuer(self, issuer):
        self.__issuer = issuer

    def set_customer(self, customer):
        self.__customer = customer

    def set_issue_date(self, issue_date):
        self.__issue_date = issue_date

    def set_due_date(self, due_date):
        self.__due_date = due_date

    def set_items(self, items):
        self.__items = items

    def set_currency(self, currency):
        self.__currency = currency

    def set_notes(self, notes):
        self.__notes = notes

    def set_tax(self, tax):
        self.__tax = tax

    def __eq__(self, other):
        if self.get_id() != other.get_id():
            return False
        if self.get_currency() != other.get_currency():
            return False
        if self.get_tax() != other.get_tax():
            return False
        if self.get_items() != other.get_items():
            return False
        if self.get_notes() != other.get_notes():
            return False
        if self.get_due_date() != other.get_due_date():
            return False
        if self.get_customer() != other.get_customer():
            return False
        if self.get_issue_date() != other.get_issue_date():
            return False
        if self.get_issuer() != other.get_issuer():
            return False
        return True

    def add_items(self, item_to_add):
        found = False
        for item in self.get_items():
            if item == item_to_add:
                item.increment_quantity()
                found = True
        if not found:
            self.__items.append(item_to_add)
        discount = item_to_add.get_discount()
        price = item_to_add.get_price()
        tax_exchange_rate = self.__currency.get_exchange_rate()
        item_exchange_rate = item_to_add.get_currency().get_exchange_rate()
        if item_to_add.get_percent_discount():
            self.__tax += (price - price * discount / 100) * item_exchange_rate / tax_exchange_rate
        else:
            self.__tax += (price - discount) * item_exchange_rate / tax_exchange_rate

    def __str__(self):
        customer = self.get_customer()
        bill_base = ("\nTo: {first_name}  {last_name} - {customer_email_address}\n"
                  "Issued by: {company_name} - {issuer_email_address}\n"
                  "Date: {issue_date}\n"
                  "Due Date: {due_date}\n"
                  "Items:\n{items}"
                  "Total: {total}{currency_symbol}\nNotes: {notes}\n")
        index = 1

        items = ""
        for item in self.get_items():
            items += item_base.format(
                        index=index,
                        item_name=item.get_name(),
                        item_description=item.get_description(),
                        quantity=item.get_quantity(),
                        price=item.get_price(),
                        currency_symbol=item.get_currency().get_symbol()
                    )

            index += 1
        formated_bill = bill_base.format(
            first_name=customer.get_first_name(),
            last_name=customer.get_last_name(),
            customer_email_address=customer.get_email_address(),
            company_name=self.__issuer.get_company_name(),
            issuer_email_address=self.__issuer.get_email_address(),
            issue_date=self.__issue_date,
            due_date=self.__due_date,
            items=items,
            total=self.__tax,
            currency_symbol=self.__currency.get_symbol(),
            notes=self.__notes
        )

        return formated_bill
