from heap_algorithms.minimum_sum import solve
import pytest


@pytest.mark.parametrize('input, output',
                         [
                             ([ 6, 8, 4, 5, 2, 3 ], 604)
                         ])
def test_solve(input, output):
    assert solve(input) == output

