from flask import Flask, request, jsonify

app = Flask(__name__)

# Student Class
class Student:
    def __init__(self, student_id, first_name, last_name, courses, grades):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.courses = courses
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def update_info(self, first_name=None, last_name=None, courses=None, grades=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if courses is not None:
            self.courses = courses
        if grades is not None:
            self.grades = grades

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "courses": self.courses,
            "grades": self.grades,
            "average_grade": self.average_grade()
        }

# Student Management System Class
class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, first_name, last_name, courses, grades):
        student = Student(student_id, first_name, last_name, courses, grades)
        self.students[student_id] = student

    def get_student(self, student_id):
        return self.students.get(student_id)

    def update_student(self, student_id, first_name=None, last_name=None, courses=None, grades=None):
        student = self.get_student(student_id)
        if student:
            student.update_info(first_name, last_name, courses, grades)

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

    def search_student(self, name):
        found_students = {id: student for id, student in self.students.items() if name.lower() in student.first_name.lower() or name.lower() in student.last_name.lower()}
        return found_students

    def list_students(self, page_size=3, page_number=1):
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        student_ids = list(self.students.keys())
        students_to_display = student_ids[start_index:end_index]
        
        students_info = []
        for student_id in students_to_display:
            student = self.students[student_id]
            students_info.append(student.to_dict())
        
        total_students = len(self.students)
        total_pages = (total_students + page_size - 1) // page_size
        
        return students_info, total_pages

# Initialize Student Management System
sms = StudentManagementSystem()

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    student_id = data['student_id']
    first_name = data['first_name']
    last_name = data['last_name']
    courses = data['courses']
    grades = data['grades']
    
    sms.add_student(student_id, first_name, last_name, courses, grades)
    return jsonify({"message": "Student added successfully."}), 201

@app.route('/students/<student_id>', methods=['GET'])
def view_student(student_id):
    student = sms.get_student(student_id)
    if student:
        return jsonify(student.to_dict())
    return jsonify({"message": "Student not found."}), 404

@app.route('/students/<student_id>/grades', methods=['GET'])
def calculate_grades(student_id):
    student = sms.get_student(student_id)
    if student:
        return jsonify({"average_grade": student.average_grade()})
    return jsonify({"message": "Student not found."}), 404

@app.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    student = sms.get_student(student_id)
    if student:
        sms.update_student(
            student_id,
            data.get('first_name'),
            data.get('last_name'),
            data.get('courses'),
            data.get('grades')
        )
        return jsonify({"message": "Student updated successfully."})
    return jsonify({"message": "Student not found."}), 404

@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = sms.get_student(student_id)
    if student:
        sms.delete_student(student_id)
        return jsonify({"message": "Student deleted successfully."})
    return jsonify({"message": "Student not found."}), 404

# array of same name data
@app.route('/students/search', methods=['GET'])
def search_student():
    name = request.args.get('name')
    found_students = sms.search_student(name)
    if found_students:
        return jsonify([student.to_dict() for student in found_students.values()])
    return jsonify({"message": "No students found."}), 404

@app.route('/students/list', methods=['GET'])
def list_students():
    page_size = int(request.args.get('page_size', 3))
    page_number = int(request.args.get('page_number', 1))
    
    students_info, total_pages = sms.list_students(page_size, page_number)
    
    return jsonify({
        "students": students_info,
        "total_pages": total_pages,
        "page_number": page_number
    })

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)
