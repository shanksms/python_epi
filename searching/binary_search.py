from typing import List


def binary_search(_input: List, target: int):
    """
    Algorithm:
    _input: List
     target: int
     start = 0
     end = len(_input) - 1
    1. Loop until start < end

        M = start + (end - start) / 2
        if  _input[M] == target:
            return M
        elif _input[M] > target:
            end = M - 1
        else:
            start = M +1


    """
    start, end = 0, len(_input) - 1
    while start < end:
        M = int(start + (end - start) / 2)
        if _input[M] == target:
            return M
        elif _input[M] > target:
            end = M - 1
        else:
            start = M + 1
    return -1


def find_first_occurrence(sorted_list: List, target: int) -> int:
    """
    Algorithm
    input --> list
    target --> int
    low, high, result = 0, len(input), -1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if input[mid] > target:
            high = mid - 1
        elif input[mid] == target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result
    """
    low, high, result = 0, len(sorted_list), -1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if sorted_list[mid] > target:
            high = mid - 1
        elif sorted_list[mid] == target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result


def first_occurence_of_element_greater_than_key(sorted_list: List, target: int) -> int:
    low, high, result = 0, len(sorted_list), -1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if sorted_list[mid] > target:
            high = mid - 1
            result = mid
        elif sorted_list[mid] == target:
            high = mid - 1
        else:
            low = mid + 1
    return result


"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row
"""


def search_sorted_matrix(matrix, target):
    if len(matrix) == 0:
        raise ValueError('Blank matrix')
    rows, columns = len(matrix), len(matrix[0])
    low, high = 0, rows * columns
    while low <= high:
        mid = int(high - (high - low) / 2)
        row_idx = mid // columns
        col_idx = mid % columns
        if matrix[row_idx][col_idx] == target:
            return row_idx, col_idx
        elif matrix[row_idx][col_idx] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
