import unittest
from repository.individual_repo import IndividualRepo
from domain.individual import Individual


class TestIndividualRepo(unittest.TestCase):
    def test_individual_repo(self):
        individual1= Individual("1991212042312")
        individual1.set_id(1)
        individual1.set_phone_number("0753123487")
        individual1.set_first_name("Petre")
        individual1.set_last_name("Laur")
        individual1.set_email_address("laur.petre68@gmail.com")
        individual_repo = IndividualRepo()
        individual_repo.store(individual1)
        self.assertEqual(len(individual_repo.get_all()), 1)
        individual2 = Individual("1981216065431")
        individual2.set_id(2)
        individual2.set_last_name("Claurentiu")
        individual2.set_first_name("Petre")
        individual2.set_phone_number("0753123487")
        individual2.set_email_address("laur.petre68@gmail.com")
        individual_repo.update(individual1, individual2)
        self.assertEqual(individual2, individual_repo.get(2))
        individual_repo.delete(2)
        self.assertEqual(individual_repo.get_all(), [])