# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:50:23 2024

@author: Arun.Rameshbabu
"""
import csv

# Function to write collection to a csv file
def write_2d_collection(collection, filename='movies.csv'):
    """
    Takes in a collection and writes it to a csv file

    Parameters
    ----------
    collection : 2D list
        2D list with contents.
    filename : TYPE, optional
        DESCRIPTION. The default is 'movies.csv'.

    Returns
    -------
    None.

    """
    with open(filename, 'w', newline='') as reg_file_writer:
        csv_file_writer = csv.writer(reg_file_writer)
        csv_file_writer.writerows(collection)

def read_2d_collection(filename='movies.csv'):
    """
    Takes in an optional filename and reads all the rows, returning a list

    Parameters
    ----------
    filename : TYPE, optional
        DESCRIPTION. The default is 'movies.csv'.

    Returns
    -------
    movie_list : list
        2D list containing the objects.

    """
    movie_list = []
    with open(filename, 'r', newline='') as reg_file_reader:
        csv_file_reader = csv.reader(reg_file_reader)
        for row in csv_file_reader:
            movie_list.append(row)
    return movie_list

