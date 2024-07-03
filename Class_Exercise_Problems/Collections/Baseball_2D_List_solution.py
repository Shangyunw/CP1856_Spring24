# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:01:43 2024

@author: Arun.Rameshbabu
"""

POSITIONS = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')

def seperator(charc = '='):
    print(charc * 60)


def print_title(title = "Baseball Team Manager"):
    print(f'\t\t\t\t\t{title}')


def print_menu():
    print('MENU OPTIONS')
    print('1 - Display Lineup')
    print('2 - Add Player')
    print('3 - Remove Player')
    print('4 - Move Player')
    print('5 - Edit PLayer position')
    print('6 - Edit PLayer stats')
    print('7 - Exit Program\n')


def print_positions():
    print('POSITIONS')
    for position in POSITIONS[:-1]:
        print(f'{position}, ', end='')
    print(POSITIONS[-1])


def get_player_position():
    while True:
        position = input('Position: ').upper()
        if position in POSITIONS:
            return position
        else:
            print('Invalid position. Try again.')
            print_positions()
        

def get_at_bats():
    while True:
        at_bats = int(input('At bats: '))
        if at_bats < 0 or at_bats > 1500: # Assuming 30 yr career and 50 games/year
            print('Invalid entry. Must be between 0 and 1500.')
        else:
            return at_bats


def get_hits(at_bats):
    while True:
        hits = int(input('Hits: '))
        if hits < 0 or hits > at_bats:
            print(f'Invalid entry. Must be between 0 and {at_bats}.')
        else:
            return hits


def batting_average(at_bats, hits):
    """
    Calculates and returns batting average

    Parameters
    ----------
    at_bats : int
        Number of at_bats.
    hits : int
        Number of hits.

    Returns
    -------
    float
        Returns batting average.

    """
    return hits/at_bats


def add_player(collection):
    player_name = input('Name: ').title()
    player_position = get_player_position()
    player_at_bats = get_at_bats()
    player_hits = get_hits(player_at_bats)
    
    player = []
    player.append(player_name)
    player.append(player_position)
    player.append(player_at_bats)
    player.append(player_hits)
    
    collection.append(player)
    print(f'{player_name} was added.\n')


def display_players(collection):
    if collection == None:
        print("There are no players in the lineup.")
    else:
        print("\tPlayer\t\tPOS\tAB\tH\tAVG")
        seperator('-')
        for i, player in enumerate(collection, start=1):
            name = player[0]
            position = player[1]
            at_bats = player[2]
            hits = player[3]
            avg = batting_average(at_bats, hits)
            print(f'{i}\t{name[:4]}\t\t{position}\t{at_bats}\t{hits}\t{avg:.2f}')


def main():
    seperator()
    print_title()
    print_menu()
    print_positions()
    seperator()


if __name__ == '__main__':
    main()
       