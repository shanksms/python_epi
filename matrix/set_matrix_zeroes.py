"""
Given an m x n integer  matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""


def set_zeroes_approach1(matrix):
    '''
    Algorithm:
    1. Make first pass on the matrix. Record row and column index having zero in sets
    2. Make another pass on the matrix. This time, if any column or row index falls in the set, set it to zero
    :param matrix:
    :return:
    '''
    row, col = set(), set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in row or j in col:
                matrix[i][j] = 0

    return matrix





