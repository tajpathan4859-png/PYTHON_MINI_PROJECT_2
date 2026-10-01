# ============================================================
# STUDENT RECORD AND ACADEMIC MANAGEMENT SYSTEM
# Data Organization using Python Collections
# ============================================================

# Dictionary to store all student profiles
students = {}

# Set to store unique departments
departments = set()

# Set to store unique subjects
subjects_set = set()

# Set to store student clubs
clubs = set()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_non_empty_input(message):
    """Get a non-empty string from the user."""
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_positive_integer(message):
    """Get a positive integer."""
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Please enter a positive number.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_mark(message):
    """Get marks between 0 and 100."""
    while True:
        try:
            mark = float(input(message))

            if 0 <= mark <= 100:
                return mark

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Invalid marks. Please enter a number.")


def get_attendance(message):
    """Get attendance percentage between 0 and 100."""
    while True:
        try:
            attendance = float(input(message))

            if 0 <= attendance <= 100:
                return attendance

            print("Attendance must be between 0 and 100.")

        except ValueError:
            print("Invalid attendance. Please enter a number.")


def display_student(student):
    """Display complete student information."""

    print("\n" + "=" * 60)
    print("STUDENT PROFILE")
    print("=" * 60)

    print("Roll Number       :", student["roll_number"])
    print("Registration No.  :", student["registration_number"])
    print("Name              :", student["name"])
    print("Department        :", student["department"])
    print("Date of Birth     :", student["date_of_birth"])

    print("Subjects          :", ", ".join(student["subjects"]))

    print("Marks:")
    for subject, mark in student["marks"].items():
        print("   ", subject, ":", mark)

    print("Attendance        :", student["attendance"], "%")

    print("Address           :", student["contact"]["address"])
    print("Email             :", student["contact"]["email"])
    print("Phone             :", student["contact"]["phone"])

    print("Club              :", student["club"])

    print("=" * 60)


# ============================================================
# ADD STUDENT
# ============================================================

def add_student():

    print("\n")
    print("=" * 60)
    print("ADD NEW STUDENT")
    print("=" * 60)

    roll_number = get_positive_integer("Enter Roll Number: ")

    # Duplicate record testing
    if roll_number in students:
        print("A student with this roll number already exists.")
        return

    registration_number = get_non_empty_input(
        "Enter Registration Number: "
    )

    name = get_non_empty_input(
        "Enter Student Name: "
    )

    department = get_non_empty_input(
        "Enter Department: "
    )

    date_of_birth = get_non_empty_input(
        "Enter Date of Birth: "
    )

    address = get_non_empty_input(
        "Enter Address: "
    )

    email = get_non_empty_input(
        "Enter Email ID: "
    )

    phone = get_non_empty_input(
        "Enter Phone Number: "
    )

    club = get_non_empty_input(
        "Enter Student Club: "
    )

    number_of_subjects = get_positive_integer(
        "Enter Number of Subjects: "
    )

    subject_list = []
    marks = {}

    for i in range(number_of_subjects):

        subject = get_non_empty_input(
            f"Enter Subject {i + 1}: "
        )

        # Avoid duplicate subject
        while subject in subject_list:
            print("Subject already entered.")
            subject = get_non_empty_input(
                f"Enter Subject {i + 1}: "
            )

        mark = get_mark(
            f"Enter Marks for {subject}: "
        )

        subject_list.append(subject)
        marks[subject] = mark

        subjects_set.add(subject)

    attendance = get_attendance(
        "Enter Attendance Percentage: "
    )

    # Tuple: Roll number
    roll_tuple = (roll_number,)

    # Tuple: Registration number
    registration_tuple = (registration_number,)

    # Tuple: Date of birth
    dob_tuple = (date_of_birth,)

    # Dictionary: Complete student profile
    student = {

        "roll_number": roll_tuple[0],

        "registration_number": registration_tuple[0],

        "name": name,

        "department": department,

        "date_of_birth": dob_tuple[0],

        # List
        "subjects": subject_list,

        # Dictionary
        "marks": marks,

        # Attendance
        "attendance": attendance,

        # Contact information dictionary
        "contact": {
            "address": address,
            "email": email,
            "phone": phone
        },

        # String
        "club": club
    }

    students[roll_number] = student

    departments.add(department)
    clubs.add(club)

    print("\nStudent record added successfully!")


# ============================================================
# SEARCH STUDENT
# ============================================================

