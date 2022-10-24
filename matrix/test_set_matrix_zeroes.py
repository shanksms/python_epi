import pytest
from matrix import set_matrix_zeroes


@pytest.mark.parametrize('input, result',
                         [
                             (
                                     [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
                                     [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
                             )

                         ])
def test_set_zeroes_approach1(input, result):
    assert set_matrix_zeroes.set_zeroes_approach1(input) == result
