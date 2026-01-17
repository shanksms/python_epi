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
    beg, end = 0, len(sorted_list) - 1
    result = -1
    while beg <= end:
        mid = (beg + end) // 2
        if sorted_list[mid] == target:
            result = mid
            end = mid - 1
        elif sorted_list[mid] > target:
            end = mid - 1
        else:
            beg = mid + 1
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


def search_element_equal_to_index(sorted_list: List):
    """
    Algorithm:
    1. create another List, by subtracting elements of sorted_list from their index.
    new_list = [element-idx for idx, element in enumerate(sorted_list)]
    2. find 0 in the new list
     result = binary_search(new_list, 0)
     return result
    :param sorted_list:
    :return:
    """
    '''
        low, high = 0, len(sorted_list)
        while low <= high:
            mid = int(high - (high - low) / 2)
            if sorted_list[mid] == mid:
                return mid
            elif sorted_list[mid] > mid:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        '''
    new_list = [element - idx for idx, element in enumerate(sorted_list)]
    return binary_search(new_list, 0)


def find_min_element_in_cyclically_sorted_list(cyclically_sorted_list: List):
    """
    Algorithm:

    Think of the array as two segments divided by the inflection point.
    cyclically_sorted_list = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    l, h = 0, len(sorted_list) - 1
    while l < = h:
        m = (l + h) // 2
        if sorted_list[mid] > sorted_list[h]: ## min element can not be in the left segment
            search in the segment mid+1, h
        else:
            min_idx = m
            search in the segment l, mid - 1


    :param cyclically_sorted_list:
    :return:
    """
    low, high, minimum = 0, len(cyclically_sorted_list) - 1, -1
    # loop will end when low == high
    while low < high:
        mid = int(high - (high - low) / 2)
        if cyclically_sorted_list[mid] > cyclically_sorted_list[high]:
            low = mid + 1
        else:
            high = mid

    return high


def find_element_in_rotated_sorted_array(cyclically_sorted_list: List, target: int):
    pass


if __name__ == '__main__':
    print(find_min_element_in_cyclically_sorted_list([7, 8, 9, 2, 3, 4, 5, 6]))