def search_student():

    print("\n")
    print("=" * 60)
    print("SEARCH STUDENT")
    print("=" * 60)

    roll_number = get_positive_integer(
        "Enter Roll Number to Search: "
    )

    if roll_number in students:
        display_student(students[roll_number])
    else:
        print("Student record not found.")


# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student():

    print("\n")
    print("=" * 60)
    print("UPDATE STUDENT RECORD")
    print("=" * 60)

    roll_number = get_positive_integer(
        "Enter Roll Number to Update: "
    )

    if roll_number not in students:
        print("Student record not found.")
        return

    student = students[roll_number]

    print("\nCurrent Student Details:")
    display_student(student)

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Department")
    print("3. Address")
    print("4. Email")
    print("5. Phone")
    print("6. Attendance")
    print("7. Marks")
    print("8. Student Club")
    print("9. Date of Birth")
    print("10. Registration Number")

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        student["name"] = get_non_empty_input(
            "Enter New Name: "
        )

    elif choice == "2":

        student["department"] = get_non_empty_input(
            "Enter New Department: "
        )

        departments.add(student["department"])

    elif choice == "3":

        student["contact"]["address"] = get_non_empty_input(
            "Enter New Address: "
        )

    elif choice == "4":

        student["contact"]["email"] = get_non_empty_input(
            "Enter New Email: "
        )

    elif choice == "5":

        student["contact"]["phone"] = get_non_empty_input(
            "Enter New Phone: "
        )

    elif choice == "6":

        student["attendance"] = get_attendance(
            "Enter New Attendance: "
        )

    elif choice == "7":

        print("\nSubjects:")

        for index, subject in enumerate(
            student["subjects"], start=1
        ):
            print(index, ".", subject)

        subject = get_non_empty_input(
            "Enter Subject Name to Update Marks: "
        )

        if subject in student["marks"]:

            student["marks"][subject] = get_mark(
                f"Enter New Marks for {subject}: "
            )

        else:
            print("Subject not found.")

    elif choice == "8":

        student["club"] = get_non_empty_input(
            "Enter New Club: "
        )

        clubs.add(student["club"])

    elif choice == "9":

        student["date_of_birth"] = get_non_empty_input(
            "Enter New Date of Birth: "
        )

    elif choice == "10":

        student["registration_number"] = get_non_empty_input(
            "Enter New Registration Number: "
        )

    else:

        print("Invalid choice.")
        return

    print("\nStudent record updated successfully!")


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student():

    print("\n")
    print("=" * 60)
    print("DELETE STUDENT RECORD")
    print("=" * 60)

    roll_number = get_positive_integer(
        "Enter Roll Number to Delete: "
    )

    if roll_number not in students:
        print("Student record not found.")
        return

    display_student(students[roll_number])

    confirmation = input(
        "\nAre you sure you want to delete this record? (yes/no): "
    ).lower()

    if confirmation == "yes":

        del students[roll_number]

        print("Student record deleted successfully.")

    else:

        print("Delete operation cancelled.")


# ============================================================
# DISPLAY ALL STUDENTS
# ============================================================

def display_all_students():

    print("\n")
    print("=" * 60)
    print("ALL STUDENT RECORDS")
    print("=" * 60)

    if not students:
        print("No student records available.")
        return

    for roll_number, student in students.items():

        display_student(student)


# ============================================================
# CALCULATE AVERAGE MARKS
# ============================================================

def calculate_average():

    print("\n")
    print("=" * 60)
    print("CALCULATE AVERAGE MARKS")
    print("=" * 60)

    roll_number = get_positive_integer(
        "Enter Roll Number: "
    )

    if roll_number not in students:
        print("Student record not found.")
        return

    student = students[roll_number]

    marks = student["marks"]

    if not marks:
        print("No marks available.")
        return

    total = sum(marks.values())

    average = total / len(marks)

    print("\nStudent Name :", student["name"])
    print("Total Marks  :", total)
    print("Average Marks:", round(average, 2))


# ============================================================
# FIND HIGHEST SCORER
# ============================================================

