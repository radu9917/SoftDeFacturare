import unittest
from domain.individual import Individual
import copy


class TestIndividualDomain(unittest.TestCase):
    def test_cnp_getter_and_setter(self):
        individual = Individual()
        individual.set_cnp("1991007032565")
        self.assertEqual(individual.get_cnp(), "1991007032565")
        individual.set_cnp("1980923032456")
        self.assertEqual(individual.get_cnp(), "1980923032456")

    def test_equal(self):
        individual = Individual()
        individual.set_cnp("1991007032565")
        individual2 = copy.deepcopy(individual)
        individual2.set_cnp("1980923032456")
        self.assertNotEqual(individual2, individual)
