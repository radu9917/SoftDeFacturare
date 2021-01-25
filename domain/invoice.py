from domain.bill import Bill


class Invoice(Bill):
    def __init__(self):
        super().__init__()

    def __str__(self):

        string = ("Invoice #" + str(self.get_id()) + "\n")
        string += super().__str__()
        return string
