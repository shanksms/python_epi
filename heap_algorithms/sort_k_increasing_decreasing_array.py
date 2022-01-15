"""
Algorithms:
A -> Input Array
result_array = []
start_index = 0
1. Decompose the Array in to a list of subarrays
    Loop the A from i = 1 to len(A):
        if i is the inflection point:
            Copy elements from start_index to i - 1 to a new subarray (a). Reverse this subarray if this segment of dereasing
            result_array.append(a)

2. return merge_sorted_arrays

"""
from typing import List

from heap_algorithms.merge_k_sorted_array import merge_sorted_arrays

INCREASING, DECREASING = range(2)


def sort_increasing_decreasing_array(input_array: List):
    # [5, 8, 10, 9, 7, 6]
    sorted_arrays = []
    start_index = 0
    current_segment = INCREASING
    for i in range(1, len(input_array) + 1):
        if i == len(input_array) or \
                (input_array[i - 1] < input_array[i] and current_segment == DECREASING) or \
                (input_array[i - 1] > input_array[i] and current_segment == INCREASING):
            sorted_arrays.append(input_array[start_index:i]
                                 if current_segment == INCREASING
                                 else input_array[i - 1:start_index - 1:-1])
            current_segment = INCREASING if current_segment == DECREASING else DECREASING
            start_index = i

    return merge_sorted_arrays(sorted_arrays)


if __name__ == '__main__':
    print(sort_increasing_decreasing_array([5, 8, 10, 9, 7, 6]))
