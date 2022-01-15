import pytest
from heap_algorithms import sort_k_increasing_decreasing_array

@pytest.mark.parametrize('input, result',
                         [
                             ([5, 8, 10, 9, 7, 6], [5, 6, 7, 8, 9, 10]),

                         ])
def test_sort_increasing_decreasing_array(input, result):

    assert sort_k_increasing_decreasing_array.sort_increasing_decreasing_array(input) == result

