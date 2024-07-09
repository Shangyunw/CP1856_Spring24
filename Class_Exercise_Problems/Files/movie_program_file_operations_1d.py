# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:41:36 2024

@author: Arun.Rameshbabu
"""

# Function to write movies to a file
def write_1d_collection(collection, filename = 'movies_1d_txt'):
    """
    Takes in a 1D collection and writes it to a file

    Parameters
    ----------
    collection : list
        Collection of movies.

    Returns
    -------
    None.

    """
    with open(filename, 'w') as wf_handler:
        for obj in collection:
            wf_handler.write(f"{obj}\n")
            
# Function to read movies from a file
def read_1d_collection(filename = 'movies_1d_txt'):
    """
    Reads in a file and returns a 1D list from the file contents.

    Parameters
    ----------
    filename : str, optional
        DESCRIPTION. The default is 'movies_1d_txt'.

    Returns
    -------
    objs_list : list
        List of 1D objects in the file (each line) with newline stripped.

    """
    objs_list = []
    with open(filename, 'r') as rf_handler:
        for line in rf_handler:
            line = line.replace('\n', '')
            objs_list.append(line)
    return objs_list
