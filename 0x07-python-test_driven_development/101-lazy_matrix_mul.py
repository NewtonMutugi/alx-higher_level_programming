#!/usr/bin/python3
"""Module for lazy_matrix_mul method."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices.

    Args:
        m_a (list): first matrix.
        m_b (list): second matrix.

    Returns:
        list: the result of the multiplication.
    """
    return np.matmul(m_a, m_b)
