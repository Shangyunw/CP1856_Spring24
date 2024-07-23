# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:36:27 2024

@author: Arun.Rameshbabu
"""

"""
Syntax
dictionary_name = {key1:value1, key2:value2, .....}
"""

# Creating a dictionary
countries = {"CA":"Canada", "US":"United States", "MX":"Mexico"}

numbers = {1:"One", 2:"Two", 3:"Three", 4:"Four"}

movie = {"name":"The Holy Grail", "year":1975, "rating":9.99}

catalog = {}

# Access the dictionary
print(countries)

"""
Syntax
dictionary_name[key]
"""
countries["US"]
country = "US"
countries[country]
#countries["IN"]

"US" in countries
country in countries
if country in countries:
    print(f'{countries[country]} is in the dictionary')
    
# Methods
# get()
country_obj = countries.get("MX")
country_obj2 = countries['MX']
country_obj = countries.get("IN", 'Unknown')

# del()
del countries['MX']
#del countries['IN']

country_obj3 = countries.pop('CA')
country_obj4 = countries.pop('IN', 'Unknown')

countries.clear()

# items() - key, value pair
countries = {"CA":"Canada", "US":"United States", "MX":"Mexico"}
countries.items()
for code, name in countries.items():
    print(f"{code} - {name}")
    
# keys(), values()
example1 = countries.keys()
for code in countries.keys():
    print(f"{code}")

countries.values()
for country in countries.values():
    print(f"{country}")

example2 = list(countries.keys())

players_list = [['Joe', ['P', 10, 2]],
                ['Tom', ['SS', 11, 4]],
                ['Ben', ['C', 4, 1]]]
players = dict(players_list)

# adding to a dictionary
countries['IN'] = 'India'
countries['IN'] = 'Indonesia'
