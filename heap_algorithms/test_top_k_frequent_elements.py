import pytest
from heap_algorithms import top_k_frequent_elements


@pytest.mark.parametrize('nums, k, result',
                         [([1, 1, 1, 2, 2, 3], 2, [1, 2])])
def test_top_k_frequents_approach1(nums, k, result):
    assert result == top_k_frequent_elements.top_k_frequents_approach1(nums, k)