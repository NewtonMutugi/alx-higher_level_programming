#!/usr/bin/python3
"""Module that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    for i in m_a:
        if len(i) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for i in m_b:
        if len(i) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
