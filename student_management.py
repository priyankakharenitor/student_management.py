# Create a Python application that simulates a Student Management System. The system will allow users to:
# Add new students
# View details of students
# Calculate their grades
# Update their information
# Perform various operations on the student records (e.g., search, delete)

# Use UI
# list of students with details(pagination)
# oops concenpts (class based)
# Add new students
def add_student(students, student_id, first_name, last_name, courses, grades):
    student = {
        "first_name": first_name,
        "last_name": last_name,
        "courses": courses,
        "grades": grades
    }
    students[student_id] = student
    print(f"Student {first_name} {last_name} added successfully.")


# View Student Details
def view_student(students, student_id):
    student = students.get(student_id)
    if student:
        print(f"Student ID: {student_id}")
        print(f"Name: {student['first_name']} {student['last_name']}")
        print(f"Courses: {', '.join(student['courses'])}")
        print(f"Grades: {', '.join(map(str, student['grades']))}")
    else:
        print("Student not found.")

# Calculate Student Grades
def calculate_grades(students, student_id):
    student = students.get(student_id)
    if student:
        grades = student["grades"]
        avg_grade = sum(grades) / len(grades) if grades else 0
        print(f"Average Grade for {student['first_name']} {student['last_name']}: {avg_grade:.2f}")
    else:
        print("Student not found.")

# Update Student Information
def update_student(students, student_id, first_name=None, last_name=None, courses=None, grades=None):
    student = students.get(student_id)
    if student:
        if first_name:
            student["first_name"] = first_name
        if last_name:
            student["last_name"] = last_name
        if courses:
            student["courses"] = courses
        if grades:
            student["grades"] = grades
        print(f"Student {student_id} updated successfully.")
    else:
        print("Student not found.")

# Delete Student Record
def delete_student(students, student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student with ID {student_id} deleted successfully.")
    else:
        print("Student not found.")

# Search Student by Name
def search_student(students, name):
    found_students = {id: student for id, student in students.items() if name.lower() in student['first_name'].lower() or name.lower() in student['last_name'].lower()}
    if found_students:
        for student_id, student in found_students.items():
            print(f"ID: {student_id} | Name: {student['first_name']} {student['last_name']}")
    else:
        print("No student found with that name.")

def display_menu():
    print("\n--- Student Management System ---")
    print("1. Add New Student")
    print("2. View Student Details")
    print("3. Calculate Student Grades")
    print("4. Update Student Information")
    print("5. Delete Student Record")
    print("6. Search Student by Name")
    print("7. Exit")

def main():
    students = {}  # In-memory student storage
    
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
            add_student(students, student_id, first_name, last_name, courses, grades)
        
        # View Student Details
        elif choice == "2":
            student_id = input("Enter Student ID to view: ")
            view_student(students, student_id)
        
        # Calculate Student Grades
        elif choice == "3":
            student_id = input("Enter Student ID to calculate grades: ")
            calculate_grades(students, student_id)
        
        # Update Student Information
        elif choice == "4":
            student_id = input("Enter Student ID to update: ")
            print("Leave blank if no change is required.")
            first_name = input("Enter New First Name: ") or None
            last_name = input("Enter New Last Name: ") or None
            courses = input("Enter New Courses (comma separated): ").split(',') or None
            grades = input("Enter New Grades (comma separated): ").split(',') or None
            grades = [int(grade) for grade in grades] if grades and grades[0] else None
            update_student(students, student_id, first_name, last_name, courses, grades)
        
        # Delete Student Record
        elif choice == "5":
            student_id = input("Enter Student ID to delete: ")
            delete_student(students, student_id)
        
        # Search Student by Name
        elif choice == "6":
            name = input("Enter name to search: ")
            search_student(students, name)
        
        elif choice == "7":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
