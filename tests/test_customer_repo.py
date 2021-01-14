import unittest
from repository.customer_repo import CustomerRepo
from domain.customer import Customer


class TestCustomerRepo(unittest.TestCase):
    def test_customer_repo(self):
        customer = Customer("Ion", "Radu", "ion.radu17@yahoo.com", "0758245170")
        customer.set_id(1)
        customer_repo = CustomerRepo()
        customer_repo.store(customer)
        self.assertEqual(customer_repo.get(1), customer)
        customer2 = Customer("Balan", "Dan", "dan_balan69@gmail.com", "0758653345")
        customer2.set_id(2)
        customer_repo.update(customer, customer2)
        self.assertEqual(customer_repo.get(2), customer2)
        customer_repo.delete(2)
        self.assertEqual(customer_repo.get_all(), [])
