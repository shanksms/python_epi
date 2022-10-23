"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""
from collections import Counter
import heapq


def top_k_frequents_approach1(nums, k):
    counter = Counter(nums)
    return [e[0] for e in counter.most_common(k)]


def top_k_frequents_approach2(nums, k):
    counter = Counter(nums)
    min_heap = []
    for key, val in counter.items():
        if len(min_heap) == k:
            heapq.heappushpop(min_heap, (val, key))
        else:
            heapq.heappush(min_heap, (val, key))
    return [e[1] for e in min_heap]


if __name__ == '__main__':
    print(top_k_frequents_approach2([1, 1, 1, 2, 2, 3], 2))