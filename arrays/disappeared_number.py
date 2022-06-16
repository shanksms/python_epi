from typing import List
"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers
in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
"""

def findDisappearedNumbers(nums: List[int]) -> List[int]:
    size_of_nums = len(nums)
    nums_membership_set = set(nums)
    sorted_nums = sorted(nums)
    result = []
    for idx in range(1, size_of_nums + 1):
        if idx not in nums_membership_set:
            result.append(idx)
    return result


if __name__ == '__main__':
    #[1, 2, 2, 3, 3, 4, 7, 8]
    print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
