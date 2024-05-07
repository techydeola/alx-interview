#!/usr/bin/python3
""" Alx interview solution on island perimeter
"""


def island_perimeter(grid):
    """ a function for finding the perimeter of a grid

    Return: perimeter island
    """
    length_row = len(grid)
    length_column = len(grid[0])

    p = 0
    connection = 0

    for r in range(0, length_row):
        for c in range(0, length_column):

            if grid[r][c] == 1:
                p += 4

                if r != 0 and grid[r - 1][c] == 1:
                    connection += 1
                if c != 0 and grid[r][c - 1] == 1:
                    connection += 1

    return (p - (connection * 2))
