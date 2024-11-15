# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   IBEldin,13 Nov 2024, <Activity>
# ------------------------------------------------------------------------------------------ #
# import the json module
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str, str] = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data separated by a comma.
file: str = ''   # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user


# When the program starts, read the file data into a list of dictionaries(table)
# Extract the data from the file and load into list of dictionaries
try:        # Run this code
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError:
    print('File not found. Creating file...')
    open(FILE_NAME, "w")
except Exception as e:      #Execute print when there is an exception
    print('unknown exception', type(e), e, sep ='\n')
    student = []        #missing key/value
finally:        #Always run this code to check if file is closed.
    if file and not file.closed:
        file.close()

# Present and Process the data
while (True):
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:        #To catch exception errors in user input
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():        #Capture exception errors in first name input
                 raise ValueError('First name must be alphabtic')
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():        #Capture exception errors in last name input
                raise ValueError('Last name must be alphabtic')
            course_name = input("Please enter the name of the course: ")
            if course_name.isalpha():        #Ensure course name is alphanumeric
                raise ValueError('Course name must be alphanumeric')
            student_data = {'first_name': student_first_name, 'last_name': student_last_name, 'course_name': course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
                print(e)
                continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-" * 80)
        print(students)
        print("-" * 80)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:        #ensure data is saved to json file
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            raise Exception()
        except Exception as e:
            print('Error saving data to file')
            print(e)
        finally:
            if file and not file.closed:
                file.close()
        print("The following data was saved to file!")
        print(f" {student_first_name} {student_last_name} is enrolled in {course_name}\n")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
