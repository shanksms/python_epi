from typing import List

"""
Algorithm:
_input: List
 target: int
 start = 0
 end = len(_input) - 1
1. Loop until start < end
    
    M = start + (end - start) / 2
    if  _input[M] == target:
        return M
    elif _input[M] > target:
        end = M - 1
    else:
        start = M +1

 
"""

def search(_input: List, target: int):
    start, end = 0, len(_input) - 1
    while start < end:
        M = int(start + (end - start) / 2)
        if _input[M] == target:
            return M
        elif _input[M] > target:
            end = M - 1
        else:
            start = M + 1
    return -1


if __name__ == '__main__':
    assert search([1, 2, 3, 4, 5], 3) == 2
    assert search([1, 2, 3, 5], 10) == -1

