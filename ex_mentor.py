from mentor import Mentor


class Ex_Mentor(Mentor):
    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, device):
        super().__init__(first_name, last_name, year_of_birth, gender, nickname, device)
        self.alcohol_level = 0

    def set_alcohol_level(self, amount):
        self.alcohol_level += amount

    def cry(self):
        for count in range(self.alcohol_level):
            print("Brühühü")
