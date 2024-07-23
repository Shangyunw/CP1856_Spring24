# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:36:14 2024

@author: Arun.Rameshbabu
"""

def menu():
    print("COMMAND MENU")
    print("view - View country name")
    print("add\t - Add a country")
    print("del\t - Delete a country")
    print("exit - Exit program\n")


def view_codes(dict_collection):
    codes = list(dict_collection.keys())
    codes.sort()
    print_line = "Country codes: "
    for code in codes:
        print_line += code + ' '
    print(print_line)


def view(dict_collection):
    view_codes(dict_collection)
    code = input("Enter country code: ")
    code = code.upper()
    if code in dict_collection:
        country_name = dict_collection[code]
        print(f'Country name: {country_name}.\n')
    else:
        print('There is no country with that code.\n')


def add(dict_collection):
    country_code = input("Enter country code: ")
    country_code = country_code.upper()
    if country_code in dict_collection:
        country_name = dict_collection[country_code]
        print(f'{country_name} is already using the country code.\n')
    else:
        country_name = input("Enter country name: ")
        country_name = country_name.title()
        dict_collection[country_code] = country_name
        print(f'{country_name} was added.\n')


def delete(dict_collection):
    country_code = input('Enter country code: ')
    country_code = country_code.upper()
    if country_code in dict_collection:
        country_name = dict_collection.pop(country_code)
        print(f'{country_name} was deleted.\n')
    else:
        print('There is no country with that code.\n')


def main():
    countries = {"CA":"Canada", "US":"United States", "MX":"Mexico"}
    menu()
    while True:
        command = input('Command: ')
        command = command.lower()
        if command == 'view':
            view(dict_collection=countries)
        elif command == 'add':
            add(countries)
        elif command == 'del':
            delete(countries)
        elif command == 'exit':
            print('Bye!')
            break
        else:
            print('Not a valid command. Please try again.\n')


if __name__=='__main__':
    main()