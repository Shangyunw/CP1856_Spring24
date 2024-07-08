# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:37:15 2024

@author: Arun.Rameshbabu
"""

"""
3 kinds of files
text
csv
binary
"""

"""
Sequence
1. Open a file.
    open(file, mode)
    Modes:
        r - read
        w - write
        a - append
        b - binary
2. Write data to a file / Read data from the file
3. Close the file.
    close()
"""
# Writing to a file
# First method
out_file = open("test.txt","w")
out_file.write("This is my first file.")
out_file.close()

# Second method
"""
Syntax using with
with open(file, mode) as file_obj:
    statements..
    statements..
"""
with open("test.txt", 'w') as out_file_with:
    out_file_with.write("This is writing to file using 'with'.")

# Reading from a file
"""
3 different ways
readline()
readlines()
read()
"""
with open("test.txt", 'r') as read_file_handler:
    print(read_file_handler.readline())

# Appending to a file
with open("test.txt", 'w') as out_file_with:
    out_file_with.write("This is appending to file using 'with'.\n")

with open("test.txt", 'a') as out_file_with:
    out_file_with.write("This is the actual append operation.\n")

# Other read methods
# Reading file contents through a loop
with open('test.txt') as file_handler:
    for line in file_handler:
        print(line, end='')

# Reading entire file as a string
with open('test.txt') as file_handler:
    file_contents = file_handler.read()
    print(file_contents)

# Reading the entire file as a list
with open('test.txt') as file_handler:
    file_contents_list = file_handler.readlines()
    print(file_contents_list[0], end='')
    print(file_contents_list[1])

# Reading each line of a file
with open('test.txt') as file_handler:
    file_line = file_handler.readline()
    print(file_line)
    file_line_2 = file_handler.readline()
    print(file_line_2)

# Writing a list to a file
cars = ['BMW', 'Volkswagen', 'Audi', "Mercedes"]
with open('cars.txt', 'w') as wf_handler:
    for car in cars:
        wf_handler.write(f"{car}\n")

# Reading back from a file to a list
cars_list = []
with open('cars.txt', 'r') as rf_handler:
    #cars_list_readlines = rf_handler.readlines()
    for line in rf_handler:
        line = line.replace('\n', '')
        cars_list.append(line)

# Writing and reading numbers
years = [1975, 1988, 1995, 2004, 2015]
with open('years.txt', 'w') as years_file:
    for year in years:
        years_file.write(f"{year}\n") # Int to str conversion

years_read = []
with open('years.txt') as years_file_read:
    for line in years_file_read:
        line = line.replace('\n', '')
        years_read.append(int(line))


