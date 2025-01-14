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

    def view_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Courses: {', '.join(self.courses)}")
        print(f"Grades: {', '.join(map(str, self.grades))}")

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, first_name, last_name, courses, grades):
        student = Student(student_id, first_name, last_name, courses, grades)
        self.students[student_id] = student
        print(f"Student {first_name} {last_name} added successfully.")

    def view_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            student.view_details()
        else:
            print("Student not found.")

    def calculate_grades(self, student_id):
        student = self.students.get(student_id)
        if student:
            avg_grade = student.average_grade()
            print(f"Average Grade for {student.first_name} {student.last_name}: {avg_grade:.2f}")
        else:
            print("Student not found.")

    def update_student(self, student_id, first_name=None, last_name=None, courses=None, grades=None):
        student = self.students.get(student_id)
        if student:
            student.update_info(first_name, last_name, courses, grades)
            print(f"Student {student_id} updated successfully.")
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with ID {student_id} deleted successfully.")
        else:
            print("Student not found.")

    def search_student(self, name):
        found_students = {id: student for id, student in self.students.items() if name.lower() in student.first_name.lower() or name.lower() in student.last_name.lower()}
        if found_students:
            for student_id, student in found_students.items():
                print(f"ID: {student_id} | Name: {student.first_name} {student.last_name}")
        else:
            print("No student found with that name.")

    # New functionality to list all students
    def list_all_students(self):
        if self.students:
            print("\n--- All Students ---")
            for student_id, student in self.students.items():
                print(f"ID: {student_id} | Name: {student.first_name} {student.last_name} | Courses: {', '.join(student.courses)}")
        else:
            print("No students found in the system.")

def display_menu():
    print("\n--- Student Management System ---")
    print("1. Add New Student")
    print("2. View Student Details")
    print("3. Calculate Student Grades")
    print("4. Update Student Information")
    print("5. Delete Student Record")
    print("6. Search Student by Name")
    print("7. List All Students")  # New option for listing all students
    print("8. Exit")

def main():
    system = StudentManagementSystem()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        # Add New Student
        if choice == "1":
            student_id = input("Enter Student ID: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            courses = input("Enter Courses (comma separated): ").split(',')
            grades = list(map(int, input("Enter Grades (comma separated): ").split(',')))
            system.add_student(student_id, first_name, last_name, courses, grades)
        
        # View Student Details
        elif choice == "2":
            student_id = input("Enter Student ID to view: ")
            system.view_student(student_id)
        
        # Calculate Student Grades
        elif choice == "3":
            student_id = input("Enter Student ID to calculate grades: ")
            system.calculate_grades(student_id)
        
        # Update Student Information
        elif choice == "4":
            student_id = input("Enter Student ID to update: ")
            print("Leave blank if no change is required.")
            first_name = input("Enter New First Name: ") or None
            last_name = input("Enter New Last Name: ") or None
            courses = input("Enter New Courses (comma separated): ").split(',') or None
            grades_input = input("Enter New Grades (comma separated): ").split(',')
            grades = [int(grade) for grade in grades_input if grade] if grades_input else None
            system.update_student(student_id, first_name, last_name, courses, grades)
        
        # Delete Student Record
        elif choice == "5":
            student_id = input("Enter Student ID to delete: ")
            system.delete_student(student_id)
        
        # Search Student by Name
        elif choice == "6":
            name = input("Enter name to search: ")
            system.search_student(name)

        # List All Students
        elif choice == "7":
            system.list_all_students()
        
        elif choice == "8":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
