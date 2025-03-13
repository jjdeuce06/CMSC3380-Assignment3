#Group 3 Assignment 3
# John Gerega, Luke Ruffing, Ethan Janovich

import os, sys

courses = {
    "CMSC3380": "Python",
}

students = {

}

try:
    f1 = open("CMSC3380_Assignment3_Group3.dat", "wb")  #opens file for writing binary
    print("Menu: \n 1. Add a course \n 2. Remove a course \n 3. View all courses \n "
    "4. Add a student \n 5. Remove a student \n 6. View all students \n 7. Enroll a student in a course \n "
    "8. Unenroll a student from a course \n 9. List student course \n 0. Quit\n")
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
        
        print("Menu: \n 1. Add a course \n 2. Remove a course \n 3. View all courses \n "
            "4. Add a student \n 5. Remove a student \n 6. View all students \n 7. Enroll a student in a course \n "
            "8. Unenroll a student from a course \n 9. List student course \n 0. Quit\n")
        user_choice = input("Enter an option from the menu: ")
                
except FileNotFoundError:   #FileNotFoundError exception, message printed
    print("File not found")