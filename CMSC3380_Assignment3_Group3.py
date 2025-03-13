#Group 3 Assignment 3
# John Gerega, Luke Ruffing, Ethan Janovich

import pickle



def add_course():
    print("Adding a course...")

def remove_course():
    print("Removing a course...")

def view_all_courses():
    print("Viewing all courses...")

def add_student():
    print("Adding a student...")

def remove_student():
    print("Removing a student...")

def view_all_students():
    print("Viewing all students...")

def enroll_student():
    print("Enrolling a student...")

def unenroll_student():
    print("Unenrolling a student...")

def list_student_courses():
    print("Listing student courses...")

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

courses = {
    "CMSC3380": "Python",
}

students = {

}

def add_course(code, name):
    print("Adding a course...")
    try:
        courses[code] = name
        
    except KeyError:
        print("Course already exists")

def remove_course(code):
    print("Removing a course...")
    for code in courses:
        del courses[code]
    else:
        print("Course not found")

def view_all_courses():
    print("Viewing all courses...")
    print(courses)

def add_student():
    print("Adding a student...")

def remove_student():
    print("Removing a student...")

def view_all_students():
    print("Viewing all students...")

def enroll_student():
    print("Enrolling a student...")

def unenroll_student():
    print("Unenrolling a student...")

def list_student_courses():
    print("Listing student courses...")

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


try:
    f1 = open("CMSC3380_Assignment3_Group3.dat", "wb")  #opens file for writing binary
    show_menu()  #calls show_menu function to display menu
    user_choice = input("Enter an option from the menu: ")

    while user_choice != '0':
        if user_choice == '1':
            new_course = input("Enter the course code: ")
            new_name = input("Enter the course name: ")
            add_course(new_course, new_name)
            pickle.dump(courses, f1)  #writes courses dictionary to file
        elif user_choice == '2':
            new_course = input("Enter the course code to be removed: ")
            remove_course(new_course)
            pickle.dump(courses, f1)  #writes courses dictionary to file
        elif user_choice == '3':
            view_all_courses()
        elif user_choice == '4':
            add_student()
        elif user_choice == '5':
            remove_student()
        elif user_choice == '6':
            view_all_students()
        elif user_choice == '7':
            enroll_student()
        elif user_choice == '8':
            unenroll_student()
        elif user_choice == '9':
            list_student_courses()
        else:
            print("Invalid input, please enter a valid option")
        
        show_menu()  #calls show_menu function to display menu
        user_choice = input("Enter an option from the menu: ")
<<<<<<< HEAD
    print("Exiting program...")             
=======
    print("Exiting program...")
             
>>>>>>> 01482c3bf819caecb5a807582c2e3bcc76144fdb
except FileNotFoundError:   #FileNotFoundError exception, message printed
    print("File not found")