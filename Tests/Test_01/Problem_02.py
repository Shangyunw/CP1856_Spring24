# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:27:43 2024

@author: Arun.Rameshbabu
"""

print("Change Calculator")

choice = 'y'
while choice.lower() == 'y':
    # Get the input
    cents = int(input("\nEnter number of cents (0-99): "))
    print()
    
    # Conversion Logic
    # Calculating Quarters
    if (cents >= 25):
        quarters = cents // 25
        cents = cents % 25
    else:
        quarters = 0
    # Calculating Dimes
    if (cents >= 10):
        dimes = cents // 10
        cents = cents % 10
    else:
        dimes = 0
    # Calculating Nickels
    if (cents >= 5):
        nickels = cents // 5
        cents = cents % 5
    else:
        nickels = 0
    
    # Printing output
    print(f"Quarters:\t{quarters}")
    print(f"Dimes:\t\t{dimes}")
    print(f"Nickels:\t{nickels}")
    print(f"Pennies:\t{cents}\n")
    
    choice = input("Continue? (y/n): ")
    
print("\nBye!")
