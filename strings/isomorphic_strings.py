"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map = {}
        revers_char_map = {}
        for c1, c2 in zip(s, t):
            if c1 in char_map and char_map[c1] != c2:
                return False
            char_map[c1] = c2
            if c2 in revers_char_map and revers_char_map[c2] != c1:
                return False
            revers_char_map[c2] = c1

        return True
