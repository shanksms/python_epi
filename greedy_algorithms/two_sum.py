"""
There is a sorted array of integers. You need to find out if there are two elements in the array whose sum
equals to given sum

Algorithm:
input_list = [1, 2, 3, 4, 5, 9]
desired_sum = 9

1. Loop over the list with counters pointing to start and end of the index
    start, end = 0, len(input_list) - 1
    while start < end:
        if input_list[start] + input_list[end] == desired_sum:
            return True
        elif input_list[start] + input_list[end] > desired_sum
            end -= 1
        else:
            start += 1

    return False

"""
from typing import List


def two_sum(input_list: List[int], desired_sum: int) -> bool:
    start, end = 0, len(input_list) - 1
    while start < end:
        if input_list[start] + input_list[end] == desired_sum:
            return True
        elif input_list[start] + input_list[end] > desired_sum:
            end -= 1
        else:
            start += 1

    return False


if __name__ == '__main__':
    print(two_sum([1, 2, 3, 4, 5, 9], 9))
    print(two_sum([1, 2, 3, 4, 5, 9], 14))
    print(two_sum([1, 2, 3, 4, 5, 9], 15))