import pandas as pd
import numpy as np
import csv
import os

CSV_FILE = 'students.csv'

# ─────────────────────────────────────────────
# OOPS: Base Class - Student
# ─────────────────────────────────────────────
class Student:
    def __init__(self, name, cgpa, skills, attendance):
        self.name = name
        self.cgpa = float(cgpa)
        self.skills = skills
        self.attendance = float(attendance)

    def is_eligible(self):
        """Check placement eligibility"""
        return self.cgpa >= 7.0 and self.attendance >= 75.0

    def to_dict(self):
        return {
            'name': self.name,
            'cgpa': self.cgpa,
            'skills': self.skills,
            'attendance': self.attendance,
            'eligible': 'Yes' if self.is_eligible() else 'No'
        }

    def __str__(self):
        return f"Student: {self.name} | CGPA: {self.cgpa} | Attendance: {self.attendance}%"


# ─────────────────────────────────────────────
# OOPS: Inheritance - SpecializedStudent
# ─────────────────────────────────────────────
class SpecializedStudent(Student):
    def __init__(self, name, cgpa, skills, attendance, certifications='', research=''):
        super().__init__(name, cgpa, skills, attendance)
        self.certifications = certifications
        self.research = research

    def to_dict(self):
        data = super().to_dict()
        data['certifications'] = self.certifications
        data['research'] = self.research
        return data


# ─────────────────────────────────────────────
# OOPS: PlacementCell Class - manages all students
# ─────────────────────────────────────────────
class PlacementCell:
    def __init__(self):
        self._ensure_csv()

    # Encapsulation: private method
    def _ensure_csv(self):
        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['name', 'cgpa', 'skills', 'attendance', 'eligible'])
                writer.writeheader()

    def add_student(self, name, cgpa, skills, attendance):
        student = Student(name, cgpa, skills, attendance)
        with open(CSV_FILE, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'cgpa', 'skills', 'attendance', 'eligible'])
            writer.writerow(student.to_dict())

    def get_all_students(self):
        try:
            df = pd.read_csv(CSV_FILE)
            return df.to_dict(orient='records')
        except Exception:
            return []

    def get_eligible_students(self):
        students = self.get_all_students()
        return [s for s in students if s.get('eligible') == 'Yes']

    def filter_by_cgpa(self, min_cgpa):
        students = self.get_all_students()
        return [s for s in students if float(s['cgpa']) >= min_cgpa]

    def get_statistics(self):
        students = self.get_all_students()
        if not students:
            return {}

        df = pd.DataFrame(students)
        cgpa_values = df['cgpa'].astype(float).values
        attendance_values = df['attendance'].astype(float).values

        return {
            'total': len(students),
            'eligible': len(self.get_eligible_students()),
            'avg_cgpa': round(np.mean(cgpa_values), 2),
            'avg_attendance': round(np.mean(attendance_values), 2),
            'max_cgpa': round(np.max(cgpa_values), 2),
            'min_cgpa': round(np.min(cgpa_values), 2),
        }