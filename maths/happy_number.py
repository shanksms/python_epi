"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
"""

class Solution:
    def return_digits(self, n):
        digits = []
        while n:
            digits.append(n % 10)
            n = n // 10

        return list(reversed(digits))
    def isHappy(self, n: int) -> bool:
        alredy_seen = set()
        while n and n not in alredy_seen:
            alredy_seen.add(n)
            digits = self.return_digits(n)
            n = sum([num * num for num in digits])
            if n == 1:
                return True
        return False