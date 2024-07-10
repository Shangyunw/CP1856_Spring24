# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:07:23 2024

@author: Arun.Rameshbabu
"""

"""
Sequence
1. Open a file.
    open(file, 'rb' or 'wb')
    Modes:
        r - read
        w - write
        a - append
        b - binary
2. Write data to a file (dump) / Read data from the file(load)
3. Close the file.
    close()
"""

players_list = [['Joe', 'P', [10,13,30,12], 2],
                ['Tom', 'SS', [11, 17], 4],
                ['Ben', 'C', [4, 7.5, 'Yeah'], 1]]

import pickle

# Writing to a binary file
with open('binary_example.bin', 'wb') as bin_file_handler:
    pickle.dump(players_list, bin_file_handler)

# Reading from a binary file
with open('binary_example.bin', 'rb') as bin_file_reader:
    players = pickle.load(bin_file_reader)

