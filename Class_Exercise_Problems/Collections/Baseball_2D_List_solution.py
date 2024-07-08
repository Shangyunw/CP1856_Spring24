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
    print('5 - Edit Player position')
    print('6 - Edit Player stats')
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


def get_lineup_number(collection, prompt):
    while True:
        lineup_number = int(input(prompt))
        if lineup_number < 1 or lineup_number > len(collection):
            print('Invalid lineup number. Please try again.')
        else:
            return lineup_number


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
        print("There are no players in the lineup.\n")
    else:
        print("\tPlayer\t\tPOS\tAB\tH\tAVG")
        seperator('-')
        for i, player in enumerate(collection, start=1):
            name = player[0]
            position = player[1]
            at_bats = player[2]
            hits = player[3]
            avg = batting_average(at_bats, hits)
            print(f'{i}\t{name[:3]}\t\t\t{position}\t{at_bats}\t{hits}\t{avg:.2f}')
        print()


def remove_player(collection):
    player_number = get_lineup_number(collection, 'Player Number: ')
    player = collection.pop(player_number - 1)
    print(f"{player[0]} was removed.\n")


def move_player(collection):
    old_number = get_lineup_number(collection, "Current Lineup Number: ")
    player = collection.pop(old_number - 1)
    print(f"{player[0]} was selected.")
    
    new_number = get_lineup_number(collection, "New Lineup Number: ")
    collection.insert(new_number-1, player)
    print(f"{player[0]} was moved.\n")
    

def edit_player_position(collection):
    number = get_lineup_number(collection, "Lineup Number: ")
    player = collection[number-1]
    print(f"You selected {player[0]} POS={player[1]}")
    
    position = get_player_position()
    player[1] = position
    print(f"{player[0]} was updated.\n")


def edit_player_stats(collection):
    number = get_lineup_number(collection, "Lineup Number: ")
    player = collection[number-1]
    print(f"You selected {player[0]} AB={player[2]} H={player[3]}")
    
    ab = get_at_bats()
    h = get_hits(ab)
    
    player[2] = ab
    player[3] = h
    
    print(f"{player[0]} was updated.\n")


def main():
    seperator()
    print_title()
    print_menu()
    print_positions()
    seperator()
    
    players_list = [['Joe', 'P', 10, 2],
                    ['Tom', 'SS', 11, 4],
                    ['Ben', 'C', 4, 1]]
    while True:
        option = int(input("Menu option: "))
        
        if option == 1:
            display_players(players_list)
        elif option == 2:
            add_player(players_list)
        elif option == 3:
            remove_player(players_list)
        elif option == 4:
            move_player(players_list)
        elif option == 5:
            edit_player_position(players_list)
        elif option == 6:
            edit_player_stats(players_list)
        elif option == 7:
            print("Bye!")
            break
        else:
            print('Invalid option selected. Try again.')
            print_menu()
    

if __name__ == '__main__':
    main()
       