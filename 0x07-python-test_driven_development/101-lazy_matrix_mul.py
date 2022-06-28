#!/usr/bin/python3
"""
Defines lazy_matrix function
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ multiplies two  matrices
        using the module NumPy
    """
    return numpy.matmul(m_a, m_b)
