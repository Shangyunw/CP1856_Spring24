# -*- coding: utf-8 -*-
"""
sales

This module contains functions for getting 
sales data from a user.
"""

def get_amount() -> float:
    """
    Gets a sales amount from the user, converts it into a 
    float value, and returns the float value.

    """
    while True:
        amount = float(input("Amount:\t\t\t\t"))
        if amount > 0:
            break
        else:
            print("Amount is less than or equal to 0. Enter correct amount")
    return amount


def get_day() -> int:
    """
    Gets a day from the user, converts it into an
    int value, and returns the int value.
    """
    while True:
        day = int(input("Day (1-31):\t\t\t"))
        if (day < 1) or (day > 31):
            print("Wrong date entered, try again.")
        else:
            break
    return day


def get_month() -> int:
    """
    Gets a month from the user, converts it into an
    int value, and returns the int value.
    """
    while True:
        month = int(input("Month (1-12):\t\t"))
        if (month < 1) or (month > 31):
            print("Wrong month entered, try again.")
        else:
            break
    return month


def get_year() -> int:
    """
    Gets a year from the user, converts it into an
    int value, and returns the int value.
    """
    while True:
        year = int(input("Year:\t\t\t\t"))
        if (year < 1):
            print("Wrong year entered, try again.")
        else:
            break
    return year


if __name__ == "__main__":
    print(get_year())
    