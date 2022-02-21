"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
missing from the array.
Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range

"""
from typing import List


def missing_number(nums: List[int]) -> int:
    desired_sum = sum(range(1, len(nums) + 1))
    given_sum = sum(nums)
    return desired_sum - given_sum


if __name__ == '__main__':
    print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
