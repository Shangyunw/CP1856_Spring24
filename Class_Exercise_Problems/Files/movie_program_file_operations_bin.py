# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:54:21 2024

@author: Arun.Rameshbabu
"""

import pickle

def write_bin_collection(collection, filename='movies.bin'):
    """
    Write a colllection to a binary file.

    Parameters
    ----------
    collection : TYPE
        DESCRIPTION.
    filename : TYPE, optional
        DESCRIPTION. The default is 'movies.bin'.

    Returns
    -------
    None.

    """
    with open(filename, 'wb') as bin_file_handler:
        pickle.dump(collection, bin_file_handler)

def read_bin_collection(filename='movies.bin'):
    """
    Read a binary file and return the contents

    Parameters
    ----------
    filename : TYPE, optional
        DESCRIPTION. The default is 'movies.bin'.

    Returns
    -------
    movies : TYPE
        DESCRIPTION.

    """
    with open(filename, 'rb') as bin_file_handler:
        movies = pickle.load(bin_file_handler)
    return movies
