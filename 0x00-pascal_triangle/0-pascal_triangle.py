#!/usr/bin/python3

"""A function that returns the pascal triangle of a given number
Keyword arguments:
triangle_list -- a list of lists of each row in the triangle
Return: triangle list if exist
        else - return an empty list
"""


def pascal_triangle(n):
    """ returns the triangle
    """
    
    if (n <= 0):
        return []

    triangle_list = [[1]]

    try:
        for i in range(n - 1):
            temp = [0] + triangle_list[-1] + [0]
            row = []
            for j in range(len(triangle_list[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            triangle_list.append(row)
    except ValueError as e:
        return triangle_list

    return triangle_list
