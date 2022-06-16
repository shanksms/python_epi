"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.



Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2
"""

from collections import Counter


def longest_palindrome(s: str) -> int:
    """
    Algorithm:
    1. create word counter
    2. loop the counter and fetch word and its count
    3. add even number of word into total_even_word_count and 1 to total_odd_word_count
        e.g. if a -> 5, 4 will be added to total_even_word_count and 1 to total_odd_word_count
    :param s:
    :return:
    """
    word_count_map = dict(Counter(s))
    total_even_word_count = 0
    total_odd_word_count = 0
    for word, count in word_count_map.items():
        d, m = divmod(count, 2)
        total_even_word_count += d * 2
        total_odd_word_count += m
    return total_even_word_count + (1 if total_odd_word_count else 0)


if __name__ == '__main__':
    print(longest_palindrome('abccccdd'))