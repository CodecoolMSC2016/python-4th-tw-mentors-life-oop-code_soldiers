from person import Person
from device import Device


class Student(Person):
    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level, energy_level):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.knowledge_level = int(knowledge_level)
        self.energy_level = int(energy_level)
        self.laptop = None

    def set_device(self, name, price):
        self.laptop = Device(name, price)

    @classmethod
    def create_by_csv(cls, file_name):
        with open(file_name, "r") as csv_file:
            lines = csv_file.readlines()
        students_list = []
        for line in lines:
            first, last, birth, gender, knowledge_level, energy_level = line.strip("\n").split(",")
            students_list.append(cls(first, last, birth, gender, knowledge_level, energy_level))
        return students_list
