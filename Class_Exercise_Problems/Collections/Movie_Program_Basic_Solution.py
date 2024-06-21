# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:33:54 2024

@author: Arun.Rameshbabu
"""

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program\n")


def list_movies(movies):
    """
    Prints the list of movies

    Parameters
    ----------
    movies : list
        List that contains movies.

    Returns
    -------
    None.

    """
    # for i in range(len(movies)):
    #     print(f"{i+1}. {movies[i]}")
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")
    print()


def add_movie(movies):
    """
    Add a movie to the movies list provided

    Parameters
    ----------
    movies : list
        List that contains movies.

    Returns
    -------
    None.

    """
    movie = input('Name: ')
    movies.append(movie)
    print(f'{movie} was added\n')


def delete_movie(movies):
    num = int(input("Number: "))
    if (num < 1) or (num > len(movies)):
        print("Invalid movie number.\n")
    else:
        movie = movies.pop(num-1)
        print(f"{movie} was deleted.\n")


def main():
    """
    Main function for the Basic Movies Program

    Returns
    -------
    None.

    """
    # Creating an empty list
    movies_list = ['Monty Python and the Holy Grail', 'On the Waterfront', 'Cat on a hot tin roof']
    display_menu()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies_list)
        elif command.lower() == 'add':
            add_movie(movies_list)
        elif command.lower() == 'del':
            delete_movie(movies_list)
        elif command.lower() == 'exit':
            break
        else:
            print("Invalid command. Please try again.\n")
    print("Bye!")


if __name__ == '__main__':
    main()
