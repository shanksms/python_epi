"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply
X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.



Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

def int_to_roman_greedy(num: int) -> str:
    """
    Representing a given integer as a Roman Numeral requires finding a sequence of the above 13 symbols, where their
    corresponding values add up to the integer. This sequence must be in order from largest to smallest, based on symbol value.
    As explained in the overview, the representation should use the largest possible symbols, working from the left. Therefore, it makes sense to use a Greedy algorithm. A Greedy algorithm is an algorithm that makes the best possible decision at the current time; in this case taking out the largest possible symbol it can.

    S`o to represent a given integer, we look for the largest symbol that fits into it. We subtract that, and then look for the largest symbol that fits into the remainder, and so on until the remainder is 0. Each of the symbols we take out are appended onto the output Roman Numeral string.

    For example, suppose we need to make the number 671.

    The largest symbol that fits into 671 is D (which is worth 500). The next symbol up, CM, is worth 900 and so is too big to fit. Therefore, we now have the following.

    Roman Numeral so far: D
    Integer remainder: 671 - 500 = 171
    We now repeat the process with 171. The largest symbol that fits into it is C (worth 100).

    Roman Numeral so far: DC
    Integer remainder: 171 - 100 = 71
    Repeating this with 71, we find the largest symbol that fits in is L (worth 50).

    Roman Numeral so far: DCL
    Integer remainder: 71 - 50 = 21
    For 21, the largest symbol that fits in is X (worth 10).

    Roman Numeral so far: DCLX
    Integer remainder: 21 - 10 = 11
    For 11, the largest symbol that fits in is again X.

    Roman Numeral so far: DCLXX
    Integer remainder: 11 - 10 = 1
    Finally, the 1 is represented with a I and we're done.

    Roman Numeral so far: DCLXXI`
    Integer remainder: 1 - 1 = 0
    :param num:
    :return:

    Algorithm:
    num = 16
     digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
                  (5, "V"), (4, "IV"), (1, "I")]

    result = []
    for value, symbol in symbol_num_list:
        if num == 0:
            break
        count, num = divmod(num, value)
        if count > 0:
            result.append(count * symbol)



    """
    symbol_num_list = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
              (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
              (5, "V"), (4, "IV"), (1, "I")]


    result = []
    for value, symbol in symbol_num_list:
        if num == 0:
            break
        count, num = divmod(num, value)
        if count > 0:
            result.append(count * symbol)
    return ''.join(result)


if __name__ == '__main__':
    #print(int_to_roman_greedy(16))
    print(int_to_roman_greedy(171))
    print(int_to_roman_greedy(671))