#AbhishekDungraniMidTerm REST API :CRUD operations for a Student entity such as; ID, Name, and Grade.
from flask import Flask, request, jsonify
app = Flask(__name__)
students = []

class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

@app.route('/students', methods=['GET'])
def get_students():
    student_list = [vars(student) for student in students]
    return jsonify(student_list)

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s.id == id), None)
    if student:
        return jsonify(vars(student))
    else:
        return "Student not found", 404

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student = Student(len(students) + 1, data['name'], data['grade'])
    students.append(student)
    return jsonify(vars(student)), 201

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = next((s for s in students if s.id == id), None)
    if not student:
        return "Student not found", 404
    data = request.get_json()
    student.name = data['name']
    student.grade = data['grade']
    return jsonify(vars(student))

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = next((s for s in students if s.id == id), None)
    if not student:
        return "Student not found", 404
    students.remove(student)
    return "Student deleted", 204

if __name__ == '__main__':
    app.run(debug=True)
