"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
"""
import math

def naive_approach(n):
    result = 1
    counter = 0
    while result <= n:
        result = 3 ** counter
        if result == n:
            return True
        counter += 1
    return False


def using_maths(n):
    """
    We can use mathematics as follows

    n = 3 ** i
    i = log3(n)
    i = log10(n) / log10(3)
    i should be an integer
    :param n:
    :return:
    """
    i = math.log(n, 3)
    return i % 1 == 0

if __name__ == '__main__':
    print(using_maths(10))


