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
        item = None
        for index in self.get_items():
            if index[0] == item_to_add:
                item = (item_to_add, index[1] + 1)
                found = True
                self.__items.remove(index)
        if not found:
            item = (item_to_add, 1)
        self.__items.append(item)
        discount = item_to_add.get_discount()
        price = item_to_add.get_price()
        tax_exchange_rate = self.__currency.get_exchange_rate()
        item_exchange_rate = item_to_add.get_currency().get_exchange_rate()
        if item_to_add.get_percent_discount():
            self.__tax += (price - price * discount / 100) / item_exchange_rate * tax_exchange_rate
        else:
            self.__tax += (price - discount) / item_exchange_rate * tax_exchange_rate

    def __str__(self):
        customer = self.get_customer()
        string = ("To: " + customer.get_first_name() + " " + customer.get_last_name())
        string += (" " + customer.get_email_address() + " ")
        string += "\n"
        string += ("Issued by:" + self.get_issuer().get_company_name() + " " + self.get_issuer().get_email_address())
        string += "\n"
        string += ("Date:" + self.get_issue_date() + "\n")
        string += ("Due Date:" + self.get_due_date() + "\n")
        string += "Items:\n"
        index = 1
        for item in self.get_items():
            string += (str(index) + ". ")
            string += (item.get_name() + " - " + item.get_description() + " - " + str(item.get_quantity()) + "x" +
                       str(item.get_price()) + item.get_currency().get_symbol())
            string += "\n"
            index += 1
        string += ("Total: " + str(self.get_tax()) + self.get_currency().get_symbol())
        string += "\n"
        string += ("Notes:" + self.get_notes())
        return string
