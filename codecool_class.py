from mentor import Mentor
from student import Student


class CodecoolClass:
    def __init__(self, location, year, mentors, students):
        self.location = str(location)
        self.year = int(year)
        self.mentors = list(mentors)
        self.students = list(students)

    @staticmethod
    def _search(db, full_name):
        for person in db:
            if person.fullname.casefold() == full_name.casefold():
                return person
        return None

    def find_mentor_by_full_name(self, full_name):
        return self._search(self.mentors, full_name)

    def find_student_by_full_name(self, full_name):
        return self._search(self.students, full_name)

    @classmethod
    def generate_local(cls):
        local_students = [Student("László", "Székely-Tóth", 1993, "Male", 80, 10),
                          Student("Dávid", "Szilágyi", 1993, "Male", 80, 60),
                          Student("Tamás", "Kenyeres", 1997, "Male", 80, 10)]
        return cls("msc", 2016, Mentor.create_by_csv("data/mentors.csv"),
                   local_students + Student.create_by_csv("data/students.csv"))
