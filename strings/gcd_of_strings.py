"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""


class Solution:
    def gcd(self, num1, num2):
        if num1 % num2 == 0:
            return num2
        return self.gcd(num2, num1 % num2)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) > len(str2):
            short_str = str2
            long_str = str1
        else:
            short_str = str1
            long_str = str2
        n1 = len(str1) if len(str1) > len(str2) else len(str2)
        n2 =  len(str2) if len(str1) > len(str2) else len(str1)
        gcd_num = self.gcd(n1, n2)
        return short_str[:gcd_num]