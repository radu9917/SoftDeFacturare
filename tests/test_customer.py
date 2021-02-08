import unittest
from domain.customer import Customer
import copy


class TestCustomerDomain(unittest.TestCase):
    def test_customer_getters(self):
        customer = Customer("Ion", "Radu", "ion.radu17@yahoo.com", "0758245170")
        self.assertEqual(customer.get_first_name(), "Ion")
        self.assertEqual(customer.get_last_name(), "Radu")
        self.assertEqual(customer.get_email_address(), "ion.radu17@yahoo.com")
        self.assertEqual(customer.get_phone_number(), "0758245170")

    def test_customer_setters(self):
        customer = Customer(None, None, None, None)
        customer.set_first_name("Ion")
        customer.set_last_name("Radu")
        customer.set_email_address("ion.radu17@yahoo.com")
        customer.set_phone_number("0758245170")
        self.assertEqual(customer.get_first_name(), "Ion")
        self.assertEqual(customer.get_last_name(), "Radu")
        self.assertEqual(customer.get_email_address(), "ion.radu17@yahoo.com")
        self.assertEqual(customer.get_phone_number(), "0758245170")

    def test_equal(self):
        customer = Customer("Ion", "Radu", "ion.radu17@yahoo.com", "0758245170")
        customer2 = copy.deepcopy(customer)
        customer.set_id(1)
        customer2.set_id(2)
        self.assertNotEqual(customer, customer2)
        customer2.set_id(1)
        customer2.set_last_name("Dan")
        self.assertNotEqual(customer, customer2)
        customer2.set_last_name(customer.get_last_name())
        customer2.set_first_name("Pop")
        self.assertNotEqual(customer, customer2)
        customer2.set_first_name(customer.get_first_name())
        customer2.set_email_address("isk")
        self.assertNotEqual(customer, customer2)
        customer2.set_email_address(customer.get_email_address())
        customer2.set_phone_number("dokf")
        self.assertNotEqual(customer, customer2)