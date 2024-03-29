"""
You are given a string s containing lowercase English letters, and a matrix shift,
where shift[i] = [directioni, amounti]:

directioni can be 0 (for left shift) or 1 (for right shift).
amounti is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.



Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation:
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
"""

from collections import deque
from typing import List


def stringShift(s: str, shift: List[List[int]]) -> str:
    d = deque(s)
    for _shift in shift:
        if _shift[0]:
            for _ in range(_shift[1]):
                d.appendleft(d.pop())
        else:
            for _ in range(_shift[1]):
                d.append(d.popleft())

    return ''.join(d)


if __name__ == '__main__':
    print(stringShift('abc', [[0,1],[1,2]]))