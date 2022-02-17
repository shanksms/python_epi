from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

def twoSum_approach1(self, nums: List[int], target: int) -> List[int]:
    nums_tuple = []
    for i, num in enumerate(nums):
        nums_tuple.append((i, num))
    nums_tuple = sorted(nums_tuple, key=lambda num_tuple: num_tuple[1])
    start, end = 0, len(nums_tuple) - 1
    while end > start:
        current_sum = nums_tuple[start][1] + nums_tuple[end][1]
        if current_sum == target:
            return [nums_tuple[start][0], nums_tuple[end][0]]
        elif current_sum > target:
            end -= 1
        else:
            start += 1


def twoSum_approach2(self, nums: List[int], target: int) -> List[int]:
    """

    :param self:
    :param nums:
    :param target:
    :return:
    Algorithm
        1. Create a set to hold the numbers
            num_set = {}
        2. Iterate over the list
            while i, num in enumerate(nums):
                if (target - num) in num_set:
                    return [i, num_set[target - num]]
                num_set[num] = i

    """
    num_dict = dict()
    for i, num in enumerate(nums):
        if (target - num) in num_dict:
            return [
                i, num_dict[(target - num)]
            ]
        num_dict[num] = i

