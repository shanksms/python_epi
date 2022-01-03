import pytest
from heap_algorithms.k_largest_elements import kLargest


@pytest.mark.parametrize('arr, k, result',
                         [
                             ([1, 2, 3, 4, 5], 1, [5]),
                             ([1, 2, 3, 4, 5], 2, [5, 4])

                         ])
def test_kLargest(arr, k, result):
    assert kLargest(arr, k) == result
