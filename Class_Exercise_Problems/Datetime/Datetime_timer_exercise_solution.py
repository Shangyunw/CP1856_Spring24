# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:37:39 2024

@author: Arun.Rameshbabu
"""

from datetime import datetime

def main():
    print("The Timer program\n")
    
    input("Press Enter to start...")
    start_time = datetime.now()
    print("Start time: ", start_time)
    
    input("Press Enter to stop...")
    stop_time = datetime.now()
    print("Start time: ", stop_time)
    
    elapsed_time = stop_time - start_time
    print("ELAPSED TIME")
    print('Time: ', elapsed_time)


if __name__ == '__main__':
    main()

