"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.



Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
"""
from typing import List


def findRepeatedDnaSequences(s: str) -> List[str]:
    N, L = len(s), 10
    seen = set()
    result = set()
    for start in range(N-L+1):
        segment = s[start:start+L]
        if segment in seen:
            result.add(segment)
        else:
            seen.add(segment)
    return result

if __name__ == '__main__':
    print(findRepeatedDnaSequences('AAAAAAAAAAAAA'))




