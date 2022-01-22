import pytest

from searching import binary_search


@pytest.mark.parametrize('sorted_input_list, target, result',
                         [
                             ([1, 2, 3, 3, 4, 5], 3, 2),
                             ([1, 2, 3, 3, 4, 5], 5, 5),
                         ]

)
def test_find_first_occurrence(sorted_input_list, target, result):
    assert binary_search.find_first_occurrence(sorted_input_list, target) == result


@pytest.mark.parametrize('sorted_input_list, target, result',
                         [
                             ([1, 2, 3, 4, 5], 2, 2),
                             ([-14, -10, 2, 108, 108, 243], -13, 1),
                         ]

)
def test_first_occurrence_of_element_greater_than_key(sorted_input_list, target, result):
    assert binary_search.first_occurence_of_element_greater_than_key(sorted_input_list, target) == result

@pytest.mark.parametrize(
    'matrix, target, result',
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, (1, 0)),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, (1, 1))
    ]
)
def test_search_sorted_matrix(matrix, target, result):
    assert binary_search.search_sorted_matrix(matrix, target) == result