from domain.bill import Bill


class FiscalBill(Bill):
    def __init__(self):
        super().__init__()

    def __str__(self):
        fiscal_bill_base = ("Fiscal Bill # {id}\n{bill}")
        formated_fiscal_bill = fiscal_bill_base.format(id=self.get_id(), bill=super().__str__())
        return formated_fiscal_bill
