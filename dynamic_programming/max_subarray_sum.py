from typing import List
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and 
return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""

def maxSubArray(nums: List[int]) -> int:
    """
    Algorithm:
    At each index, we make a decision:
        1. Should current index value be added to current subarray sum
        2. Or current subarray sum be discarded
    :param nums:
    :return:
    """
    current_sum = max_sum = nums[0]
    for idx in range(1, len(nums)):
        current_sum = max(nums[idx], current_sum + nums[idx])
        max_sum = max(max_sum, current_sum)

    return max_sum