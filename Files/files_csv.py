# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:40:40 2024

@author: Arun.Rameshbabu
"""

"""
CSV - Comma Seperated Values
csv module
Sequence
1. Open a file.
    open(file, mode)
    Modes:
        r - read
        w - write
        a - append
        b - binary
2. file handler object -> csv handler (writer)(reader)
3. Write data to a file / Read data from the file (writerows)
3. Close the file.
    close()
"""

# Example of a csv write
players_list = [['Joe', 'P', 10, 2],
                ['Tom', 'SS', 11, 4],
                ['Ben', 'C', 4, 1]]

import csv
with open('players.csv', 'w', newline='') as reg_file_writer:
    csv_file_writer = csv.writer(reg_file_writer)
    csv_file_writer.writerows(players_list)

## Doing with regular writer (not recommended)
with open('players2.csv', 'w', newline='') as reg_file_writer:
    for line in players_list:
        for obj in line[:-1]:
            reg_file_writer.write(str(obj) + ',')
        reg_file_writer.write(str(line[-1]) + '\n')

# Example of a csv read
cars_read = []
with open('test_file.csv', 'r', newline='') as reg_file_reader:
    csv_file_reader = csv.reader(reg_file_reader)
    for row in csv_file_reader:
        cars_read.append([row[0], row[1]])

players_read = []
with open('players.csv', 'r', newline='') as reg_file_reader:
    csv_file_reader = csv.reader(reg_file_reader)
    for row in csv_file_reader:
        player = [row[0], row[1], int(row[2]), int(row[3])]
        players_read.append(player)

