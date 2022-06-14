"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums = sorted(nums)
    current_continuous_len = max_continuous_len = 1
    for idx in range(1, len(nums)):
        if nums[idx] != nums[idx-1]:
            if nums[idx-1] + 1 == nums[idx]:
                current_continuous_len += 1
            else:
                max_continuous_len = max(max_continuous_len, current_continuous_len)
                current_continuous_len = 1
    return max(current_continuous_len, max_continuous_len)


if __name__ == '__main__':
    longestConsecutive([100,4,200,1,3,2])