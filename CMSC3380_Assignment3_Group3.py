'''
    CMSC 3380 Group 3 Assignment 3
    John Gerega, Luke Ruffing, Ethan Janovich
    This program is a menu driven program that allows the user to add, remove, and view courses and students using two dictionaries.
    One dictionary is for courses and the other is for students. The program will also allow the user to enroll and unenroll students in courses.
    Any addition or removal of courses or students will be saved to a file using the pickle library.
    The program will conitnue to display the menu option until the user enters 0 to quit the program.
    The program will pull the diictionary data from the file before the user enters any menu options.
    If the file is not found, the program will create a new file and two empty dictionaries.
    If the file is empty, the program will create two empty dictionaries.
'''
#Libraries
import pickle
import os



# Beginning of Function definitons
#add_course function
def add_course(code, name):
    print("Adding a course...")
    global courses
    # Program will try to add the passed in course code and name to the dictionary
    try:
        courses[code] = name

    except KeyError:
        print("Course already exists")


# Remove course function
def remove_course(code):
    global courses
    # If the course code is found in the dictionary, the course will be removed
    if (courses.get(code)):
        print("Removing a course...")
        del courses[code]
    else:
        print("Course not found")


# View all courses function
def view_all_courses():
    print("Viewing all courses...")
    # Prints every course in the dictionary
    global courses
    for key, value in courses.items():
        print(f"{key}: {value}")


# Add student function
def add_student(code, name, major, email):
    print("Adding a student...")
    global students
    # Program will try to add the passed in student ID, name, major, and email to the dictionary
    try:
        students[code] = {"Name": name, "Major": major, "Email": email, "Courses": []}

    except KeyError:
        print("student already exists")


# Remove student function
def remove_student(code):
    global students
    # If the student ID is found in the dictionary, the student will be removed
    if (students.get(code)):
        print("Removing a student...")
        del students[code]
    else:
        print("Student not found")


# View all students function
def view_all_students():
    print("Viewing all students...")
    global students
    # Prints every student in the dictionary
    for key, value in students.items():
        print(f"{key}: {value}")

#enroll student function
def enroll_student(course, student):
    global courses, students
    if (courses.get(course)):  # if course exists
        if (students.get(student)):
            print("Enrolling the student")
            try:
                # Add the course to the student's courses list
                students[student]["Courses"].append(courses[course])
            except KeyError:
                # If the course is not found, print an error message
                print("Error enrolling student")
        else:
            # If the student is not found, print an error message
            print("Student ID does not exist.")
    else:
        # If the course is not found, print an error message
        print("Course does not exist.")

#unenroll student function
def unenroll_student(course, student):
    global courses, students
    if (courses.get(course)):  # if course exists
        if (students.get(student)): # if student exists
            print("Unenrolling a student...")
            try:
                # Remove the course from the student's courses list
                del students[student]["Courses"][students[student]["Courses"].index(courses[course])]
            except KeyError:
                # If the course is not found, print an error message
                print("Error unenrolling student")
        else:
            # If the student is not found, print an error message
            print("Student ID does not exist.")
    else:
        # If the course is not found, print an error message
        print("Course does not exist.")


# List student courses function
def list_student_courses(id):
    global students, courses
    print("Listing student courses...")
    # Traverse the dictionary to find the student ID
    for key, value in students.items():
        if key == id:
            # Once the id is found, print the courses the student is taking
            for course in value["Courses"]:
                # Print the course
                print(f"This student is taking {course}")


def updateFile(file):
    global courses, students
    try:
        # Write the courses and students dictionaries to the file
        pickle.dump(courses, file)
        pickle.dump(students, file)
    except FileNotFoundError:
        print("File not found")


def getInfo(file):
    global courses, students
    try:
        # Load the courses and students dictionaries from the file
        courses = pickle.load(file)
        students = pickle.load(file)
    except EOFError:
        print("File is empty")


# Display menu
def show_menu():
    print("""
    Menu:
    1. Add a course
    2. Remove a course
    3. View all courses
    4. Add a student
    5. Remove a student
    6. View all students
    7. Enroll a student in a course
    8. Unenroll a student from a course
    9. List student courses
    0. Quit
    """)
#End of Function definitions

# Begin of Main program, starting with empty dictionaries
courses={}
students={}
# Try to open the file for reading binary
try:
    f1 = open("CMSC3380_Assignment3_Group3.dat", "rb")  # opens file for reading binary
    getInfo(f1)
    # Print the courses and students dictionaries
    #print("Courses: ", courses)
    #print("Students: ", students) debugging
    f1.close()
    f1 = open("CMSC3380_Assignment3_Group3.dat", "wb")  # opens file for appending binary
    show_menu()  # calls show_menu function to display menu
    user_choice = input("Enter an option from the menu: ")
except (FileNotFoundError, EOFError):  # FileNotFoundError exception, message printed
    print("File not found or is empty, creating said file...")
    f1 = open("CMSC3380_Assignment3_Group3.dat", "wb")  # opens file for writing binary
    # Dictionary definition for courses
    courses = {

    }
    # Dictionary definition for students
    students = {

    }
    show_menu()  # calls show_menu function to display menu
    user_choice = input("Enter an option from the menu: ")

# While loop to keep the program running until the user enters 0
while user_choice != '0':
    # If the user enters 1, call the add_course function
    if user_choice == '1':
        # Get the information needed for the add_course function
        new_course = input("Enter the course code: ")
        new_name = input("Enter the course name: ")
        # Call the add_course function
        add_course(new_course, new_name)

    # If the user enters 2, call the remove_course function
    elif user_choice == '2':
        # Get the course code to be removed, then call the remove_course function
        new_course = input("Enter the course code to be removed: ")
        remove_course(new_course)

    elif user_choice == '3':
        # View all courses function call
        view_all_courses()
    elif user_choice == '4':
        # Get the information needed for the add_student function, then call the function
        new_Id = input("Enter the student ID: ")
        new_name = input("Enter the student name: ")
        new_major = input("Enter the student's major: ")
        new_email = input("Enter the student's email: ")
        add_student(new_Id, new_name, new_major, new_email)

    elif user_choice == '5':
        # Get the student ID to be removed, then call the remove_student function
        new_name = input("Enter the student id to be deleted: ")
        remove_student(new_name)

    elif user_choice == '6':
        # View all students function
        view_all_students()
    elif user_choice == '7':
        # Get the student ID and course ID to enroll the student in, then call the enroll_student function
        student = input("Enter the student's ID to add course: ")
        new_course = input("Enter the course ID to add: ")
        enroll_student(new_course, student)

    elif user_choice == '8':
        # Get the student ID and course ID to unenroll the student from, then call the unenroll_student function
        student = input("Enter the student's ID to remove course: ")
        new_course = input("Enter the course ID to remove: ")
        unenroll_student(new_course, student)

    elif user_choice == '9':
        # Get the student ID to list the courses the student is taking, then call the list_student_courses function
        new_Id = input("Enter the student ID: ")
        list_student_courses(new_Id)
    else:
        # If the user enters an invalid option, print an error message
        print("Invalid input, please enter a valid option")

    # Close the file and reopen it in append binary mode
    input("Press any key to continue...")
    show_menu()  # calls show_menu function to display menu
    user_choice = input("Enter an option from the menu: ")
print("Exiting program...")


pickle.dump(courses, f1)  # writes courses dictionary to file
f1 = open("CMSC3380_Assignment3_Group3.dat", "ab")
pickle.dump(students,f1)

# Close the file, end of program
f1.close()