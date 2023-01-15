import pytest
from arrays.find_pivot_index import Solution

@pytest.mark.parametrize('input, output',
                         [
                             ([1, 7, 3, 6, 5, 6], 3)
                         ])
def test_pivotIndex(input, output):
    solution = Solution()
    assert solution.pivotIndex(input) == output
