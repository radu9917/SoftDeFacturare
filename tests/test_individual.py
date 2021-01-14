import unittest
from domain.individual import Individual


class TestIndividualDomain(unittest.TestCase):
    def test_cnp_getter_and_setter(self):
        individual = Individual("1991007032565")
        self.assertEqual(individual.get_cnp(), "1991007032565")
        individual.set_cnp("1980923032456")
        self.assertEqual(individual.get_cnp(), "1980923032456")