# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:44:10 2024

@author: Arun.Rameshbabu
"""

from datetime import datetime, timedelta

def invoice_date():
    invoice_date_str = input("Enter the invoice date (MM/DD/YY): ")
    try:
        invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%y")
        return invoice_date
    except ValueError:
        print("Wrong Date entered")


def main():
    print("The invoice due date program\n")
    
    condition = 'y'
    while condition.lower() == 'y':
        invoice_dt = invoice_date()
        print()
        
        due_date = invoice_dt + timedelta(days=30)
        current_date = datetime.now()
        days_overdue = (current_date - due_date).days
        
        format_var = "%B %d, %Y"
        print(f"Invoice Date: {invoice_dt:{format_var}}")
        print(f"Due Date: {due_date:{format_var}}")
        print(f"Current Date: {current_date:{format_var}}")
        
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        
        print()
        
        condition = input("Continue? (y/n): ")
        print()
    
    print("Bye!")


if __name__ == '__main__':
    main()
    