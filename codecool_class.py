from mentor import Mentor
from student import Student


class CodecoolClass:
    def __init__(self, location, year, mentors, students):
        self.location = str(location)
        self.year = int(year)
        self.mentors = list(mentors)
        self.students = list(students)

    def find_student_by_full_name(self, full_name):
        for student in self.students:
            if student.fullname.casefold() == full_name.casefold():
                return student
        return None

    @classmethod
    def generate_local(cls):
        local_mentors = [Mentor("Imre", "Lindi", 1990, "Male", "Imicsanga"),
                         Mentor("Pál", "Monoczki", 1975, "Male", "Pali")]
        local_students = [Student("László", "Székely-Tóth", 1993, "Male"),
                          Student("Dávid", "Szilágyi", 1993, "Male")]
        return cls("msc", 2016, local_mentors, local_students)
