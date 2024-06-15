# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:01:17 2024

@author: Arun.Rameshbabu
"""

print("Tip Calculator\n")
# Collecting the inputs
meal_cost = float(input("Cost of meal:\t"))
tip_percent = float(input("Tip percent:\t"))

# Calculations
tip_amount = meal_cost * (tip_percent / 100)
total_amount = meal_cost + tip_amount

# Formatting and printing output
print(f"\nTip amount:\t\t{tip_amount:.2f}")
print(f"Total amount:\t{total_amount:.2f}")
