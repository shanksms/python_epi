import pytest
from strings.is_subsequence import Solution

@pytest.mark.parametrize('input1, input2, output',
                         [
                             ('ace', 'abcde', True),
                             ('aec', 'abcde', False)
                         ])
def test_isSubsequence(input1, input2, output):
    solution = Solution()
    assert solution.isSubsequence(input1, input2) == output