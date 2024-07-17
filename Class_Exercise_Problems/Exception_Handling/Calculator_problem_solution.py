# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 16:00:34 2024

@author: Arun.Rameshbabu
"""

def get_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer number. Please try again.")

def main():
    print("The Total Calculator program\n")
    
    price = get_price()
    quant = get_quantity()
    
    total = price * quant
    
    print(f'\nPRICE:\t\t{price}')
    print(f'QUANTITY:\t{quant}')
    print(f'TOTAL:\t\t{total}')

if __name__ == '__main__':
    main()
    