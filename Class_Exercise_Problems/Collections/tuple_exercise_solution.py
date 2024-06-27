# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:10:48 2024

@author: Arun.Rameshbabu
"""

"""
Algorithm
Average = sum(collection)/len(collection)
median:
    collection.sort()
    median_index <- len(collection)//2
    collection[median_index]
min
max
dups:
    dups = []
    min, max
    for i range(min, max):
        count_i = collection.count(i)
        if count_i >= 2:
            dups.append[i]
    return dups

"""
import random

def get_dups(collection):
    dups =[]
    for i in range(min(collection), max(collection)):
        count_val = collection.count(i)
        if count_val >= 2:
            dups.append(i)
    return dups


def print_statistics(collection):
    avg = sum(collection) / len(collection)
    median_index = len(collection) // 2
    median_value = collection[median_index]
    min_value = min(collection)
    max_value = max(collection)
    dups = get_dups(collection)
    
    print(f"Average = {avg:.0f} Median = {median_value} Min = {min_value} Max = {max_value} Dups = {dups}\n")


def main():
    collection_tuple = (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
    collection_list = [0] * 11
    
    for i in range(len(collection_list)):
        collection_list[i] = random.randint(0, 50)
    collection_list.sort()    
    
    print("TUPLE DATA: ", collection_tuple)
    print_statistics(collection_tuple)
    
    print("RANDOM DATA: ", collection_list)
    print_statistics(collection_list)


if __name__ == '__main__':
    main()
