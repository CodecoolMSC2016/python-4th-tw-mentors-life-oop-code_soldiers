from mentor import Mentor
from student import Student


class CodecoolClass:
    def __init__(self, location, year, mentors, students):
        self.location = str(location)
        self.year = int(year)
        self.mentors = list(mentors)
        self.students = list(students)

    def find_student_by_full_name(self, full_name):
        # TODO: implement thi$
        pass

    @classmethod
    def generate_local(cls):
        local_mentors = []
        local_students = []
        return cls("msc", 2016, local_mentors, local_students)
