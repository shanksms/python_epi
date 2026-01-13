import pytest
from typing import List

from hash.two_sums import Solution


@pytest.fixture
def solution():
    return Solution()


def test_basic_case(solution):
    nums = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(nums, target) == [0, 1]


def test_numbers_later_in_list(solution):
    nums = [3, 2, 4]
    target = 6
    assert solution.twoSum(nums, target) == [1, 2]


def test_duplicate_values(solution):
    nums = [3, 3]
    target = 6
    assert solution.twoSum(nums, target) == [0, 1]


def test_negative_numbers(solution):
    nums = [-1, -2, -3, -4, -5]
    target = -8
    assert solution.twoSum(nums, target) == [2, 4]


def test_zero_and_positive(solution):
    nums = [0, 4, 3, 0]
    target = 0
    assert solution.twoSum(nums, target) == [0, 3]


def test_minimum_valid_input(solution):
    nums = [1, 2]
    target = 3
    assert solution.twoSum(nums, target) == [0, 1]


def test_no_solution_returns_none(solution):
    nums = [1, 2, 3]
    target = 7
    assert solution.twoSum(nums, target) is None
