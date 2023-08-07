"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""
from collections import Counter

def solution(s):
    """
    Algo:
    Create a frequency Counter of each character in the string.
    for char, its_index in string:
        if char not in freq_counter:
            return index of the char
    return -1
    :param s:
    :return:
    """
    freq_counter = dict(Counter(s))
    for idx, ch in enumerate(s):
        if freq_counter[ch] == 1:
            return idx

    return -1
