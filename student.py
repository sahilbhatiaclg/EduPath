class Student:

    def __init__(self, name, roll, cgpa, attendance, skills):

        self.name = name
        self.roll = roll
        self.cgpa = cgpa
        self.attendance = attendance
        self.skills = skills

    def check_eligibility(self):

        if self.cgpa >= 7 and self.attendance >= 75:
            return True

        return False


class SpecializedStudent(Student):

    def __init__(self, name, roll, cgpa, attendance, skills, certification):

        super().__init__(name, roll, cgpa, attendance, skills)

        self.certification = certification


class PlacementCell:

    def __init__(self):

        self.students = []

    def add_student(self, student):

        self.students.append(student)

    def display_students(self):

        return self.students