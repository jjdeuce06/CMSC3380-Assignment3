#Group 3 Assignment 3
# John Gerega, Luke Ruffing, Ethan Janovich

import os, sys


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

try:
    f1 = open("CMSC3380_Assignment3_Group3.dat", "wb")  #opens file for writing binary
    show_menu()  #calls show_menu function to display menu
    user_choice = input("Enter an option from the menu: ")

    while user_choice != '0':
        if user_choice == '1':
            add_course()
        elif user_choice == '2':
            remove_course()
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
    print("Exiting program...")
             
except FileNotFoundError:   #FileNotFoundError exception, message printed
    print("File not found")