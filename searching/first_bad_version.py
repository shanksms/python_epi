
"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.



Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
"""
def isBadVersion(n):
    return n == 4

class Solution:

    def firstBadVersion(self, n: int) -> int:
        """
        1. do a binary search on the array
        2. if you find bad version, save that as result.
            a. end = mid - 1
        3. if you dont find bad version
            a. start = mid + 1
        """

        start = 0
        result = -1
        end = n - 1
        while end >= start:
            mid = int(end - (end - start) / 2)
            if isBadVersion(mid + 1):
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        return result + 1

