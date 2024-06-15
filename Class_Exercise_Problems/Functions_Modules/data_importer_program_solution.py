# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:57:24 2024

@author: Arun.Rameshbabu
"""

import sales as s
# help(sales)

def menu():
    print("SALES DATA IMPORTER\n")
    print("Enter sales data")

def get_quarter(month) -> str:
    """
    Takes in month and return the quarter the month belongs to

    Parameters
    ----------
    month : int
        Numerical value for month.

    Returns
    -------
    str
        Quarter that corresponds to the month value.

    """
    if (month == 1) or (month == 2) or (month == 3):
        quarter = 'Quarter 1'
    elif (month == 4) or (month == 5) or (month == 6):
        quarter = 'Quarter 2'
    elif (month == 7) or (month == 8) or (month == 9):
        quarter = 'Quarter 3'
    elif (month == 10) or (month == 11) or (month == 12):
        quarter = 'Quarter 4'
    else:
        print ("Wrong input entered, try again")
        return None
    return quarter


def main():
    total_sales = 0
    counter = 1
    choice = 'y'
    
    while choice == 'y':
        amount = s.get_amount()
        year = s.get_year()
        month = s.get_month()
        day = s.get_day()
        
        quarter = get_quarter(month)
        if quarter is None:
            continue
        
        print (f"\n{counter}.\t\t\t\t{year}-{month}-{day}\t\t{quarter}\t\t${amount:.1f}")
        total_sales += amount
        counter += 1
        choice = input("\nEnter more sales? (y/n): ")
    
    print("\nTotal Sales:")
    print('-'*16)
    print(f"${total_sales:.1f}\n")
    print("Bye!")


if __name__ == "__main__":
    menu()
    main()