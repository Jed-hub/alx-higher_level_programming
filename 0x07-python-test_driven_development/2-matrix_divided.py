#!/usr/bin/python3
"""
    Divide module
    containing one function
    that divid all the elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    This function takes a matrix
    divide all its elements
    and return the new matrix
    """
    new_matrix = []
    length = 0

    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError('div must be a number')
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix[0], list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if len(matrix[0]) <= 0:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    for row in matrix:
        new_row = []
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
        if length == 0:
            length = len(row)
        elif len(row) is not length:
            raise TypeError('Each row of the matrix must have the same size')
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)
    return new_matrix
