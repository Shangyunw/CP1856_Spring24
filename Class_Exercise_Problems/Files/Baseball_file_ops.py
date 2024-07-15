# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:28:02 2024

@author: Arun.Rameshbabu
"""

import csv

# Function to write collection to a csv file
def write_2d_collection(collection, filename='baseball.csv'):
    """
    Takes in a collection and writes it to a csv file

    Parameters
    ----------
    collection : 2D list
        2D list with contents.
    filename : TYPE, optional
        DESCRIPTION. The default is 'baseball.csv'.

    Returns
    -------
    None.

    """
    with open(filename, 'w', newline='') as reg_file_writer:
        csv_file_writer = csv.writer(reg_file_writer)
        csv_file_writer.writerows(collection)

def read_2d_collection(filename='baseball.csv'):
    """
    Takes in an optional filename and reads all the rows, returning a list

    Parameters
    ----------
    filename : TYPE, optional
        DESCRIPTION. The default is 'baseball.csv'.

    Returns
    -------
    movie_list : list
        2D list containing the objects.

    """
    player_list = []
    with open(filename, 'r', newline='') as reg_file_reader:
        csv_file_reader = csv.reader(reg_file_reader)
        for row in csv_file_reader:
            player_name = row[0]
            player_pos = row[1]
            player_at_bats = int(row[2])
            player_hits = int(row[3])
            player_list.append([player_name, player_pos, player_at_bats, player_hits])
            #player_list.append([row[0], row[1], int(row[2]), int(row[3])])
    return player_list

