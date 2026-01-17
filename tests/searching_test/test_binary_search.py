import pytest
from typing import List

from searching.binary_search import find_first_occurrence


# assuming the function is imported
# from your_module import find_first_occurrence


def test_single_element_found():
    assert find_first_occurrence([5], 5) == 0


def test_single_element_not_found():
    assert find_first_occurrence([5], 3) == -1


def test_target_at_start():
    assert find_first_occurrence([2, 2, 2, 3, 4], 2) == 0


def test_target_in_middle_multiple_occurrences():
    assert find_first_occurrence([1, 2, 3, 3, 3, 4, 5], 3) == 2


def test_target_at_end():
    assert find_first_occurrence([1, 2, 3, 4, 5], 5) == 4


def test_target_not_present_smaller_than_all():
    assert find_first_occurrence([10, 20, 30], 5) == -1


def test_target_not_present_larger_than_all():
    assert find_first_occurrence([10, 20, 30], 40) == -1


def test_empty_list():
    assert find_first_occurrence([], 1) == -1


def test_all_elements_same_target_present():
    assert find_first_occurrence([7, 7, 7, 7], 7) == 0


def test_all_elements_same_target_absent():
    assert find_first_occurrence([7, 7, 7, 7], 5) == -1
