import pytest

from strings import first_unique_char



@pytest.mark.parametrize('s, index', [('shashank', 6)])
def test_solution(s, index):
    assert first_unique_char.solution(s) == index