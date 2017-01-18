from person import Person


class Mentor(Person):
    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, device):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = nickname
        self.device = Device()

    @property
    def fullname(self):
        return self.first_name + " " self.last_name
