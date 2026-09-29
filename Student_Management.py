students = []
courses = []
marks = {}

def input_students():
    number_students = int(input("Enter number of students in the class: "))
    for i in range(number_students):
        student_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth: ")
        students.append({"id": student_id, "name": name, "dob": dob})
        print("---")

def input_courses():
    number_courses = int(input("Enter number of courses: "))
    for i in range(number_courses):
        course_id = input("Course ID: ")
        name = input("Course Name: ")
        courses.append({"id": course_id, "name": name})
        print("---")

def input_marks():
    course_id = input("Select a course ID to input marks: ")
    marks[course_id] = {}
    
    print("Enter marks for each student:")
    for student in students:
        mark = float(input(f"- {student['name']} (ID: {student['id']}): "))
        marks[course_id][student['id']] = mark
    print("---")

def list_courses():
    print("\n--- List of Courses ---")
    for course in courses:
        print(f"ID: {course['id']} | Name: {course['name']}")

def list_students():
    print("\n--- List of Students ---")
    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | DoB: {student['dob']}")

def show_marks():
    course_id = input("Enter course ID to view marks: ")
    if course_id in marks:
        print(f"\n--- Marks for Course ID: {course_id} ---")
        for student in students:
            s_id = student['id']
            if s_id in marks[course_id]:
                print(f"{student['name']}: {marks[course_id][s_id]}")
    else:
        print("No marks recorded for this course yet.")

if __name__ == "__main__":
    while True:
        print("\n1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_marks()
        elif choice == '0':
            break
        else:
            print("Invalid choice, try again.")