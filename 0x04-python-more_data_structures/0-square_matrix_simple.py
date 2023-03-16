#!/usr/bin/python3
""" 0-square_matrix_simple.py """


def square_matrix_simple(matrix=[]):
    """ square_matrix_simple """
    return [[x ** 2 for x in row] for row in matrix]
