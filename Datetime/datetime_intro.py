# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:33:05 2024

@author: Arun.Rameshbabu
"""

import datetime
from datetime import date, time, timedelta

date_obj = datetime.date.today()
datetime_obj = datetime.datetime.now()

# Constructors
halloween = date(2024, 10, 31)
type(halloween)
current_time = time(15, 40)
datetime_obj = (2024, 10, 28, 15, 45)
datetime_obj_2 = (2024, 10, 28, 15, 45, 55)


"""
Syntax to parse datetime objects:
datetime.datetime.strptime(date_string, format)

Common format string codes:
    %d Day of the month
    %m Month as a number
    %y 2-digit year
    %Y 4-digit year
    %H Hour in 24hr format
    %M Minutes as a number
    %S Seconds as a number
    """

halloween_1 = datetime.datetime.strptime('10/31/2024', "%m/%d/%Y")
halloween_1.date()
halloween_2 = datetime.datetime.strptime('31-10-2024', "%d-%m-%Y")
halloween_3 = datetime.datetime.strptime('31-10-2024 22:45', "%d-%m-%Y %H:%M")


print(f'{halloween:%d/%m/%Y}')
print(f'{halloween:%B %d, %Y (%A)}')

print(f'{halloween_3:%B %d, %I:%M %p}')
print_var = '%B %d, %Y %I:%M %p'
print(f'{halloween_3:{print_var}}')

three_weeks = timedelta(weeks=3)
two_thirty = timedelta(hours=2, minutes=30)

three_weeks_frm_nw = date.today() + timedelta(weeks=3)
three_weeks_ago = date.today() - timedelta(weeks=3)

three_weeks.days
three_weeks.total_seconds()

