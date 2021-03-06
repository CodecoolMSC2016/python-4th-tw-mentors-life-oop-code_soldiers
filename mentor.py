from person import Person
from device import Device


class Mentor(Person):
    def __init__(self, first_name, last_name, year_of_birth, gender, nickname):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = nickname
        self.device = None

    def set_device(self, name, price):
        self.device = Device(name, price)

    @classmethod
    def create_by_csv(cls, file_name):
        with open(file_name, "r") as csv_file:
            lines = csv_file.readlines()
        mentors_list = []
        for line in lines:
            first, last, birth, gender, nickname = line.strip("\n").split(",")
            mentors_list.append(cls(first, last, birth, gender, nickname))
        return mentors_list
