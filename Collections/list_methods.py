# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 15:35:43 2024

@author: Arun.Rameshbabu
"""

"""
Three list methods
count(item)
reverse(list)
sort([key=function])
sorted(list, [key=function])
"""

# Count
numerical_list = [23, 67, 98, 45, 17, 3, 46, 23, 98, 23]
count_value = numerical_list.count(108)
# Reverse
numerical_list.reverse()
# Sort
numerical_list.sort()

mixed_list = ['Volkswagen', 'BMW', 'Audi', 'acura', 'maserati', 'Citroen']
mixed_list.sort()
mixed_list.sort(key=str.lower)

sorted(mixed_list)
sorted(mixed_list, key=str.lower)

"""
Built in functions
min(list)
max(list)
sum(list, [start])
"""
min(numerical_list)
min(mixed_list)

max(numerical_list)
max(mixed_list)

sum(numerical_list)
sum(numerical_list, start=100)
sum(mixed_list)

# mixed_list = ['Volkswagen', 'BMW', 'Audi', 'acura', 'maserati', 'Citroen', True, 86]
# sorted(mixed_list)

"""
Sampling
choice(list)
shuffle(list)
"""
import random
random.choice(numerical_list)
random.choice(mixed_list)

random.shuffle(numerical_list)
random.shuffle(mixed_list)

"""
deepcopy(list)
"""
list_one = [1,2,3,4]
list_two = list_one
list_two[1] = 4
list_one[2] = 10


import copy
list_two = copy.deepcopy(list_one)
list_two[1] = 4

"""
Slicing
list_object[start:end:step]
"""
numerical_list[0:3]
mixed_list[0:3]

numerical_list[3:]
numerical_list[:5]

numerical_list[0:6:2]
numerical_list[:5:-1]
numerical_list.reverse()
numerical_list[:5]

"""
Concatenation
"""
combined_list = numerical_list + mixed_list

"""
map(function, list)
filter(function, list)
list(object)
reduce(function, list, [start])
"""
def square(n):
    return n*n

squares = map(square, numerical_list)
squares = list(squares)

def is_odd(n):
    return n%2 == 1

odds = filter(is_odd, numerical_list)
odds = list(odds)

import functools

numerical_list_2 = [1, 2, 3, 4, 5, 6]

def add_squares(total, current):
    return total + (current * current)

sum_total = functools.reduce(add_squares, numerical_list_2)
sum_total = functools.reduce(add_squares, numerical_list_2, 10)

"""
List comprehension
"""
squares_list = []
for i in numerical_list:
    squares_list.append(i * i)

squares_list_2 = [square(i) for i in numerical_list]
squares_list_3 = [i*i for i in numerical_list]

even_squares = [i*i for i in numerical_list if i % 2 == 0]
