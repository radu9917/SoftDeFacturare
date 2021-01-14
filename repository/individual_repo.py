from repository.repo_interface import IRepo


class IndividualRepo(IRepo):
    def __init__(self):
        self._list = []

    def store(self, individual):
        self._list.append(individual)

    def get(self, individual_id):
        for individual in self.get_all():
            if individual.get_id() == individual_id:
                return individual

    def get_all(self):
        return self._list

    def delete(self, individual_id):
        for individual in self.get_all():
            if individual.get_id() == individual_id:
                self._list.remove(individual)

    def update(self, old_individual, new_individual):
        for individual in self.get_all():
            if individual.get_id() == old_individual.get_id():
                individual.set_id(new_individual.get_id())
                individual.set_last_name(new_individual.get_last_name())
                individual.set_first_name(new_individual.get_first_name())
                individual.set_email_address(new_individual.get_email_address())
                individual.set_phone_number(new_individual.get_phone_number())
                individual.set_cnp(new_individual.get_cnp())
