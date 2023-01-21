import pytest
from searching.first_bad_version import Solution

@pytest.mark.parametrize('input, output',
                         [
                             (5, 4)
                         ])
def test_search(input, output):
    solution = Solution()
    assert solution.firstBadVersion(input) == output