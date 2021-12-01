import pytest

from strings import string_to_int


@pytest.mark.parametrize('s, i',
                         [
                             ('123', 123),
                             ('-123', -123)
                         ])
def test_to_int(s, i):
    assert i == string_to_int.to_int(s)


def test_to_int_with_blank_string():
    with pytest.raises(IndexError) as exc_msg:
        string_to_int.to_int('')

    assert 'string index out of range' == exc_msg.value.args[0]

