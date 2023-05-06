#!/usr/bin/python3
""" function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists of integers or floats representing the
        matrix.
        div (int or float): The number to divide the elements of the matrix by.

    Returns:
        list: A new matrix with all elements divided by `div`, rounded to 2
        decimal places.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers/floats,
        `div` is not a number, or if each row of the matrix is not of the same
        size.
        ZeroDivisionError: If `div` is equal to 0.
    """
    # Validate input
    if type(matrix) != list or any(type(row) != list for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    '''
    Divide each element by `div`, round to 2 decimal places,
    and store in new matrix
    '''
    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
