import pytest

from searching.binary_search import find_first_occurrence


@pytest.mark.parametrize('sorted_input_list, target, result',
                         [
                             ([1, 2, 3, 3, 4, 5], 3, 2),
                             ([1, 2, 3, 3, 4, 5], 5, 5),
                         ]

)
def test_find_first_occurrence(sorted_input_list, target, result):
    assert find_first_occurrence(sorted_input_list, target) == result
