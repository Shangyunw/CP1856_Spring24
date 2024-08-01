# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:38:10 2024

@author: Arun.Rameshbabu
"""

def get_full_name():
    while True:
        full_name = input("Enter full name:\t").strip()
        if ' ' in full_name:
            return full_name
        else:
            print("You must enter your full name.")


def get_password():
    while True:
        password = input("Enter password:\t").strip()
        digit = False
        capital = False
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                capital = True
        
        if ((digit==False) or (capital==False) or (len(password) < 8)):
            print("Password must be 8 characters or more")
            print("with at least one digit and one uppercase letter")
        else:
            return password


def get_first_name(name):
    index = name.find(' ')
    first_name = name[:index]
    return first_name


def main():
    full_name = get_full_name()
    print()
    
    password = get_password()
    print()
    
    first_name = get_first_name(full_name)
    print(f'Hi {first_name}, thanks for creating an account.')


if __name__ == '__main__':
    main()

