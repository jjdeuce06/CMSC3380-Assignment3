#Group 3 Assignment 3
# John Gerega, Luke Ruffing, Ethan Janovich






print("Menu: \n 1. Add a course \n 2. Remove a course \n 3. View all courses \n "
"4. Add a student \n 5. Remove a student \n 6. View all students \n 7. Enroll a student in a course \n "
"8. Unenroll a student from a course \n 9. List student course \n 0. Quit\n")
user_choice = input("Enter an option from the menu: ")

while(user_choice != 0)
{
    switch(user_choice)
    {
        case 1:
            add_course()
            break
        case 2:
            remove_course()
            break
        case 3:
            view_all_courses()
            break
        case 4:
            add_student()
            break
        case 5:
            remove_student()
            break
        case 6:
            view_all_students()
            break
        case 7:
            enroll_student()
            break
        case 8:
            unenroll_student()
            break
        case 9:
            list_student_courses()
            break
        case 0:
            break
        default:
            print("Invalid input, please enter a valid option")
            break
    }
    if user_choice != 0:
    {
        print("Menu: \n 1. Add a course \n 2. Remove a course \n 3. View all courses \n "
        "4. Add a student \n 5. Remove a student \n 6. View all students \n 7. Enroll a student in a course \n "
        "8. Unenroll a student from a course \n 9. List student course \n 0. Quit\n")
        user_choice = input("Enter an option from the menu: ")
    }
}