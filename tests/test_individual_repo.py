import unittest
from repository.customer_repo import CustomerRepo
from domain.individual import Individual


class TestIndividualRepo(unittest.TestCase):
    def test_individual_repo(self):
        individual1 = Individual()
        individual1.set_cnp("1991212042312")
        individual1.set_id(1)
        individual1.set_phone_number("0753123487")
        individual1.set_first_name("Petre")
        individual1.set_last_name("Laur")
        individual1.set_email_address("laur.petre68@gmail.com")
        individual_repo = CustomerRepo(Individual)
        individual_repo.store(individual1)
        self.assertEqual(len(individual_repo.get_all()), 1)
        individual2 = Individual()
        individual2.set_cnp("1981216065431")
        individual2.set_last_name("Claurentiu")
        individual2.set_first_name("Petre")
        individual2.set_phone_number("0753123487")
        individual2.set_email_address("laur.petre68@gmail.com")
        individual_repo.update(individual1.get_id(), individual2)
        self.assertEqual(individual2, individual_repo.get(1))
        individual_repo.delete(individual2.get_id())
        self.assertEqual(individual_repo.get_all(), [])
        with self.assertRaises(TypeError):
            individual_repo.store(-1)
# Testare si fara with