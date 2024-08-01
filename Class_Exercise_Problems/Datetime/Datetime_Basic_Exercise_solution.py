# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:04:14 2024

@author: Arun.Rameshbabu
"""
from datetime import datetime

date_string_input = input("Enter date of birth (MM/DD/YYYY): ")
try:
    dob = datetime.strptime(date_string_input, '%m/%d/%Y')
except ValueError:
    print("Incorrect values entered for datetime")

print("Date of birth: ", dob)