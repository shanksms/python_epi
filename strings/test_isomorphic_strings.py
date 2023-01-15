import pytest
from strings.isomorphic_strings import Solution

@pytest.mark.parametrize('input1, input2, output',
                         [
                             ('egg', 'add', True)
                         ])
def test_isIsomorphic(input1, input2, output):
    solution = Solution()
    assert solution.isIsomorphic(input1, input2) == output