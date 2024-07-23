# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:36:08 2024

@author: Arun.Rameshbabu
"""

"""
try:
    statements
except ExceptionName1:
    statements
except ExceptionName2:
    statements
finally:
    statements
    
raise ExceptionName("custom message")
"""

try:
    k = 5//0 # raises divide by zero exception.
    print(k)
# handles zerodivision exception    
except ZeroDivisionError:   
    print("Can't divide by zero")
finally:
    # this block is always executed 
    # regardless of exception generation.
    print('This is always executed') 

def test_finally():
    try:
        print("Inside try Block")
        raise ValueError           # Exception raised
        return 1                   # before this, finally gets executed 
    except Exception as e:
        print(e)
        return 2
    finally:
        print("Inside Finally")
 
print(test_finally())
