
"""
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in
any place in the array.



Example 1:

Input: data = [1,0,1,0,1]
Output: 1
Explanation: There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:

Input: data = [0,0,0,1,0]
Output: 0
Explanation: Since there is only one 1 in the array, no swaps are needed.
Example 3:

Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
"""
from typing import List


def minSwaps(data: List[int]) -> int:
    """
    Algorithm
    Essentially, we need to find a window (not bigger than total number of ones) which has the most number of ones.
    Then difference between total ones and number of ones in the above defined window will be our answer.
    :param self:
    :param data:
    :return:
    """
    ones = sum(data)
    left = right = 0
    max_count = current_count = 0
    while right < len(data):
        current_count += data[right]
        right += 1
        if (right - left) > ones:
            current_count -= data[left]
            left += 1
        max_count = max(max_count, current_count)
    return ones - max_count


if __name__ == '__main__':
    print(minSwaps([1,0,1,0,1]))




