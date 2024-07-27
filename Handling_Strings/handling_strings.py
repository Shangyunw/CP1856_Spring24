# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:59:22 2024

@author: Arun.Rameshbabu
"""

"""
Slice a string
Find and repace part of a string
Split a string into a list of strings
Join a list of items into a string
"""

# Find the ordinal value
print('A = ', ord('A'))
print('a = ', ord('a'))
print('8 = ', ord('8'))

# Accessing each character
string_val = "Welcome to CP1856!"
string_val[2]
string_val[-2]
string_val[19]
string_val[2] = 't'

# Slicing
string_val[0:3]
string_val[6:9]
string_val[7:]
string_val[7:-2]

# Repetetion operator (*)
print('-'*20)
print('CP1856'*2)

explaination = """
Slice a string
Find and repace part of a string
Split a string into a list of strings
Join a list of items into a string
"""

# Search a keyword
if('Sp' in explaination):
    print('Boo!')
else:
    print("Nah!")

# String methods
if('12345'.isdigit()):
    print('Yay!')
else:
    print("Nah!")

explaination.startswith('\nSli')

'eternal sunshine'.title()
'    709 341 8765    '.strip()

print('Arun'.ljust(10), '$18.50'.rjust(8))
print('Ronald'.ljust(10), '$200.76'.rjust(8))

print(explaination.replace('Split', 'Distribute'))
'arun.rameshbabu@cna.nl.ca'.removeprefix('arun')
'arun.rameshbabu@cna.nl.ca'.removesuffix('.nl.ca')
