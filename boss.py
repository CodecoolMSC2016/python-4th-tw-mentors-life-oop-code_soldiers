from person import Person


class Boss(Person):
    def __init__(self, first_name, last_name, year_of_birth, gender, nickname, salary, anger_level):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = str(nickname)
        self.salary = int(salary)
        self.anger_level = int(anger_level)

    def get_salary(self):
        return "__topsecret__"

    def change_anger_level(self, value):
        self.anger_level += value
