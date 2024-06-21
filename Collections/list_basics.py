# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:37:18 2024

@author: Arun.Rameshbabu
"""

"""
Learning Objectives
1. How to create / use a list.
2. Methods: append, insert, remove, index, pop,
            enumerate, zip 
            map, filter, list, reduce
3. List comprehension
4. count, reverse, sort, min, max, sum, choice, shuffle, deepcopy
"""

"""
Syntax for a list
list_name = [item1, item2, item3, ....]
"""

years = [1988, 1993, 2005, 2008, 2015]
type(years)
inventory = ['staff', 'hat', 'shoes']
movie = ["The Holy Grail", 1975, 9.99]

# Use repetetion operator *
scores = [0] * 5

# Access 2005 from years
years[2]
# Access 'The Holy Grail' from movies
movie[0]

inventory[-1]
inventory[2]
inventory[4]

# Updating a list
inventory[2] = 'robe'
inventory[2] = 10

# List modification methods
# append
inventory.append('food')
inventory.append(20)
# remove
inventory.remove('20')
inventory.remove(20)
# insert
inventory.insert(1, 20)
# index
inventory.index('food')
# pop
inventory.pop()
item = inventory.index('food')
item = inventory.pop(item)

# Properties
len(years)

# in keyword
2008 in years
if (2008 in years):
    years.remove(2008)

# Printing lists
print(movie)

# Loop through lists
for item in movie:
    print(item)