# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:34:50 2024

@author: Arun.Rameshbabu
"""

import sys
number = int(input("Enter an integer: "))
print(f"The number entered is {number}")
print("End of program")


"""
try:
    statements
except [ExceptionName]:
    statements
"""
try:
    number = int(input("Enter an integer: "))
    print(f"The number entered is {number}")
except ValueError as v:
    print("You entered an invalid integer. Please try again.")
except Exception as e:
    print("Blanket Exception.")
print("End of program")

"""
Exception
    OSError
        FileNotFoundError
        FileExistsError
        ...
        ...
    ValueError

try:
    statements
except ExceptionName1:
    statements
except ExceptionName2:
    statements
"""
filename = input("Enter filename: ")
inp_objs = []
try:
    with open(filename) as file:
        for obj in file:
            obj = obj.replace('\n', '')
            inp_objs.append(obj)
except FileNotFoundError:
    print("File not found. Enter the correct filename.")
except OSError:
    print("File found, you do not have the permission to access it.")
    sys.exit()
except Exception as e:
    print("An unexpected error happend. Here is the details:")
    print(e)
print("I am still executing")
