import pytest
from arrays.binary_search_tree import Solution

@pytest.mark.parametrize('input, target, index',
                         [
                             ([-1, 0, 3, 5, 9, 12],9, 4)
                         ])
def test_search(input, target, index):
    solution = Solution()
    assert solution.search(input, target) == index