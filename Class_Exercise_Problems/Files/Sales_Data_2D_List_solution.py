# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:01:15 2024

@author: Arun.Rameshbabu
"""

import sales as s
import Sales_Data_file_operations as sfo

def title():
    print("SALES DATA IMPORTER\n")


def command_menu():
    print("COMMAND MENU")
    print("view\t - View all sales")
    print("add\t\t - Add sales")
    print("import\t - Import data from a file")
    print("menu\t - Show menu")
    print("exit\t - Exit program\n")

def get_quarter(month) -> int:
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
        quarter = 1
    elif (month == 4) or (month == 5) or (month == 6):
        quarter = 2
    elif (month == 7) or (month == 8) or (month == 9):
        quarter = 3
    elif (month == 10) or (month == 11) or (month == 12):
        quarter = 4
    else:
        print ("Wrong input entered, try again")
        return None
    return quarter


def import_file(collection):
    file_to_import = input("Enter name of the file to import: ")
    tracking_list = sfo.read_text_file()
    if file_to_import not in tracking_list:
        new_sales_data = sfo.read_sales_data(file_to_import)
        tracking_list.append(file_to_import)
        sfo.write_text_file(tracking_list)
        view_sales(new_sales_data)
        for row in new_sales_data:
            collection.append(row)
        print("Imported sales added to list.\n")
    else:
        print(f"\nFile '{file_to_import}' has already been imported.")


def add_sale(collection):
    amount = s.get_amount()
    year = s.get_year()
    month = s.get_month()
    day = s.get_day()
    
    quarter = get_quarter(month)
    
    data = [amount, year, month, day, quarter]
    collection.append(data)
    
    print(f"\nSales for {year}-{month}-{day} added.\n ")


def view_sales(collection):
    if len(collection) == 0:
        print("No sales to view\n")
    else:
        total_sales = 0
        print("\tDate\t\tQuarter\t\tAmount")
        print("-" * 35)
        for num, data in enumerate(collection, start=1):
            amount = data[0]
            year = data[1]
            month = data[2]
            day = data[3]
            quarter = get_quarter(month)
            
            total_sales += amount
            
            print(f'{num}.\t{year}-{month}-{day}\t{quarter}\t\t\t${data[0]}')
        print('-'*35)
        print(f"TOTAL:\t\t\t\t\t\t${total_sales}\n")


def main():
    title()
    command_menu()
    
    sales_list = sfo.read_sales_data()
    
    # While loop to handle commands
    while True:
        command = input("Please enter a command: ").lower()
        if command == 'view':
            view_sales(sales_list)
        elif command == 'add':
            add_sale(sales_list)
        elif command == 'import':
            import_file(sales_list)
        elif command == 'menu':
            command_menu()
        elif command == 'exit':
            sfo.write_sales_data(sales_list)
            break
        else:
            print("Invalid command. Please try again.\n")
            command_menu()
    
    print('Bye!')

if __name__ == '__main__':
    main()
