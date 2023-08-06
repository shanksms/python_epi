import pytest
from maths.power_of_three import using_maths

@pytest.mark.parametrize('n, result',
                         [
                             (9, True), (8, False)
                         ])
def test_using_maths(n, result):
    assert using_maths(n) == result