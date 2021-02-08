from domain.bill import Bill


class Invoice(Bill):
    def __init__(self):
        super().__init__()

    def __str__(self):
        invoice_base = ("Invoice # {id}\n{bill}")
        formated_invoice = invoice_base.format(id=self.get_id(), bill=super().__str__())
        return formated_invoice
