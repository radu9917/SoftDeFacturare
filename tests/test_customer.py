import unittest
from domain.customer import Customer
from domain.address import Address
import copy


class TestCustomerDomain(unittest.TestCase):
    def test_customer_getters(self):
        address = Address()
        address.set_address("Strada Academiei nr. 7")
        address.set_county("Bucuresti")
        address.set_country("Romania")
        address.set_postal_code("010011")
        customer = Customer("Ion", "Radu", "ion.radu17@yahoo.com", "0758245170", address)
        self.assertEqual(customer.get_first_name(), "Ion")
        self.assertEqual(customer.get_last_name(), "Radu")
        self.assertEqual(customer.get_email_address(), "ion.radu17@yahoo.com")
        self.assertEqual(customer.get_phone_number(), "0758245170")
        self.assertEqual(customer.get_address(), address)

    def test_customer_setters(self):
        address = Address()
        address.set_address("Strada Academiei nr. 7")
        address.set_county("Bucuresti")
        address.set_country("Romania")
        address.set_postal_code("010011")
        customer = Customer(None, None, None, None, None)
        customer.set_first_name("Ion")
        customer.set_last_name("Radu")
        customer.set_email_address("ion.radu17@yahoo.com")
        customer.set_phone_number("0758245170")
        customer.set_address(address)
        self.assertEqual(customer.get_first_name(), "Ion")
        self.assertEqual(customer.get_last_name(), "Radu")
        self.assertEqual(customer.get_email_address(), "ion.radu17@yahoo.com")
        self.assertEqual(customer.get_phone_number(), "0758245170")
        self.assertEqual(customer.get_address(),address)

    def test_equal(self):
        address = Address()
        address.set_address("Strada Academiei nr. 7")
        address.set_county("Bucuresti")
        address.set_country("Romania")
        address.set_postal_code("010011")
        customer = Customer("Ion", "Radu", "ion.radu17@yahoo.com", "0758245170", address)
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
