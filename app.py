from flask import Flask, render_template, request
import csv
from student_recommendation import studentrec
app = Flask(__name__)

@app.route('/')
def home():
    student_data = []
    with open('students_data.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student_data.append({'name': row['Name'], 'unique_id': row['unique_id']})
    # print(student_data)
    return render_template('home.html', student_data=student_data)

@app.route('/student/<name>/<unique_id>')
def student_page(name, unique_id):
    print(unique_id)
    rec_id = studentrec(unique_id)
    print(rec_id)
    return render_template('student.html', name=name, unique_id=unique_id, rec_id = rec_id)

if __name__ == '__main__':
    app.run(debug=True)