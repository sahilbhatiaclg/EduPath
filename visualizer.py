import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for Flask
import matplotlib.pyplot as plt
import os

SAVE_DIR = os.path.join('static', 'images')

class Visualizer:
    def __init__(self, students):
        self.students = students
        os.makedirs(SAVE_DIR, exist_ok=True)

    def _get_values(self, key):
        return [float(s[key]) for s in self.students if s.get(key)]

    def _get_names(self):
        return [s['name'] for s in self.students]

    def generate_cgpa_chart(self):
        """Bar chart: Student vs CGPA"""
        names = self._get_names()
        cgpas = self._get_values('cgpa')
        if not names:
            return

        plt.figure(figsize=(8, 4))
        colors = ['#4CAF50' if c >= 7.0 else '#F44336' for c in cgpas]
        plt.bar(names, cgpas, color=colors)
        plt.axhline(y=7.0, color='blue', linestyle='--', label='Eligibility Line (7.0)')
        plt.title('Student CGPA Chart')
        plt.xlabel('Students')
        plt.ylabel('CGPA')
        plt.ylim(0, 10)
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(SAVE_DIR, 'cgpa_chart.png'))
        plt.close()

    def generate_attendance_chart(self):
        """Bar chart: Student vs Attendance"""
        names = self._get_names()
        attendance = self._get_values('attendance')
        if not names:
            return

        plt.figure(figsize=(8, 4))
        colors = ['#2196F3' if a >= 75 else '#FF9800' for a in attendance]
        plt.bar(names, attendance, color=colors)
        plt.axhline(y=75, color='red', linestyle='--', label='Min Attendance (75%)')
        plt.title('Student Attendance Chart')
        plt.xlabel('Students')
        plt.ylabel('Attendance (%)')
        plt.ylim(0, 100)
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(SAVE_DIR, 'attendance_chart.png'))
        plt.close()

    def generate_eligibility_pie(self):
        """Pie chart: Eligible vs Not Eligible"""
        eligible = sum(1 for s in self.students if s.get('eligible') == 'Yes')
        not_eligible = len(self.students) - eligible
        if len(self.students) == 0:
            return

        plt.figure(figsize=(5, 5))
        labels = ['Eligible', 'Not Eligible']
        sizes = [eligible, not_eligible]
        colors = ['#4CAF50', '#F44336']
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title('Placement Eligibility')
        plt.tight_layout()
        plt.savefig(os.path.join(SAVE_DIR, 'eligibility_pie.png'))
        plt.close()