def highest_scorer():

    print("\n")
    print("=" * 60)
    print("HIGHEST SCORER")
    print("=" * 60)

    if not students:
        print("No student records available.")
        return

    highest_student = None
    highest_average = -1

    for student in students.values():

        marks = student["marks"]

        if marks:

            average = sum(marks.values()) / len(marks)

            if average > highest_average:

                highest_average = average
                highest_student = student

    if highest_student:

        print("\nHighest Scorer:")

        print("Name       :", highest_student["name"])
        print(
            "Roll Number:",
            highest_student["roll_number"]
        )
        print(
            "Department :",
            highest_student["department"]
        )
        print(
            "Average    :",
            round(highest_average, 2)
        )


# ============================================================
# LIST STUDENTS BY DEPARTMENT
# ============================================================

def students_by_department():

    print("\n")
    print("=" * 60)
    print("STUDENTS BY DEPARTMENT")
    print("=" * 60)

    if not students:
        print("No student records available.")
        return

    department = get_non_empty_input(
        "Enter Department: "
    )

    found = False

    for student in students.values():

        if student["department"].lower() == department.lower():

            print(
                "\nRoll Number:",
                student["roll_number"]
            )

            print(
                "Name:",
                student["name"]
            )

            print(
                "Department:",
                student["department"]
            )

            found = True

    if not found:

        print(
            "No students found in this department."
        )


# ============================================================
# COUNT STUDENTS
# ============================================================

def count_students():

    print("\n")
    print("=" * 60)
    print("STUDENT COUNT")
    print("=" * 60)

    print(
        "Total Number of Students:",
        len(students)
    )


# ============================================================
# DISPLAY DEPARTMENTS
# ============================================================

def display_departments():

    print("\n")
    print("=" * 60)
    print("AVAILABLE DEPARTMENTS")
    print("=" * 60)

    if not departments:

        print("No departments available.")
        return

    for department in sorted(departments):

        print("-", department)


# ============================================================
# DISPLAY SUBJECTS
# ============================================================

def display_subjects():

    print("\n")
    print("=" * 60)
    print("AVAILABLE SUBJECTS")
    print("=" * 60)

    if not subjects_set:

        print("No subjects available.")
        return

    for subject in sorted(subjects_set):

        print("-", subject)


# ============================================================
# DISPLAY CLUBS
# ============================================================

def display_clubs():

    print("\n")
    print("=" * 60)
    print("STUDENT CLUBS")
    print("=" * 60)

    if not clubs:

        print("No clubs available.")
        return

    for club in sorted(clubs):

        print("-", club)


# ============================================================
# GENERATE REPORT
# ============================================================

def generate_report():

    print("\n")
    print("=" * 60)
    print("ACADEMIC REPORT")
    print("=" * 60)

    if not students:

        print("No student records available.")
        return

    print(
        "Total Students:",
        len(students)
    )

    print(
        "Total Departments:",
        len(departments)
    )

    print(
        "Total Subjects:",
        len(subjects_set)
    )

    print(
        "Total Clubs:",
        len(clubs)
    )

    print("\nStudent Academic Summary")
    print("-" * 60)

    for student in students.values():

        marks = student["marks"]

        if marks:

            average = sum(
                marks.values()
            ) / len(marks)

        else:

            average = 0

        print(
            "Roll:",
            student["roll_number"],
            "| Name:",
            student["name"],
            "| Department:",
            student["department"],
            "| Average:",
            round(average, 2)
        )


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 60)
        print(" STUDENT RECORD AND ACADEMIC MANAGEMENT SYSTEM")
        print("=" * 60)

        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Calculate Average Marks")
        print("7. Find Highest Scorer")
        print("8. List Students by Department")
        print("9. Count Students")
        print("10. Display Departments")
        print("11. Display Subjects")
        print("12. Display Student Clubs")
        print("13. Generate Academic Report")
        print("14. Exit")

        print("=" * 60)

        choice = input(
            "Enter your choice (1-14): "
        ).strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            search_student()

        elif choice == "3":

            update_student()

        elif choice == "4":

            delete_student()

        elif choice == "5":

            display_all_students()

        elif choice == "6":

            calculate_average()

        elif choice == "7":

            highest_scorer()

        elif choice == "8":

            students_by_department()

        elif choice == "9":

            count_students()

        elif choice == "10":

            display_departments()

        elif choice == "11":

            display_subjects()

        elif choice == "12":

            display_clubs()

        elif choice == "13":

            generate_report()

        elif choice == "14":

            print("\nThank you for using the Student Management System.")
            print("Program terminated successfully.")

            break

        else:

            print(
                "Invalid choice. Please select between 1 and 14."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
