from domain.bill import Bill


class FiscalBill(Bill):
    def __init__(self):
        super().__init__()

    def __str__(self):

        string = ("Fiscal Bill #" + str(self.get_bill_id()) + "\n")
        string += super().__str__()
        return string
