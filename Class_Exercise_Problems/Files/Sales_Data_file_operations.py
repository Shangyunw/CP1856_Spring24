# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:49:14 2024

@author: Arun.Rameshbabu
"""
import csv

def read_sales_data(filename='all_sales.csv'):
    sales_data = []
    with open(filename, 'r') as reg_file_handler:
        csv_read_handler = csv.reader(reg_file_handler)
        for row in csv_read_handler:
            #print(row)
            sales_data.append([float(row[0]), int(row[1]), int(row[2]), int(row[3])])
    return sales_data


def write_sales_data(collection, filename='all_sales.csv'):
    with open(filename, 'w', newline='') as reg_file_writer:
        csv_file_writer = csv.writer(reg_file_writer)
        csv_file_writer.writerows(collection)


def write_text_file(collection, filename='tracking.txt'):
    with open(filename, 'w') as reg_file_handler:
        for item in collection:
            reg_file_handler.write(item + '\n')

    
def read_text_file(filename='tracking.txt'):
    filenames = []
    with open(filename, 'r') as reg_file_reader:
        for filename in reg_file_reader:
            filename_append = filename.replace('\n', '')
            filenames.append(filename_append)
    return filenames
