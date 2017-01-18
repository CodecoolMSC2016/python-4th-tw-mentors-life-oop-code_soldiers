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
        local_mentors = [Mentor("Imre", "Lindi", 1990, "Male", "Imicsanga"),
                         Mentor("Pál", "Monoczki", 1975, "Male", "Pali")]
        local_students = [Student("László", "Székely-Tóth", 1993, "Male"),
                          Student("Dávid", "Szilágyi", 1993, "Male"),
                          Student("Tamás", "Kenyeres", 1997, "Male")]
        return cls("msc", 2016, local_mentors, local_students)
