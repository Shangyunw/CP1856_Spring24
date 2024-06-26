# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:34:21 2024

@author: Arun.Rameshbabu
"""

"""
Syntax

tuple_name = (item1, item2, item3)

"""

float_numbers = (23.0, 56.9, 87.9, 24.0, 17.0)
manufacturers = ('Volkswagen', 'BMW', 'Audi', 'acura', 'maserati', 'Citroen')
movie = ('Monty Python and the Holy Grail', 1975, 9.98)

# Accessing elements
manufacturers[0]
manufacturers[-1]
manufacturers[1:4]

# Assignment
manufacturers[0] = 'Mercedes'
val1, val2, val3 = (1, 5.0, "BMW")

def square_and_cube(n):
    return (n*n, n*n*n)

square_2, cube_2 = square_and_cube(2)
