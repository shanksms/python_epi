from strings.spread_sheet_column_encoding import decode
import pytest


@pytest.mark.parametrize('column, result',
                         [
                             ('A', 1),
                             ('B', 2),
                             ('Z', 26),
                             ('AA', 27)
                         ])
def test_decode(column, result):
    assert result == decode(column)