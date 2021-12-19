from typing import List

def max_product(l: List[int]) -> int:
    if len(l) < 2:
        raise ValueError('There should be at least 2 elements in the list')
    a, b = sorted(l, reverse=True)[0:2]
    return a * b


