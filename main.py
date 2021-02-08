from console.console import Console


def main():
    console = Console("database/currency.json", "database/item.json", "database/customer.json", "database/bill.json")
    console.run()

    
main()
