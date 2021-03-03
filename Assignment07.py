# ------------------------------------------------- #
# Title: Assigment 07
# Description: Working with binary files, the pickle module and exception handling.
#               The program ask the user for student ID, Name and Grades, stores it in a dictionary row
#               and saves it to a binary file using the pickle module. Also, there is an option for printing
#               the content of the binary file to screen. Custom Error Handling is introduced to catch type errors.
#
# ChangeLog: (Who, When, What)
# Pablo Montijo, 3/2/2021,Created Script
# -------------------------------------------------
# import pickle # This imports code from another code file!,
# import sys

import pickle
import sys

# Data ---------------------------------------------------------------------- #
# Declare variables and constants

id_int = "" # Student ID
name_str = ""   # Student Name
grade_flt = ""  # Student Grade
row_lst = []    # A row that captures ID, Name and Grade
dic_row = {}    # A dictionary row that captures ID, Name and Grade
objFile = None   # An object that represents a file
strFileName = 'grades.dat'  # A binary file with the dictionary object
lstStudent = [] # a list of Student
lstTable=[]
strStatus = ""

# Custom Error Handling

class NameIsNumericError(Exception):    # Custom class to catch Names that include numbers
    def __str__(self):
        return 'A Name Cannot be Numeric'

class IDisNotIntError(Exception):       # Custom class to catch non integer values for Student ID's
    def __str__(self):
        return 'An ID has to be an Integer'
class CustomError(Exception):           # Custom class to catch a generic type exception
    def __str__(self):
        return 'Custom Error'

# Processing -------------------------------------- #

def save_data_to_file(file_name, list_of_data):
    """ Saves data to a binary file into a dictionary row

    :param file_name: (string) with name of file:
    :param list_of_data: (list) you want filled with file data:
    :return: none
    """
    pass # TODO: Add code here
    objFile = open(file_name,'wb')
    pickle.dump(list_of_data, objFile)
    objFile.close()

def read_data_from_file(file_name):
    """ Reads data from binary file

    :param file_name: (string) with name of file:
    :return: the dictionary row with student info
    """
    pass # TODO: Add code here
    objFile = open(file_name, 'rb')
    objFileData = pickle.load(objFile)
    objFile.close()
    return objFileData

# Presentation ------------------------------------ #

class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a student
        2) Print Data
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_id_student_and_grade():
        """ Pause program and show a message before continuing

        :return: the student ID, Name and Grade
        """
        pass  # TODO: Add Code Here!
        try:
            id_int = int(input('enter an ID: '))
        except ValueError as e:
            print(e, e.__doc__, type(e), sep='\n')
            sys.exit()

        try:
            name_str = input('enter an Student Name: ')

            if name_str.isnumeric():
                raise NameIsNumericError()

        except Exception as e:
            print(e, e.__doc__, type(e), sep='\n')
            sys.exit()
        try:
            grade_flt = float(input('enter a numeric Grade: '))

        except ValueError as e:
            print(e, e.__doc__, type(e), sep='\n')
            sys.exit()

        return id_int, name_str, grade_flt

# Main Body ------------------------------------ #

while(True):

    IO.print_menu_Tasks()  # Shows menu
    # menu printed
    strChoice = IO.input_menu_choice()  # Get menu option
    # choice returned

    if strChoice.strip() == '1':  # Add a new Task
        # TODO: Add Code Here
        id_int, name_str, grade_flt = IO.input_new_id_student_and_grade()
        row_lst = [id_int, name_str, grade_flt]
        dic_row = {"ID": id_int, "Name": name_str, "Grade": grade_flt}
        continue  # to show the menu

    elif strChoice == '2':  # Print Data
        # TODO: Add Code Here
        returned_data = read_data_from_file('grades.dat')
        print(returned_data)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # TODO: Add Code Here!
            IO.input_press_to_continue(strStatus)
            save_data_to_file('grades.dat', dic_row)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Exit Program
        print("Goodbye!")
        break   # and Exit
