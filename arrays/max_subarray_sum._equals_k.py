
"""
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k.
If there is not one, return 0 instead.



Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
"""
from typing import List


def maxSubArrayLen(nums: List[int], k: int) -> int:
    prefix_sum = []
    max_subarray_length = 0
    for idx, num in enumerate(nums):
        prefix_sum.append(num + prefix_sum[idx - 1] if idx > 0 else nums[idx])
    d = {}
    for idx, num in enumerate(nums):
        if k == prefix_sum[idx]:
            max_subarray_length = idx + 1
        if (prefix_sum[idx] - k) in d:
            max_subarray_length = max(max_subarray_length, idx - d[prefix_sum[idx] - k])

        if prefix_sum[idx] not in d:
            d[prefix_sum[idx]] = idx

    return max_subarray_length





if __name__ == '__main__':
    print(maxSubArrayLen([1,-1,5,-2,3], 3))