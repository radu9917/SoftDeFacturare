class CurrencyService:
    def __init__(self, currency_repo):
        self.__currency_repo = currency_repo

    def create_currency(self, currency):
        self.__currency_repo.store(currency)

    def delete_currency(self, currency_id):
        self.__currency_repo.delete(int(currency_id))

    def modify_currency(self, old_currency, new_currency):
        self.__currency_repo.update(int(old_currency), new_currency)

    def view_currency(self):
        return self.__currency_repo.get_all()

    def get_currency(self, index):
        return self.__currency_repo.get(index)
