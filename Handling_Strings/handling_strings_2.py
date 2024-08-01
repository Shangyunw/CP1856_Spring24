# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:10:15 2024

@author: Arun.Rameshbabu
"""

some_text = 'Some celebrity cameos were already teased or spoiled pre-release, but others may come as complete shocks to fans.'

word_space_split = some_text.split()
word_space_split[0]

word_comma_split = some_text.split(',')

word_space_split[0] + '|' +  word_comma_split[1]

'|'.join(word_space_split)
