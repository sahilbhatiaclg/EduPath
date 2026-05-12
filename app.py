from flask import Flask, render_template, request, redirect, url_for
from data_handler import PlacementCell
from visualizer import Visualizer

app = Flask(__name__)
placement_cell = PlacementCell()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        name = request.form['name']
        cgpa = float(request.form['cgpa'])
        skills = request.form['skills']
        attendance = float(request.form['attendance'])

        placement_cell.add_student(name, cgpa, skills, attendance)
        message = f"Student '{name}' registered successfully!"

    return render_template('register.html', message=message)

@app.route('/dashboard')
def dashboard():
    students = placement_cell.get_all_students()
    stats = placement_cell.get_statistics()

    # Generate graphs
    visualizer = Visualizer(students)
    visualizer.generate_cgpa_chart()
    visualizer.generate_attendance_chart()
    visualizer.generate_eligibility_pie()

    return render_template('dashboard.html', students=students, stats=stats)

if __name__ == '__main__':
    app.run(debug=True)