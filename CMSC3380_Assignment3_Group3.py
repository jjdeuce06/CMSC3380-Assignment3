# Group 3 Assignment 3
# John Gerega, Luke Ruffing, Ethan Janovich

import pickle
import os


courses = {
    "CMSC3380": "Python",

}

students = {
    "P11019816": {"Name":"Ethan Janovich", "Major":"Computer Science","Email":"jan60248@pennwest.edu", "Courses":["Python"]},

}


def add_course(code, name):
    print("Adding a course...")
    try:
        courses[code] = name

    except KeyError:
        print("Course already exists")


def remove_course(code):

    if(courses.get(code)):
        print("Removing a course...")
        del courses[code]
    else:
        print("Course not found")


def view_all_courses():
    print("Viewing all courses...")
    for key, value in courses.items():
        print(f"{key}: {value}")


def add_student(code, name, major, email):
    print("Adding a student...")

    try:
        students[code]={"Name":name, "Major": major,"Email":email}

    except KeyError:
        print("student already exists")


def remove_student(code):
    if (students.get(code)):
        print("Removing a student...")
        del students[code]
    else:
        print("Student not found")


def view_all_students():
    print("Viewing all students...")
    for key, value in students.items():
        print(f"{key}: {value}")


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
    f1 = open("CMSC3380_Assignment3_Group3.dat", "wb")  # opens file for writing binary
    show_menu()  # calls show_menu function to display menu
    user_choice = input("Enter an option from the menu: ")

    while user_choice != '0':

        if user_choice == '1':
            new_course = input("Enter the course code: ")
            new_name = input("Enter the course name: ")
            add_course(new_course, new_name)
            pickle.dump(courses, f1)  # writes courses dictionary to file
        elif user_choice == '2':
            new_course = input("Enter the course code to be removed: ")
            remove_course(new_course)
            pickle.dump(courses, f1)  # writes courses dictionary to file
        elif user_choice == '3':
            view_all_courses()
        elif user_choice == '4':
            new_Id=input("Enter the student ID: ")
            new_name=input("enter the student name: ")
            new_major=input("Enter the student's major")
            new_email=input("enter the student's email")
            add_student(new_Id,new_name,new_major,new_email)

        elif user_choice == '5':
            new_name=input("Enter the student id to be deleted: ")
            remove_student(new_name)
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

        f1.close()
        f1 = open("CMSC3380_Assignment3_Group3.dat", "ab")
        pickle.dump(students,f1)
        f1.close()
        f1 = open("CMSC3380_Assignment3_Group3.dat", "wb")


        show_menu()  # calls show_menu function to display menu
        user_choice = input("Enter an option from the menu: ")
    print("Exiting program...")
except FileNotFoundError:  # FileNotFoundError exception, message printed
    print("File not found")